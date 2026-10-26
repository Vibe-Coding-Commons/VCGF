# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Compliance evaluator for target projects: applicable controls, recorded results, verified evidence, honest statuses."""
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT, validate_contract
from runtime.compliance import applicable_controls, evaluate_compliance

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)


class ComplianceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup); self.root = Path(self.temp.name)
        self.record = json.loads((ROOT / 'tests/fixtures/v1.1/acceptance-results.json').read_text(encoding='utf-8'))['record']
        for r in self.record['results']:
            for a in r['evidence']:
                path = self.root / a['reference']; path.write_text(json.dumps({'synthetic': a['artifact_id']}))
                a['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()

    def evaluate(self, record=None, controls=('VCGF-UX-004',), **kw):
        return evaluate_compliance(record or self.record, self.root, list(controls), now=NOW, **kw)

    def test_fixture_is_a_valid_contract_and_compliant_for_its_control(self):
        self.assertEqual(validate_contract('acceptance-results', self.record), [])
        out = self.evaluate()
        self.assertEqual(out['status'], 'COMPLIANT'); self.assertEqual(out['controls']['VCGF-UX-004']['status'], 'COMPLIANT')
        self.assertEqual(out['controls']['VCGF-UX-004']['passed'], 4); self.assertIn('no project test was executed', out['claim'])

    def test_definitions_without_results_are_not_tested_never_passed(self):
        out = self.evaluate(controls=['VCGF-UX-004', 'VCGF-UX-003'])
        self.assertEqual(out['status'], 'NOT_COMPLIANT'); self.assertEqual(out['controls']['VCGF-UX-003']['status'], 'NOT_TESTED')
        self.assertEqual(out['controls']['VCGF-UX-003']['passed'], 0); self.assertEqual(out['counts'], {'COMPLIANT': 1, 'FAILED': 0, 'NOT_TESTED': 1})

    def test_pass_without_valid_evidence_fails(self):
        changed = copy.deepcopy(self.record); changed['results'][1]['evidence'][0]['sha256'] = '0' * 64
        out = self.evaluate(changed); self.assertEqual(out['controls']['VCGF-UX-004']['status'], 'FAILED')
        self.assertTrue(any('evidence changed' in d['reason'] for d in out['controls']['VCGF-UX-004']['detail']))
        missing = copy.deepcopy(self.record); missing['results'][1]['evidence'][0]['reference'] = 'absent.json'
        self.assertTrue(any('evidence missing/unsafe' in d['reason'] for d in self.evaluate(missing)['controls']['VCGF-UX-004']['detail']))
        traversal = copy.deepcopy(self.record); traversal['results'][1]['evidence'][0]['reference'] = '../x.json'
        self.assertEqual(self.evaluate(traversal)['controls']['VCGF-UX-004']['status'], 'FAILED')
        empty = copy.deepcopy(self.record); empty['results'][1]['evidence'] = []
        self.assertTrue(any('PASS without evidence' in d['reason'] for d in self.evaluate(empty)['controls']['VCGF-UX-004']['detail']))

    def test_human_review_requires_reviewer_and_skip_is_not_satisfied(self):
        no_reviewer = copy.deepcopy(self.record); del no_reviewer['results'][0]['reviewer']
        self.assertTrue(any('without a reviewer' in d['reason'] for d in self.evaluate(no_reviewer)['controls']['VCGF-UX-004']['detail']))
        skipped = copy.deepcopy(self.record); skipped['results'][2].update(status='SKIP', notes='not in scope this sprint')
        out = self.evaluate(skipped); self.assertEqual(out['controls']['VCGF-UX-004']['status'], 'NOT_TESTED'); self.assertEqual(out['status'], 'NOT_COMPLIANT')
        failed = copy.deepcopy(self.record); failed['results'][2]['status'] = 'FAIL'
        self.assertEqual(self.evaluate(failed)['controls']['VCGF-UX-004']['status'], 'FAILED')

    def test_freshness_binding_and_unknown_tests(self):
        stale = copy.deepcopy(self.record); stale['valid_until'] = '2026-10-03T12:00:00Z'
        out = self.evaluate(stale); self.assertEqual(out['status'], 'INVALID'); self.assertIn('stale/future results', out['errors'])
        out = self.evaluate(expected={'code_sha256': 'e' * 64}); self.assertIn('changed results binding: code_sha256', out['errors'])
        foreign = copy.deepcopy(self.record); foreign['results'][0]['test_id'] = 'VCGF-SEC-001-AT01'
        out = self.evaluate(foreign); self.assertTrue(any('outside the applicable set' in e for e in out['errors']))
        future = copy.deepcopy(self.record); future['results'][0]['executed_at'] = '2026-10-03T13:00:00Z'
        self.assertEqual(self.evaluate(future)['controls']['VCGF-UX-004']['status'], 'FAILED')

    def test_contract_rejections(self):
        bad = copy.deepcopy(self.record); bad['results'][0]['status'] = 'PASSED'
        self.assertEqual(self.evaluate(bad)['status'], 'INVALID')
        bad = copy.deepcopy(self.record); bad['unapproved'] = True
        self.assertTrue(validate_contract('acceptance-results', bad))

    def test_applicable_controls_from_profile_and_route(self):
        controls, profile = applicable_controls(profile='baseline'); self.assertEqual(len(controls), 25); self.assertEqual(profile, 'baseline')
        with self.assertRaises(ValueError):
            applicable_controls(profile='platinum')
        with self.assertRaises(ValueError):
            applicable_controls()

    def test_cli_round_trip(self):
        results = self.root / 'results.json'; results.write_text(json.dumps(self.record))
        env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'compliance', str(results), '--artifact-root', str(self.root), '--profile', 'high-assurance', '--as-of', '2026-10-03T12:30:00Z'],
                             capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
        self.assertEqual(run.returncode, 1, run.stderr)  # 88 applicable controls, only one with results
        payload = json.loads(run.stdout); self.assertEqual(payload['status'], 'NOT_COMPLIANT'); self.assertEqual(payload['counts']['COMPLIANT'], 1); self.assertEqual(payload['applicable_controls'], 88)


if __name__ == '__main__':
    unittest.main()
