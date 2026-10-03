# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Encrypted local outbox. Ambiguous failures require reconciliation, not blind retry."""
from email import policy
from email.parser import BytesParser
import json,os,sqlite3,time,uuid
from pathlib import Path
import smtplib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Outbox:
    def __init__(self,path,key):
        if len(key)!=32:raise ValueError('32-byte key required')
        self.path=Path(path);self.key=key
        if self.path.is_symlink():raise ValueError('outbox symlink forbidden')
        if not self.path.exists():
            fd=os.open(self.path,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
        self.db=sqlite3.connect(self.path)
        self.db.execute('CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY,payload BLOB,status TEXT,attempts INTEGER,due REAL)');self.db.commit()
    def close(self):self.db.close()
    def enqueue(self,message,now=None):
        ident=uuid.uuid4().hex;nonce=os.urandom(12);data=nonce+AESGCM(self.key).encrypt(nonce,message.as_bytes(),ident.encode())
        self.db.execute('INSERT INTO jobs VALUES(?,?,?,0,?)',(ident,data,'pending',time.time() if now is None else now));self.db.commit();return ident
    def process_one(self,send,now=None,max_attempts=3):
        now=time.time() if now is None else now
        self.db.execute('BEGIN IMMEDIATE')
        row=self.db.execute("SELECT id,payload,attempts FROM jobs WHERE status='pending' AND due<=? ORDER BY due,id LIMIT 1",(now,)).fetchone()
        if row is None:self.db.commit();return {'status':'idle'}
        ident,payload,attempts=row
        self.db.execute("UPDATE jobs SET status='inflight',attempts=attempts+1 WHERE id=?",(ident,));self.db.commit()
        state='accepted_by_provider'
        try:
            raw=AESGCM(self.key).decrypt(payload[:12],payload[12:],ident.encode())
            send(BytesParser(policy=policy.default).parsebytes(raw))
        except smtplib.SMTPDataError as exc:
            # Explicit 4xx DATA refusal means server did not accept this message.
            state='pending' if 400<=exc.smtp_code<500 and attempts+1<max_attempts else 'failed'
        except Exception:
            state='needs_reconciliation' # timeout/disconnect may have happened after acceptance
        due=now+min(3600,30*(2**attempts))
        self.db.execute('UPDATE jobs SET status=?,due=? WHERE id=?',(state,due,ident));self.db.commit()
        return {'id':ident,'status':state,'attempts':attempts+1,'content_logged':False}
