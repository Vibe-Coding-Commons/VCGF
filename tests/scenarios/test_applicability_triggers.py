# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Hand-assigned applicability triggers: positive, negative and missing-context cases for every control whose matrix
triggers go beyond the capability floor (the controls the Phase 1 matrix made reachable). Missing or untrusted context
must block the route rather than silently drop a mandatory control."""
import copy
import hashlib
import json
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
ROUTER_ADDS = {'VCGF-GOV-002', 'VCGF-GOV-004', 'VCGF-TEST-002', 'VCGF-SEC-006', 'VCGF-REL-003'}


def closure(caps, start):
    seen = set(); stack = list(start)
    while stack:
        c = stack.pop()
        if c in seen or c not in caps: continue
        seen.add(c)
        for d in caps[c].get('dependencies') or []:
            if d.get('relation') in {'requires', 'requires_when', 'any_of'}: stack.extend(d.get('targets') or [])
    return seen


class TriggerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        public = copy.deepcopy(f); public['key'] = 'public-indexable'; public['value'] = True; cls.context['facts'].append(public)
        cls.policy = yaml.safe_load((ROOT / 'runtime/routing-policy.yaml').read_text(encoding='utf-8'))
        cls.matrix = yaml.safe_load((ROOT / 'spec/applicability-matrix.yaml').read_text(encoding='utf-8'))['controls']
        cls.caps = {}
        for p in sorted((ROOT / 'capabilities').glob('*.yaml')):
            d = yaml.safe_load(p.read_text(encoding='utf-8')); cls.caps[d['capability_id']] = d
        floor = {}
        for cap, d in cls.caps.items():
            for cid in d['control_ids']: floor.setdefault(cid, set()).add(cap)
        cls.floor = floor
        cls.minimum = set(cls.policy['minimum_controls'])
        cls.hand_assigned = sorted(cid for cid, e in cls.matrix.items()
                                   if set((e.get('triggers') or {}).get('capabilities') or []) - floor.get(cid, set()))
        cls.intent_caps = {name: closure(cls.caps, list(i['capabilities']) + ['development-agent']) for name, i in cls.policy['intents'].items()}
        cls.routes = {}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def route(self, intent, profile='high-assurance', context=None, **extra):
        key = (intent, profile, json.dumps(context, sort_keys=True) if context is not None else None, json.dumps(extra, sort_keys=True))
        if key not in self.routes:
            task = {'task_id': 'synthetic', 'intent': intent, 'classification_confirmed': True, 'profile': profile, 'profile_confirmed': True,
                    'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
            task.update(extra)
            self.routes[key] = route(task, copy.deepcopy(context if context is not None else self.context), self.project, NOW)
        return self.routes[key]

    def test_hand_assigned_set_is_the_reviewed_one(self):
        # 22 matrix entries were hand-reviewed in Phase 1; four of them (GOV-003, GOV-006, REL-002, REL-004) are now carried
        # exactly by the new capabilities, so 18 keep triggers beyond the capability floor.
        self.assertEqual(self.hand_assigned, ['VCGF-AI-007', 'VCGF-ARCH-002', 'VCGF-ARCH-005', 'VCGF-AUDIT-003', 'VCGF-DATA-003', 'VCGF-DATA-004',
                                              'VCGF-DATA-005', 'VCGF-DB-003', 'VCGF-DB-004', 'VCGF-OPS-001', 'VCGF-OPS-004', 'VCGF-OPS-005',
                                              'VCGF-SECR-002', 'VCGF-TEST-004', 'VCGF-UX-001', 'VCGF-UX-002', 'VCGF-UX-003', 'VCGF-UX-004'])

    def test_positive_every_trigger_capability_loads_the_control(self):
        for cid in self.hand_assigned:
            triggers = set(self.matrix[cid]['triggers']['capabilities'])
            for cap in sorted(triggers - self.floor.get(cid, set())):
                intents = [i for i, caps in self.intent_caps.items() if cap in caps]
                with self.subTest(control=cid, trigger=cap):
                    if cap == 'product-ai':  # requested from the product_ai context flags, never from an intent
                        context = copy.deepcopy(self.context); context['product_ai']['uses_llm'] = True
                        r = self.route('api', context=context)
                    else:
                        self.assertTrue(intents, f'no intent selects trigger capability {cap}')
                        r = self.route(intents[0])
                    self.assertIn(cid, r['route']['selected_control_ids'])
                    reason = next(x for x in r['route']['reasons'] if x['control_id'] == cid)
                    self.assertIn(reason['capability_id'], {'profile-layer', 'runtime-core', 'risk-governance', *self.floor.get(cid, set())})

    def test_negative_no_trigger_means_not_loaded(self):
        checked = 0
        for cid in self.hand_assigned:
            if cid in self.minimum or cid in ROUTER_ADDS: continue
            triggers = set(self.matrix[cid]['triggers']['capabilities']) | self.floor.get(cid, set())
            others = [i for i, caps in self.intent_caps.items() if not (caps & triggers)]
            for intent in others[:3]:
                with self.subTest(control=cid, intent=intent):
                    r = self.route(intent)
                    self.assertEqual(r['route']['decision'], 'ready_to_plan', r['route']['blockers'])
                    self.assertNotIn(cid, r['route']['selected_control_ids']); checked += 1
        self.assertGreater(checked, 20)

    def test_baseline_never_receives_hand_assigned_controls_through_the_profile_layer(self):
        baseline = set(yaml.safe_load((ROOT / 'profiles/baseline/profile.yaml').read_text(encoding='utf-8'))['required_controls'])
        for intent in self.policy['intents']:
            r = self.route(intent, 'baseline')
            for x in r['route']['reasons']:
                if x['capability_id'] == 'profile-layer':
                    self.assertIn(x['control_id'], baseline)

    def test_missing_fact_blocks_instead_of_dropping_controls(self):
        context = copy.deepcopy(self.context); context['facts'] = [f for f in context['facts'] if f['key'] != 'auth-model']
        r = self.route('login', context=context)
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertEqual(r['active_context'], []); self.assertEqual(r['route']['loaded_control_ids'], [])

    def test_unknown_fact_value_blocks(self):
        context = copy.deepcopy(self.context); context['facts'][0]['value'] = 'unknown-mechanism'
        r = self.route('login', context=context)
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertTrue(any('authentication model' in b for b in r['route']['blockers']))

    def test_expired_fact_blocks(self):
        context = copy.deepcopy(self.context); context['facts'][0]['expires_at'] = '2026-10-03T12:01:00Z'
        r = self.route('login', context=context)
        self.assertEqual(r['route']['decision'], 'blocked'); self.assertEqual(r['active_context'], [])

    def test_ready_routes_are_fully_explained(self):
        for intent in self.policy['intents']:
            r = self.route(intent)
            if r['route']['decision'] != 'ready_to_plan': continue
            caps = set(r['capabilities'])
            for x in r['route']['reasons']:
                with self.subTest(intent=intent, control=x['control_id']):
                    kind = x['capability_id']
                    if kind in caps: continue
                    self.assertIn(kind, {'runtime-core', 'risk-governance', 'deep-review', 'standard-review', 'overlay', 'profile-layer'})
                    if kind == 'profile-layer':
                        via = x['reason'].split('applicable via ', 1)[1]
                        self.assertTrue(via == 'every task' or set(via.split(', ')) <= caps, x['reason'])


if __name__ == '__main__':
    unittest.main()
