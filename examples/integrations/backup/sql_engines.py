# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Sandbox-only executable DB adapters. Live engine integration is Unverified.

The trusted caller must hold an application write barrier while taking the dump
and attachments. These adapters do not pretend a DB transaction locks files.
"""
from pathlib import Path
import os,re,subprocess


def _binary(path):
    p=Path(path)
    if not p.is_absolute() or not p.is_file() or not os.access(p,os.X_OK):raise ValueError('explicit installed binary required')
    return str(p)


def _private_file(path):
    p=Path(path)
    if not p.is_absolute() or p.is_symlink() or not p.is_file() or p.stat().st_mode & 0o077:raise ValueError('private 0600 credential file required')
    return str(p)


def _database(name):
    if not re.fullmatch(r'vcgf_sandbox_[a-z0-9_]+',name):raise ValueError('only explicit VCGF sandbox database names allowed')
    return name


def commands(engine,dump_binary,restore_binary,database,credential_file,host='127.0.0.1',port=None,user='vcgf_sandbox'):
    db=_database(database);dump=_binary(dump_binary);restore=_binary(restore_binary);credentials=_private_file(credential_file)
    if host not in ['127.0.0.1','localhost']:raise ValueError('reference is local-sandbox only')
    if not re.fullmatch(r'[a-zA-Z0-9_]+',user):raise ValueError('invalid user')
    env={'PATH':os.environ.get('PATH',''),'LANG':'C.UTF-8'}
    if engine=='postgresql':
        env.update(PGPASSFILE=credentials,PGHOST=host,PGPORT=str(port or 5432),PGUSER=user)
        return {'dump':[dump,'--format=custom','--no-password','--dbname='+db],
                'restore':[restore,'--no-password','--exit-on-error','--single-transaction','--no-owner','--no-privileges','--dbname='+db], 'env':env}
    if engine=='mysql':
        base=['--defaults-extra-file='+credentials,'--host='+host,'--port='+str(port or 3306),'--user='+user]
        return {'dump':[dump,*base,'--single-transaction','--quick','--skip-lock-tables','--set-gtid-purged=OFF',db],
                'restore':[restore,*base,db],'env':env}
    raise ValueError('reference engine unsupported; no generic fallback')


def dump_to_file(configuration,path,*,timeout=120):
    p=Path(path)
    fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    try:
        with os.fdopen(fd,'wb') as out:
            result=subprocess.run(configuration['dump'],env=configuration['env'],stdout=out,stderr=subprocess.PIPE,timeout=timeout,check=False)
        if result.returncode or p.stat().st_size==0:raise RuntimeError('database dump failed; raw stderr suppressed to protect credentials')
    except Exception:
        p.unlink(missing_ok=True);raise
    return {'status':'dump_created','restore_verified':False,'bytes':p.stat().st_size}


def restore_to_empty_sandbox(configuration,path,confirm_empty_target,*,timeout=120):
    if confirm_empty_target is not True:raise PermissionError('explicit empty sandbox confirmation required')
    with Path(path).open('rb') as source:
        result=subprocess.run(configuration['restore'],env=configuration['env'],stdin=source,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
    if result.returncode:raise RuntimeError('restore failed; target may need sandbox cleanup; raw output suppressed')
    return {'status':'restore_command_completed','data_consistency':'Unverified: compare rows, schema and attachment checksums before acceptance'}
