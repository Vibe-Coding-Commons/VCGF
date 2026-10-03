# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Reference schedule/retention/download gates; hosting and identity stay external."""
from datetime import datetime,timezone,timedelta
import hashlib,secrets
import math


def schedule(frequency,custom=None):
    schedules={'manual':None,'daily':'0 2 * * *','weekly':'0 2 * * 0','monthly':'0 2 1 * *'}
    if frequency=='custom':
        if not isinstance(custom,str) or len(custom.split())!=5 or any(c not in '0123456789*/,- ' for c in custom):raise ValueError('restricted five-field cron schedule required')
        for field,(low,high) in zip(custom.split(),[(0,59),(0,23),(1,31),(1,12),(0,7)]):
            for part in field.split(','):
                pair=part.split('/')
                if len(pair)>2 or (len(pair)==2 and (not pair[1].isdigit() or not 1<=int(pair[1])<=high-low+1)):raise ValueError('invalid cron step')
                if pair[0]=='*':continue
                bounds=pair[0].split('-')
                if len(bounds)>2 or any(not x.isdigit() or not low<=int(x)<=high for x in bounds):raise ValueError('invalid cron range')
                if len(bounds)==2 and int(bounds[0])>int(bounds[1]):raise ValueError('reversed cron range')
        return custom
    if frequency not in schedules:raise ValueError('unknown schedule')
    return schedules[frequency]


def retention_candidates(history,keep,now):
    """Return candidates only. Never remove backups or legal holds automatically."""
    if type(keep) is not int or keep<1:raise ValueError('retain at least one successful tested backup')
    successful=sorted([x for x in history if x['restore_verified'] and not x.get('hold',False)],key=lambda x:x['created_at'],reverse=True)
    return [x['backup_id'] for x in successful[keep:] if x['created_at']<now]


class DownloadGate:
    def __init__(self):self.tickets={}
    def issue(self,artifact_sha256,subject,authorize_recent,now,ttl=60):
        if not 1<=ttl<=300:raise ValueError('short-lived ticket required')
        if authorize_recent(subject,artifact_sha256) is not True:raise PermissionError('authorization and recent authentication required')
        token=secrets.token_urlsafe(32);self.tickets[hashlib.sha256(token.encode()).hexdigest()]=(artifact_sha256,subject,now+ttl)
        return token
    def consume(self,token,subject,artifact_sha256,now):
        key=hashlib.sha256(token.encode()).hexdigest();entry=self.tickets.get(key)
        if not entry or entry[0]!=artifact_sha256 or entry[1]!=subject or now>=entry[2]:raise PermissionError('expired/mismatched download ticket')
        del self.tickets[key];return {'authorized':True,'audit_event':'backup_download_authorized','subject':subject,'artifact_sha256':artifact_sha256}


def recovery_gate(environment,persistent_data,objectives,verified_backup,now,max_age_seconds):
    errors=[]
    valid_goal=lambda x:type(x) in [int,float] and math.isfinite(x) and x>=0
    if not valid_goal(max_age_seconds):raise ValueError('nonnegative finite backup age limit required')
    if environment=='production' and persistent_data and not (objectives.get('not_applicable_reason') or (valid_goal(objectives.get('rpo')) and valid_goal(objectives.get('rto')) and objectives.get('justification'))):errors.append('justified recovery objectives in seconds or N/A required')
    if not verified_backup.get('restore_verified') or not 0<=now-verified_backup.get('created_at',float('-inf'))<=max_age_seconds:errors.append('fresh restore-verified backup required')
    return {'allowed':not errors,'errors':errors,'production_approval_still_required':environment=='production'}
