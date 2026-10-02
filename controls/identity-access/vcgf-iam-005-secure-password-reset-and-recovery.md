---
id: VCGF-IAM-005
title: Secure Password Reset and Recovery
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

# VCGF-IAM-005 - Secure Password Reset and Recovery

**Control ID:** VCGF-IAM-005  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Password reset and account recovery MUST use non-enumerating responses, high-entropy single-use expiring tokens, abuse controls, trusted origins, and post-reset session security.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for secure password reset and recovery.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Secure Password Reset and Account Recovery Policy

Password recovery is a high-risk authentication path.

## Reset request
When an email/username is submitted:
- return a consistent message for existing/non-existing accounts
- minimize timing differences
- rate-limit by target and source characteristics
- apply anti-automation controls when needed
- do not lock an account merely because resets were requested

## Reset token
Use an opaque CSPRNG-generated token.

Framework default:
- at least 128 bits unpredictable entropy
- short expiry appropriate to risk, commonly 15–30 minutes
- single use
- bound to one user and recovery purpose
- invalidated after use and according to superseding-request policy

Store high-entropy reset tokens securely; prefer a one-way hash/HMAC representation rather than plaintext when practical.

Never log the full token or URL.

## Reset URL
- HTTPS
- configured trusted origin
- do not blindly use untrusted Host header
- allowlist redirect targets
- Referrer-Policy appropriate to preventing token leakage
- avoid third-party scripts/analytics on token-bearing reset pages where possible

## Password replacement
- user enters new password twice in interactive UI
- normal password policy applies
- use provider/approved password hashing
- never email the password
- do not automatically log the user in solely because reset succeeded

## Session handling
For enterprise/sensitive systems, default to invalidating existing sessions after successful reset unless a documented risk-based exception exists.

Invalidate outstanding reset/recovery tokens after completion.

## Notification
Send a security notification after password reset/change, without including passwords or secrets.

## Recovery factor changes
Changing recovery email/phone requires strong authentication and should notify existing trusted channels.

Consider a delay/cooldown for high-risk changes.

## MFA recovery
Password reset must not automatically disable MFA.

MFA recovery needs a separate high-assurance flow using backup codes, existing factors, verified support, or equivalent controls.

## Security questions
Never use security questions as the sole reset mechanism.

## Suspected compromise
Review active sessions, recovery channels, MFA methods, API tokens, trusted devices, and recent security events; invalidate compromised authenticators.

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
