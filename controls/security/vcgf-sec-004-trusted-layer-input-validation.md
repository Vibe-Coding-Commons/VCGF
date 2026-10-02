---
id: VCGF-SEC-004
title: Trusted-Layer Input Validation
domain: security
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
- baseline
- production
---

<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF-SEC-004 - Trusted-Layer Input Validation

**Control ID:** VCGF-SEC-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

All data crossing a trust boundary MUST be parsed and validated on a trusted layer before it affects authorization, business logic, persistence, interpreters, or outbound requests.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for trusted-layer input validation.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Input Validation Policy

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

## Verification Method

Inspect implementation and configuration, execute positive and negative tests appropriate to the control, and review evidence at the trusted enforcement layer.

## Required Evidence

At least one reproducible artifact such as a test result, code review, configuration record, security scan, migration review, or manual verification record.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, and applicable architecture or identity controls.

## Related Controls

See the domain index and selected profile.

## References

- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Change History

- 1.0.0: Initial VCGF control migrated and normalized from the previous framework.
