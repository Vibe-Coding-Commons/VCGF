---
id: VCGF-GOV-003
title: Security Exception Management
domain: governance
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

# VCGF-GOV-003 - Security Exception Management

**Control ID:** VCGF-GOV-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Any exception to a normative security control MUST be explicit, risk-owned, approved, time-bounded, and tracked with compensating controls.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for security exception management.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Security Exception Process

Security controls must not be silently bypassed.

If a control cannot be implemented:
1. describe the control
2. explain the blocker
3. identify affected users/data
4. rate the risk
5. define compensating controls
6. assign an owner
7. define expiry/review date
8. obtain explicit authorized approval
9. track remediation

Exceptions are time-bounded.

"AI could not make it work" is not an acceptable security justification.

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
