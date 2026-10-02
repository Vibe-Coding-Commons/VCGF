---
id: VCGF-IAM-003
title: MFA and Session Security
domain: identity-access
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

# VCGF-IAM-003 - MFA and Session Security

**Control ID:** VCGF-IAM-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Privileged or high-risk access SHOULD use MFA, and sessions MUST be protected, revocable, rotated when appropriate, and invalidated on security-sensitive events.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for mfa and session security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# MFA and Session Security

## MFA
Require or strongly enforce MFA for:
- administrators
- privileged operators
- finance/payment roles
- users with Restricted-data access where risk warrants

Prefer phishing-resistant methods where practical.

OTP/TOTP/recovery codes must be securely generated and protected. Recovery codes should be single-use.

## Session cookies
Prefer:
- Secure
- HttpOnly
- appropriate SameSite
- narrow domain/path
- risk-appropriate lifetime

## Session lifecycle
Define:
- idle timeout
- absolute timeout
- remember-me behavior
- privileged-session timeout

Regenerate/rotate session identifiers after authentication or privilege elevation where framework/provider guidance requires it.

## Invalidation
Support logout, logout-all, password-reset revocation, admin security revocation, and refresh-token revocation where supported.

## Sensitive actions
Use recent authentication/step-up auth for critical account/admin changes.

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
