<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-002-authentication-baseline.md -->
# VCGF-IAM-002 — Authentication Baseline
MUST · identity-access · profiles: baseline, high-assurance, production · full text: controls/identity-access/vcgf-iam-002-authentication-baseline.md

## Requirement
Authentication MUST use trusted mechanisms, secure transport, explicit session handling, and server-side identity verification.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
