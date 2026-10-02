---
id: VCGF-REL-002
title: Pre-Release Security Gate
domain: release
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

# VCGF-REL-002 - Pre-Release Security Gate

**Control ID:** VCGF-REL-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Production release MUST be blocked when unresolved critical security, authorization, secret exposure, destructive migration, or required evidence failures remain.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for pre-release security gate.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Pre-Release Security Gate

Production release is blocked by unresolved Critical findings.

High findings require remediation or an explicitly approved, time-bounded exception.

## Identity
- login controls reviewed
- password/recovery reviewed
- MFA for privileged access
- session invalidation works

## Authorization
- object authorization
- tenant isolation
- RLS/grants
- admin audit

## Validation/Injection
- server validation
- parameterized queries
- unsafe HTML reviewed
- SSRF endpoints reviewed
- file validation

## Data protection
- classification
- encryption decisions
- keys protected
- logs redacted
- exports private
- backups protected

## API
- endpoint auth/authz
- rate limits
- safe errors
- webhooks
- request limits/timeouts

## Supply chain
- secret scan
- dependency review
- no client-exposed privileged keys

## Testing
- critical paths
- negative auth tests
- regression tests
- platform security scan reviewed where available

## Release
- migration plan
- rollback/forward-fix plan
- monitoring
- incident owner

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
