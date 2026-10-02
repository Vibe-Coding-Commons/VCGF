---
id: VCGF-TEST-002
title: Secure Code Review
domain: testing
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

# VCGF-TEST-002 - Secure Code Review

**Control ID:** VCGF-TEST-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Security-relevant changes MUST receive structured review of trust boundaries, validation, authorization, secrets, data handling, dependencies, errors, and tests.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for secure code review.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Secure Code Review Checklist

Ask:
- Is every untrusted input validated on a trusted layer?
- Are queries parameterized?
- Are dynamic identifiers allowlisted?
- Is authorization checked on the exact object/action?
- Can user/tenant IDs be manipulated?
- Are privileged clients necessary?
- Are secrets exposed?
- Is sensitive data logged?
- Is output safely encoded?
- Are unsafe HTML sinks present?
- Can server URL fetches reach internal networks?
- Are files treated as untrusted?
- Is rate limiting needed?
- Are state transitions validated?
- Are money/discounts recalculated server-side?
- Is cryptography standard with managed keys?
- Is password recovery safe?
- Are negative tests included?

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
