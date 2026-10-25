# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Phase 1 routing properties: Router reachability of every control, profile-aware monotonic selection, no unrelated loading."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT
from runtime.router import route

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)
PROFILES = ['baseline', 'production', 'high-assurance']
# Controls that no routing intent could reach before the applicability matrix and the profile layer (audit V13-101/102).
PREVIOUSLY_UNREACHABLE = ['VCGF-AI-007', 'VCGF-ARCH-002', 'VCGF-ARCH-005', 'VCGF-AUDIT-003', 'VCGF-DATA-003', 'VCGF-DATA-004',
                          'VCGF-DATA-005', 'VCGF-DB-003', 'VCGF-DB-004', 'VCGF-GOV-003', 'VCGF-GOV-006', 'VCGF-OPS-001',
                          'VCGF-OPS-004', 'VCGF-OPS-005', 'VCGF-REL-001', 'VCGF-REL-002', 'VCGF-REL-004', 'VCGF-SECR-002',
                          'VCGF-TEST-004']


class ProfileLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        public = copy.deepcopy(f); public['key'] = 'public-indexable'; public['value'] = True; cls.context['facts'].append(public)
        cls.policy = yaml.safe_load((ROOT / 'runtime/routing-policy.yaml').read_text(encoding='utf-8'))
        cls.catalog = {c['id'] for c in yaml.safe_load((ROOT / 'spec/control-catalog.yaml').read_text(encoding='utf-8'))['controls']}
        cls.profiles = {p.parent.name: set(yaml.safe_load(p.read_text(encoding='utf-8'))['required_controls']) for p in (ROOT / 'profiles').glob('*/profile.yaml')}
        cls.routes = {}
        for intent in sorted(cls.policy['intents']):
            for profile in PROFILES:
                cls.routes[(intent, profile)] = cls.route(intent, profile)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def route(cls, intent, profile, **extra):
        task = {'task_id': 'synthetic', 'intent': intent, 'classification_confirmed': True, 'profile': profile, 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
        task.update(extra)
        return route(task, copy.deepcopy(cls.context), cls.project, NOW)

    def selected(self, intent, profile):
        return set(self.routes[(intent, profile)]['route']['selected_control_ids'])

    def test_every_intent_routes_and_only_risk_recommendation_blocks(self):
        # CRITICAL intents recommend high-assurance; a lower confirmed profile is blocked by design (pre-existing rule),
        # yet the selected set is still computed so monotonicity and reachability hold for every profile.
        for key, result in self.routes.items():
            with self.subTest(intent=key[0], profile=key[1]):
                blockers = result['route']['blockers']
                if self.policy['intents'][key[0]]['risk'] == 'CRITICAL' and key[1] != 'high-assurance':
                    self.assertEqual(blockers, ['confirmed profile below risk recommendation: high-assurance'])
                else:
                    self.assertEqual(result['route']['decision'], 'ready_to_plan', blockers)
                self.assertTrue(result['route']['selected_control_ids'])

    def test_profiles_are_monotonic_per_task(self):
        for intent in sorted(self.policy['intents']):
            with self.subTest(intent=intent):
                self.assertLessEqual(self.selected(intent, 'baseline'), self.selected(intent, 'production'))
                self.assertLessEqual(self.selected(intent, 'production'), self.selected(intent, 'high-assurance'))

    def test_profiles_actually_differ(self):
        differing = [i for i in self.policy['intents'] if self.selected(i, 'baseline') < self.selected(i, 'high-assurance')]
        self.assertGreaterEqual(len(differing), 0.75 * len(self.policy['intents']), differing)
        for intent in ['login', 'admin', 'payment', 'migration', 'upload', 'button-color']:
            with self.subTest(intent=intent):
                self.assertLess(self.selected(intent, 'baseline'), self.selected(intent, 'production'))
                self.assertLess(self.selected(intent, 'production'), self.selected(intent, 'high-assurance'))

    def test_every_control_reachable_for_high_assurance(self):
        union = set().union(*(self.selected(i, 'high-assurance') for i in self.policy['intents']))
        self.assertEqual(sorted(self.catalog - union), [])

    def test_previously_unreachable_controls_are_now_reachable(self):
        union = set().union(*(self.selected(i, 'high-assurance') for i in self.policy['intents']))
        self.assertTrue(set(PREVIOUSLY_UNREACHABLE) <= union, sorted(set(PREVIOUSLY_UNREACHABLE) - union))

    def test_profile_layer_only_adds_profile_required_controls_with_trigger_hit(self):
        for key, result in self.routes.items():
            capabilities = set(result['capabilities'])
            for reason in result['route']['reasons']:
                if reason['capability_id'] != 'profile-layer':
                    continue
                with self.subTest(intent=key[0], profile=key[1], control=reason['control_id']):
                    self.assertIn(reason['control_id'], self.profiles[key[1]])
                    self.assertEqual(reason['source'], 'spec/applicability-matrix.yaml')
                    via = reason['reason'].split('applicable via ', 1)[1]
                    self.assertTrue(via == 'every task' or set(via.split(', ')) <= capabilities, reason['reason'])

    def test_profile_layer_does_not_load_unrelated_controls(self):
        ui_only = self.selected('button-color', 'high-assurance')
        self.assertFalse([c for c in ui_only if c.startswith(('VCGF-IAM-', 'VCGF-DB-', 'VCGF-API-', 'VCGF-FILE-', 'VCGF-SECR-', 'VCGF-DATA-'))])
        self.assertTrue({'VCGF-UX-001', 'VCGF-UX-002', 'VCGF-UX-003', 'VCGF-UX-004'} <= ui_only)
        self.assertEqual({'VCGF-UX-001', 'VCGF-UX-002'}, self.selected('button-color', 'production') & {'VCGF-UX-001', 'VCGF-UX-002', 'VCGF-UX-003', 'VCGF-UX-004'})
        self.assertFalse(self.selected('button-color', 'baseline') & {'VCGF-UX-001', 'VCGF-UX-002', 'VCGF-UX-003', 'VCGF-UX-004'})

    def test_definition_of_done_is_minimum_governance(self):
        for key in self.routes:
            self.assertIn('VCGF-REL-001', self.selected(*key))

    def test_new_intents_reach_project_level_controls(self):
        expected = {'release': {'VCGF-REL-002', 'VCGF-REL-004', 'VCGF-TEST-004', 'VCGF-OPS-001', 'VCGF-OPS-005'},
                    'exception': {'VCGF-GOV-003', 'VCGF-GOV-002'}, 'governance-change': {'VCGF-GOV-006', 'VCGF-AI-007', 'VCGF-OPS-004'},
                    'backup': {'VCGF-OPS-001', 'VCGF-DATA-003', 'VCGF-DB-003', 'VCGF-SECR-002'}, 'email': {'VCGF-ARCH-002', 'VCGF-SECR-002'}}
        for intent, controls in expected.items():
            with self.subTest(intent=intent):
                self.assertTrue(controls <= self.selected(intent, 'high-assurance'), sorted(controls - self.selected(intent, 'high-assurance')))

    def test_threat_modeling_reached_for_trust_boundary_tasks_in_lean_mode(self):
        for intent in ['admin', 'payment', 'login', 'migration']:
            with self.subTest(intent=intent):
                self.assertIn('VCGF-ARCH-005', self.selected(intent, 'high-assurance'))

    def test_capability_floor_unchanged_by_profile(self):
        for intent in sorted(self.policy['intents']):
            floor = {r['control_id'] for r in self.routes[(intent, 'baseline')]['route']['reasons'] if r['capability_id'] != 'profile-layer'}
            for profile in PROFILES[1:]:
                self.assertLessEqual(floor, self.selected(intent, profile))

    def test_overlay_can_add_ux_control_to_baseline(self):
        result = self.route('button-color', 'baseline', overlay_add_controls=['VCGF-UX-001'])
        self.assertEqual(result['route']['decision'], 'ready_to_plan')
        self.assertIn('VCGF-UX-001', result['route']['selected_control_ids'])

    def test_validators_pass(self):
        for script in ['validate-applicability.py', 'validate-profiles.py']:
            with self.subTest(script=script):
                completed = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts' / script)], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == '__main__':
    unittest.main()
