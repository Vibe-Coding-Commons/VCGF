<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-002-database-integrity.md -->
# VCGF-DB-002 — Database Integrity
MUST · database · profiles: baseline, high-assurance, production · full text: controls/database/vcgf-db-002-database-integrity.md

## Requirement
Important data invariants MUST be protected with suitable database constraints, relationships, transactional boundaries, and consistency controls.

## Guidance
Use DB controls where appropriate:
- primary keys
- foreign keys
- unique constraints
- NOT NULL
- CHECK
- sane defaults
- transactions
- indexes

Use decimal/numeric types for money.

Enforce tenant relationship integrity when strict isolation is required.

If soft delete is used, define uniqueness, authorization, retention, restore, and reporting behavior.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
