# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Dependency integrity: the repository's own requirements are exact pins (==), every GitHub Action is SHA-pinned, and the
frozen Smart UI package's range-pinned requirements are reported (its file is frozen; ranges there are a known gap)."""
import re

from vcgf_lib import *

EXACT = re.compile(r'^[A-Za-z0-9_.\-\[\]]+==[0-9][A-Za-z0-9_.\-+]*$')
ACTION = re.compile(r'^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)', re.M)


def main():
    errors = []; pins = 0
    for rel_path in ['requirements-dev.txt']:
        for line in (ROOT / rel_path).read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if not EXACT.match(line):
                errors.append(f'{rel_path}: dependency must be an exact pin (==): {line}')
            pins += 1
    actions = 0
    for wf in sorted((ROOT / '.github' / 'workflows').glob('*.yml')):
        for name, ref in ACTION.findall(wf.read_text(encoding='utf-8')):
            actions += 1
            if not re.fullmatch(r'[0-9a-f]{40}', ref):
                errors.append(f'{rel(wf)}: action {name} is not pinned to a full commit SHA ({ref})')
    pack_req = ROOT / 'packs/ux/smart-ui/requirements.txt'
    ranged = []
    if pack_req.is_file():
        ranged = [l.strip() for l in pack_req.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#') and not EXACT.match(l.strip())]
    if not (ROOT / '.github' / 'dependabot.yml').is_file():
        errors.append('.github/dependabot.yml missing')
    fail_if(errors)
    note = f'; frozen Smart UI package keeps {len(ranged)} range-pinned requirement(s) (known gap, package revision item)' if ranged else ''
    print(f'PASS validate-dependencies: {pins} exact pins, {actions} SHA-pinned action uses{note}')


if __name__ == '__main__':
    main()
