# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Governed Smart UI selection: Router-bound, profile-aware, hash-pinned, budgeted, deterministic."""
import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT, validate_contract
from runtime.router import route
from runtime.ui_select import select_ui, bindings
from runtime.acceptance import acceptance_tests

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)
UX = {'VCGF-UX-001', 'VCGF-UX-002', 'VCGF-UX-003', 'VCGF-UX-004'}


class UISelectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()
        cls.screen = json.loads((ROOT / 'tests/fixtures/v1.1/screen-context.json').read_text(encoding='utf-8'))['record']
        cls.manifest = {e['path']: e for e in json.loads((ROOT / 'packs/ux/smart-ui/manifest.json').read_text(encoding='utf-8'))['files']}
        cls.routes = {p: cls.route(p) for p in ['baseline', 'production', 'high-assurance']}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def route(cls, profile, intent='button-color', **extra):
        task = {'task_id': 'synthetic', 'intent': intent, 'classification_confirmed': True, 'profile': profile, 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 7, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
        task.update(extra)
        return route(task, copy.deepcopy(cls.context), cls.project, NOW)

    def select(self, profile, screen=None, **kw):
        return select_ui(self.routes[profile], screen or copy.deepcopy(self.screen), **kw)

    def test_baseline_without_ux_controls_is_not_applicable(self):
        out = self.select('baseline'); s = out['selection']
        self.assertEqual(s['status'], 'not_applicable'); self.assertEqual(s['ux_controls_in_route'], [])
        self.assertEqual(s['standards'], []); self.assertEqual(out['active_context'], []); self.assertEqual(s['budget']['cost_tokens'], 0)
        self.assertTrue(all(layer['missing_controls'] for layer in s['layers'].values()))
        self.assertTrue(any('VCGF-UX-001' in w for w in s['warnings']))

    def test_production_loads_governed_layers_and_defers_the_rest(self):
        out = self.select('production'); s = out['selection']
        self.assertEqual(s['status'], 'selected'); self.assertEqual(s['ux_controls_in_route'], ['VCGF-UX-001', 'VCGF-UX-002'])
        self.assertEqual({x['layer'] for x in s['standards']}, {'components', 'external-standards'})
        self.assertEqual({x['layer'] for x in s['deferred_standards']}, {'interactions', 'screen-compositions', 'journeys'})
        self.assertEqual(s['layers']['interactions'], {'state': 'deferred', 'governing_controls': ['VCGF-UX-003'], 'missing_controls': ['VCGF-UX-003']})
        self.assertEqual([d['path'] for d in s['governance_documents']], ['governance/ACCESSIBILITY-RTL.md'])
        loaded_paths = {i['path'] for i in out['active_context']}
        self.assertEqual(loaded_paths, {x['path'] for x in s['standards']} | {d['path'] for d in s['governance_documents']})
        self.assertFalse(loaded_paths & {x['path'] for x in s['deferred_standards']})

    def test_high_assurance_loads_every_signalled_layer(self):
        out = self.select('high-assurance'); s = out['selection']
        self.assertEqual(set(s['ux_controls_in_route']), UX); self.assertEqual(s['deferred_standards'], [])
        self.assertEqual({v['state'] for v in s['layers'].values()}, {'loaded'})
        self.assertEqual({x['layer'] for x in s['standards']}, {'components', 'external-standards', 'interactions', 'screen-compositions', 'journeys'})
        self.assertEqual(len(out['active_context']), len(s['standards']) + len(s['governance_documents']))

    def test_selection_is_monotonic_across_profiles(self):
        prod = {x['path'] for x in self.select('production')['selection']['standards']}
        high = {x['path'] for x in self.select('high-assurance')['selection']['standards']}
        self.assertLess(prod, high)

    def test_never_loads_the_whole_package(self):
        s = self.select('high-assurance')['selection']
        self.assertLess(len(s['standards']) + len(s['governance_documents']), 15)
        self.assertLess(s['budget']['cost_tokens'], sum(e['bytes'] for e in self.manifest.values()) // 4)

    def test_every_loaded_path_is_manifest_pinned(self):
        s = self.select('high-assurance')['selection']
        for item in s['standards'] + s['governance_documents']:
            with self.subTest(path=item['path']):
                self.assertEqual(self.manifest[item['path']]['sha256'], item['sha256'])
                self.assertEqual(self.manifest[item['path']]['bytes'], item['bytes'])

    def test_no_signals_loads_only_governance_documents(self):
        screen = copy.deepcopy(self.screen)
        for key in ['signals', 'interaction_signals', 'composition_signals', 'journey_signals']:
            screen[key] = []
        s = self.select('high-assurance', screen)['selection']
        self.assertEqual(s['status'], 'selected'); self.assertEqual(s['standards'], []); self.assertTrue(s['governance_documents'])

    def test_no_ui_screen(self):
        screen = copy.deepcopy(self.screen); screen['has_ui'] = False
        out = self.select('high-assurance', screen); s = out['selection']
        self.assertEqual(s['status'], 'no_ui'); self.assertEqual(s['standards'], []); self.assertEqual(out['active_context'], [])

    def test_budget_blocks_without_dropping_standards(self):
        full = self.select('high-assurance'); small = self.select('high-assurance', budget=1)
        self.assertEqual(small['selection']['status'], 'blocked'); self.assertEqual(small['active_context'], [])
        self.assertEqual(small['selection']['standards'], full['selection']['standards'])
        self.assertEqual(small['selection']['budget']['cost_tokens'], full['selection']['budget']['cost_tokens'])

    def test_blocked_route_blocks_selection(self):
        blocked = self.route('high-assurance', profile_confirmed=False)
        self.assertEqual(blocked['route']['decision'], 'blocked')
        out = select_ui(blocked, copy.deepcopy(self.screen))
        self.assertEqual(out['selection']['status'], 'blocked'); self.assertEqual(out['active_context'], [])

    def test_overlay_added_ux_control_enables_selection_for_baseline(self):
        result = self.route('baseline', overlay_add_controls=['VCGF-UX-001'])
        s = select_ui(result, copy.deepcopy(self.screen))['selection']
        self.assertEqual(s['status'], 'selected'); self.assertEqual(s['ux_controls_in_route'], ['VCGF-UX-001'])
        self.assertEqual({x['layer'] for x in s['standards']}, {'components'})
        self.assertIn('CALENDAR-GOVERNANCE-ADDENDUM', [x['standard_id'] for x in s['deferred_standards']])  # governed by VCGF-UX-002, absent

    def test_tampered_standard_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'runtime').mkdir(); shutil.copy(ROOT / 'runtime/ui-bindings.yaml', root / 'runtime/ui-bindings.yaml')
            (root / 'spec/acceptance').mkdir(parents=True); shutil.copy(ROOT / 'spec/acceptance/user-experience.yaml', root / 'spec/acceptance/user-experience.yaml')
            shutil.copytree(ROOT / 'packs/ux/smart-ui', root / 'packs/ux/smart-ui')
            target = root / 'packs/ux/smart-ui/governance/ACCESSIBILITY-RTL.md'
            target.write_bytes(target.read_bytes() + b'\n<!-- tampered -->\n')
            with self.assertRaisesRegex(ValueError, 'stale registry hash'):
                select_ui(self.routes['high-assurance'], copy.deepcopy(self.screen), root=root)

    def test_invalid_screen_context_rejected(self):
        screen = copy.deepcopy(self.screen); screen['devices'] = ['watch']
        with self.assertRaisesRegex(ValueError, 'invalid screen context'):
            self.select('high-assurance', screen)
        with self.assertRaisesRegex(ValueError, 'invalid route result'):
            select_ui({'route': {}}, copy.deepcopy(self.screen))

    def test_result_is_a_valid_contract_and_deterministic(self):
        first = self.select('high-assurance'); second = self.select('high-assurance')
        self.assertEqual(first, second); self.assertEqual(validate_contract('ui-selection', first['selection']), [])

    def test_acceptance_tests_bound_to_ux_controls(self):
        s = self.select('high-assurance')['selection']
        self.assertEqual(set(s['acceptance_tests']), UX)
        for cid, ids in s['acceptance_tests'].items():
            self.assertGreaterEqual(len(ids), 2); self.assertEqual(ids, sorted(t['id'] for t in acceptance_tests(cid)['tests']))
        self.assertEqual(acceptance_tests('VCGF-UX-' + '999')['tests'], [])  # unknown id built dynamically so cross-reference validation ignores it

    def test_bindings_reference_existing_controls_and_files(self):
        b = bindings(); pack = ROOT / 'packs/ux/smart-ui'
        for layer in b['layers'].values():
            self.assertTrue(set(layer['governing_controls']) <= UX)
        for docs in b['governance_documents'].values():
            for path in docs:
                self.assertTrue((pack / path).is_file(), path); self.assertIn(path, self.manifest)

    def test_cli_round_trip(self):
        with tempfile.TemporaryDirectory() as temp:
            task = {'task_id': 'cli', 'intent': 'button-color', 'classification_confirmed': True, 'profile': 'production', 'profile_confirmed': True,
                    'mode': 'lean', 'budget': 10 ** 7, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
            Path(temp, 'task.json').write_text(json.dumps(task)); Path(temp, 'context.json').write_text(json.dumps(self.context))
            Path(temp, 'screen.json').write_text(json.dumps(self.screen))
            env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
            routed = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'route', str(Path(temp, 'task.json')), str(Path(temp, 'context.json')), '--project-root', str(self.project), '--quiet'],
                                    capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            self.assertEqual(routed.returncode, 0, routed.stdout[-500:] + routed.stderr[-500:])
            Path(temp, 'route.json').write_text(routed.stdout, encoding='utf-8')
            selected = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'ui-select', str(Path(temp, 'route.json')), str(Path(temp, 'screen.json')), '--quiet'],
                                      capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            self.assertEqual(selected.returncode, 0, selected.stdout[-500:] + selected.stderr[-500:])
            payload = json.loads(selected.stdout)
            self.assertEqual(payload['selection']['status'], 'selected'); self.assertNotIn('active_context', payload)
            shown = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vcgf.py'), 'acceptance', 'VCGF-UX-001'], capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            self.assertEqual(shown.returncode, 0); self.assertEqual(json.loads(shown.stdout)['domain'], 'user-experience')


if __name__ == '__main__':
    unittest.main()
