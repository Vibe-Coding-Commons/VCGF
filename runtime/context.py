# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from datetime import datetime, timezone
from .contracts import validate_contract
from .loader import confined


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def instant(value):
    return datetime.fromisoformat(value.upper().replace('Z', '+00:00'))


def context_facts(record, project_root, now=None):
    errors = validate_contract('context', record)
    if errors:
        raise ValueError('; '.join(errors))
    now = now or datetime.now(timezone.utc)
    facts, invalid = {}, {}
    for fact in record['facts']:
        key, source = fact['key'], fact['source']
        reason = None
        if fact['state'] != 'known':
            reason = 'unknown fact'
        elif not instant(fact['observed_at']) <= now < instant(fact['expires_at']):
            reason = 'stale/future observation'
        elif source['kind'] == 'repository':
            try:
                if hashlib.sha256(confined(project_root, source['reference']).read_bytes()).hexdigest() != source['content_sha256']:
                    reason = 'source changed'
            except (OSError, ValueError):
                reason = 'source unavailable'
        else:
            reason = 'external/user assertion requires trusted observation adapter'
        facts[key] = None if reason else fact['value']
        if reason:
            invalid[key] = reason
    return facts, invalid


def handoff(context, route):
    return {'contract_version': '1.1.0', 'context_sha256': digest(context),
            'task_id': route['task_id'], 'decision': route['decision'],
            'blockers': route['blockers'], 'next_step': 'resolve blockers' if route['blockers'] else 'plan scoped change',
            'revalidate_before_use': True, 'secrets_included': False}


def preferences_prompt(preferences):
    if preferences is not None and not validate_contract('preferences', preferences) and preferences['first_run_confirmed']:
        return None
    return {'ar': 'ما لغة الحوار المفضلة: العربية أم الإنجليزية أم تلقائي؟ وما اللهجة إن رغبت؟',
            'en': 'Choose interaction language: ar, en, or auto; optionally a dialect.',
            'choices': ['ar', 'en', 'auto'], 'changes_product_language': False}
