---
id: VCGF-API-003
title: Rate Limiting and Abuse Prevention
domain: api
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

# VCGF-API-003 - Rate Limiting and Abuse Prevention

**Control ID:** VCGF-API-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Abuse-sensitive and resource-intensive endpoints MUST apply proportionate rate, quota, size, and concurrency protections.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for rate limiting and abuse prevention.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Rate Limiting and Abuse Prevention

Candidate endpoints:
- login
- password reset
- signup
- OTP/MFA
- search
- AI generation
- upload
- export
- webhooks
- email/SMS
- invitations
- expensive reports
- payments
- public APIs

Define:
- subject/key
- window
- burst limit
- sustained limit
- response behavior
- internal exceptions
- monitoring

Distributed apps need shared enforcement state.

Additional controls may include CAPTCHA/challenges, quotas, per-tenant limits, idempotency keys, queues, circuit breakers, and cost ceilings.

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
