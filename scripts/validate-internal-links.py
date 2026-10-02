# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import re, urllib.parse
from vcgf_lib import *

def main():
    errors=[]; rx=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        for target in rx.findall(text):
            target=target.strip().strip('<>')
            if not target or target.startswith(('#','http://','https://','mailto:')): continue
            raw=urllib.parse.unquote(target.split('#',1)[0])
            if not raw: continue
            dest=(p.parent/raw).resolve()
            try: dest.relative_to(ROOT.resolve())
            except ValueError: errors.append(f"{rel(p)}: link escapes repository: {target}"); continue
            if not dest.exists(): errors.append(f"{rel(p)}: broken relative link {target}")
    fail_if(errors); print("PASS validate-internal-links")
if __name__=="__main__": main()
