# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import argparse
from vcgf_lib import *

def purpose(path):
    rp=rel(path)
    if rp.startswith('controls/'): return 'Canonical normative control or domain index'
    if rp.startswith('platforms/'): return 'Platform adapter implementation, mapping, verification, or asset'
    if rp.startswith('profiles/'): return 'VCGF assurance profile'
    if rp.startswith('schemas/'): return 'Machine-validation schema'
    if rp.startswith('scripts/'): return 'Framework validation or generation automation'
    if rp.startswith('.github/workflows/'): return 'GitHub Actions validation workflow'
    if rp.startswith('templates/'): return 'Reusable governance artifact'
    if rp.startswith('checklists/'): return 'Operational verification checklist'
    if rp.startswith('playbooks/'): return 'Operational execution playbook'
    if rp.startswith('examples/'): return 'Adoption example'
    if rp.startswith('docs/project-history/'): return 'v1.0.0 migration and release traceability record'
    if rp.startswith('docs/references/'): return 'External standards/reference documentation'
    if rp.startswith('docs/'): return 'Framework explanatory documentation'
    if rp.startswith('legal/'): return 'Legal, attribution, or trademark guidance'
    return 'Repository governance, release, identity, or project metadata'

def main():
    ap=argparse.ArgumentParser(description='Generate FILE-MANIFEST.md from the tracked repository files.')
    ap.add_argument('--check',action='store_true',help='compare with the existing manifest and exit 1 when stale; writes nothing')
    args=ap.parse_args()
    generated={'FILE-MANIFEST.md','REPOSITORY-TREE.md','spec/control-catalog.yaml'}
    release_version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
    rows=[]
    # Tracked files only (vcgf_lib.all_files): untracked local files cannot change the manifest.
    for p in sorted(all_files(),key=rel):
        rp=rel(p)
        if rp=='FILE-MANIFEST.md': continue
        category=rp.split('/',1)[0] if '/' in rp else 'root'
        rows.append((rp,purpose(p),category,'Generated' if rp in generated else 'Canonical/maintained',release_version))
    table='\n'.join('| '+ ' | '.join(r).replace('\n',' ') +' |' for r in rows)
    hdr="<!--\nVCGF — Vibe Coding Governance Framework\nSPDX-FileCopyrightText: 2026 Eng. Hamada Sami\nSPDX-License-Identifier: Apache-2.0\nFounder & Maintainer: Eng. Hamada Sami\nEmail: i@hamada.io\nGitHub: https://github.com/Vibe-Coding-Commons\n-->\n\n"
    body=f"# File manifest\n\n> AUTO-GENERATED — DO NOT EDIT MANUALLY\n\nFiles listed: **{len(rows)}**\n\n| Path | Purpose | Category | Canonical / Generated | Version relevance |\n|---|---|---|---|---|\n{table}\n"
    code=write_generated(ROOT/'FILE-MANIFEST.md',hdr+body,'generate-file-manifest',args.check)
    if not args.check: print(f'generated file manifest: {len(rows)} entries')
    return code
if __name__=='__main__': raise SystemExit(main())
