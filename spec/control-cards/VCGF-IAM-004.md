<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-004-password-storage-and-policy.md -->
# VCGF-IAM-004 — Password Storage and Policy
MUST · identity-access · profiles: baseline, high-assurance, production · full text: controls/identity-access/vcgf-iam-004-password-storage-and-policy.md

## Requirement
Passwords MUST NOT be stored in plaintext or reversible encryption; trusted password hashing or a managed identity provider MUST be used.

## Guidance
## Storage
Passwords must never be stored in plaintext or reversible encryption.

Use:
- trusted authentication provider; or
- Argon2id where available
- scrypt if Argon2id unavailable
- bcrypt for suitable legacy cases
- PBKDF2-HMAC-SHA-256 where validated/FIPS requirements apply

Review cost parameters periodically.

## Length
Framework default:
- minimum 15 characters preferred for password-only authentication
- never silently truncate
- support long passphrases
- use a high enough maximum to allow password managers while protecting resources

Where platform policy differs, document the decision.

## Composition
Do not rely on arbitrary composition rules as the primary defense.

Allow password-manager paste and broad safe character sets.

## Common/breached values
Block common/breached passwords using a privacy-conscious mechanism.

## Rotation
Do not force periodic password changes without compromise/policy reason.

## Logging
Never log password values.

## Pepper
If used, keep the pepper outside the password database in a secure secret/key system and plan compromise handling.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
