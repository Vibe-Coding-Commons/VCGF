<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/data-protection/vcgf-data-002-data-classification-and-retention.md -->
# VCGF-DATA-002 — Data Classification and Retention
MUST · data-protection · profiles: high-assurance, production · full text: controls/data-protection/vcgf-data-002-data-classification-and-retention.md

## Requirement
Projects MUST classify data and define retention and deletion requirements proportionate to sensitivity and business need.

## Guidance
Every persistent field should have:
- category
- classification
- purpose
- source
- owner
- retention
- deletion behavior
- backup behavior
- encryption requirement
- logging rule
- export rule

## Retention
Do not retain sensitive data indefinitely by default.

## Deletion scope
Consider:
- primary DB
- replicas
- search indexes
- object storage
- caches
- exports
- logs
- backups

If backups cannot delete individual records immediately, document how deleted data is prevented from being restored into active use.

## Test data
Do not copy production PII casually into development or demos. Prefer synthetic/de-identified data.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
