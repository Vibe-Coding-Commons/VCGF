# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Validate spec/applicability-matrix.yaml and the Router reachability invariant.

Invariants (static, over the canonical files; no product claim):
1. Every control in spec/control-catalog.yaml has exactly one matrix entry and every entry names a catalog control.
2. Every trigger capability exists in capabilities/; load_point is a declared load point; always is boolean true.
3. A capability that lists a control in control_ids appears in that control's triggers (the floor is never hidden).
4. Every non-deprecated control is reachable for the high-assurance profile from at least one routing intent, through
   the capability floor, routing-policy additions (minimum, risk, review modes) or the profile layer.
5. No trigger names a capability that no intent can select (dead triggers would promise reachability that never happens).
"""
from vcgf_lib import *

ROUTER_RISK_ADDS = {'VCGF-GOV-002', 'VCGF-GOV-004', 'VCGF-TEST-002', 'VCGF-SEC-006'}  # runtime/router.py HIGH/CRITICAL
ROUTER_CRITICAL_ADDS = {'VCGF-REL-003'}                                               # runtime/router.py CRITICAL
TRIGGER_KEYS = {'capabilities', 'always', 'router_policy'}


def closure(caps, start):
    seen = set(); stack = list(start)
    while stack:
        c = stack.pop()
        if c in seen or c not in caps: continue
        seen.add(c)
        for d in caps[c].get('dependencies') or []:
            if d.get('relation') in {'requires', 'requires_when', 'any_of'}: stack.extend(d.get('targets') or [])
    return seen


def main():
    errors = []
    catalog = {c['id']: c for c in load_yaml(ROOT / 'spec/control-catalog.yaml')['controls']}
    doc = load_yaml(ROOT / 'spec/applicability-matrix.yaml')
    if doc.get('matrix_version') != '1.0.0': errors.append('spec/applicability-matrix.yaml: matrix_version must be 1.0.0')
    load_points = set(doc.get('load_points') or [])
    matrix = doc.get('controls') or {}
    caps = {}
    for p in sorted((ROOT / 'capabilities').glob('*.yaml')):
        d = load_yaml(p); caps[d['capability_id']] = d
    policy = load_yaml(ROOT / 'runtime/routing-policy.yaml')
    profiles = {p.parent.name: set(load_yaml(p)['required_controls']) for p in (ROOT / 'profiles').glob('*/profile.yaml')}
    for cid in sorted(set(catalog) - set(matrix)): errors.append(f'spec/applicability-matrix.yaml: missing entry for {cid}')
    for cid in sorted(set(matrix) - set(catalog)): errors.append(f'spec/applicability-matrix.yaml: unknown control {cid}')
    for cid, entry in matrix.items():
        if not isinstance(entry, dict): errors.append(f'{cid}: entry must be a mapping'); continue
        if entry.get('load_point') not in load_points: errors.append(f'{cid}: load_point must be one of {sorted(load_points)}')
        if not str(entry.get('rationale') or '').strip(): errors.append(f'{cid}: rationale is required')
        trig = entry.get('triggers')
        if not isinstance(trig, dict) or not trig: errors.append(f'{cid}: triggers mapping is required'); continue
        unknown = sorted(set(trig) - TRIGGER_KEYS)
        if unknown: errors.append(f'{cid}: unknown trigger keys {unknown}')
        if 'always' in trig and trig['always'] is not True: errors.append(f'{cid}: always must be true when present')
        for cap in trig.get('capabilities') or []:
            if cap not in caps: errors.append(f'{cid}: unknown trigger capability {cap!r}')
    for cap, d in caps.items():
        for cid in d.get('control_ids') or []:
            entry = matrix.get(cid)
            if not isinstance(entry, dict): continue
            trig = entry.get('triggers') or {}
            if cap not in (trig.get('capabilities') or []) and not trig.get('always'):
                errors.append(f'{cid}: capability {cap} loads this control but is not listed in its triggers')
    # Reachability for high-assurance (the superset profile) over every intent, mirroring runtime/router.py statically.
    minimum = set(policy['minimum_controls']); deep = set(policy['deep_review_controls']); standard = set(policy['standard_review_controls'])
    selectable = set()
    reachable = minimum | deep | standard | ROUTER_RISK_ADDS | ROUTER_CRITICAL_ADDS
    for intent in policy['intents'].values():
        sel = closure(caps, list(intent['capabilities']) + ['development-agent', 'product-ai'])
        selectable |= sel
        for cap in sel: reachable |= set(caps[cap].get('control_ids') or [])
        for cid in profiles.get('high-assurance', set()):
            trig = (matrix.get(cid) or {}).get('triggers') or {} if isinstance(matrix.get(cid), dict) else {}
            if trig.get('always') or set(trig.get('capabilities') or []) & sel: reachable.add(cid)
    unreachable = sorted(cid for cid, c in catalog.items() if c.get('status') != 'deprecated' and cid not in reachable)
    if unreachable: errors.append(f'controls unreachable by the Router for high-assurance from every intent: {unreachable}')
    for cid, entry in matrix.items():
        if not isinstance(entry, dict): continue
        dead = sorted(set((entry.get('triggers') or {}).get('capabilities') or []) - selectable)
        if dead: errors.append(f'{cid}: trigger capabilities no intent can select: {dead}')
    for cid in sorted(profiles.get('high-assurance', set()) - set(catalog)): errors.append(f'profiles/high-assurance: unknown control {cid}')
    fail_if(errors)
    print(f'PASS validate-applicability: {len(matrix)} controls, 0 unreachable, {len(selectable)} selectable capabilities')


if __name__ == '__main__': main()
