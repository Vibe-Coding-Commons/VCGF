# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from pathlib import Path
import subprocess, sys
from vcgf_lib import ROOT

GENERATORS=['generate-control-catalog.py','generate-repository-tree.py','generate-file-manifest.py']
VALIDATORS=['validate-controls.py','validate-profiles.py','validate-adapters.py','validate-schemas.py','validate-yaml.py','validate-license.py','validate-cross-references.py','validate-vendor-neutral-core.py','validate-internal-links.py','validate-attribution.py','validate-placeholders.py','validate-version.py','validate-documentation.py','validate-repository-structure.py']

def run(name):
    p=subprocess.run([sys.executable,str(ROOT/'scripts'/name)],cwd=ROOT)
    if p.returncode: raise SystemExit(p.returncode)

def main():
    for s in GENERATORS: run(s)
    for s in VALIDATORS: run(s)
    print('PASS release-quality-gate')
if __name__=='__main__': main()
