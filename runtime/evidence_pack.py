# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Disclosure views do not change conformance thresholds or remove blockers."""
from copy import deepcopy
from .contracts import validate_contract


def present(record,decision,mode='standard'):
    if validate_contract('evidence',record):raise ValueError('invalid evidence contract')
    if mode not in ['minimal','standard','audit']:raise ValueError('unknown evidence mode')
    base={'mode':mode,'evidence_id':record['evidence_id'],'scope':record['scope'],
          'decision':deepcopy(decision),'code_sha256':record['code_sha256'],'policy_sha256':record['policy_sha256'],
          'environment':record['environment'],'controls':deepcopy(record['controls']),
          'exceptions':deepcopy(record['exceptions']),'outstanding_findings':deepcopy(record['outstanding_findings'])}
    if mode in ['standard','audit']:base['artifacts']=deepcopy(record['artifacts']);base['reviewer']=deepcopy(record['reviewer'])
    if mode=='audit':base['full_record']=deepcopy(record)
    return base
