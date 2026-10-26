# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import argparse
from vcgf_lib import *

def main():
    ap=argparse.ArgumentParser(description='Generate REPOSITORY-TREE.md from the tracked repository files.')
    ap.add_argument('--check',action='store_true',help='compare with the existing tree and exit 1 when stale; writes nothing')
    args=ap.parse_args()
    # Tracked files only (vcgf_lib.all_files); a directory appears when it contains a tracked file.
    tree={}
    for p in all_files():
        node=tree
        for part in rel(p).split('/'): node=node.setdefault(part,{})
    lines=['VCGF/']
    def walk(node,prefix=''):
        items=sorted(node.items(),key=lambda kv:(not kv[1],kv[0].lower(),kv[0]))  # directories first
        for i,(name,child) in enumerate(items):
            last=i==len(items)-1; lines.append(prefix+('└── ' if last else '├── ')+name)
            if child: walk(child,prefix+('    ' if last else '│   '))
    walk(tree)
    body="# Repository tree\n\n> AUTO-GENERATED — DO NOT EDIT MANUALLY\n\n```text\n"+'\n'.join(lines)+"\n```\n"
    hdr="<!--\nVCGF — Vibe Coding Governance Framework\nSPDX-FileCopyrightText: 2026 Eng. Hamada Sami\nSPDX-License-Identifier: Apache-2.0\nFounder & Maintainer: Eng. Hamada Sami\nEmail: i@hamada.io\nGitHub: https://github.com/Vibe-Coding-Commons\n-->\n\n"
    code=write_generated(ROOT/'REPOSITORY-TREE.md',hdr+body,'generate-repository-tree',args.check)
    if not args.check: print('generated repository tree')
    return code
if __name__=='__main__': raise SystemExit(main())
