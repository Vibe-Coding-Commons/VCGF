# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from pathlib import Path
import yaml
from vcgf_lib import ROOT, rel, fail_if, parse_frontmatter, control_files


def main():
    errors=[]
    for p in sorted(list(ROOT.rglob('*.yaml')) + list(ROOT.rglob('*.yml')) + list(ROOT.rglob('*.cff'))):
        try:
            with p.open(encoding='utf-8') as f:
                yaml.safe_load(f)
        except Exception as e:
            errors.append(f"{rel(p)}: invalid YAML/CFF: {e}")
    for p in control_files():
        try:
            parse_frontmatter(p)
        except Exception as e:
            errors.append(f"{rel(p)}: invalid control front matter: {e}")
    # GitHub issue forms/templates require front matter to be the first document content.
    for p in sorted((ROOT/'.github/ISSUE_TEMPLATE').glob('*.md')):
        text=p.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            errors.append(f"{rel(p)}: GitHub issue template front matter is not first")
            continue
        end=text.find('\n---\n',4)
        if end < 0:
            errors.append(f"{rel(p)}: unterminated GitHub issue template front matter")
            continue
        try:
            data=yaml.safe_load(text[4:end]) or {}
            for key in ('name','about'):
                if key not in data:
                    errors.append(f"{rel(p)}: missing issue template key {key}")
        except Exception as e:
            errors.append(f"{rel(p)}: invalid issue template YAML: {e}")
    fail_if(errors)
    print('PASS validate-yaml')

if __name__=='__main__':
    main()
