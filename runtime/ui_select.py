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

from .tokens import count

# Section headings kept in a Smart UI requirement card (scope, binding requirements, state/stage contracts, discovery
# signals, acceptance). Settings tables, package candidates, prompts and delivery guides stay in the full standard.
CARD_HEADINGS = ('الهدف ونطاق', 'المتطلبات', 'القبول', 'عقد الحالة', 'إشارات الاكتشاف', 'عقد المراحل')
# Sections of a bound external standard that are catalogues or templates rather than requirements.
EXTERNAL_DROP = ('المكتبات', 'الباكيجز', 'المخرجات المطلوبة', 'الهيكل البرمجي', 'المكوّنات المقترحة', 'المكونات المقترحة')


def smart_card(text):
    """Deterministic requirement card of a Smart UI standard; the full text is returned when no known section is found."""
    parts = text.split('\n## ')
    title = next((line for line in parts[0].splitlines() if line.startswith('# ')), '').strip()
    kept = ['## ' + part.strip() for part in parts[1:] if any(k in part.partition('\n')[0] for k in CARD_HEADINGS)]
    if not kept:
        return text
    return (title + '\n' if title else '') + '\n'.join(kept) + '\n'


def external_card(text):
    """Requirement card of a bound external standard: every section except library catalogues, code skeletons and output templates."""
    parts = text.split('\n## ')
    kept = ['## ' + part.strip() for part in parts[1:] if not any(k in part.partition('\n')[0] for k in EXTERNAL_DROP)]
    if len(kept) == len(parts) - 1 or not kept:
        return text
    return parts[0].rstrip() + '\n\n' + '\n'.join(kept) + '\n'


def _serve(item, detail, card_paths, external_paths=()):
    if detail == 'card' and item['path'] in card_paths:
        text = smart_card(item['text']); measured = count(text)
        return {**item, 'text': text, 'bytes': measured['bytes'], 'tokens': measured['tokens'], 'served': 'card'}
    if detail == 'card' and item['path'] in external_paths:
        text = external_card(item['text']); measured = count(text)
        return {**item, 'text': text, 'bytes': measured['bytes'], 'tokens': measured['tokens'], 'served': 'card' if text != item['text'] else 'full'}
    return {**item, 'served': 'full'}


SIGNAL_KEYS = ('signals', 'interaction_signals', 'composition_signals', 'journey_signals')


def infer_signals(binding, route_result, screen_context):
    """Signals derived from the reviewed route intents and from screen facts (deterministic, recorded as inferred)."""
    rules = binding.get('inference') or {}
    inferred = {k: [] for k in SIGNAL_KEYS}

    def add(table):
        for key, values in (table or {}).items():
            for v in values:
                if v not in (screen_context.get(key) or []) and v not in inferred[key]:
                    inferred[key].append(v)
    intents = route_result.get('intents') or []
    for intent in intents:
        add((rules.get('intents') or {}).get(intent))
    screen_rules = rules.get('screen') or {}
    devices = set(screen_context.get('devices') or [])
    if devices and devices <= {'mobile', 'tablet'}:
        add(screen_rules.get('mobile_only_devices'))
    if 'large-screen' in devices:
        add(screen_rules.get('large_screen_devices'))
    if screen_context.get('sensitive_data') is True:
        add(screen_rules.get('sensitive_data'))
    if 'rtl' in (screen_context.get('directions') or []):
        add(screen_rules.get('rtl_direction'))
    return {k: sorted(v) for k, v in inferred.items() if v}


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
    detail = 'full' if route_result.get('mode') == 'deep' else 'card'  # requirement cards unless the route is a deep review
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

    inferred = infer_signals(binding, route_result, screen_context)
    merged_context = dict(screen_context)
    for key, values in inferred.items():
        merged_context[key] = sorted(set(merged_context.get(key) or []) | set(values))
    never = tuple(binding.get('never_load_prefixes') or [])
    if not ux_controls:
        status = 'not_applicable'
        warnings.append(f'no user-experience control is in the route for profile {profile}; Smart UI standards are not '
                        'loaded. Confirm a profile that requires VCGF-UX-001 or add it with overlay_add_controls.')
    elif screen_context.get('has_ui') is False:
        status = 'no_ui'
    else:
        status = 'selected'
        plan = _run_selector(root, pack, binding, merged_context)
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
    for item in standards + documents:
        if item['path'].startswith(never):  # catalogues, reports and snapshots are never context, whatever a selection says
            raise ValueError('refusing to serve a non-standard package file: ' + item['path'])
    standards.sort(key=lambda s: (s['layer'], s['standard_id']))
    deferred.sort(key=lambda s: (s['layer'], s['standard_id']))
    documents.sort(key=lambda d: d['path'])
    records = [{'path': s['path'], 'sha256': s['sha256']} for s in standards] + [{'path': d['path'], 'sha256': d['sha256']} for d in documents]
    active, cost, cost_bytes = [], 0, 0
    measurement, method = count('')['measurement'], count('')['method']
    if records:
        if budget <= 0:
            cost_bytes = sum(s['bytes'] for s in standards) + sum(d['bytes'] for d in documents)
            cost = sum(count(confined(pack, r['path']).read_text(encoding='utf-8'))['tokens'] for r in records)
            blockers.append('no remaining task budget for Smart UI standards: split the task or explicitly raise the budget; never drop governing controls')
        else:
            loaded = load(pack, records, 10 ** 12)  # pinned, confined read; the budget is applied to the served text below
            card_paths = {s['path'] for s in standards if s['layer'] != 'external-standards'}
            external_paths = {s['path'] for s in standards if s['layer'] == 'external-standards'}
            served = [_serve(item, detail, card_paths, external_paths) for item in loaded['items']]
            cost, cost_bytes = sum(x['tokens'] for x in served), sum(x['bytes'] for x in served)
            served_bytes = {x['path']: x['bytes'] for x in served}
            for s in standards:
                s['served_bytes'] = served_bytes.get(s['path'], s['bytes'])
            if cost > budget:
                blockers.append('budget exceeded: Smart UI standards not loaded; split the task or explicitly raise the budget; never drop governing controls')
            else:
                active = served
    if blockers:
        status = 'blocked'
    index = acceptance_index(root)
    acceptance = {cid: sorted(t['id'] for t in index[cid]['tests']) for cid in ux_controls if cid in index}
    result = {'contract_version': '1.1.0', 'task_id': route_result['task_id'], 'route_sha256': digest(route_result),
              'input_sha256': digest({'route': route_result, 'screen_context': screen_context, 'budget': budget}),
              'profile': profile, 'status': status, 'ux_controls_in_route': ux_controls, 'context_detail': detail,
              'package': {'path': binding['package_root'], 'version': manifest['package_version'], 'status': manifest['status'],
                          'manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest()},
              'layers': layers, 'standards': standards, 'deferred_standards': deferred, 'governance_documents': documents,
              'acceptance_tests': acceptance,
              'signals': {'explicit': {k: sorted(screen_context.get(k) or []) for k in SIGNAL_KEYS if screen_context.get(k)}, 'inferred': inferred},
              'precedence': {'authoritative': binding['precedence']['authoritative'], 'implementing': binding['precedence']['implementing']},
              'budget': {'limit_tokens': max(budget, 0), 'cost_tokens': cost, 'cost_bytes': cost_bytes, 'measurement': measurement, 'method': method},
              'blockers': blockers, 'warnings': warnings, 'selection_plan_sha256': digest(plan) if plan is not None else None}
    errors = validate_contract('ui-selection', result)
    if errors:
        raise ValueError('; '.join(errors))
    return {'selection': result, 'active_context': [] if blockers else active, 'selection_plan': plan}
