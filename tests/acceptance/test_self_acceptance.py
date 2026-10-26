# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Executable acceptance tests whose system under test is VCGF itself.

Each method implements one acceptance definition from spec/acceptance/*.yaml (its identifier is the method name with
dashes replaced by underscores; a suffix after a double underscore distinguishes several checks of one definition).
scripts/run-self-acceptance.py records the outcomes. These results say nothing about any target project."""
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
from runtime.router import route
from runtime.context import handoff
from runtime.evidence import evaluate

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)
ENV = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}


class SelfAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        cls.evidence = json.loads((ROOT / 'tests/fixtures/v1.1/evidence.json').read_text())['record']
        (cls.project / 'result.json').write_text('{"synthetic_test":true}')
        a = cls.evidence['artifacts'][0]; a['reference'] = 'result.json'; a['sha256'] = hashlib.sha256((cls.project / 'result.json').read_bytes()).hexdigest()
        cls.expected = {k: copy.deepcopy(cls.evidence[k]) for k in ['code_sha256', 'policy_sha256', 'environment', 'profile', 'scope', 'required_control_ids']}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def task(self, **extra):
        task = {'task_id': 'acceptance', 'intent': 'login', 'classification_confirmed': True, 'profile': 'high-assurance', 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:inspection'}}
        task.update(extra); return task

    def route(self, context=None, **extra):
        return route(self.task(**extra), copy.deepcopy(context or self.context), self.project, NOW)

    def gate(self, record, expected=None, **kw):
        return evaluate(record, self.project, expected or self.expected, now=NOW, **kw)

    def cli_route(self, task, context):
        with tempfile.TemporaryDirectory() as temp:
            Path(temp, 'task.json').write_text(json.dumps(task)); Path(temp, 'context.json').write_text(json.dumps(context))
            return subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'route', str(Path(temp, 'task.json')), str(Path(temp, 'context.json')),
                                   '--project-root', str(self.project), '--quiet'], capture_output=True, text=True, encoding='utf-8', env=ENV, cwd=ROOT)

    # ---- VCGF-AI-001-AT02 / VCGF-ARCH-003-AT01: inspection before routing ----
    def test_VCGF_AI_001_AT02(self):
        for inspection in [{'completed': False, 'evidence_ref': 'x'}, {'completed': True, 'evidence_ref': ''}]:
            r = self.route(inspection=inspection)
            self.assertEqual(r['route']['decision'], 'blocked'); self.assertIn('targeted inspection required', r['route']['blockers'])
            self.assertEqual(r['route']['loaded_control_ids'], []); self.assertEqual(r['active_context'], [])
        run = self.cli_route(self.task(intent='button-color', inspection={'completed': False, 'evidence_ref': None}), self.context)
        self.assertEqual(run.returncode, 1, run.stderr); self.assertIn('targeted inspection required', json.loads(run.stdout)['route']['blockers'])

    def test_VCGF_ARCH_003_AT01(self):
        ready = self.route(); self.assertEqual(ready['route']['decision'], 'ready_to_plan')
        blocked = self.route(inspection={'completed': False, 'evidence_ref': ''})
        self.assertEqual(blocked['route']['decision'], 'blocked'); self.assertIn('targeted inspection required', blocked['route']['blockers'])
        self.assertEqual(blocked['route']['loaded_control_ids'], [])
        run = self.cli_route(self.task(intent='button-color', inspection={'completed': False, 'evidence_ref': ''}), self.context)
        self.assertEqual(run.returncode, 1)

    # ---- VCGF-AI-002-AT03 / VCGF-AI-008-AT04: no assumed facts ----
    def test_VCGF_AI_002_AT03(self):
        absent = copy.deepcopy(self.context); absent['facts'] = [f for f in absent['facts'] if f['key'] != 'auth-model']
        expired = copy.deepcopy(self.context); expired['facts'][0]['expires_at'] = '2026-10-03T12:01:00Z'
        changed = copy.deepcopy(self.context); changed['facts'][0]['source']['content_sha256'] = '0' * 64
        unknown = copy.deepcopy(self.context); unknown['facts'][0].update(state='unknown', value=None, reason='authentication model not yet inspected')
        for name, ctx in [('absent', absent), ('expired', expired), ('changed', changed), ('unknown', unknown)]:
            with self.subTest(case=name):
                r = self.route(ctx)
                self.assertEqual(r['route']['decision'], 'blocked'); self.assertEqual(r['capabilities'], [])
                self.assertIn('unknown conditional dependency: identity/auth-model', r['route']['blockers'])
        other = copy.deepcopy(self.context); other['facts'][0]['value'] = 'magic-link'
        r = self.route(other)
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertIn('unsupported or unknown authentication model; inspect before recovery selection', r['route']['blockers'])

    def test_VCGF_AI_008_AT04(self):
        for kind in ['user', 'tool', 'official_documentation']:
            ctx = copy.deepcopy(self.context); ctx['facts'][0]['source']['kind'] = kind
            with self.subTest(kind=kind):
                r = self.route(ctx)
                self.assertEqual(r['invalid_facts'].get('auth-model'), 'external/user assertion requires trusted observation adapter', r['invalid_facts'])
                self.assertEqual(r['route']['decision'], 'blocked'); self.assertEqual(r['capabilities'], [])
        ctx = copy.deepcopy(self.context); ctx['facts'][0]['source']['content_sha256'] = '0' * 64
        r = self.route(ctx)
        self.assertEqual(r['invalid_facts'].get('auth-model'), 'source changed', r['invalid_facts']); self.assertEqual(r['capabilities'], [])

    # ---- VCGF-AI-006-AT01/AT04/AT05 and VCGF-AI-007-AT04: risk, signals, profiles ----
    def test_VCGF_AI_006_AT01(self):
        for intent in ['login', 'reset', 'admin', 'payment', 'migration', 'pii', 'authorization']:
            with self.subTest(intent=intent):
                r = self.route(intent=intent); self.assertEqual(r['route']['risk'], 'HIGH'); self.assertTrue(r['route']['approval_required'])
        r = self.route(intent='deletion'); self.assertEqual(r['route']['risk'], 'CRITICAL'); self.assertTrue(r['route']['approval_required'])
        prod = copy.deepcopy(self.context); prod['environment'] = 'production'
        r = self.route(prod, intent='button-color'); self.assertEqual(r['route']['risk'], 'HIGH'); self.assertTrue(r['route']['approval_required'])
        sensitive = copy.deepcopy(self.context); fact = copy.deepcopy(sensitive['facts'][0]); fact['key'] = 'sensitive-data'; fact['value'] = True; sensitive['facts'].append(fact)
        r = self.route(sensitive, intent='button-color'); self.assertEqual(r['route']['risk'], 'HIGH'); self.assertTrue(r['route']['approval_required'])

    def test_VCGF_AI_006_AT04(self):
        for signal in ['destructive', 'production-secrets', 'high-impact-payment', 'irreversible']:
            with self.subTest(signal=signal):
                r = self.route(intent='button-color', risk_signals=[signal])
                self.assertEqual(r['route']['risk'], 'CRITICAL'); self.assertIn('VCGF-REL-003', r['route']['selected_control_ids'])
        for signal in ['sensitive-data', 'privileged', 'unknown-impact']:
            with self.subTest(signal=signal):
                r = self.route(intent='button-color', risk_signals=[signal])
                self.assertEqual(r['route']['risk'], 'HIGH'); self.assertTrue(r['route']['approval_required']); self.assertNotIn('VCGF-REL-003', r['route']['selected_control_ids'])

    def test_VCGF_AI_006_AT05(self):
        prod = copy.deepcopy(self.context); prod['environment'] = 'production'
        r = self.route(prod, intent='button-color', profile='baseline')
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertEqual(r['route']['loaded_control_ids'], [])
        self.assertIn('confirmed profile below risk recommendation: production', r['route']['blockers'])
        for profile in ['baseline', 'production']:
            for extra in [{'intent': 'deletion'}, {'intent': 'button-color', 'risk_signals': ['destructive']}]:
                with self.subTest(profile=profile, **extra):
                    r = self.route(profile=profile, **extra)
                    self.assertEqual(r['route']['decision'], 'blocked'); self.assertIn('confirmed profile below risk recommendation: high-assurance', r['route']['blockers'])

    def test_VCGF_AI_007_AT04(self):
        r = self.route(overlay_remove_controls=['VCGF-SEC-001'])
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertIn('overlay cannot remove canonical or capability requirements', r['route']['blockers'])
        r = self.route(intent='button-color', risk_signals=['security-disablement'])
        self.assertEqual(r['route']['risk'], 'CRITICAL'); self.assertTrue(r['route']['approval_required']); self.assertIn('VCGF-REL-003', r['route']['selected_control_ids'])

    # ---- VCGF-AI-009-AT03: hand-off ----
    def test_VCGF_AI_009_AT03(self):
        r = self.route(inspection={'completed': False, 'evidence_ref': ''})
        record = handoff(self.context, r['route'])
        self.assertTrue(record['revalidate_before_use']); self.assertFalse(record['secrets_included'])
        self.assertEqual(record['context_sha256'], r['route']['context_sha256']); self.assertEqual(record['blockers'], r['route']['blockers'])

    # ---- VCGF-GOV-001-AT03 / VCGF-GOV-002-AT01: minimum governance and approval ----
    def test_VCGF_GOV_001_AT03(self):
        for intent, mode, profile in [('login', 'lean', 'baseline'), ('button-color', 'standard', 'production'), ('deletion', 'deep', 'high-assurance'), ('release', 'lean', 'high-assurance')]:
            with self.subTest(intent=intent, mode=mode, profile=profile):
                r = self.route(intent=intent, mode=mode, profile=profile)
                reason = next(x for x in r['route']['reasons'] if x['control_id'] == 'VCGF-GOV-001')
                self.assertEqual(reason['reason'], 'minimum task governance'); self.assertEqual(reason['source'], 'routing-policy.yaml')
        r = self.route(overlay_remove_controls=['VCGF-GOV-001'])
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertIn('overlay cannot remove canonical or capability requirements', r['route']['blockers'])
        self.assertEqual(r['route']['loaded_control_ids'], [])

    def test_VCGF_GOV_002_AT01(self):
        prod = copy.deepcopy(self.context); prod['environment'] = 'production'
        for r in [self.route(intent='admin'), self.route(intent='deletion'), self.route(intent='button-color', risk_signals=['privileged']), self.route(prod, intent='button-color')]:
            self.assertIn(r['route']['risk'], ('HIGH', 'CRITICAL')); self.assertTrue(r['route']['approval_required'])
        edited = copy.deepcopy(self.route(intent='admin')['route']); edited['approval_required'] = False
        self.assertIn('HIGH/CRITICAL route cannot suppress required approval', validate_contract('route-result', edited))

    # ---- evidence gate: VCGF-AI-001-AT05, VCGF-GOV-004-AT02, VCGF-REL-005-AT02, VCGF-GOV-004-AT04, VCGF-REL-001-AT04 ----
    def test_VCGF_AI_001_AT05(self):
        missing = copy.deepcopy(self.evidence); missing['artifacts'][0]['reference'] = 'absent.json'
        out = self.gate(missing); self.assertEqual(out['status'], 'FAIL'); self.assertIn('artifact missing/unsafe: fixture-test', out['errors'])
        changed = copy.deepcopy(self.evidence); changed['artifacts'][0]['sha256'] = '0' * 64
        out = self.gate(changed); self.assertEqual(out['status'], 'FAIL'); self.assertIn('artifact changed: fixture-test', out['errors'])

    def test_VCGF_GOV_004_AT02(self):
        ok = self.gate(self.evidence, trusted_review=lambda record: True); self.assertEqual(ok['status'], 'PASS')
        escaping = copy.deepcopy(self.evidence); escaping['artifacts'][0]['reference'] = '../result.json'
        out = self.gate(escaping); self.assertIn('artifact missing/unsafe: fixture-test', out['errors']); self.assertEqual(out['status'], 'FAIL')
        (self.project / 'result.json').write_text('{"synthetic_test":false}')
        try:
            out = self.gate(self.evidence, trusted_review=lambda record: True); self.assertEqual(out['status'], 'FAIL'); self.assertIn('artifact changed: fixture-test', out['errors'])
        finally:
            (self.project / 'result.json').write_text('{"synthetic_test":true}')

    def test_VCGF_REL_005_AT02(self):
        approved = self.gate(self.evidence, trusted_review=lambda record: True); self.assertEqual(approved['status'], 'PASS')
        (self.project / 'result.json').write_bytes(b'{"synthetic_test":true} ')  # same name, altered bytes
        try:
            replaced = self.gate(self.evidence, trusted_review=lambda record: True)
            self.assertEqual(replaced['status'], 'FAIL'); self.assertIn('artifact changed: fixture-test', replaced['errors'])
        finally:
            (self.project / 'result.json').write_text('{"synthetic_test":true}')
        fresh = copy.deepcopy(self.evidence); fresh['artifacts'][0]['sha256'] = hashlib.sha256((self.project / 'result.json').read_bytes()).hexdigest()
        self.assertEqual(self.gate(fresh, trusted_review=lambda record: True)['status'], 'PASS')

    def test_VCGF_GOV_004_AT04(self):
        for field in ['code_sha256', 'policy_sha256', 'environment', 'profile', 'scope']:
            with self.subTest(field=field):
                expected = copy.deepcopy(self.expected)
                expected[field] = {'kind': 'release', 'target': 'other'} if field == 'scope' else ('production' if field == 'environment' else ('production' if field == 'profile' else 'f' * 64))
                out = self.gate(self.evidence, expected); self.assertEqual(out['status'], 'FAIL'); self.assertIn('changed evidence binding: ' + field, out['errors'])
        stale = copy.deepcopy(self.evidence); stale['valid_until'] = '2026-10-03T12:10:00Z'
        self.assertIn('stale/future evidence', self.gate(stale)['errors'])

    def test_VCGF_REL_001_AT04(self):
        expected = copy.deepcopy(self.expected); expected['code_sha256'] = 'b' * 64
        out = self.gate(self.evidence, expected, trusted_review=lambda record: True)
        self.assertEqual(out['status'], 'FAIL'); self.assertIn('changed evidence binding: code_sha256', out['errors'])
        altered = copy.deepcopy(self.evidence); altered['artifacts'][0]['sha256'] = 'c' * 64
        self.assertIn('artifact changed: fixture-test', self.gate(altered, trusted_review=lambda record: True)['errors'])

    # ---- VCGF-GOV-003-AT02 / VCGF-GOV-004-AT01: exceptions and coverage ----
    def exception(self, **over):
        item = {'exception_id': 'exc-1', 'control_id': 'VCGF-GOV-001', 'reason': 'synthetic acceptance exception', 'risk_owner': 'owner', 'compensating_control': 'manual review',
                'approval_ref': 'approval-1', 'created_at': '2026-10-03T11:00:00Z', 'expires_at': '2026-10-10T12:00:00Z', 'review_at': '2026-10-09T12:00:00Z', 'status': 'approved'}
        item.update(over); return item

    def test_VCGF_GOV_003_AT02(self):
        base = copy.deepcopy(self.evidence); base['controls'][0]['verification'] = 'failed'; base['controls'][0]['exception_ref'] = 'exc-1'
        active = copy.deepcopy(base); active['exceptions'] = [self.exception()]
        out = self.gate(active, trusted_review=lambda record: True)
        self.assertEqual(out['status'], 'CONDITIONAL'); self.assertEqual(out['exceptions'], ['exc-1'])
        self.assertFalse([e for e in out['errors'] if e.startswith(('exception expired', 'unverified/failed', 'a control cannot'))])
        for over in [{'status': 'revoked'}, {'expires_at': '2026-10-03T12:00:00Z', 'review_at': '2026-10-03T11:30:00Z'}, {'review_at': '2026-10-03T12:00:00Z'}]:
            with self.subTest(over=over):
                record = copy.deepcopy(base); record['exceptions'] = [self.exception(**over)]
                out = self.gate(record, trusted_review=lambda record: True)
                self.assertEqual(out['status'], 'FAIL')
                self.assertTrue(any(e == 'exception expired/revoked/review due: exc-1' or e == 'a control cannot rely on an unapproved exception' for e in out['errors']), out['errors'])
        pending = copy.deepcopy(base); pending['exceptions'] = [self.exception(status='pending')]
        self.assertIn('a control cannot rely on an unapproved exception', validate_contract('evidence', pending))
        no_ref = copy.deepcopy(self.evidence); no_ref['controls'][0]['verification'] = 'not_run'
        self.assertIn('unverified/failed control: VCGF-GOV-001', self.gate(no_ref, trusted_review=lambda record: True)['errors'])

    def test_VCGF_GOV_004_AT01(self):
        for field in ['framework_version', 'adapter_id', 'adapter_version', 'profile', 'environment', 'scope', 'code_sha256', 'policy_sha256', 'required_control_ids']:
            self.assertIn(field, self.evidence)
        mismatch = copy.deepcopy(self.evidence); mismatch['required_control_ids'] = ['VCGF-GOV-001', 'VCGF-GOV-002']
        self.assertIn('control records must exactly cover the DECLARED required set', validate_contract('evidence', mismatch))
        expected = copy.deepcopy(self.expected); expected['required_control_ids'] = ['VCGF-GOV-001', 'VCGF-GOV-005']
        self.assertIn('incomplete required coverage', self.gate(self.evidence, expected)['errors'])

    # ---- VCGF-GOV-006-AT01 / AT02: validators ----
    def test_VCGF_GOV_006_AT01(self):
        for script in ['validate-controls.py', 'validate-adapters.py']:
            run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts' / script)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, script + ': ' + run.stdout + run.stderr)
        import yaml
        catalog = [c['id'] for c in yaml.safe_load((ROOT / 'spec/control-catalog.yaml').read_text(encoding='utf-8'))['controls']]
        self.assertEqual(len(catalog), len(set(catalog)))
        for adapter in ['claude', 'cursor', 'generic']:
            rows = [r['control_id'] for r in yaml.safe_load((ROOT / 'platforms' / adapter / 'control-mapping.yaml').read_text(encoding='utf-8'))['mappings']]
            self.assertEqual(sorted(rows), sorted(catalog))

    def test_VCGF_GOV_006_AT02(self):
        import re
        for script in ['validate-vendor-neutral-core.py', 'validate-adapters.py']:
            run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts' / script)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, script + ': ' + run.stdout + run.stderr)
        for entry in ['platforms/claude/rules/CLAUDE.md', 'platforms/cursor/rules/AGENTS.md', 'platforms/generic/rules/portable-project-rules.md']:
            text = re.sub(r'<!--.*?-->', '', (ROOT / entry).read_text(encoding='utf-8'), flags=re.S)
            self.assertIn('this rule file is an adapter, not the source of policy', text)


if __name__ == '__main__':
    unittest.main()
