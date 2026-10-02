# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import re
from vcgf_lib import *

def main():
    errors=[]; forbidden=[r'\b'+'TO'+'DO'+r'\b', r'\b'+'FIX'+'ME'+r'\b', r'\b'+'T'+'BD'+r'\b', 'Lo'+'rem ipsum', 'Com'+'ing soon']
    for p in text_files():
        rp=rel(p)
        if rp.startswith('docs/project-history/'): continue
        text=p.read_text(encoding='utf-8',errors='replace')
        for pat in forbidden:
            if re.search(pat,text,re.I): errors.append(f"{rp}: forbidden release marker matched {pat}")
    fail_if(errors); print("PASS validate-placeholders")
if __name__=='__main__': main()
