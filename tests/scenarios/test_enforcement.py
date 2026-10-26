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
ENV.pop('VCGF_ALLOW_GOVERNANCE_CHANGE', None); ENV.pop('VCGF_GOVERNANCE_APPROVAL', None)


def approval_record(path, **over):
    import copy
    record = copy.deepcopy(json.loads((ROOT / 'tests/fixtures/v1.1/approval.json').read_text())['record'])
    record.update({'action': 'governance-change', 'resources': ['profiles/baseline/profile.yaml'], 'issued_at': '2026-10-01T00:00:00Z', 'decision_at': '2026-10-01T00:00:00Z', 'expires_at': '2030-01-01T00:00:00Z'})
    record.update(over)
    Path(path).write_text(json.dumps(record))
    return str(path)


def guard(call, allowance=None, approval=None):
    env = dict(ENV)
    if allowance:
        env['VCGF_ALLOW_GOVERNANCE_CHANGE'] = allowance
    if approval:
        env['VCGF_GOVERNANCE_APPROVAL'] = approval
    run = subprocess.run([sys.executable, '-B', str(GUARD)], input=json.dumps(call), capture_output=True, text=True, encoding='utf-8', env=env, cwd=ROOT)
    return run.returncode, json.loads(run.stdout)


class EnforcementTests(unittest.TestCase):
    def test_edit_of_canonical_control_is_blocked_without_allowance(self):
        code, decision = guard({'tool_name': 'Edit', 'tool_input': {'file_path': 'controls/security/vcgf-sec-001-critical-field-validation.md'}})
        self.assertEqual(code, 2); self.assertEqual(decision['decision'], 'block'); self.assertIn('VCGF-GOV-006', decision['reason'])

    def test_environment_flag_alone_never_unlocks(self):
        code, decision = guard({'tool_name': 'Write', 'tool_input': {'file_path': str(ROOT / 'profiles/baseline/profile.yaml')}}, allowance='task-42')
        self.assertEqual(code, 2); self.assertIn('approval record', decision['reason'])

    def test_edit_allowed_only_with_a_covering_approval_record(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            ok = approval_record(Path(temp, 'ok.json'))
            code, decision = guard({'tool_name': 'Write', 'tool_input': {'file_path': str(ROOT / 'profiles/baseline/profile.yaml')}}, approval=ok)
            self.assertEqual(code, 0); self.assertIn('fixture', decision['reason']); self.assertIn('structural check only', decision['reason'])
            for name, over in [('other-resource', {'resources': ['controls/README.md']}), ('expired', {'expires_at': '2026-10-02T00:00:00Z'}), ('pending', {'status': 'pending'}),
                               ('other-action', {'action': 'deploy'}), ('self-approved', {'requested_by': 'reviewer', 'decision_by': {'subject': 'reviewer', 'role': 'owner', 'authority_evidence': 'x'}})]:
                with self.subTest(case=name):
                    bad = approval_record(Path(temp, name + '.json'), **over)
                    code, decision = guard({'tool_name': 'Write', 'tool_input': {'file_path': str(ROOT / 'profiles/baseline/profile.yaml')}}, approval=bad)
                    self.assertEqual(code, 2, decision)
            Path(temp, 'garbage.json').write_text('{not json')
            code, _ = guard({'tool_name': 'Write', 'tool_input': {'file_path': 'controls/README.md'}}, approval=str(Path(temp, 'garbage.json')))
            self.assertEqual(code, 2)
            code, _ = guard({'tool_name': 'Bash', 'tool_input': {'command': 'rm -rf build'}}, approval=ok)
            self.assertEqual(code, 2)  # the record names no shell:destructive resource

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
            self.assertIn('covering approval record', run.stdout)  # staged governance files in the developer's tree, not a validator failure


if __name__ == '__main__':
    unittest.main()
