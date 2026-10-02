# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import re
from vcgf_lib import ROOT, rel, fail_if

VENDORS = re.compile(r'\b(?:Lovable|Claude|Anthropic|Bolt|StackBlitz|Replit|Cursor|Vercel)\b|\bv0\b', re.I)
CORE_DIRS = ('controls','spec','profiles','schemas')


def main():
    errors=[]
    for d in CORE_DIRS:
        for p in (ROOT/d).rglob('*'):
            if not p.is_file():
                continue
            if p.suffix.lower() not in {'.md','.yaml','.yml','.json'}:
                continue
            text=p.read_text(encoding='utf-8', errors='replace')
            m=VENDORS.search(text)
            if m:
                errors.append(f"{rel(p)}: vendor-specific term in logical Core: {m.group(0)}")
    fail_if(errors)
    print('PASS validate-vendor-neutral-core')

if __name__=='__main__':
    main()
