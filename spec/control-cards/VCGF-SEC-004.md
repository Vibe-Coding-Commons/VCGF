<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-004-trusted-layer-input-validation.md -->
# VCGF-SEC-004 — Trusted-Layer Input Validation
MUST · security · profiles: baseline, high-assurance, production · full text: controls/security/vcgf-sec-004-trusted-layer-input-validation.md

## Requirement
All data crossing a trust boundary MUST be parsed and validated on a trusted layer before it affects authorization, business logic, persistence, interpreters, or outbound requests.

## Guidance
Every value crossing a trust boundary must be validated on a trusted layer before it influences business logic, queries, authorization, files, or external requests.

Frontend validation improves UX but is never the authoritative security check.

## Validation sequence
1. identify source/trust level
2. parse with a strict type-aware parser
3. canonicalize only where business-safe
4. validate type
5. validate length
6. validate range
7. validate format
8. validate allowed values
9. validate cross-field/business rules
10. authorize the operation
11. encode/sanitize at output/interpreter boundary

## Allowlists
Prefer known allowed values over blacklists.

## Unicode
Use documented normalization where appropriate. Do not casually normalize passwords, crypto tokens, signatures, or opaque IDs.

## Length
Define maximum length for every external string before logging, expensive parsing, persistence, or downstream calls.

## Numbers
Parse explicitly. Use fixed-point/decimal for money and enforce business bounds server-side.

## Dates
Use strict formats, explicit timezone behavior, and reasonable ranges.

## IDs
Validate syntax but never treat a valid ID as authorization.

## Unknown fields
For security-sensitive APIs, reject unexpected fields where practical to reduce mass assignment.

## Failure
Fail closed and return safe errors without stack traces, SQL, secrets, or internal paths.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
