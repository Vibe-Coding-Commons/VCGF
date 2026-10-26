# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Read-only access to the control acceptance tests in spec/acceptance/*.yaml (see spec/acceptance/README.md).

Defined is not executed. Every test carries an execution state:
- `framework_self` scope: the acceptance definition describes VCGF itself (Router, loader, contracts, gates, validators);
  tests/acceptance/test_self_acceptance.py executes it and scripts/run-self-acceptance.py records the result in
  docs/quality/v1.4/self-acceptance-results.json, which this module reads (passed / failed / skipped).
- `target_project` scope: the definition describes a project adopting VCGF; its state is always `not_executed` here and
  manual or review tests without a recorded project result stay unverified. No project conformance is inferred.
"""
import json
from pathlib import Path

import yaml

from .contracts import ROOT

CLAIM = 'acceptance definitions; framework_self results come from tests/acceptance, target_project execution and conformance belong to the target project'
RESULTS = 'docs/quality/v1.4/self-acceptance-results.json'


def self_results(root=ROOT):
    path = Path(root) / RESULTS
    if not path.is_file():
        return {}, None
    record = json.loads(path.read_text(encoding='utf-8'))
    return record.get('results') or {}, record.get('head')


def _verification_kind(test):
    kind = (test.get('automation') or {}).get('kind', 'none')
    if test.get('type') in ('manual', 'review'):
        return 'human_review' if kind == 'none' else 'human_review_with_tooling'
    return 'automated'


def _execution(test, results, head):
    automation = test.get('automation') or {}
    recorded = results.get(test['id'])
    if recorded is not None:
        scope, status = 'framework_self', recorded
    else:
        scope, status = 'target_project', 'not_executed'
    return {'scope': scope, 'status': status, 'verified': status == 'passed', 'recorded_head': head if recorded is not None else None,
            'verification': _verification_kind(test),
            'executor': {'kind': automation.get('kind', 'none'), 'reference': automation.get('reference'),
                         'self_test': 'tests/acceptance/test_self_acceptance.py' if recorded is not None else None},
            'evidence_types': list(test.get('evidence') or []),
            'parameters': [{'name': p['name'], 'default': p['default'], 'source': p['source']} for p in test.get('parameters') or []]}


def acceptance_index(root=ROOT):
    """Return {control_id: {'domain', 'source', 'requirement_sources', 'tests'}} over every acceptance file."""
    results, head = self_results(root)
    index = {}
    for path in sorted((Path(root) / 'spec' / 'acceptance').glob('*.yaml')):
        document = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        for control_id, entry in (document.get('controls') or {}).items():
            entry = entry or {}
            tests = [dict(t, execution=_execution(t, results, head)) for t in entry.get('tests') or []]
            index[control_id] = {'domain': document.get('domain'), 'source': path.relative_to(root).as_posix(),
                                 'requirement_sources': list(entry.get('requirement_sources') or []), 'tests': tests}
    return index


def _summary(tests):
    by_type, by_verification = {}, {}
    for t in tests:
        by_type[t.get('type', 'unknown')] = by_type.get(t.get('type', 'unknown'), 0) + 1
        v = t['execution']['verification']; by_verification[v] = by_verification.get(v, 0) + 1
    executed = [t for t in tests if t['execution']['status'] != 'not_executed']
    passed = [t for t in executed if t['execution']['status'] == 'passed']
    return {'defined': len(tests), 'executed': len(executed), 'passed': len(passed), 'failed': sum(1 for t in executed if t['execution']['status'] == 'failed'),
            'framework_self': len(executed), 'target_project_not_executed': len(tests) - len(executed), 'unverified': len(tests) - len(passed),
            'by_type': by_type, 'by_verification': by_verification,
            'negative_path': sum(1 for t in tests if t.get('negative_path') is True), 'with_parameters': sum(1 for t in tests if t.get('parameters'))}


def acceptance_tests(control_id, root=ROOT):
    entry = acceptance_index(root).get(control_id)
    if entry is None:
        return {'control_id': control_id, 'domain': None, 'source': None, 'requirement_sources': [], 'tests': [], 'summary': _summary([]), 'claim': CLAIM}
    return {'control_id': control_id, **entry, 'summary': _summary(entry['tests']), 'claim': CLAIM}


def acceptance_summary(root=ROOT):
    index = acceptance_index(root)
    tests = [t for e in index.values() for t in e['tests']]
    per_control = {cid: _summary(e['tests']) for cid, e in sorted(index.items())}
    return {'controls': len(index), **_summary(tests), 'per_control': per_control, 'claim': CLAIM}
