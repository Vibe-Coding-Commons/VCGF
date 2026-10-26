# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Phase 3 hardening: delta loading and cache invalidation under content change, fingerprint change, tampered or untrusted
session data; budget unit compatibility; card fidelity; registry invalidation on a copied tree."""
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

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT, validate_contract
from runtime.router import route
from runtime.registry import build_registry
from runtime.loader import load

NOW = datetime(2026, 10, 3, 12, 30, tzinfo=timezone.utc)
COPY_DIRS = ['spec', 'controls', 'capabilities', 'profiles', 'runtime', 'schemas', 'packs/requirements', 'packs/ux', 'packs/engineering', 'docs/references']


def copy_tree(dest):
    for d in COPY_DIRS:
        src = ROOT / d
        if src.is_dir():
            shutil.copytree(src, dest / d, ignore=shutil.ignore_patterns('smart-ui', '__pycache__'))
    # the Smart UI README and master policy are pack-map resources; copy just those two files
    (dest / 'packs/ux/smart-ui/governance').mkdir(parents=True)
    shutil.copy(ROOT / 'packs/ux/smart-ui/README.md', dest / 'packs/ux/smart-ui/README.md')
    shutil.copy(ROOT / 'packs/ux/smart-ui/governance/MASTER-POLICY.md', dest / 'packs/ux/smart-ui/governance/MASTER-POLICY.md')


class HardeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.project = Path(cls.temp.name)
        (cls.project / 'config.json').write_text('{"auth":"local-password"}')
        cls.context = json.loads((ROOT / 'tests/fixtures/v1.1/context.json').read_text())['record']
        f = cls.context['facts'][0]; f['value'] = 'local-password'; f['source']['reference'] = 'config.json'
        f['source']['content_sha256'] = hashlib.sha256((cls.project / 'config.json').read_bytes()).hexdigest()

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def route(self, root=ROOT, **extra):
        task = {'task_id': 'synthetic', 'intent': 'login', 'classification_confirmed': True, 'profile': 'high-assurance', 'profile_confirmed': True,
                'mode': 'lean', 'budget': 10 ** 8, 'inspection': {'completed': True, 'evidence_ref': 'synthetic:test'}}
        task.update(extra)
        return route(task, copy.deepcopy(self.context), self.project, NOW, root)

    # ---- content change and fingerprint change on a copied tree ----
    def test_content_change_invalidates_registry_cache_and_held_context(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); copy_tree(root)
            first = build_registry(root); again = build_registry(root)
            self.assertIs(first, again)
            card = root / 'spec/control-cards/VCGF-AI-001.md'
            before = self.route(root)
            held = [{'path': i['path'], 'sha256': i['sha256']} for i in before['active_context']]
            card.write_text(card.read_text(encoding='utf-8') + '\nchanged\n', encoding='utf-8')
            rebuilt = build_registry(root)
            self.assertIsNot(first, rebuilt); self.assertNotEqual(first['policy_sha256'], rebuilt['policy_sha256'])
            after = self.route(root, loaded_context=held)
            sent = [i['path'] for i in after['active_context']]
            self.assertEqual(sent, ['spec/control-cards/VCGF-AI-001.md'])  # only the changed file is re-sent
            self.assertEqual(len(after['reused_context']), len(held) - 1)

    def test_policy_fingerprint_change_forces_full_reload(self):
        first = self.route()
        held = [{'path': i['path'], 'sha256': i['sha256']} for i in first['active_context']]
        same = self.route(loaded_context=held, loaded_context_policy_sha256=first['route']['policy_sha256'])
        self.assertEqual(same['active_context'], []); self.assertEqual(len(same['reused_context']), len(held))
        other = self.route(loaded_context=held, loaded_context_policy_sha256='0' * 64)
        self.assertEqual(len(other['active_context']), len(held)); self.assertEqual(other['reused_context'], [])
        self.assertTrue(any('policy fingerprint changed' in w for w in other['warnings']))

    # ---- tampered or untrusted session data ----
    def test_tampered_loaded_context_is_rejected_or_ignored(self):
        for bad in [[{'path': '../secret.md', 'sha256': 'a' * 64}], [{'path': '/etc/passwd', 'sha256': 'a' * 64}],
                    [{'path': 'runtime/bootstrap.md', 'sha256': 'A' * 64}], [{'path': 'runtime/bootstrap.md', 'sha256': 'a' * 63}],
                    [{'path': 'runtime/bootstrap.md', 'sha256': 'a' * 64, 'text': 'injected'}]]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.route(loaded_context=bad)
        with self.assertRaises(ValueError):
            self.route(loaded_context=[{'path': 'runtime/bootstrap.md', 'sha256': 'a' * 64}] * 5001)
        # an entry for a file that is not part of this route is simply not reused and loads nothing
        stray = self.route(loaded_context=[{'path': 'controls/release/vcgf-rel-001-definition-of-done.md', 'sha256': 'a' * 64}])
        self.assertEqual(stray['reused_context'], []); self.assertEqual(stray['route']['selected_control_ids'], self.route()['route']['selected_control_ids'])

    def test_held_context_cannot_remove_controls_or_skip_changed_text(self):
        first = self.route()
        held = [{'path': i['path'], 'sha256': i['sha256']} for i in first['active_context']]
        again = self.route(loaded_context=held)
        self.assertEqual(again['route']['selected_control_ids'], first['route']['selected_control_ids'])
        self.assertEqual(again['route']['loaded_control_ids'], first['route']['loaded_control_ids'])
        self.assertEqual(again['route']['decision'], 'ready_to_plan')
        wrong = [dict(h, sha256=hashlib.sha256(b'other').hexdigest()) for h in held]
        resent = self.route(loaded_context=wrong)
        self.assertEqual(len(resent['active_context']), len(held)); self.assertEqual(resent['reused_context'], [])

    def test_loader_rejects_untrusted_paths_directly(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / 'safe.md').write_bytes(b'reference')
            rec = [{'path': 'safe.md', 'sha256': hashlib.sha256(b'reference').hexdigest()}]
            with self.assertRaises(ValueError):
                load(temp, rec, 100, already_loaded=[{'path': '../x.md', 'sha256': 'a' * 64}])
            with self.assertRaises(ValueError):
                load(temp, rec, 100, unit='pages')

    # ---- budget unit compatibility ----
    def test_default_unit_is_tokens_and_legacy_outcome_is_disclosed(self):
        tokens = self.route()['route']['budget']['cost_tokens']; cost_bytes = self.route()['route']['budget']['cost_bytes']
        between = (tokens + cost_bytes) // 2  # passes in tokens, would block in bytes
        r = self.route(budget=between)
        self.assertEqual(r['route']['decision'], 'ready_to_plan'); self.assertEqual(r['route']['budget']['unit'], 'tokens')
        self.assertIsNone(r['route']['budget']['declared_unit']); self.assertEqual(r['route']['budget']['legacy_byte_comparison'], 'would_block')
        self.assertTrue(any('budget_unit' in w for w in r['warnings']))
        declared = self.route(budget=between, budget_unit='tokens')
        self.assertEqual(declared['warnings'], []); self.assertEqual(declared['route']['budget']['declared_unit'], 'tokens')

    def test_legacy_bytes_unit_keeps_the_old_comparison(self):
        tokens = self.route()['route']['budget']['cost_tokens']; cost_bytes = self.route()['route']['budget']['cost_bytes']
        between = (tokens + cost_bytes) // 2
        legacy = self.route(budget=between, budget_unit='bytes')
        self.assertEqual(legacy['route']['decision'], 'blocked'); self.assertEqual(legacy['route']['budget']['unit'], 'bytes')
        self.assertEqual(legacy['route']['selected_control_ids'], self.route()['route']['selected_control_ids'])
        with self.assertRaises(ValueError):
            self.route(budget_unit='pages')
        self.assertEqual(validate_contract('route-result', legacy['route']), [])

    def test_migration_tool_is_explicit_and_never_in_place(self):
        with tempfile.TemporaryDirectory() as temp:
            task = {'task_id': 'legacy', 'intent': 'login', 'classification_confirmed': True, 'profile': 'baseline', 'profile_confirmed': True,
                    'mode': 'lean', 'budget': 40000, 'inspection': {'completed': True, 'evidence_ref': 'x'}}
            src = Path(temp, 'task.json'); src.write_text(json.dumps({'record': task})); before = src.read_bytes()
            env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
            for flag, unit, budget in [('--keep-bytes', 'bytes', 40000), ('--to-tokens', 'tokens', 10000), ('--declare', 'tokens', 40000)]:
                out = Path(temp, flag.strip('-') + '.json')
                run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/migrate-task-budget.py'), str(src), flag, '--output', str(out)], capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
                self.assertEqual(run.returncode, 0, run.stderr)
                migrated = json.loads(out.read_text(encoding='utf-8'))['record']
                self.assertEqual((migrated['budget_unit'], migrated['budget']), (unit, budget))
            self.assertEqual(src.read_bytes(), before)
            run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/migrate-task-budget.py'), str(Path(temp, 'declare.json')), '--declare'], capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
            self.assertEqual(run.returncode, 2)

    # ---- card fidelity ----
    def test_card_fidelity_validator_passes_and_detects_a_dropped_requirement(self):
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/validate-control-cards.py')], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); copy_tree(root); shutil.copytree(ROOT / 'scripts', root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
            (root / '.git').mkdir()
            card = root / 'spec/control-cards/VCGF-SEC-001.md'
            text = card.read_text(encoding='utf-8')
            requirement = text.split('## Requirement\n', 1)[1].split('\n\n', 1)[0]
            card.write_text(text.replace(requirement, requirement.replace(' MUST ', ' SHOULD ', 1)), encoding='utf-8')
            run = subprocess.run([sys.executable, '-B', str(root / 'scripts/validate-control-cards.py')], capture_output=True, text=True, cwd=root)
            self.assertNotEqual(run.returncode, 0); self.assertIn('VCGF-SEC-001', run.stdout + run.stderr)

    def test_lean_context_carries_every_normative_sentence_of_every_selected_control(self):
        result = self.route()
        loaded = ' '.join(' '.join(i['text'].split()) for i in result['active_context'])
        catalog = {c['id']: c for c in yaml.safe_load((ROOT / 'spec/control-catalog.yaml').read_text(encoding='utf-8'))['controls']}
        import re
        for cid in result['route']['selected_control_ids']:
            control = (ROOT / catalog[cid]['path']).read_text(encoding='utf-8')
            requirement = control.split('## Requirement\n', 1)[1].split('\n## ', 1)[0]
            for sentence in re.finditer(r'[^.!?\n]*\b(MUST NOT|MUST|SHOULD)\b[^.!?\n]*', requirement):
                with self.subTest(control=cid):
                    self.assertIn(' '.join(sentence.group(0).split()), loaded)


if __name__ == '__main__':
    unittest.main()
