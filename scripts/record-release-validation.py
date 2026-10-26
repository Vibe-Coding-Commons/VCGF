# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Record a local release-validation run bound to the commit, environment and tool versions it ran on.

Writes docs/quality/v<major.minor>/release-validation-local.json with: candidate commit, dirty-tree flag, OS, Python,
dependency versions, the gate result, the self-acceptance summary and the test-suite counts passed on the command line.
It executes the read-only gate and the self-acceptance check; it does not run the full test suite (pass its counts with
--tests "passed,failed,skipped" from the run you performed). Local results are not CI results and not a release decision.
"""
import argparse
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return out.returncode, (out.stdout + out.stderr).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--tests', help='"passed,failed,skipped" counts of the full pytest run performed on this tree')
    parser.add_argument('--notes', default='')
    args = parser.parse_args()
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    head = run(['git', 'rev-parse', 'HEAD'])[1]
    dirty = bool(run(['git', 'status', '--porcelain'])[1])
    gate_code, gate_out = run([sys.executable, '-B', 'scripts/release-quality-gate.py'])
    self_code, self_out = run([sys.executable, '-B', 'scripts/run-self-acceptance.py', '--check'])
    deps = {}
    for line in (ROOT / 'requirements-dev.txt').read_text(encoding='utf-8').splitlines():
        if '==' in line and not line.startswith('#'):
            name, ver = line.strip().split('==', 1); deps[name] = ver
    tests = None
    if args.tests:
        p, f, s = (int(x) for x in args.tests.split(','))
        tests = {'passed': p, 'failed': f, 'skipped': s, 'source': 'full pytest run on this tree, counts supplied by the operator'}
    record = {
        '$comment': 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0',
        'framework_version': version, 'candidate_commit': head, 'working_tree_dirty': dirty,
        'environment': {'os': platform.platform(), 'python': platform.python_version(), 'dependencies': deps},
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'release_quality_gate': {'status': 'PASS' if gate_code == 0 else 'FAIL', 'tail': gate_out.splitlines()[-1] if gate_out else ''},
        'self_acceptance': {'status': 'PASS' if self_code == 0 else 'FAIL', 'summary': self_out.splitlines()[-1] if self_out else ''},
        'test_suite': tests or {'status': 'NOT_RECORDED'},
        'ci': 'NOT_TESTED: no CI run observed for this commit (local record only)',
        'claims': 'local validation bound to the commit above; not independent review, not a release decision, not production admission',
        'notes': args.notes,
    }
    major, minor = version.split('.')[:2]
    out = ROOT / 'docs' / 'quality' / f'v{major}.{minor}' / 'release-validation-local.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'written': out.relative_to(ROOT).as_posix(), 'gate': record['release_quality_gate']['status'], 'self_acceptance': record['self_acceptance']['status'], 'dirty': dirty}))
    return 0 if gate_code == 0 and self_code == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
