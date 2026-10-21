# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Deterministic UX advisor using explicit, reviewed discovery classifications.

The coordinator verifies local source bytes. This module proposes experience
patterns; it does not render target applications or certify accessibility.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
DISCOVERY_SCHEMA = ROOT / 'schemas/v1.2.0/ux-discovery.schema.json'
DECISION_SCHEMA = ROOT / 'schemas/v1.2.0/ux-decision.schema.json'
CATALOG_PATH = ROOT / 'packs/ux/catalog.yaml'


from .common import canonical_sha as digest, validate, load_catalog
from .schools import rank_schools, locale_direction


def is_rtl(locale: str) -> bool:
    return locale_direction(locale) == 'rtl'


def explain(discovery: dict) -> dict:
    validate(DISCOVERY_SCHEMA, discovery)
    catalog = load_catalog(CATALOG_PATH)
    if catalog['status'] != 'integration-candidate':
        raise ValueError('An explicitly identified integration-candidate catalog is required')

    source_refs = [s['ref'] for s in discovery['source_refs']]
    blockers: list[str] = []
    trace: list[dict] = []
    goals = discovery['product_goals']
    people = discovery['audiences']
    workflows = discovery['workflows']
    device = discovery['devices']
    localization = discovery['localization']
    unknowns = discovery['unknown_facts']
    ranking = rank_schools(discovery, catalog)
    school_data = next(x for x in catalog['design_schools'].values() if x['school'] == ranking[0]['school'])
    primary_school = school_data['school']
    density = school_data['density']
    navigation = school_data['navigation']

    def rule(rule_id: str, outcome: str, reason: str, facts: list[str]):
        trace.append({'rule_id': rule_id, 'outcome': outcome, 'reason': reason,
                      'observed_facts': facts})

    def block_if(cond: bool, why: str):
        if cond:
            blockers.append(why)

    block_if(not goals, 'Product goals are missing: require observed or owner-confirmed outcomes')
    block_if(not people, 'No target audience: need at least one confirmed actor/persona')
    block_if(not workflows, 'No top tasks: require at least one evidenced end-to-end user journey')
    block_if(discovery['product_type'] == 'unknown', 'Product type is unknown: design school cannot be committed')
    block_if(device['primary'] == 'unknown', 'Primary device usage context is unknown')
    block_if(localization['primary_locale'] not in localization['languages'],
             'Primary locale is not part of declared supported languages')
    block_if(discovery['criticality'] == 'unknown', 'Project criticality is unknown: cannot determine required UX safeguards')

    identifiers = [p['id'] for p in people]
    block_if(len(identifiers) != len(set(identifiers)), 'Duplicate audience identifiers')
    tasks = [flow['id'] for flow in workflows]
    block_if(len(tasks) != len(set(tasks)), 'Duplicate workflow identifiers')
    audiences = set(identifiers)
    supported = set(device['supported'])
    block_if(device['primary'] not in {'mixed', 'unknown'} and device['primary'] not in supported,
             'Primary device not included in supported device contexts')
    for flow in workflows:
        block_if(flow['actor_id'] not in audiences, 'Unknown workflow actor: ' + flow['id'])
        block_if(not flow['devices'], 'Workflow has no supported device: ' + flow['id'])
        block_if(bool(set(flow['devices']) - supported), 'Workflow device not declared: ' + flow['id'])
        block_if(flow['interaction'] == 'unknown', 'Workflow interaction is unknown: ' + flow['id'])
        block_if(flow['risk'] == 'unknown', 'Workflow risk is unknown: ' + flow['id'])
    if discovery['product_type'] == 'kiosk':
        block_if('kiosk' not in supported, 'Kiosk journey requires a kiosk device target')

    for lang in localization['languages']:
        block_if(locale_direction(lang) is None, 'Unknown locale script direction: ' + lang)
    block_if(not discovery.get('goal_priorities'), 'Product goal priorities need explicit owner classification')
    for goal in discovery.get('goal_priorities', []):
        block_if(goal['goal_index'] >= len(goals), 'Goal priority references a missing product goal')
    have_rtl = any(is_rtl(lang) for lang in localization['languages'])
    have_ltr = any(not is_rtl(lang) for lang in localization['languages'])
    must_support_both = have_rtl and have_ltr
    block_if(must_support_both and localization['requires_bidirectional_ui'] is not True,
             'Arabic and LTR locales require confirmed dual-direction UI behavior')
    block_if(localization['requires_bidirectional_ui'] is None,
             'Bidirectional behavior must be confirmed, never silently assumed')
    block_if(localization['numeric_policy'] == 'unknown',
             'Locale/numbering policy is unresolved; identifiers and currency presentation need explicit review')

    high_stakes = discovery['criticality'] in {'high', 'critical'} or any(
        flow['risk'] in {'high', 'critical'} for flow in workflows
    )
    if high_stakes and discovery['human_confirmation'] != 'confirmed':
        blockers.append('High-impact journeys require trusted owner confirmation before implementation')
    if high_stakes and unknowns:
        blockers.append('High-impact unresolved facts: ' + ', '.join(unknowns))
    elif unknowns:
        blockers.append('Unresolved UX discovery facts: ' + ', '.join(unknowns))

    rule('UX-SCHOOL-001', 'unknown' if primary_school == 'undetermined' else 'selected',
         school_data['reason'], [discovery['product_type']] + goals[:3])

    if any(flow['data_density'] == 'high' or flow['record_volume'] == 'large' for flow in workflows):
        density = 'adaptive'
        rule('UX-DENSITY-001', 'selected',
             'Dense data requires detailed desktop views plus reachable mobile details, not universal compactness',
             ['high_density_or_large_volume=true'])
    else:
        rule('UX-DENSITY-001', 'rejected',
             'No high-density workflow fact; keep density calibrated to product context', ['high_density_or_large_volume=false'])

    existing = discovery['existing_design_system']
    design_system_policy = 'preserve_existing' if existing else 'propose_new'
    rule('UX-SYSTEM-001', 'selected',
         'Keep existing design tokens/components and require a separate approved migration if replacement is justified'
         if existing else 'Propose a project-specific token system; do not impose a universal brand template',
         [f'existing_design_system={existing or "none"}'])

    choices = []
    for flow in workflows:
        spec = catalog['workflow_patterns'][flow['interaction']]
        desktop = spec['desktop']
        mobile = spec['mobile']
        tablet = spec['tablet']
        pattern = spec['pattern']
        reasons = [f'User goal: {flow["user_goal"]}', f'Interaction: {flow["interaction"]}']
        tests = ['Perform primary flow on declared devices with keyboard and touch when applicable']
        if flow['interaction'] == 'browse' and (flow['data_density'] == 'high' or flow['record_volume'] == 'large'):
            desktop = 'dense_filterable_data_workbench'
            tablet = 'two_pane_task_view'
            mobile = 'priority_summary_plus_accessible_details'
            pattern = 'high_density_task_workbench'
            reasons.append('Full detail must remain reachable on mobile; server-side operations may be required')
            tests.append('Prove all mandatory desktop fields have accessible mobile paths; no hover-only access')
        if flow['interaction'] == 'form' and flow['recovery_required'] is True:
            reasons.append('Keep checks and validation inside the current process; recover unfinished drafts where applicable')
            tests.append('Test navigation away/error/retry without loss of eligible draft information')
        if flow['risk'] in {'high', 'critical'}:
            reasons.append('Risk-sensitive action requires proportional confirmation, authorization and recovery')
            tests.append('Negative authorization and duplicate/irreversible action tests')
        if flow['interaction'] == 'approval':
            tests.append('Verify action labels, status transitions and accessible approval details')
        choices.append({
            'workflow_id': flow['id'], 'pattern': pattern, 'desktop': desktop if 'desktop' in flow['devices'] else 'not_applicable', 'mobile': mobile if 'mobile' in flow['devices'] else 'not_applicable',
            'tablet': tablet if 'tablet' in flow['devices'] else 'not_applicable',
            'kiosk': 'touch_guided_flow' if 'kiosk' in flow['devices'] else 'not_applicable',
            'wide': desktop + '_with_context_panel' if 'desktop' in flow['devices'] and device['ultrawide_use_case'] else 'not_applicable',
            'supported_devices': list(flow['devices']), 'important_data': list(flow['important_data']), 'reason': '; '.join(reasons), 'evidence_refs': source_refs,
            'verification_needed': tests})
        rule('UX-WORKFLOW-001', 'unknown' if flow['interaction'] == 'unknown' else 'selected',
             f'Workflow {flow["id"]} pattern chosen according to device, density, risk and task goals',
             [flow['id'], f'frequency={flow["frequency"]}', f'risk={flow["risk"]}',
              f'data_density={flow["data_density"]}', f'interaction={flow["interaction"]}'])

    direction = 'per_locale' if must_support_both else ('rtl' if have_rtl else 'ltr')
    rule('UX-BIDI-001', 'selected',
         'Use document dir/lang and semantic per-component orientation, mixed-text isolation and locale policies',
         [f'direction={direction}', f'numeric={localization["numeric_policy"]}'])
    font_policy = 'retain_existing_pending_review' if existing else 'prefer_self_hosting_after_review'
    rule('UX-FONTS-001', 'selected',
         'Local WOFF2 font delivery is conditional on verified license, font coverage and performance budget',
         ['preload_only_measured_critical_font', 'not_all_variable_fonts_are_smaller'])
    if high_stakes:
        rule('UX-RISK-001', 'selected',
             'Sensitive journeys need human approval and threat-relevant UI tests before implementation',
             ['high_impact=true'])
    elif discovery['criticality'] != 'unknown':
        rule('UX-RISK-001', 'rejected', 'No declared high-impact UI flows; baseline security/accessibility still applies',
             ['high_impact=false'])

    decision = {
        'contract_version':'1.2.0',
        'decision_id':'UXDR-'+digest({'input': discovery, 'policy': catalog})[:20],
        'project_id':discovery['project_id'],
        'discovery_sha256':digest(discovery),
        'catalog_sha256':hashlib.sha256(CATALOG_PATH.read_bytes()).hexdigest(),
        'rule_version':catalog['rule_version'],
        'state':'blocked' if blockers else 'proposed',
        'primary_school':primary_school,
        'ranking':ranking,
        'density':density,
        'navigation':navigation,
        'design_system_policy':design_system_policy,
        'workflow_choices':choices,
        'direction_strategy':{
            'document_direction':direction,'logical_properties_required':True,
            'icon_mirroring':'semantic_per_icon_not_global','mixed_text_isolation':'bdi_or_dir_auto_contextual',
            'numeric_policy':localization['numeric_policy'],
            'test_locales':localization['languages']},
        'font_strategy':{
            'delivery':font_policy,'preferred_format':'woff2_when_supported',
            'variable_font':'benchmark_before_choosing',
            'font_display':'test_swap_optional_tradeoff',
            'preload':'only_critical_verified_font',
            'license_review_required':True,'real_font_assets_included':False},
        'quality_gates':[{'id':gate,'description':gate.replace('_',' ').capitalize(),
            'status':'not_run','manual_evidence_required':gate in {
                'task_completions','rtl_ltr_bidi','wcag22_aa_manual_automated',
                'keyboard_touch_screenreader','responsive_zoom'}}
            for gate in catalog['verification_required']],
        'reasoning_trace':trace,
        'alternatives':[{'id':x['school'],'rejected_because':
                'A lower reviewed goal/task/audience score than the primary school; inspect ranking for contributions.'}
            for k,x in catalog['design_schools'].items() if x['school'] != primary_school and k != 'unknown'],
        'blockers':blockers,
        'human_approval':{'required':high_stakes,
                          'status':'pending' if high_stakes else 'not_required',
                          'approval_ref':None},
        'limitations':[
            'Proposal from the integrated pure UX engine. Source verification and legacy routing belong to the coordinator.',
            'Schema validation is not UI, accessibility, performance or security verification.',
            'All quality gates require real evidence and cannot report PASS from these inferred choices.',
            'No real font binaries, icon assets, or production components are delivered by this advisor.',
        ]
    }
    validate(DECISION_SCHEMA, decision)
    return decision


