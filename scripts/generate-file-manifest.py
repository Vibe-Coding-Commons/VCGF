# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

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
    generated={'FILE-MANIFEST.md','REPOSITORY-TREE.md','spec/control-catalog.yaml'}
    rows=[]
    for p in sorted((x for x in ROOT.rglob('*') if x.is_file()),key=lambda x:rel(x)):
        rp=rel(p)
        if rp=='FILE-MANIFEST.md': continue
        category=rp.split('/',1)[0] if '/' in rp else 'root'
        rows.append((rp,purpose(p),category,'Generated' if rp in generated else 'Canonical/maintained','1.0.0'))
    table='\n'.join('| '+ ' | '.join(r).replace('\n',' ') +' |' for r in rows)
    hdr="<!--\nVCGF — Vibe Coding Governance Framework\nSPDX-FileCopyrightText: 2026 Eng. Hamada Sami\nSPDX-License-Identifier: Apache-2.0\nFounder & Maintainer: Eng. Hamada Sami\nEmail: i@hamada.io\nGitHub: https://github.com/Vibe-Coding-Commons\n-->\n\n"
    body=f"# File manifest\n\n> AUTO-GENERATED — DO NOT EDIT MANUALLY\n\nFiles listed: **{len(rows)}**\n\n| Path | Purpose | Category | Canonical / Generated | Version relevance |\n|---|---|---|---|---|\n{table}\n"
    (ROOT/'FILE-MANIFEST.md').write_text(hdr+body,encoding='utf-8'); print(f'generated file manifest: {len(rows)} entries')
if __name__=='__main__': main()
