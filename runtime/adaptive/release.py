# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Fail-closed release acceptance, separate from repository structural checks.

No file can authenticate its own author. A trusted host-owned review callback is
required even when every declared check is green. The public CLI has no such
identity integration and deliberately cannot return release PASS.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable

from .common import InputError, canonical_sha, parse_time, read_json, read_source, sha_bytes, utc_now, validate

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / 'packs/engineering/release-policy.json'
SCHEMA = ROOT / 'schemas/v1.2.0/release-evidence.schema.json'
TrustedReview = Callable[[dict, str, str], bool]


def assess(record: dict, artifact_root: Path, expected_candidate: str, *,
           now: datetime | None = None, trusted_review: TrustedReview | None = None,
           policy_path: Path = POLICY) -> dict:
    """Evaluate explicit gate coverage and byte-bound evidence; never publish."""
    validate(SCHEMA, record)
    if not re.fullmatch(r'[0-9a-f]{40}', expected_candidate):
        raise InputError('Expected candidate must be an explicit Git commit SHA')
    now = now or utc_now()
    if now.tzinfo is None:
        raise InputError('Release evaluation time must be timezone aware')
    policy = read_json(policy_path)
    policy_hash = canonical_sha(policy)
    blockers: list[str] = []
    if record['candidate_commit'] != expected_candidate:
        blockers.append('Evidence belongs to a different candidate commit')
    if record['policy_sha256'] != policy_hash:
        blockers.append('Evidence is stale for the required release policy')
    issued, expires = parse_time(record['created_at']), parse_time(record['valid_until'])
    if not issued <= now < expires or expires - issued > timedelta(days=7):
        blockers.append('Release evidence is future, expired or exceeds seven-day validity')
    wanted = {row['id']: row for row in policy['required_gates']}
    ids = [row['id'] for row in record['checks']]
    if len(ids) != len(set(ids)):
        blockers.append('Duplicate gate identifiers')
    supplied = {row['id']: row for row in record['checks']}
    for extra in sorted(set(supplied) - set(wanted)):
        blockers.append('Unknown gate: ' + extra)
    verified = []
    for gid, rule in wanted.items():
        check = supplied.get(gid)
        if check is None:
            blockers.append('Missing gate: ' + gid)
            continue
        if check['status'] != 'passed':
            blockers.append(gid + ': ' + check['status'])
        if check['scope'] not in rule['accepted_scopes']:
            blockers.append(gid + ': evidence scope is insufficient')
        if not check['artifacts']:
            blockers.append(gid + ': no evidence artifacts')
        seen: dict[str, str] = {}
        for artifact in check['artifacts']:
            reference = artifact['path']
            if reference in seen:
                blockers.append(gid + ': duplicate artifact reference')
                continue
            seen[reference] = artifact['sha256']
            try:
                actual = sha_bytes(read_source(artifact_root, reference))
                if actual != artifact['sha256']:
                    blockers.append(gid + ': artifact hash mismatch')
                else:
                    verified.append({'gate': gid, 'path': reference, 'sha256': actual})
            except (InputError, OSError):
                blockers.append(gid + ': evidence artifact unavailable or unsafe')
    # Authenticity must come from the execution host, never record['reviewer'].
    if trusted_review is None:
        blockers.append('Trusted host review/identity integration is unavailable')
    else:
        try:
            if trusted_review(record, expected_candidate, policy_hash) is not True:
                blockers.append('Trusted review did not authenticate scoped evidence')
        except Exception:
            # Authentication failure must be fail-closed, including host outages.
            blockers.append('Trusted review service failed')
    return {'status': 'BLOCKED' if blockers else 'PASS',
            'candidate_commit': expected_candidate, 'policy_sha256': policy_hash,
            'required_gate_count': len(wanted), 'declared_gate_count': len(ids),
            'verified_artifacts': verified, 'blockers': sorted(set(blockers)),
            'execution_authorized': False,
            'claim': 'Evidence admission decision only; no publication or deployment performed'}
