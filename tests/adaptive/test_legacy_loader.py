# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Targeted regression of the actual VCGF loader, not the full legacy suite."""
import hashlib
import pytest
from runtime.loader import load

@pytest.fixture
def entries(tmp_path):
    (tmp_path/'safe.md').write_bytes(b'reference')
    return [{'path':'safe.md','sha256':hashlib.sha256(b'reference').hexdigest()}]

def test_same_digest_deduplicates(tmp_path, entries):
    out=load(tmp_path,entries*2,100)
    # bytes are measured; cost_tokens is the documented estimate (9 ASCII characters -> 3 tokens)
    assert len(out['items'])==1 and out['cost_bytes']==9 and out['cost_tokens']==3

def test_conflicting_digest_rejected(tmp_path,entries):
    with pytest.raises(ValueError,match='conflicting hashes'):
        load(tmp_path,entries+[{'path':'safe.md','sha256':'0'*64}],100)

def test_stale_digest_rejected(tmp_path,entries):
    (tmp_path/'safe.md').write_bytes(b'edited')
    with pytest.raises(ValueError,match='stale registry'):
        load(tmp_path,entries,100)

def test_over_budget_never_drops_controls_silently(tmp_path,entries):
    out=load(tmp_path,entries,1)
    assert out['blocked'] and not out['items'] and out['cost_bytes']==9 and out['cost_tokens']==3

@pytest.mark.parametrize('budget',[True,0,-1,1.5,'100'])
def test_invalid_budget_rejected(tmp_path,entries,budget):
    with pytest.raises(ValueError):load(tmp_path,entries,budget)

def test_symlink_rejected(tmp_path,entries):
    (tmp_path/'link.md').symlink_to(tmp_path/'safe.md')
    with pytest.raises(ValueError,match='symlink'):
        load(tmp_path,[{**entries[0],'path':'link.md'}],100)
