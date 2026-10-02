---
id: VCGF-TEST-001
title: Authorization Negative Testing
domain: testing
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
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

# VCGF-TEST-001 - Authorization Negative Testing

**Control ID:** VCGF-TEST-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Protected features MUST test both allowed and denied access, including object-level and tenant-level negative cases where applicable.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for authorization negative testing.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Authorization Negative Test Matrix

| Actor | Read | Create | Update | Delete | Special action |
|---|---|---|---|---|---|
| Anonymous | Deny unless public | Deny unless designed | Deny | Deny | Deny |
| User A owner | Expected policy | Expected | Expected | Expected | Expected |
| User B non-owner | Deny private | Controlled | Deny | Deny | Deny |
| Tenant A | Tenant A only | Tenant A only | Tenant A only | Tenant A only | Scoped |
| Tenant B against A | Deny | Deny | Deny | Deny | Deny |
| Privileged | Explicit | Explicit | Explicit | Explicit | Audited |

Also test:
- modified `user_id`
- modified `tenant_id`
- direct API calls
- guessed IDs
- bulk endpoints
- exports
- storage URLs
- privileged server functions

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
