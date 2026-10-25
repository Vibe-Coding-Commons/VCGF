# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Read-only access to the control acceptance tests in spec/acceptance/*.yaml (see spec/acceptance/README.md).

The tests describe what a target project must demonstrate; nothing here executes them or infers conformance.
"""
from pathlib import Path

import yaml

from .contracts import ROOT


def acceptance_index(root=ROOT):
    """Return {control_id: {'domain', 'source', 'requirement_sources', 'tests'}} over every acceptance file."""
    index = {}
    for path in sorted((Path(root) / 'spec' / 'acceptance').glob('*.yaml')):
        document = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        for control_id, entry in (document.get('controls') or {}).items():
            entry = entry or {}
            index[control_id] = {'domain': document.get('domain'), 'source': path.relative_to(root).as_posix(),
                                 'requirement_sources': list(entry.get('requirement_sources') or []),
                                 'tests': list(entry.get('tests') or [])}
    return index


def acceptance_tests(control_id, root=ROOT):
    entry = acceptance_index(root).get(control_id)
    if entry is None:
        return {'control_id': control_id, 'domain': None, 'source': None, 'requirement_sources': [], 'tests': [],
                'claim': 'acceptance definitions only; execution and conformance belong to the target project'}
    return {'control_id': control_id, **entry,
            'claim': 'acceptance definitions only; execution and conformance belong to the target project'}
