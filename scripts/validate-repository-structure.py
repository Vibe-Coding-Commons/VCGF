# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

def main():
    errors=[]
    required_dirs=['.github/ISSUE_TEMPLATE','.github/workflows','controls','spec','profiles','schemas','platforms','templates','checklists','playbooks','examples','docs/project-history/v1.0.0','docs/references','legal','scripts','assets/brand']
    required_files=['README.md','README.ar.md','LICENSE','NOTICE.md','COPYRIGHT.md','AUTHORS.md','CITATION.cff','VERSION','CHANGELOG.md','ROADMAP.md','GOVERNANCE.md','SECURITY.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md','VCGF-MANIFEST.yaml','FILE-MANIFEST.md','REPOSITORY-TREE.md','.gitignore','.gitattributes','.editorconfig']
    for d in required_dirs:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory {d}")
    for f in required_files:
        if not (ROOT/f).is_file(): errors.append(f"missing file {f}")
    for old in ['FILE-INVENTORY.md','CONFLICT-REPORT.md','MIGRATION-MAP.md','TRACEABILITY.md','VCGF-ARCHITECTURE-REPORT.md','FINAL-QA-AUDIT.md']:
        if (ROOT/old).exists(): errors.append(f"historical build file must not remain in root: {old}")
    banned={'.git','node_modules','.DS_Store','Thumbs.db'}
    for p in ROOT.rglob('*'):
        if p.name in banned: errors.append(f"forbidden release path {rel(p)}")
        if p.is_file() and p.stat().st_size==0: errors.append(f"empty file {rel(p)}")
        if p.is_file() and p.suffix.lower() in {'.zip','.bak','.tmp','.swp'}: errors.append(f"forbidden release file {rel(p)}")
    fail_if(errors); print('PASS validate-repository-structure')
if __name__=='__main__': main()
