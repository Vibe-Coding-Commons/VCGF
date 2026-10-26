# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Final consolidation checks: CLI dry-run and as-of, Smart UI inference and denylist, operational map, dependency
integrity, requirement packs without tracking parameters, release-validation recorder."""
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
from runtime.ui_select import select_ui, infer_signals, bindings

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)
ENV = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}


class FinalConsolidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        cls.screen = json.loads((ROOT / 'tests/fixtures/v1.1/screen-context.json').read_text(encoding='utf-8'))['record']

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def route(self, **extra):
        task = {'task_id': 'final', 'intent': 'login', 'classification_confirmed': True, 'profile': 'high-assurance', 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
        task.update(extra); return route(task, copy.deepcopy(self.context), self.project, NOW)

    def test_cli_as_of_makes_fixture_examples_reproducible_and_dry_run_is_recorded(self):
        with tempfile.TemporaryDirectory() as temp:
            task = {'task_id': 'cli', 'intent': 'login', 'classification_confirmed': True, 'profile': 'high-assurance', 'profile_confirmed': True,
                    'mode': 'lean', 'budget': 10 ** 7, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
            Path(temp, 'task.json').write_text(json.dumps(task)); Path(temp, 'context.json').write_text(json.dumps(self.context))
            base = [sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'route', str(Path(temp, 'task.json')), str(Path(temp, 'context.json')), '--project-root', str(self.project), '--quiet']
            stale = subprocess.run(base, capture_output=True, text=True, encoding='utf-8', env=ENV, cwd=ROOT)
            self.assertEqual(stale.returncode, 1)  # the fixture facts expired in real time
            fresh = subprocess.run(base + ['--as-of', '2026-10-03T12:30:00Z', '--dry-run'], capture_output=True, text=True, encoding='utf-8', env=ENV, cwd=ROOT)
            self.assertEqual(fresh.returncode, 0, fresh.stdout[-300:] + fresh.stderr[-300:])
            payload = json.loads(fresh.stdout)
            self.assertEqual(payload['route']['decision'], 'ready_to_plan'); self.assertTrue(payload['dry_run']); self.assertIn('read-only', payload['dry_run_note'])
            self.assertEqual(payload['evaluated_at'], '2026-10-03T12:30:00Z')

    def test_inference_adds_signals_from_route_and_screen_without_removing_explicit_ones(self):
        r = self.route(intent='login', intents=['payment'])
        screen = copy.deepcopy(self.screen); screen['devices'] = ['mobile']; screen['sensitive_data'] = True
        screen['composition_signals'] = ['create_edit_screen']  # mobile_focused_task is no longer explicit, so it must be inferred
        inferred = infer_signals(bindings(), r['route'], screen)
        self.assertIn('sign_in_screen', inferred['composition_signals']); self.assertIn('mobile_focused_task', inferred['composition_signals'])
        self.assertIn('payment_like_command', inferred['interaction_signals']); self.assertIn('high_assurance_action', inferred['interaction_signals'])
        out = select_ui(r, screen)['selection']
        self.assertEqual(out['signals']['explicit']['signals'], sorted(screen['signals']))
        self.assertEqual(out['signals']['inferred'], inferred); self.assertEqual(out['precedence']['authoritative'], 'controls')
        ids = {s['standard_id'] for s in out['standards']}
        self.assertTrue(any(i.startswith('VCGF-UI-SCR-') for i in ids))  # a composition was selected from inferred signals
        self.assertEqual(validate_contract('ui-selection', out), [])

    def test_inference_is_deterministic_and_does_not_load_backend_only_standards(self):
        r = self.route(intent='api')
        screen = copy.deepcopy(self.screen); screen['sensitive_data'] = False; screen['directions'] = ['ltr']
        for key in ['signals', 'interaction_signals', 'composition_signals', 'journey_signals']:
            screen[key] = []
        a = select_ui(r, copy.deepcopy(screen)); b = select_ui(r, copy.deepcopy(screen))
        self.assertEqual(a, b); self.assertEqual(a['selection']['signals']['inferred'], {})
        self.assertEqual([s['standard_id'] for s in a['selection']['standards']], [])  # an API task with no screen signals loads no UI standard

    def test_denylisted_package_files_are_never_served(self):
        never = tuple(bindings()['never_load_prefixes'])
        r = self.route(intent='button-color')
        out = select_ui(r, copy.deepcopy(self.screen))
        for item in out['active_context']:
            self.assertFalse(item['path'].startswith(never), item['path'])
        self.assertIn('CATALOG.html', never); self.assertIn('reports/', never)

    def test_validators_for_operational_map_and_dependencies_pass(self):
        for script in ['validate-operational-map.py', 'validate-dependencies.py']:
            run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts' / script)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, script + ': ' + run.stdout + run.stderr)
        import yaml
        mapped = yaml.safe_load((ROOT / 'spec/operational-control-map.yaml').read_text(encoding='utf-8'))['files']
        self.assertEqual(len(mapped), 35)

    def test_requirement_packs_carry_no_tracking_parameters_and_keep_their_text(self):
        for p in sorted((ROOT / 'packs/requirements').glob('section-*.md')):
            text = p.read_text(encoding='utf-8')
            self.assertNotIn('utm_source', text, p.name)
        self.assertIn('UX Review', (ROOT / 'packs/requirements/section-15.md').read_text(encoding='utf-8'))

    def test_release_validation_recorder_binds_to_commit_and_environment(self):
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/record-release-validation.py'), '--tests', '1,0,0', '--notes', 'unit test run'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', env=ENV)
        self.assertIn(run.returncode, (0, 1), run.stdout + run.stderr)
        record = json.loads((ROOT / 'docs/quality/v1.4/release-validation-local.json').read_text(encoding='utf-8'))
        for key in ['candidate_commit', 'environment', 'release_quality_gate', 'self_acceptance', 'ci']:
            self.assertIn(key, record)
        self.assertEqual(len(record['candidate_commit']), 40); self.assertIn('NOT_TESTED', record['ci'])


if __name__ == '__main__':
    unittest.main()
