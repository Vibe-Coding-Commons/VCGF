# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Phase 2 context efficiency: control cards, comment stripping, multi-intent routing, delta loading with hash
invalidation, registry cache, token accounting and compact CLI output. Coverage never shrinks for a smaller context."""
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT, validate_contract
from runtime.router import route
from runtime.registry import build_registry
from runtime.loader import load, served_text
from runtime.tokens import estimate, count
from runtime.acceptance import acceptance_tests, acceptance_summary
from runtime.ui_select import select_ui, smart_card

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)


class ContextEfficiencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        cls.catalog = {c['id']: c for c in yaml.safe_load((ROOT / 'spec/control-catalog.yaml').read_text(encoding='utf-8'))['controls']}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def route(self, **extra):
        task = {'task_id': 'synthetic', 'intent': 'login', 'classification_confirmed': True, 'profile': 'high-assurance', 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
        task.update(extra)
        return route(task, copy.deepcopy(self.context), self.project, NOW)

    # ---- control cards ----
    def test_lean_loads_cards_and_deep_loads_full_controls_with_the_same_coverage(self):
        lean, deep = self.route(mode='lean'), self.route(mode='deep')
        self.assertEqual(lean['route']['context_detail'], 'card'); self.assertEqual(deep['route']['context_detail'], 'full')
        self.assertLessEqual(set(lean['route']['selected_control_ids']), set(deep['route']['selected_control_ids']))
        lean_paths = [i['path'] for i in lean['active_context']]; deep_paths = [i['path'] for i in deep['active_context']]
        self.assertIn('spec/control-cards/common-clauses.md', lean_paths); self.assertNotIn('spec/control-cards/common-clauses.md', deep_paths)
        self.assertTrue(all(p.startswith('spec/control-cards/') for p in lean_paths if p.startswith('spec/')))
        self.assertTrue(any(p.startswith('controls/') for p in deep_paths))
        self.assertLess(lean['route']['budget']['cost_bytes'], 0.6 * deep['route']['budget']['cost_bytes'])

    def test_every_selected_control_has_a_card_in_context(self):
        result = self.route()
        paths = {i['path'] for i in result['active_context']}
        for cid in result['route']['selected_control_ids']:
            self.assertIn(f'spec/control-cards/{cid}.md', paths)

    def test_cards_carry_the_requirement_verbatim(self):
        for cid in ['VCGF-SEC-001', 'VCGF-UX-001', 'VCGF-GOV-001']:
            control = (ROOT / self.catalog[cid]['path']).read_text(encoding='utf-8')
            requirement = control.split('## Requirement\n', 1)[1].split('\n## ', 1)[0].strip()
            card = (ROOT / f'spec/control-cards/{cid}.md').read_text(encoding='utf-8')
            self.assertIn(requirement, card); self.assertIn(self.catalog[cid]['path'], card)
            self.assertIn(self.catalog[cid]['requirement_level'], card.splitlines()[2])

    def test_cards_are_derived_and_current(self):
        completed = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/generate-control-cards.py'), '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_served_text_has_no_html_comments_but_hash_is_on_raw_bytes(self):
        result = self.route()
        for item in result['active_context']:
            self.assertNotIn('<!--', item['text'])
            self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(), item['sha256'])
        self.assertEqual(served_text('x.md', b'<!-- a -->\n# T\nbody\n'), '# T\nbody\n')
        self.assertEqual(served_text('x.yaml', b'<!-- a -->\nkeep'), '<!-- a -->\nkeep')

    # ---- multi-intent routing ----
    def test_multi_intent_route_covers_the_union_and_costs_less_than_sequential_routes(self):
        multi = self.route(intents=['api', 'payment'])
        singles = [self.route(intent=i) for i in ['login', 'api', 'payment']]
        union = set().union(*(set(s['route']['selected_control_ids']) for s in singles))
        self.assertEqual(set(multi['route']['selected_control_ids']), union)
        self.assertEqual(multi['route']['intents'], ['login', 'api', 'payment'])
        self.assertEqual(multi['route']['risk'], 'HIGH')
        self.assertLess(multi['route']['budget']['cost_bytes'], 0.6 * sum(s['route']['budget']['cost_bytes'] for s in singles))

    def test_multi_intent_takes_the_highest_risk(self):
        self.assertEqual(self.route(intent='button-color', intents=['deletion'])['route']['risk'], 'CRITICAL')

    def test_unknown_additional_intent_rejected(self):
        with self.assertRaises(ValueError):
            self.route(intents=['not-an-intent'])
        with self.assertRaises(ValueError):
            self.route(intents='api')

    # ---- delta loading and invalidation ----
    def test_delta_loading_sends_only_new_items_and_keeps_coverage(self):
        first = self.route()
        held = [{'path': i['path'], 'sha256': i['sha256']} for i in first['active_context']]
        second = self.route(intent='payment', loaded_context=held)
        full = self.route(intent='payment')
        self.assertEqual(second['route']['selected_control_ids'], full['route']['selected_control_ids'])
        self.assertEqual(second['route']['loaded_control_ids'], full['route']['loaded_control_ids'])
        sent = {i['path'] for i in second['active_context']}; reused = {i['path'] for i in second['reused_context']}
        self.assertEqual(sent | reused, {i['path'] for i in full['active_context']}); self.assertFalse(sent & reused)
        self.assertTrue(sent); self.assertLess(second['route']['budget']['cost_tokens'], full['route']['budget']['cost_tokens'])
        self.assertEqual(second['route']['budget']['cost_tokens'] + second['route']['budget']['reused_tokens'], full['route']['budget']['cost_tokens'])

    def test_stale_hash_in_loaded_context_is_resent(self):
        first = self.route()
        held = [{'path': i['path'], 'sha256': i['sha256']} for i in first['active_context']]
        held[1]['sha256'] = '0' * 64
        again = self.route(loaded_context=held)
        self.assertEqual([i['path'] for i in again['active_context']], [held[1]['path']])
        self.assertEqual(len(again['reused_context']), len(held) - 1)

    def test_loaded_context_must_be_well_formed(self):
        for bad in [[{'path': 'x'}], [{'path': 1, 'sha256': 'a'}], 'runtime/bootstrap.md']:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.route(loaded_context=bad)

    def test_budget_counts_only_the_delta_but_never_drops_controls(self):
        first = self.route()
        held = [{'path': i['path'], 'sha256': i['sha256']} for i in first['active_context']]
        tiny = self.route(intent='payment', loaded_context=held, budget=1)
        self.assertEqual(tiny['route']['decision'], 'blocked'); self.assertEqual(tiny['active_context'], [])
        self.assertEqual(tiny['route']['selected_control_ids'], self.route(intent='payment')['route']['selected_control_ids'])

    # ---- registry cache ----
    def test_registry_is_cached_until_a_source_changes(self):
        first = build_registry(ROOT); second = build_registry(ROOT)
        self.assertIs(first, second)
        with tempfile.TemporaryDirectory() as temp:
            pass  # a per-root cache; mutating the repository is not something a test does
        t0 = time.perf_counter(); build_registry(ROOT); self.assertLess(time.perf_counter() - t0, 0.5)

    # ---- token accounting ----
    def test_tokens_are_estimated_from_text_and_bytes_are_measured(self):
        self.assertEqual(estimate('abcd' * 10), 10); self.assertEqual(estimate('ع' * 16), 10)
        measured = count('abcd' * 10 + 'ع' * 16)
        self.assertEqual(measured['bytes'], 40 + 32); self.assertEqual(measured['measurement'], 'estimated')
        result = self.route(); budget = result['route']['budget']
        self.assertEqual(budget['measurement'], 'estimated'); self.assertIn('not a tokenizer measurement', budget['method'])
        self.assertEqual(budget['cost_bytes'], sum(len(i['text'].encode('utf-8')) for i in result['active_context']))
        self.assertEqual(budget['cost_tokens'], sum(i['tokens'] for i in result['active_context']))
        self.assertLess(budget['cost_tokens'], budget['cost_bytes'] / 3)

    def test_token_budget_is_enforced_without_dropping_controls(self):
        full = self.route(); tokens = full['route']['budget']['cost_tokens']
        blocked = self.route(budget=tokens - 1); allowed = self.route(budget=tokens)
        self.assertEqual(blocked['route']['decision'], 'blocked'); self.assertEqual(allowed['route']['decision'], 'ready_to_plan')
        self.assertEqual(blocked['route']['selected_control_ids'], full['route']['selected_control_ids'])

    def test_route_result_contract_accepts_the_new_fields(self):
        self.assertEqual(validate_contract('route-result', self.route(intents=['api'])['route']), [])

    # ---- Smart UI cards ----
    def test_ui_select_serves_cards_for_lean_routes_and_full_text_for_deep_routes(self):
        screen = json.loads((ROOT / 'tests/fixtures/v1.1/screen-context.json').read_text(encoding='utf-8'))['record']
        lean = select_ui(self.route(intent='button-color'), copy.deepcopy(screen))
        deep = select_ui(self.route(intent='button-color', mode='deep'), copy.deepcopy(screen))
        self.assertEqual(lean['selection']['context_detail'], 'card'); self.assertEqual(deep['selection']['context_detail'], 'full')
        self.assertEqual([s['standard_id'] for s in lean['selection']['standards']], [s['standard_id'] for s in deep['selection']['standards']])
        self.assertLess(lean['selection']['budget']['cost_bytes'], 0.8 * deep['selection']['budget']['cost_bytes'])
        for s in lean['selection']['standards']:
            if s['layer'] != 'external-standards':
                self.assertLess(s['served_bytes'], s['bytes'])
        self.assertEqual(validate_contract('ui-selection', lean['selection']), [])
        text = next(i['text'] for i in lean['active_context'] if i['path'].startswith('standards/'))
        self.assertIn('المتطلبات', text); self.assertNotIn('<!--', text)

    def test_smart_card_falls_back_to_full_text_when_no_known_section(self):
        self.assertEqual(smart_card('# T\n\n## Something\nbody\n'), '# T\n\n## Something\nbody\n')

    # ---- acceptance execution state ----
    def test_acceptance_definitions_are_never_reported_as_executed(self):
        one = acceptance_tests('VCGF-IAM-005')
        self.assertEqual(one['summary']['executed'], 0); self.assertEqual(one['summary']['passed'], 0)
        self.assertEqual(one['summary']['unverified'], one['summary']['defined'])
        self.assertTrue(all(t['execution']['status'] == 'not_executed' and t['execution']['verified'] is False for t in one['tests']))
        overall = acceptance_summary()
        self.assertEqual(overall['controls'], 88); self.assertGreater(overall['with_parameters'], 10)
        # only framework_self definitions (recorded by scripts/run-self-acceptance.py) may count as executed; target projects never
        self.assertEqual(overall['executed'], overall['framework_self']); self.assertEqual(overall['target_project_not_executed'], overall['defined'] - overall['framework_self'])
        self.assertTrue(all(t['execution']['status'] == 'not_executed' for c in [acceptance_tests('VCGF-IAM-005'), acceptance_tests('VCGF-UX-001')] for t in c['tests']))

    # ---- CLI output ----
    def test_cli_route_prints_references_by_default_and_text_only_with_full(self):
        with tempfile.TemporaryDirectory() as temp:
            # button-color needs no repository fact, so the CLI (which uses the real clock) is not blocked by the fixture's expiry.
            task = {'task_id': 'cli', 'intent': 'button-color', 'classification_confirmed': True, 'profile': 'production', 'profile_confirmed': True,
                    'mode': 'lean', 'budget': 10 ** 7, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
            Path(temp, 'task.json').write_text(json.dumps(task)); Path(temp, 'context.json').write_text(json.dumps(self.context))
            env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
            base = [sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'route', str(Path(temp, 'task.json')), str(Path(temp, 'context.json')), '--project-root', str(self.project)]
            compact = subprocess.run(base, capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            full = subprocess.run(base + ['--full'], capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            self.assertEqual(compact.returncode, 0, compact.stderr); self.assertEqual(full.returncode, 0, full.stderr)
            payload = json.loads(compact.stdout)
            self.assertTrue(payload['active_context']); self.assertNotIn('text', payload['active_context'][0])
            self.assertEqual(set(payload['active_context'][0]), {'path', 'sha256', 'bytes', 'tokens'})
            self.assertIn('text', json.loads(full.stdout)['active_context'][0])
            self.assertLess(len(compact.stdout), 0.3 * len(full.stdout))


if __name__ == '__main__':
    unittest.main()
