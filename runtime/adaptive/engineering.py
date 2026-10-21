# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Deterministic engineering advisor for the opt-in integration candidate.

Receives explicit facts; local byte verification belongs to the coordinator.
It does not install packages, mutate application code or approve implementation.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FINGERPRINT_SCHEMA = ROOT / 'schemas/v1.2.0/project-fingerprint.schema.json'
DECISION_SCHEMA = ROOT / 'schemas/v1.2.0/architecture-decision.schema.json'
CATALOG = ROOT / 'packs/engineering/catalog.yaml'


from .common import canonical_sha, sha_bytes, validate, load_catalog


def advise(fingerprint: dict, *, decided_at: str | None = None) -> dict:
    """Return a reproducible suggestion. No application implementation or approval occurs."""
    decided_at = decided_at or datetime.now(timezone.utc).isoformat()
    validate(FINGERPRINT_SCHEMA, fingerprint)
    catalog = load_catalog(CATALOG)
    if catalog['status'] != 'integration-candidate':
        raise ValueError('Advisor requires an explicitly identified integration-candidate catalog')

    fp_hash = canonical_sha(fingerprint)
    risks = set(fingerprint['risk_flags']) - {'none'}
    facts = fingerprint['architecture_facts']
    complexity = fingerprint['complexity']
    backend = fingerprint['backend']
    frontend = fingerprint['frontend']
    unknowns = list(fingerprint['unknown_facts'])
    source_refs = [source['path'] for source in fingerprint['sources']]
    blockers = []
    if backend == 'unknown':
        blockers.append('Backend is unknown: cannot load a technology-specific backend pack.')
    if frontend == 'unknown':
        blockers.append('Frontend is unknown: cannot load a technology-specific frontend pack.')
    if any(v is None for v in [complexity['business_rules'], complexity['bounded_contexts']]):
        blockers.append('Business/domain complexity is unknown: final architecture selection requires review.')
    if 'none' in fingerprint['risk_flags'] and len(fingerprint['risk_flags']) > 1:
        blockers.append('Contradictory risk declaration: none cannot coexist with a risk flag.')
    if len(source_refs) != len(set(source_refs)):
        blockers.append('Duplicate fingerprint sources require reconciliation.')
    if backend == 'laravel':
        for key in ['multiple_persistence_sources', 'multiple_service_providers',
                    'highly_reused_operations', 'complex_workflow', 'retriable_financial_operations']:
            if facts[key] is None:
                blockers.append('Unresolved architecture fact: ' + key)
    high_risk = bool(risks.intersection({'payment','health','pii','regulated','multi_tenant','production'}))
    if high_risk and fingerprint['human_confirmation'] != 'confirmed':
        blockers.append('High-impact project facts require trusted human confirmation before implementation.')
    if high_risk and unknowns:
        blockers.append('High-impact unresolved facts: ' + ', '.join(unknowns))

    independent = facts['independent_domains']
    domain_score = complexity['bounded_contexts']
    business_score = complexity['business_rules']
    if independent is None and domain_score is not None and domain_score >= 2:
        blockers.append('Independence of bounded contexts needs verification.')
    if domain_score is None or business_score is None:
        architecture = 'unknown'
    elif independent is True and domain_score >= 2 and business_score >= 2:
        architecture = 'selective_ddd' if (business_score >= 3 and domain_score >= 3) else 'modular_monolith'
    elif independent is True and domain_score >= 2:
        architecture = 'modular_monolith'
    else:
        architecture = 'lean_layers'

    choices: list[dict] = []

    def record(cid: str, category: str, selected: bool, reason: str, *, constraints: list[str] | None = None, tests: list[str] | None = None):
        choices.append({
            'id': cid,
            'category': category,
            'selected': selected,
            'reason': reason,
            'evidence_refs': source_refs,
            'constraints': constraints or ['Proposal only: never modify architecture or install packages automatically.'],
            'verification_needed': tests or ['Review recommendation against existing application and runtime constraints.'],
        })

    record('lean_layers', 'architecture', architecture == 'lean_layers', 'Choose minimal Laravel/general framework layering when domain boundaries do not justify extra abstractions.')
    record('modular_monolith', 'architecture', architecture == 'modular_monolith', 'Use bounded modules and stable contracts where independent domains justify stronger separation.')
    record('selective_ddd', 'architecture', architecture == 'selective_ddd', 'Use DDD selectively for highly complex independent domains; database table count is not a selection criterion.')
    record('cqrs', 'pattern', False, 'Insufficient read/write divergence or performance measurement; CQRS requires explicit operational evidence.')

    if backend == 'laravel':
        record('dependency-injection', 'pattern', True, 'Use Laravel Service Container for collaborating services; local value object construction remains allowed.')
        record('action-classes', 'pattern', facts['highly_reused_operations'] is True or facts['complex_workflow'] is True,
               'Extract meaningful repeated operations and business transactions into Actions only when justified.')
        record('repository', 'pattern', facts['multiple_persistence_sources'] is True,
               'Repository is warranted only if meaningful persistence boundaries or multiple sources are confirmed; do not wrap Eloquent CRUD 1:1.')
        record('strategy-and-factory', 'pattern', facts['multiple_service_providers'] is True,
               'Use provider interface/Strategy/Factory for actual interchangeable integrations; not for a single hard-coded service.')
        dto_needed = facts['complex_workflow'] is True or (complexity['ui_interaction'] is not None and complexity['ui_interaction'] >= 2)
        record('data-transfer-object', 'pattern', dto_needed,
               'Typed DTOs help with complex transfers, but authorization, validation, output encoding and SQL safety remain separate obligations.')
        record('spatie/laravel-data', 'package', dto_needed,
               'Consider spatie/laravel-data only with verified current Laravel/PHP compatibility and explicit request validation strategy.',
               tests=['Review composer constraint/license/advisory and validate request and non-request creation paths.'])
        record('spatie/laravel-query-builder', 'package', bool(complexity['ui_interaction'] is not None and complexity['ui_interaction'] >= 2),
               'Consider allowlisted filtering, sorting and includes for advanced server-side data tables.',
               tests=['Verify allowedFilters/sorts/includes and server-side authorization of every returned row.'])
        if facts['complex_workflow'] is True:
            record('state-machine', 'pattern', True, 'Multistep workflow requires explicitly tested state transitions and permission invariants.')
        if 'payment' in risks or facts['retriable_financial_operations'] is True:
            record('idempotency', 'pattern', True, 'Payment and retried commands need idempotency/transaction safeguards against double processing.',
                   tests=['Prove duplicate webhook/payment retries cannot execute the same financial mutation twice.'])

    library = (facts['existing_component_library'] or '').lower()
    ui_score = complexity['ui_interaction']
    if frontend == 'react':
        if 'radix' in library:
            record('shadcn-ui-radix', 'ui_library', True, 'Preserve the existing Radix-based component foundation; upgrading is a separate ADR.')
            record('shadcn-ui-base-ui', 'ui_library', False, 'A candidate alternative is not a justification for migrating this React project automatically.')
        elif library:
            record('retain-existing-react-ui', 'ui_library', True, 'An existing component system is present; avoid an unrequested wholesale migration.')
        else:
            record('shadcn-ui-base-ui', 'ui_library', True, 'A headless React candidate, not a universal default; compare Base UI and Radix against verified versions and project constraints.')
            record('shadcn-ui-radix', 'ui_library', False, 'Radix remains a supported alternative; review if project constraints favor its APIs.')
        if ui_score is not None and ui_score >= 2:
            record('tanstack-react-table', 'ui_library', True, 'Highly tailored enterprise tables can use a headless engine combined with an accessible rendering layer.')
    elif frontend == 'vue':
        if 'primevue' in library:
            record('primevue', 'ui_library', True, 'Retain the already adopted Vue suite unless there is a documented issue or migration approval.')
            record('reka-ui', 'ui_library', False, 'Reka UI is a headless alternative, not an automatic replacement for an existing PrimeVue design system.')
        elif library:
            record('retain-existing-vue-ui', 'ui_library', True, 'Avoid unrequested migration away from an existing Vue component system.')
        elif ui_score is not None and ui_score >= 2:
            record('primevue', 'ui_library', True, 'Ready-made, feature-rich tables and inputs can reduce delivery effort on complex enterprise interfaces.')
            record('tanstack-vue-table', 'ui_library', False, 'Headless Vue table is an alternative when full markup and styling ownership outweigh out-of-box speed.')
        else:
            record('reka-ui', 'ui_library', True, 'Consider current Reka UI headless primitives for a lightweight custom Vue interface.')
            record('primevue', 'ui_library', False, 'Feature-rich PrimeVue suite is unnecessary unless the product requires those components.')

    approval_required = bool(high_risk or architecture in {'selective_ddd','modular_monolith'})
    decision = {
        'contract_version': '1.2.0',
        'decision_id': 'ADR-' + canonical_sha({'input': fingerprint, 'policy': catalog})[:20],
        'project_id': fingerprint['project_id'],
        'fingerprint_sha256': fp_hash,
        'catalog_sha256': sha_bytes(CATALOG.read_bytes()),
        'decided_at': decided_at,
        'state': 'blocked' if blockers else 'proposed',
        'architecture': architecture,
        'choices': choices,
        'blockers': blockers,
        'approval': {'required': approval_required, 'status': 'pending' if approval_required else 'not_required', 'approval_ref': None},
        'evidence_status': 'not_run',
        'limitations': ['Deterministic advisory; source-byte verification is performed by the coordinator, not this pure function.',
                        'No framework package compatibility, security, accessibility or platform enforcement has been independently verified.',
                        'A selected option is a candidate recommendation, not an installed implementation.'],
    }
    validate(DECISION_SCHEMA, decision)
    return decision


