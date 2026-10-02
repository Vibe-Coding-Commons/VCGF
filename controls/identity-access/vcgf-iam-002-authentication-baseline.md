---
id: VCGF-IAM-002
title: Authentication Baseline
domain: identity-access
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

# VCGF-IAM-002 - Authentication Baseline

**Control ID:** VCGF-IAM-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Authentication MUST use trusted mechanisms, secure transport, explicit session handling, and server-side identity verification.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for authentication baseline.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Authentication Policy

Prefer mature authentication providers/frameworks over custom password/session cryptography.

## Login protections
Apply:
- TLS
- rate limiting
- anti-automation controls where risk warrants
- generic failure responses
- common/breached password checks for password auth
- MFA for privileged/high-risk users
- secure session issuance

## Re-authentication
Require recent authentication or step-up assurance for sensitive actions such as:
- password change
- MFA change
- recovery email/phone change
- export of highly sensitive data
- destructive admin actions
- issuing privileged credentials

## Account enumeration
Do not reveal account existence through login, reset, recovery, or invitation checks where it can be avoided.

## Authentication vs authorization
Successful login never implies unrestricted resource access.

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
