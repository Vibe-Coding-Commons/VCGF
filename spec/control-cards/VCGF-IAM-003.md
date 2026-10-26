<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-003-mfa-and-session-security.md -->
# VCGF-IAM-003 — MFA and Session Security
MUST · identity-access · profiles: high-assurance, production · full text: controls/identity-access/vcgf-iam-003-mfa-and-session-security.md

## Requirement
Privileged or high-risk access SHOULD use MFA, and sessions MUST be protected, revocable, rotated when appropriate, and invalidated on security-sensitive events.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
