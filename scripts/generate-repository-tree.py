# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

def main():
    skip={'__pycache__','.git'}
    lines=[]
    def walk(path,prefix=''):
        items=[p for p in sorted(path.iterdir(),key=lambda x:(x.is_file(),x.name.lower())) if p.name not in skip]
        for i,p in enumerate(items):
            last=i==len(items)-1; lines.append(prefix+('└── ' if last else '├── ')+p.name)
            if p.is_dir(): walk(p,prefix+('    ' if last else '│   '))
    lines.append('VCGF/')
    walk(ROOT)
    body="# Repository tree\n\n> AUTO-GENERATED — DO NOT EDIT MANUALLY\n\n```text\n"+'\n'.join(lines)+"\n```\n"
    hdr="<!--\nVCGF — Vibe Coding Governance Framework\nSPDX-FileCopyrightText: 2026 Eng. Hamada Sami\nSPDX-License-Identifier: Apache-2.0\nFounder & Maintainer: Eng. Hamada Sami\nEmail: i@hamada.io\nGitHub: https://github.com/Vibe-Coding-Commons\n-->\n\n"
    (ROOT/'REPOSITORY-TREE.md').write_text(hdr+body,encoding='utf-8'); print('generated repository tree')
if __name__=='__main__': main()
