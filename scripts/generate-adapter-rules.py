# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Explicit opt-in candidates. Does not install or overwrite legacy rules."""
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
template=(ROOT/'templates/adapters/runtime-rules.template.md').read_text()
errors=[]
for directory in sorted((ROOT/'platforms').iterdir()):
    if not (directory/'adapter.yaml').is_file() or directory.name.startswith('_'):continue
    target=directory/'rules/runtime.generated.md'
    if args.check:
        if not target.exists() or target.read_text()!=template:errors.append(directory.name)
    else:target.write_text(template)
print({'status':'FAIL' if errors else 'PASS','different':errors,'claim':'source equivalence only'})
sys.exit(bool(errors))
