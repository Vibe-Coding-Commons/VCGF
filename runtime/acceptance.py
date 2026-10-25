# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Read-only access to the control acceptance tests in spec/acceptance/*.yaml (see spec/acceptance/README.md).

Defined is not executed: every test carries an execution state that is always `not_executed` inside this repository.
A target project records results against the test identifiers; manual tests without a recorded result stay unverified.
"""
from pathlib import Path

import yaml

from .contracts import ROOT

CLAIM = 'acceptance definitions only; execution, results and conformance belong to the target project'


def _execution(test):
    automation = test.get('automation') or {}
    return {'status': 'not_executed', 'result': None, 'verified': False,
            'executor': {'kind': automation.get('kind', 'none'), 'reference': automation.get('reference')},
            'evidence_types': list(test.get('evidence') or []),
            'parameters': [{'name': p['name'], 'default': p['default'], 'source': p['source']} for p in test.get('parameters') or []]}


def acceptance_index(root=ROOT):
    """Return {control_id: {'domain', 'source', 'requirement_sources', 'tests'}} over every acceptance file."""
    index = {}
    for path in sorted((Path(root) / 'spec' / 'acceptance').glob('*.yaml')):
        document = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        for control_id, entry in (document.get('controls') or {}).items():
            entry = entry or {}
            tests = [dict(t, execution=_execution(t)) for t in entry.get('tests') or []]
            index[control_id] = {'domain': document.get('domain'), 'source': path.relative_to(root).as_posix(),
                                 'requirement_sources': list(entry.get('requirement_sources') or []), 'tests': tests}
    return index


def _summary(tests):
    by_type = {}
    for t in tests:
        by_type[t.get('type', 'unknown')] = by_type.get(t.get('type', 'unknown'), 0) + 1
    return {'defined': len(tests), 'executed': 0, 'passed': 0, 'unverified': len(tests), 'by_type': by_type,
            'negative_path': sum(1 for t in tests if t.get('negative_path') is True),
            'with_parameters': sum(1 for t in tests if t.get('parameters'))}


def acceptance_tests(control_id, root=ROOT):
    entry = acceptance_index(root).get(control_id)
    if entry is None:
        return {'control_id': control_id, 'domain': None, 'source': None, 'requirement_sources': [], 'tests': [],
                'summary': _summary([]), 'claim': CLAIM}
    return {'control_id': control_id, **entry, 'summary': _summary(entry['tests']), 'claim': CLAIM}


def acceptance_summary(root=ROOT):
    index = acceptance_index(root)
    tests = [t for e in index.values() for t in e['tests']]
    per_control = {cid: _summary(e['tests']) for cid, e in sorted(index.items())}
    return {'controls': len(index), **_summary(tests), 'per_control': per_control, 'claim': CLAIM}
