# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Every operational file (checklists/, playbooks/, templates/) is mapped to at least one existing control in
spec/operational-control-map.yaml, every mapped file exists, and no mapped control is unknown. Also rejects tracking
parameters (utm_*) in canonical requirement packs, which are loaded into agent context."""
import re

from vcgf_lib import *


def main():
    errors = []
    doc = load_yaml(ROOT / 'spec/operational-control-map.yaml')
    known = set(control_index())
    mapped = doc.get('files') or {}
    operational = sorted(rel(p) for d in ('checklists', 'playbooks', 'templates') for p in (ROOT / d).rglob('*.md') if p.name != 'README.md')
    for f in operational:
        if f not in mapped:
            errors.append(f'{f}: operational file has no Control-ID mapping')
    for f, controls in mapped.items():
        if not (ROOT / f).is_file():
            errors.append(f'operational map: {f} does not exist')
        if not controls:
            errors.append(f'operational map: {f} maps to no control')
        for cid in controls or []:
            if cid not in known:
                errors.append(f'operational map: {f}: unknown control {cid}')
    for p in sorted((ROOT / 'packs' / 'requirements').glob('*.md')):
        if re.search(r'[?&]utm_[a-z]+=', p.read_text(encoding='utf-8')):
            errors.append(f'{rel(p)}: tracking parameter in a requirement pack loaded into context')
    fail_if(errors)
    print(f'PASS validate-operational-map: {len(operational)} operational files mapped to controls')


if __name__ == '__main__':
    main()
