# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import re
from vcgf_lib import *

def main():
    known=set(control_index()); errors=[]
    pattern=re.compile(r'VCGF-(?:GOV|AI|ARCH|SEC|IAM|DATA|PRIV|DB|API|SECR|DEP|FILE|AUDIT|TEST|REL|OPS|IR)-\d{3}')
    for p in text_files():
        rp=rel(p)
        if rp.startswith('docs/project-history/') or rp=='LICENSE': continue
        try: text=p.read_text(encoding='utf-8')
        except UnicodeDecodeError: continue
        for cid in sorted(set(pattern.findall(text))):
            if cid not in known: errors.append(f"{rp}: unknown control reference {cid}")
        if ('VCGF-' + 'SEC-SECRET-') in text: errors.append(f"{rp}: legacy pre-v1 secrets prefix remains")
    fail_if(errors); print("PASS validate-cross-references")
if __name__=="__main__": main()
