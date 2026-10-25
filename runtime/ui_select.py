# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Governed Smart UI selection: binds the frozen Smart UI package to the Task Router.

The Router (profile layer + spec/applicability-matrix.yaml) decides which user-experience controls apply to a task.
This module then runs the package's own reference selector on an explicit screen context and loads ONLY the
standards whose governing control (runtime/ui-bindings.yaml) is in the route, hash-pinned by the package manifest
and confined to the package directory, within the remaining task budget. Standards selected by signals but not
governed by a control in the route are reported as deferred and never loaded. The package is never loaded wholesale.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry

from .acceptance import acceptance_index
from .context import digest
from .contracts import FORMATS, ROOT, validate_contract, _offline_only
from .loader import confined, load

BUDGET_METHOD = 'UTF-8 byte upper estimate of the loaded Smart UI standards; not a tokenizer measurement'


def bindings(root=ROOT):
    return yaml.safe_load((Path(root) / 'runtime' / 'ui-bindings.yaml').read_text(encoding='utf-8'))


def governing_controls(binding):
    controls = set(binding['governance_documents'])
    for layer in binding['layers'].values():
        controls |= set(layer['governing_controls'])
    for external in binding['external_standards'].values():
        controls |= set(external['governing_controls'])
    return controls


def _run_selector(root, pack, binding, screen_context):
    with tempfile.TemporaryDirectory() as temp:
        source = Path(temp) / 'screen-context.json'
        output = Path(temp) / 'selection-plan.json'
        source.write_text(json.dumps(screen_context, ensure_ascii=False, sort_keys=True), encoding='utf-8')
        completed = subprocess.run([sys.executable, '-I', '-B', str(confined(pack, binding['selector'])), str(source),
                                    '--output', str(output)], cwd=str(root), capture_output=True, text=True, timeout=120)
        if completed.returncode != 0:
            raise ValueError('Smart UI selector failed: ' + (completed.stderr or completed.stdout).strip()[:500])
        return json.loads(output.read_text(encoding='utf-8'))


def _validate_screen_context(pack, binding, screen_context):
    schema = json.loads(confined(pack, binding['screen_context_schema']).read_text(encoding='utf-8'))
    validator = Draft202012Validator(schema, registry=Registry(retrieve=_offline_only), format_checker=FORMATS)
    errors = sorted(f'{e.json_path}: {e.message}' for e in validator.iter_errors(screen_context))
    if errors:
        raise ValueError('invalid screen context: ' + '; '.join(errors[:5]))


def select_ui(route_result, screen_context, budget=None, root=ROOT):
    root = Path(root)
    if isinstance(route_result, dict) and 'route' in route_result and 'selected_control_ids' not in route_result:
        route_result = route_result['route']  # accept the full output of `vcgf.py route`
    errors = validate_contract('route-result', route_result)
    if errors:
        raise ValueError('invalid route result: ' + '; '.join(errors))
    if not isinstance(screen_context, dict):
        raise ValueError('screen context must be an object')
    binding = bindings(root)
    pack = confined(root, binding['package_root'])
    _validate_screen_context(pack, binding, screen_context)
    manifest_bytes = confined(pack, binding['manifest']).read_bytes()
    manifest = json.loads(manifest_bytes)
    pinned = {entry['path']: entry for entry in manifest['files']}
    selected = set(route_result['selected_control_ids'])
    ux_controls = sorted(selected & governing_controls(binding))
    if budget is None:
        budget = route_result['budget']['limit_tokens'] - (route_result['budget']['cost_tokens'] or 0)
    if type(budget) is not int:
        raise ValueError('budget must be an integer')
    profile = route_result['profile']
    blockers, warnings, standards, deferred, documents = [], [], [], [], []
    layers = {}
    for name, layer in binding['layers'].items():
        governing = sorted(layer['governing_controls'])
        layers[name] = {'state': 'not_selected', 'governing_controls': governing,
                        'missing_controls': [] if set(governing) & selected else governing}
    if route_result['decision'] != 'ready_to_plan':
        blockers.append('route is not ready_to_plan; resolve the route blockers before Smart UI selection')
    plan = None

    def pin(path):
        entry = pinned.get(path)
        if entry is None:
            raise ValueError('standard is not pinned by the package manifest: ' + path)
        return entry

    if not ux_controls:
        status = 'not_applicable'
        warnings.append(f'no user-experience control is in the route for profile {profile}; Smart UI standards are not '
                        'loaded. Confirm a profile that requires VCGF-UX-001 or add it with overlay_add_controls.')
    elif screen_context.get('has_ui') is False:
        status = 'no_ui'
    else:
        status = 'selected'
        plan = _run_selector(root, pack, binding, screen_context)
        for name, layer in binding['layers'].items():
            governing = set(layer['governing_controls'])
            items = plan.get(layer['plan_key']) or []
            bound = sorted(governing & selected)
            for item in items:
                entry = pin(item['standard_path'])
                if bound:
                    standards.append({'standard_id': item['standard_id'], 'layer': name, 'path': item['standard_path'],
                                      'sha256': entry['sha256'], 'bytes': entry['bytes'], 'bound_controls': bound,
                                      'decision': item.get('decision') or 'required',
                                      'matched_signals': sorted(item.get('matched_signals') or [])})
                else:
                    deferred.append({'standard_id': item['standard_id'], 'layer': name, 'path': item['standard_path'],
                                     'missing_controls': sorted(governing),
                                     'reason': f"signals matched but none of {', '.join(sorted(governing))} is in the route for profile {profile}; not loaded"})
            if items:
                layers[name]['state'] = 'loaded' if bound else 'deferred'
        for item in plan.get('external_standards') or []:
            external = binding['external_standards'].get(item['standard_id'])
            governing = set(external['governing_controls']) if external else set()
            entry = pin(item['standard_path'])
            bound = sorted(governing & selected)
            if bound:
                standards.append({'standard_id': item['standard_id'], 'layer': 'external-standards', 'path': item['standard_path'],
                                  'sha256': entry['sha256'], 'bytes': entry['bytes'], 'bound_controls': bound,
                                  'decision': item.get('decision') or 'required', 'matched_signals': sorted(item.get('matched_signals') or [])})
            else:
                reason = ('no user-experience control governs this bound standard; not loaded' if not external else
                          f"signals matched but none of {', '.join(sorted(governing))} is in the route for profile {profile}; not loaded")
                deferred.append({'standard_id': item['standard_id'], 'layer': 'external-standards', 'path': item['standard_path'],
                                 'missing_controls': sorted(governing), 'reason': reason})
        for control_id in ux_controls:
            for path in binding['governance_documents'].get(control_id, []):
                entry = pin(path)
                existing = next((d for d in documents if d['path'] == path), None)
                if existing:
                    existing['bound_controls'] = sorted(set(existing['bound_controls']) | {control_id})
                else:
                    documents.append({'path': path, 'sha256': entry['sha256'], 'bytes': entry['bytes'], 'bound_controls': [control_id]})
        warnings.extend(str(w) for w in plan.get('warnings') or [])
    standards.sort(key=lambda s: (s['layer'], s['standard_id']))
    deferred.sort(key=lambda s: (s['layer'], s['standard_id']))
    documents.sort(key=lambda d: d['path'])
    records = [{'path': s['path'], 'sha256': s['sha256']} for s in standards] + [{'path': d['path'], 'sha256': d['sha256']} for d in documents]
    active, cost = [], 0
    if records:
        if budget <= 0:
            cost = sum(s['bytes'] for s in standards) + sum(d['bytes'] for d in documents)
            blockers.append('no remaining task budget for Smart UI standards: split the task or explicitly raise the budget; never drop governing controls')
        else:
            loaded = load(pack, records, budget)
            cost = loaded['cost_tokens']
            if loaded['blocked']:
                blockers.append('budget exceeded: Smart UI standards not loaded; split the task or explicitly raise the budget; never drop governing controls')
            else:
                active = loaded['items']
    if blockers:
        status = 'blocked'
    index = acceptance_index(root)
    acceptance = {cid: sorted(t['id'] for t in index[cid]['tests']) for cid in ux_controls if cid in index}
    result = {'contract_version': '1.1.0', 'task_id': route_result['task_id'], 'route_sha256': digest(route_result),
              'input_sha256': digest({'route': route_result, 'screen_context': screen_context, 'budget': budget}),
              'profile': profile, 'status': status, 'ux_controls_in_route': ux_controls,
              'package': {'path': binding['package_root'], 'version': manifest['package_version'], 'status': manifest['status'],
                          'manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest()},
              'layers': layers, 'standards': standards, 'deferred_standards': deferred, 'governance_documents': documents,
              'acceptance_tests': acceptance,
              'budget': {'limit_tokens': max(budget, 0), 'cost_tokens': cost, 'measurement': 'estimated', 'method': BUDGET_METHOD},
              'blockers': blockers, 'warnings': warnings, 'selection_plan_sha256': digest(plan) if plan is not None else None}
    errors = validate_contract('ui-selection', result)
    if errors:
        raise ValueError('; '.join(errors))
    return {'selection': result, 'active_context': [] if blockers else active, 'selection_plan': plan}
