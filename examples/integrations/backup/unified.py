# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""SQLite/private-file reference: cooperative app lock + encrypted unified restore.

All app writers MUST hold barrier(). This is not a lock for unrelated processes.
Only restore into a new directory, never an existing or production database.
"""
from contextlib import contextmanager
from datetime import datetime,timezone
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import sqlite3
import tempfile
import zipfile
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def sha(data):return hashlib.sha256(data).hexdigest()


def safe(root,name):
    p=Path(name);root=Path(root).resolve()
    if p.is_absolute() or '..' in p.parts or not p.parts:raise ValueError('unsafe member')
    result=root/p
    if not result.resolve().is_relative_to(root) or any(x.is_symlink() for x in [result,*result.parents] if x!=root and x.is_relative_to(root)):raise ValueError('unsafe storage path')
    return result


@contextmanager
def barrier(root):
    lock=safe(root,'.backup.lock')
    with lock.open('a+b') as handle:
        fcntl.flock(handle.fileno(),fcntl.LOCK_EX)
        try:yield
        finally:fcntl.flock(handle.fileno(),fcntl.LOCK_UN)


def create(root,destination,key,application_version,schema_version):
    root=Path(root).resolve();destination=Path(destination)
    if len(key)!=32:raise ValueError('AES-256 key must contain 32 random bytes')
    if destination.exists():raise FileExistsError('never overwrite existing backup')
    database=safe(root,'app.db')
    if not database.is_file():raise FileNotFoundError('application database missing')
    with barrier(root),tempfile.TemporaryDirectory() as d:
        dbcopy=Path(d)/'app.db'
        with sqlite3.connect(f'file:{database}?mode=ro',uri=True) as source,sqlite3.connect(dbcopy) as target:
            source.backup(target)
            if target.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ValueError('database integrity failure')
            rows=target.execute('SELECT storage_path, checksum FROM attachments ORDER BY storage_path').fetchall()
        members={'app.db':dbcopy.read_bytes()}
        for name,expected in rows:
            if not name.startswith('attachments/'):raise ValueError('attachment must use private attachment root')
            content=safe(root,name).read_bytes()
            if sha(content)!=expected:raise ValueError('attachment does not match database checksum')
            members[name]=content
        manifest={'backup_id':os.urandom(16).hex(),'created_at':datetime.now(timezone.utc).isoformat(),
                  'database_engine':'sqlite','database_version':sqlite3.sqlite_version,'application_version':application_version,
                  'schema_version':schema_version,'compression':'zip-deflate','encryption':'AES-256-GCM',
                  'consistency':'cooperative application barrier held through database and attachment read',
                  'files':{n:sha(b) for n,b in sorted(members.items())},'attachment_count':len(rows)}
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as archive:
            for name,content in members.items():archive.writestr(name,content)
            archive.writestr('manifest.json',json.dumps(manifest,sort_keys=True))
        nonce=os.urandom(12);payload=b'VCGF1'+nonce+AESGCM(key).encrypt(nonce,stream.getvalue(),b'VCGF-unified-backup-v1')
        fd=os.open(destination,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(fd,'wb') as out:out.write(payload)
    return {'backup_id':manifest['backup_id'],'sha256':sha(payload),'size':len(payload),'restore_status':'Not run'}


def restore(source,destination,key,max_uncompressed=128*1024*1024):
    destination=Path(destination)
    if destination.exists():raise FileExistsError('restore destination must be new')
    payload=Path(source).read_bytes()
    if not payload.startswith(b'VCGF1'):raise ValueError('unknown backup format')
    data=AESGCM(key).decrypt(payload[5:17],payload[17:],b'VCGF-unified-backup-v1')
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names=archive.namelist()
        if len(names)!=len(set(names)) or sum(i.file_size for i in archive.infolist())>max_uncompressed:raise ValueError('duplicate or oversized archive')
        manifest=json.loads(archive.read('manifest.json'))
        if set(names)!=set(manifest['files'])|{'manifest.json'}:raise ValueError('unlisted archive member')
        destination.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=destination.parent) as d:
            stage=Path(d)/'restore';stage.mkdir(mode=0o700)
            for name,expected in manifest['files'].items():
                target=safe(stage,name);content=archive.read(name)
                if sha(content)!=expected:raise ValueError('checksum mismatch')
                target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(content);target.chmod(0o600)
            with sqlite3.connect(f'file:{stage / "app.db"}?mode=ro',uri=True) as db:
                if db.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ValueError('restored database corrupt')
                rows=db.execute('SELECT storage_path,checksum FROM attachments').fetchall()
                if len(rows)!=manifest['attachment_count']:raise ValueError('attachment count differs')
                for name,expected in rows:
                    if sha(safe(stage,name).read_bytes())!=expected:raise ValueError('restored attachment inconsistent')
            # Exclusive directory creation prevents replacing a concurrently created target.
            destination.mkdir(mode=0o700)
            try:
                for item in stage.iterdir():shutil.move(str(item),destination/item.name)
            except Exception:
                shutil.rmtree(destination);raise
    return {'status':'restored_and_consistency_verified','engine':'sqlite','attachments':len(rows),'backup_id':manifest['backup_id']}
