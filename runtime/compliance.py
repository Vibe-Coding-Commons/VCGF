# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Compliance evaluation for a target project: applicable controls -> acceptance definitions -> recorded results -> verified evidence.

The evaluator never executes a project's tests. It checks that every acceptance definition applicable to the project
(from a route result or a profile) has a recorded result, that a PASS cites evidence artifacts that exist under the
artifact root with matching SHA-256 digests, that human-review tests carry a reviewer, that the record is current and
bound to the code it describes, and it reports per control: COMPLIANT, FAILED or NOT_TESTED. A definition without a
result, a SKIP and a NOT_TESTED are never counted as satisfied. Nothing here infers conformance from definitions.
"""
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .acceptance import acceptance_index
from .context import instant
from .contracts import ROOT, validate_contract
from .loader import confined

HUMAN = {'manual', 'review'}


def applicable_controls(route_result=None, profile=None, root=ROOT):
    if route_result is not None:
        if 'route' in route_result and 'selected_control_ids' not in route_result:
            route_result = route_result['route']
        errors = validate_contract('route-result', route_result)
        if errors:
            raise ValueError('invalid route result: ' + '; '.join(errors))
        return sorted(route_result['selected_control_ids']), route_result['profile']
    if profile is None:
        raise ValueError('a route result or a profile is required')
    path = Path(root) / 'profiles' / profile / 'profile.yaml'
    if not path.is_file():
        raise ValueError('unknown profile: ' + str(profile))
    return sorted(yaml.safe_load(path.read_text(encoding='utf-8'))['required_controls']), profile


def evaluate_compliance(results_record, artifact_root, controls, expected=None, now=None, root=ROOT):
    errors = validate_contract('acceptance-results', results_record)
    if errors:
        return {'status': 'INVALID', 'errors': errors, 'controls': {}, 'claim': 'contract rejected; nothing evaluated'}
    now = now or datetime.now(timezone.utc)
    expected = expected or {}
    if not instant(results_record['recorded_at']) <= now < instant(results_record['valid_until']):
        errors.append('stale/future results')
    for field in ('code_sha256', 'profile', 'route_sha256'):
        if field in expected and results_record.get(field) != expected[field]:
            errors.append('changed results binding: ' + field)
    index = acceptance_index(root)
    definitions = {t['id']: dict(t, control_id=cid) for cid in controls for t in index.get(cid, {'tests': []})['tests']}
    by_test = {}
    for r in results_record['results']:
        if r['test_id'] in by_test:
            errors.append('duplicate result: ' + r['test_id'])
        by_test[r['test_id']] = r
    unknown = sorted(t for t in by_test if t not in definitions)
    if unknown:
        errors.append('results for tests outside the applicable set or unknown: ' + ', '.join(unknown))
    per_control = {}
    for cid in controls:
        tests = [t for t in definitions.values() if t['control_id'] == cid]
        states = []
        for t in tests:
            r = by_test.get(t['id'])
            if r is None or r['status'] == 'NOT_TESTED':
                states.append(('NOT_TESTED', t['id'], 'no recorded result' if r is None else 'recorded as not tested'))
                continue
            if r['status'] == 'SKIP':
                states.append(('NOT_TESTED', t['id'], 'skipped: ' + (r.get('notes') or 'no reason recorded')))
                continue
            if r['status'] == 'FAIL':
                states.append(('FAILED', t['id'], 'recorded failure'))
                continue
            problems = []
            if not r['evidence']:
                problems.append('PASS without evidence')
            for a in r['evidence']:
                try:
                    data = confined(artifact_root, a['reference']).read_bytes()
                    if hashlib.sha256(data).hexdigest() != a['sha256']:
                        problems.append('evidence changed: ' + a['artifact_id'])
                except (OSError, ValueError):
                    problems.append('evidence missing/unsafe: ' + a['artifact_id'])
            if t.get('type') in HUMAN and not r.get('reviewer'):
                problems.append('human-review test without a reviewer')
            if instant(r['executed_at']) > now:
                problems.append('executed in the future')
            if r['executor']['kind'] in HUMAN and t.get('type') == 'automated':
                problems.append('automated definition recorded by a human executor; record the tool run')
            states.append(('FAILED', t['id'], '; '.join(problems)) if problems else ('PASS', t['id'], 'evidence verified'))
        failed = [s for s in states if s[0] == 'FAILED']
        untested = [s for s in states if s[0] == 'NOT_TESTED']
        status = 'FAILED' if failed else ('NOT_TESTED' if untested or not tests else 'COMPLIANT')
        per_control[cid] = {'status': status, 'definitions': len(tests), 'passed': sum(1 for s in states if s[0] == 'PASS'),
                            'failed': len(failed), 'not_tested': len(untested),
                            'detail': [{'test_id': s[1], 'state': s[0], 'reason': s[2]} for s in states if s[0] != 'PASS']}
    counts = {k: sum(1 for c in per_control.values() if c['status'] == k) for k in ('COMPLIANT', 'FAILED', 'NOT_TESTED')}
    overall = 'INVALID' if errors else ('COMPLIANT' if counts['FAILED'] == 0 and counts['NOT_TESTED'] == 0 and controls else 'NOT_COMPLIANT')
    return {'status': overall, 'errors': errors, 'profile': results_record['profile'], 'code_sha256': results_record['code_sha256'],
            'applicable_controls': len(controls), 'counts': counts, 'controls': per_control,
            'claim': 'evidence integrity, coverage and freshness verified against the acceptance definitions; no project test was executed by this evaluator and no conformance is inferred from definitions'}
