# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Automated enforcement surfaces: the governance-file guard, the pre-commit hook and the enforcement matrix validator."""
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUARD = ROOT / 'scripts/hooks/guard-governance-files.py'
ENV = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
ENV.pop('VCGF_ALLOW_GOVERNANCE_CHANGE', None)


def guard(call, allowance=None):
    env = dict(ENV)
    if allowance:
        env['VCGF_ALLOW_GOVERNANCE_CHANGE'] = allowance
    run = subprocess.run([sys.executable, '-B', str(GUARD)], input=json.dumps(call), capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
    return run.returncode, json.loads(run.stdout)


class EnforcementTests(unittest.TestCase):
    def test_edit_of_canonical_control_is_blocked_without_allowance(self):
        code, decision = guard({'tool_name': 'Edit', 'tool_input': {'file_path': 'controls/security/vcgf-sec-001-critical-field-validation.md'}})
        self.assertEqual(code, 2); self.assertEqual(decision['decision'], 'block'); self.assertIn('VCGF-GOV-006', decision['reason'])

    def test_edit_allowed_with_explicit_task_allowance(self):
        code, decision = guard({'tool_name': 'Write', 'tool_input': {'file_path': str(ROOT / 'profiles/baseline/profile.yaml')}}, allowance='task-42')
        self.assertEqual(code, 0); self.assertIn('task-42', decision['reason'])

    def test_ordinary_file_edit_is_allowed(self):
        code, decision = guard({'tool_name': 'Edit', 'tool_input': {'file_path': 'docs/runtime-guide.md'}})
        self.assertEqual(code, 0); self.assertEqual(decision['decision'], 'allow')

    def test_destructive_commands_are_blocked(self):
        for command in ['git push --force origin main', 'rm -rf controls', 'git reset --hard HEAD~3', 'DROP TABLE users;']:
            with self.subTest(command=command):
                code, decision = guard({'tool_name': 'Bash', 'tool_input': {'command': command}})
                self.assertEqual(code, 2)
        code, _ = guard({'tool_name': 'Bash', 'tool_input': {'command': 'git status'}})
        self.assertEqual(code, 0)

    def test_unreadable_call_fails_closed(self):
        run = subprocess.run([sys.executable, '-B', str(GUARD)], input='{not json', capture_output=True, text=True, encoding='utf-8', env=ENV, cwd=ROOT)
        self.assertEqual(run.returncode, 2)

    def test_traversal_into_protected_path_is_caught(self):
        code, _ = guard({'tool_name': 'Write', 'tool_input': {'file_path': 'docs/../controls/README.md'}})
        self.assertEqual(code, 2)

    def test_enforcement_matrix_validates_and_claims_nothing_unexercised(self):
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/validate-enforcement.py')], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        import yaml
        doc = yaml.safe_load((ROOT / 'platforms/enforcement-matrix.yaml').read_text(encoding='utf-8'))
        self.assertEqual(doc['adapters']['claude']['agent-hook'], 'configurable')
        self.assertTrue(all(a['platform-permissions'] != 'available' for a in doc['adapters'].values()))

    def test_pre_commit_hook_runs_fast_validators_on_this_tree(self):
        run = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/hooks/pre-commit-vcgf.py')], capture_output=True, text=True, encoding='utf-8', env=ENV, cwd=ROOT)
        # with nothing staged the hook only runs the validators; a failure here is a real validator failure
        self.assertIn(run.returncode, (0, 1), run.stdout + run.stderr)
        if run.returncode == 1:
            self.assertIn('without VCGF_ALLOW_GOVERNANCE_CHANGE', run.stdout)  # staged governance files in the developer's tree, not a validator failure


if __name__ == '__main__':
    unittest.main()
