# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Validate platforms/enforcement-matrix.yaml: every adapter rated for every mechanism with an honest status, every referenced
file present, `available` only where an exercising test or workflow exists, protected paths real."""
from vcgf_lib import *

STATUSES = {'available', 'configurable', 'unverified', 'unsupported'}


def main():
    errors = []
    doc = load_yaml(ROOT / 'platforms/enforcement-matrix.yaml')
    if doc.get('matrix_version') != '1.0.0': errors.append('platforms/enforcement-matrix.yaml: matrix_version must be 1.0.0')
    mechanisms = doc.get('mechanisms') or {}
    for name, m in mechanisms.items():
        for key in ('description', 'reference', 'exercised_by'):
            if not str(m.get(key) or '').strip(): errors.append(f'mechanism {name}: {key} required')
        ref = m.get('reference')
        if ref and not (ROOT / ref).exists(): errors.append(f'mechanism {name}: reference {ref} does not exist')
        if m.get('exercised_by') != 'none (platform surface; documented only)':
            for item in str(m.get('exercised_by')).split(','):
                item = item.strip()
                if item and not (ROOT / item).exists(): errors.append(f'mechanism {name}: exercised_by {item} does not exist')
    adapters = sorted(d.name for d in (ROOT / 'platforms').iterdir() if d.is_dir() and not d.name.startswith('_') and (d / 'adapter.yaml').is_file())
    rated = doc.get('adapters') or {}
    for aid in adapters:
        if aid not in rated: errors.append(f'adapter {aid} missing from the enforcement matrix'); continue
        for mech in mechanisms:
            status = rated[aid].get(mech)
            if status not in STATUSES: errors.append(f'adapter {aid}: mechanism {mech} status must be one of {sorted(STATUSES)} (got {status!r})')
            elif status == 'available' and mechanisms[mech].get('exercised_by', '').startswith('none'):
                errors.append(f'adapter {aid}: mechanism {mech} cannot be available without an exercising test or workflow')
        for mech in rated[aid]:
            if mech not in mechanisms: errors.append(f'adapter {aid}: unknown mechanism {mech}')
    for aid in rated:
        if aid not in adapters: errors.append(f'enforcement matrix rates unknown adapter {aid}')
    for p in doc.get('protected_paths') or []:
        if not (ROOT / p).exists(): errors.append(f'protected path {p} does not exist')
    fail_if(errors)
    print(f'PASS validate-enforcement: {len(adapters)} adapters x {len(mechanisms)} mechanisms, {len(doc.get("protected_paths") or [])} protected paths')


if __name__ == '__main__':
    main()
