<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-001-database-change-governance.md -->
# VCGF-DB-001 — Database Change Governance
MUST · database · profiles: baseline, high-assurance, production · full text: controls/database/vcgf-db-001-database-change-governance.md

## Requirement
Schema and data migrations MUST be inspected for compatibility, integrity, authorization, rollback, data-loss, locking, and operational risk before execution.

## Guidance
Database changes are high impact.

Before migration inspect:
- schema
- constraints
- relationships
- indexes
- RLS
- grants
- views
- functions/triggers
- application references
- reports/exports

Prefer additive, backward-compatible, reversible/staged changes.

Prohibited without explicit approval:
- DROP/TRUNCATE
- destructive rename
- broad policy removal
- making private data public
- permanently disabling integrity constraints

Backfill safely before enforcing new NOT NULL/constraints.

Document rollback or forward-fix plan before release.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
