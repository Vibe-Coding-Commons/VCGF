# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Integrate both engines, VCGF's canonical controls and its existing loader.

A proposal is not an authorization. With --task/--context the existing VCGF 1.1
router is also invoked, and all its blockers remain effective. No project writes,
package installation, credential access or deployment are performed here.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .common import InputError, canonical_sha, load_catalog, parse_time, read_source, sha_bytes, utc_now
from .engineering import advise
from .ux import explain

ROOT = Path(__file__).resolve().parents[2]
CONTROL_IDS = [
    'VCGF-AI-001', 'VCGF-AI-002', 'VCGF-AI-003', 'VCGF-AI-005',
    'VCGF-ARCH-003', 'VCGF-ARCH-004', 'VCGF-DEP-001', 'VCGF-DEP-002',
    'VCGF-GOV-001', 'VCGF-GOV-004', 'VCGF-GOV-005',
    'VCGF-SEC-004', 'VCGF-TEST-002', 'VCGF-TEST-003'
]
PACKS = ['packs/engineering/adaptive.md', 'packs/ux/adaptive.md']


def source_evidence(fingerprint: dict, discovery: dict, project_root: Path,
                    now: datetime, max_age_days: int = 30) -> tuple[list[dict], list[str]]:
    blockers: list[str] = []
    records: dict[str, str] = {}
    evidence: list[dict] = []
    for label, record in [('fingerprint', fingerprint), ('discovery', discovery)]:
        captured = parse_time(record['captured_at'])
        if not captured <= now < captured + timedelta(days=max_age_days):
            blockers.append(label + ': stale or future discovery; re-inspect')
    inputs = [(s['path'], s['sha256'], s['kind'] == 'local_file') for s in fingerprint['sources']]
    inputs += [(s['ref'], s['sha256'], s['kind'] in {'repo_file', 'product_document'}) for s in discovery['source_refs']]
    for ref, expected, locally_verifiable in inputs:
        if not locally_verifiable:
            blockers.append('External/reviewer assertion lacks a trusted observation adapter')
            continue
        if not expected:
            blockers.append('Missing source digest: ' + ref)
            continue
        if ref in records:
            if records[ref] != expected:
                blockers.append('Conflicting source digests: ' + ref)
            continue
        records[ref] = expected
        try:
            actual = sha_bytes(read_source(project_root, ref))
            if actual != expected:
                blockers.append('Source bytes changed: ' + ref)
            else:
                evidence.append({'path': ref, 'sha256': actual, 'verification': 'bytes_only'})
        except (InputError, OSError):
            blockers.append('Source unavailable or unsafe')
    if not evidence:
        blockers.append('At least one real, hash-verified local source is required')
    return sorted(evidence, key=lambda r: r['path']), sorted(set(blockers))


def plan(fingerprint: dict, discovery: dict, project_root: Path, *,
         task: dict | None = None, context: dict | None = None,
         budget_bytes: int = 131_072, now: datetime | None = None,
         framework_root: Path = ROOT) -> dict[str, Any]:
    """Plan from supplied facts. Trusted host authorization remains mandatory later."""
    if type(budget_bytes) is not int or not 1 <= budget_bytes <= 16 * 1_048_576:
        raise InputError('Planning budget must be an integer from 1 byte to 16 MiB')
    now = now or utc_now()
    if now.tzinfo is None:
        raise InputError('Planning time must be timezone aware')
    engineering = advise(fingerprint, decided_at=now.isoformat())
    ux = explain(discovery)
    blockers = engineering['blockers'] + ux['blockers']
    if fingerprint['project_id'] != discovery['project_id']:
        blockers.append('Engineering and UX project identifiers do not match')
    sources, source_blockers = source_evidence(fingerprint, discovery, Path(project_root), now)
    blockers.extend(source_blockers)
    if bool(task is None) != bool(context is None):
        blockers.append('Task and context must be supplied together')
    governance: dict[str, Any] = {'status': 'not_requested', 'execution_authorized': False}
    if task is not None and context is not None:
        if task.get('intent') != 'design-review':
            blockers.append('Combined design planning requires explicit design-review classification')
        elif context.get('project_id') != fingerprint['project_id']:
            blockers.append('Legacy context belongs to another project')
        else:
            try:
                from runtime.router import route
                routed = route(task, context, str(project_root), now=now, root=framework_root)
                governance = {'status': routed['route']['decision'], 'route': routed['route'],
                              'execution_authorized': False}
                blockers.extend(routed['route']['blockers'])
                if not set(CONTROL_IDS) <= set(routed['route']['selected_control_ids']):
                    blockers.append('Legacy route omitted required adaptive controls')
            except (ImportError, ValueError, OSError, KeyError, TypeError) as exc:
                governance = {'status': 'unavailable', 'error_type': type(exc).__name__, 'execution_authorized': False}
                blockers.append('Legacy routing could not be verified; full checkout and valid context required')
    # Reuse the real VCGF context loader, not a look-alike implementation.
    from runtime.loader import load
    catalog = load_catalog(framework_root / 'spec/control-catalog.yaml')
    paths = {row['id']: row['path'] for row in catalog['controls']}
    records = []
    for ref in [paths[cid] for cid in CONTROL_IDS] + PACKS:
        data = read_source(framework_root, ref)
        records.append({'path': ref, 'sha256': sha_bytes(data)})
    loaded = load(framework_root, records, budget_bytes)
    payload = {'engineering': engineering, 'ux': ux, 'governance': governance}
    payload_size = len(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf-8'))
    total_cost = loaded['cost_tokens'] + payload_size
    if loaded['blocked'] or total_cost > budget_bytes:
        blockers.append('Combined planning/context byte budget exceeded; split or explicitly raise the budget')
    # Recheck actual source bytes after the decision. Execution hosts still need a lock.
    after, changed = source_evidence(fingerprint, discovery, Path(project_root), now)
    if after != sources or changed != source_blockers:
        blockers.append('Source snapshot changed during planning')
    blockers = sorted(set(blockers))
    return {
        'contract_version': '1.2.0', 'project_id': fingerprint['project_id'],
        'plan_id': 'PLAN-' + canonical_sha({'fingerprint': fingerprint, 'discovery': discovery,
                                           'engineering_policy': engineering['catalog_sha256'],
                                           'ux_policy': ux['catalog_sha256']})[:20],
        'state': 'blocked' if blockers else 'ready_to_plan' if governance['status'] == 'ready_to_plan' else 'proposed',
        **payload, 'sources': sources, 'selected_control_ids': CONTROL_IDS,
        'loaded_context': loaded['items'] if not blockers else [], 'blockers': blockers,
        'budget': {'unit': 'utf8_bytes', 'estimated_total': total_cost, 'limit': budget_bytes},
        'execution_authorized': False,
        'limitations': [
            'Hash equality proves source bytes, not the truth of human/AI interpretation.',
            'Goal priorities are explicit reviewed classifications, not autonomous language understanding.',
            'No gate, proposed pattern, or user-confirmation field authorizes execution or certifies a product.',
            'Target framework runtime, manual accessibility and real-user evidence remain separate gates.'
        ]
    }
