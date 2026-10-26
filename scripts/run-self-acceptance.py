# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Execute the acceptance tests whose system under test is VCGF itself and record the results.

tests/acceptance/test_self_acceptance.py implements acceptance definitions (spec/acceptance/*.yaml) that describe the
framework's own Router, loader, contracts, evidence gate and validators. Each test method is named after the acceptance
identifier (VCGF_GOV_001_AT03 -> VCGF-GOV-001-AT03). This runner executes them with pytest and writes
docs/quality/v1.4/self-acceptance-results.json: {id: passed|failed} plus the commit the run belongs to.

Scope is explicit: these results cover the framework as the system under test. Acceptance definitions that describe a
target project remain not_executed; nothing here infers project conformance.

  --check   run and fail unless the stored results file matches (ignores the recording metadata)
"""
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'docs' / 'quality' / 'v1.4' / 'self-acceptance-results.json'
TESTS = ROOT / 'tests' / 'acceptance' / 'test_self_acceptance.py'


def run_suite():
    with tempfile.TemporaryDirectory() as temp:
        junit = Path(temp) / 'junit.xml'
        subprocess.run([sys.executable, '-B', '-m', 'pytest', str(TESTS), '-q', '-p', 'no:cacheprovider', f'--junitxml={junit}'],
                       cwd=ROOT, capture_output=True, text=True)
        tree = ET.parse(junit)
    results = {}
    for case in tree.iter('testcase'):
        name = case.get('name', '')
        if not name.startswith('test_VCGF_'):
            continue
        test_id = name[len('test_'):].split('__')[0].replace('_', '-')
        failed = any(child.tag in ('failure', 'error') for child in case)
        skipped = any(child.tag == 'skipped' for child in case)
        status = 'failed' if failed else ('skipped' if skipped else 'passed')
        if results.get(test_id) == 'failed':
            continue
        results[test_id] = status if results.get(test_id) != 'failed' else 'failed'
    return results


def head():
    out = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    return out.stdout.strip() or 'unknown'


def main():
    check = '--check' in sys.argv
    results = run_suite()
    record = {'$comment': 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0',
              'scope': 'framework_self', 'claim': 'results for VCGF as the system under test; target-project acceptance remains not_executed and no project conformance is inferred',
              'suite': 'tests/acceptance/test_self_acceptance.py', 'head': head(),
              'counts': {'executed': len(results), 'passed': sum(1 for v in results.values() if v == 'passed'), 'failed': sum(1 for v in results.values() if v == 'failed'), 'skipped': sum(1 for v in results.values() if v == 'skipped')},
              'results': dict(sorted(results.items()))}
    if check:
        if not RESULTS.is_file():
            print('FAIL run-self-acceptance: results file missing; run without --check'); return 1
        stored = json.loads(RESULTS.read_text(encoding='utf-8'))
        if stored.get('results') != record['results']:
            print('FAIL run-self-acceptance: stored results differ from this run'); print(json.dumps({'stored': stored.get('results'), 'now': record['results']}, indent=1)); return 1
        if record['counts']['failed']:
            print(f"FAIL run-self-acceptance: {record['counts']['failed']} self-acceptance test(s) failed"); return 1
        print(f"PASS run-self-acceptance: {record['counts']['executed']} executed, {record['counts']['passed']} passed, {record['counts']['failed']} failed (framework_self)"); return 0
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(record['counts']), 'written to', RESULTS.relative_to(ROOT).as_posix())
    return 1 if record['counts']['failed'] else 0


if __name__ == '__main__':
    sys.exit(main())
