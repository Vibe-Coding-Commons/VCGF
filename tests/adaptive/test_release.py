# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Synthetic host callbacks test the algorithm, not real host authentication."""
import copy
import json
from datetime import timedelta

import pytest

from conftest import NOW, ROOT
from runtime.adaptive.common import InputError, canonical_sha, sha_bytes
from runtime.adaptive.release import assess

SHA = 'a' * 40

@pytest.fixture
def record(tmp_path):
    policy = json.loads((ROOT / 'packs/engineering/release-policy.json').read_text())
    data = b'Synthetic test evidence. Not a production acceptance.\n'
    (tmp_path / 'synthetic.txt').write_bytes(data)
    return {
        'contract_version': '1.2.0', 'candidate_commit': SHA,
        'policy_sha256': canonical_sha(policy), 'created_at': NOW.isoformat(),
        'valid_until': (NOW + timedelta(days=1)).isoformat(),
        'checks': [{'id': row['id'], 'status': 'passed',
                    'scope': row['accepted_scopes'][0],
                    'artifacts': [{'path': 'synthetic.txt', 'sha256': sha_bytes(data)}]}
                   for row in policy['required_gates']]
    }

def test_all_green_file_without_host_never_passes(record, tmp_path):
    result = assess(record, tmp_path, SHA, now=NOW)
    assert result['status'] == 'BLOCKED'
    assert any('Trusted host' in x for x in result['blockers'])
    assert not result['execution_authorized']

def test_synthetic_trusted_callback_scoped_pass(record, tmp_path):
    calls = []
    def review(r, candidate, policy):
        calls.append((candidate, policy))
        return candidate == SHA and policy == record['policy_sha256']
    result = assess(record, tmp_path, SHA, now=NOW, trusted_review=review)
    assert result['status'] == 'PASS'
    assert len(calls) == 1 and result['required_gate_count'] == 21
    assert not result['execution_authorized']

@pytest.mark.parametrize('answer', [False, 1, 'true', None])
def test_callback_must_return_exact_true(record, tmp_path, answer):
    assert assess(record, tmp_path, SHA, now=NOW,
                  trusted_review=lambda *_: answer)['status'] == 'BLOCKED'

def test_host_outage_fails_closed(record, tmp_path):
    def unavailable(*args):
        raise RuntimeError('service down')
    result = assess(record, tmp_path, SHA, now=NOW, trusted_review=unavailable)
    assert 'Trusted review service failed' in result['blockers']

@pytest.mark.parametrize('change', ['candidate', 'policy', 'missing', 'extra', 'duplicate',
                                  'failed', 'not_run', 'scope', 'empty', 'digest',
                                  'duplicate-artifact', 'path', 'expired', 'future', 'long'])
def test_invalid_evidence_cannot_pass_even_with_trusted_callback(record, tmp_path, change):
    if change == 'candidate': record['candidate_commit'] = 'b' * 40
    elif change == 'policy': record['policy_sha256'] = 'b' * 64
    elif change == 'missing': record['checks'].pop()
    elif change == 'extra':
        row = copy.deepcopy(record['checks'][0]); row['id'] = 'QG-UNKNOWN'; record['checks'].append(row)
    elif change == 'duplicate': record['checks'].append(copy.deepcopy(record['checks'][0]))
    elif change in ['failed', 'not_run']: record['checks'][0]['status'] = change
    elif change == 'scope': record['checks'][0]['scope'] = 'target_project'
    elif change == 'empty': record['checks'][0]['artifacts'] = []
    elif change == 'digest': record['checks'][0]['artifacts'][0]['sha256'] = '0' * 64
    elif change == 'duplicate-artifact':
        record['checks'][0]['artifacts'].append(copy.deepcopy(record['checks'][0]['artifacts'][0]))
    elif change == 'path': record['checks'][0]['artifacts'][0]['path'] = '../outside.txt'
    elif change == 'expired': record['valid_until'] = NOW.isoformat()
    elif change == 'future': record['created_at'] = (NOW + timedelta(hours=1)).isoformat()
    elif change == 'long': record['valid_until'] = (NOW + timedelta(days=8)).isoformat()
    assert assess(record, tmp_path, SHA, now=NOW, trusted_review=lambda *_: True)['status'] == 'BLOCKED'

def test_artifact_unavailable(record, tmp_path):
    (tmp_path / 'synthetic.txt').unlink()
    result = assess(record, tmp_path, SHA, now=NOW, trusted_review=lambda *_: True)
    assert result['status'] == 'BLOCKED'

@pytest.mark.parametrize('sha', ['main', 'a'*39, 'A'*40, 'a'*41])
def test_candidate_must_be_exact_commit(record, tmp_path, sha):
    with pytest.raises(InputError): assess(record, tmp_path, sha, now=NOW)

def test_naive_clock_rejected(record, tmp_path):
    with pytest.raises(InputError): assess(record, tmp_path, SHA, now=NOW.replace(tzinfo=None))

def test_cli_cannot_self_authenticate(record, tmp_path):
    import subprocess, sys
    path = tmp_path / 'evidence.json'; path.write_text(json.dumps(record))
    run = subprocess.run([sys.executable, str(ROOT/'scripts/vcgf.py'), 'release-readiness',
                          str(path), '--artifact-root', str(tmp_path), '--candidate', SHA],
                         text=True, capture_output=True, timeout=30)
    assert run.returncode == 1, run.stderr
    assert json.loads(run.stdout)['status'] == 'BLOCKED'
