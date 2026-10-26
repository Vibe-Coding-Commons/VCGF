<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-005-secure-password-reset-and-recovery.md -->
# VCGF-IAM-005 — Secure Password Reset and Recovery
MUST · identity-access · profiles: baseline, high-assurance, production · full text: controls/identity-access/vcgf-iam-005-secure-password-reset-and-recovery.md

## Requirement
Password reset and account recovery MUST use non-enumerating responses, high-entropy single-use expiring tokens, abuse controls, trusted origins, and post-reset session security.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
