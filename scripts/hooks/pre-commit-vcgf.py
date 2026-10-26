#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Git pre-commit hook: refuse a commit that changes canonical governance files without an explicit allowance, and run
the fast validators on the staged tree.

Install (per clone, never automatically): copy or symlink this file to .git/hooks/pre-commit, or configure
`git config core.hooksPath scripts/hooks` after reviewing the scripts. Exit 1 blocks the commit.
Allowance: VCGF_GOVERNANCE_APPROVAL=<path to an approval record> (action governance-change, approved, unexpired, naming
the staged governance paths in resources). A bare environment flag never unlocks the commit.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAST_VALIDATORS = ['validate-controls.py', 'validate-profiles.py', 'validate-applicability.py', 'validate-acceptance.py', 'validate-control-cards.py',
                   'validate-schemas.py', 'validate-yaml.py', 'validate-enforcement.py']


def staged_paths(repo=ROOT):
    out = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMRD'], cwd=repo, capture_output=True, text=True)
    return [line.strip().replace('\\', '/') for line in out.stdout.splitlines() if line.strip()]


def main():
    sys.path.insert(0, str(ROOT / 'scripts' / 'hooks'))
    from importlib import import_module
    guard = import_module('guard-governance-files'.replace('-', '_')) if False else None  # module name has dashes; import by path below
    import importlib.util
    spec = importlib.util.spec_from_file_location('guard', ROOT / 'scripts' / 'hooks' / 'guard-governance-files.py')
    guard = importlib.util.module_from_spec(spec); spec.loader.exec_module(guard)
    prefixes = guard.protected_paths(); approval_path = os.environ.get('VCGF_GOVERNANCE_APPROVAL', '').strip()
    hits = [p for p in staged_paths() if guard.is_protected(p, prefixes)]
    if hits:
        decision = guard.decide({'tool_name': 'Write', 'tool_input': {'file_path': hits[0]}}, prefixes, approval_path)
        if decision['decision'] == 'block' or guard.covers(guard.load_approval(approval_path)[0] or {'resources': []}, hits):
            print('pre-commit: canonical governance files changed without a covering approval record (VCGF_GOVERNANCE_APPROVAL):'); print('\n'.join('  ' + h for h in hits)); print(decision['reason']); return 1
        print(f'pre-commit: governance change covered by approval record: {len(hits)} file(s)')
    failed = []
    for name in FAST_VALIDATORS:
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts' / name)], cwd=ROOT, capture_output=True, text=True)
        if run.returncode != 0:
            failed.append(name); print(f'pre-commit: {name} FAILED\n{(run.stdout + run.stderr)[-800:]}')
    if failed:
        return 1
    print(f'pre-commit: {len(FAST_VALIDATORS)} validators passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
