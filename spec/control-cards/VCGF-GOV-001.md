<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/governance/vcgf-gov-001-change-impact-analysis.md -->
# VCGF-GOV-001 — Change Impact Analysis
MUST · governance · profiles: baseline, high-assurance, production · full text: controls/governance/vcgf-gov-001-change-impact-analysis.md

## Requirement
Non-trivial changes MUST identify affected code, data, permissions, integrations, tests, and rollback concerns before implementation.

## Guidance
Before non-trivial changes inspect impact on:
- UI/routing
- authentication
- authorization
- database schema
- RLS/grants
- APIs/functions
- storage
- encryption
- logs
- integrations
- jobs/queues
- exports/reports
- clients
- compatibility
- tests

Treat auth, session, recovery, role, RLS, privileged key, encryption, tenant, payment, approval, destructive migration, and file-privacy changes as high risk.

High-risk changes require an explicit plan, tests, and rollback/forward-fix strategy.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
