<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/privacy/vcgf-priv-002-personal-data-protection.md -->
# VCGF-PRIV-002 — Personal Data Protection
MUST · privacy · profiles: high-assurance, production · full text: controls/privacy/vcgf-priv-002-personal-data-protection.md

## Requirement
Personal data MUST be minimized, purpose-limited, access-controlled, protected in transit and at rest, and handled according to classification and retention requirements.

## Guidance
## Objective
Protect personal data through minimization, access control, encryption, redaction, retention, and auditing.

## Data minimization
For each personal field document:
- purpose
- business/legal need
- owner
- retention
- who can access
- whether it must be searchable
- whether it must be exportable
- protection/encryption level

## Classification
Use at least:
- Public
- Internal
- Confidential
- Restricted

Restricted may include government IDs, passport identifiers, bank details, authentication/recovery secrets, highly sensitive HR/health records, and private cryptographic material.

## Defense in depth
1. collect less
2. least privilege
3. tenant/user isolation
4. field-level authorization
5. TLS
6. storage encryption
7. field-level authenticated encryption when needed
8. masked UI
9. redacted logs
10. export controls
11. retention/deletion
12. access audit

## Encryption is not authorization
Decryption only occurs after authorization. Field encryption does not replace RBAC/RLS.

## URLs
Avoid sensitive personal data in query strings, path parameters, analytics, and referrer-sensitive locations.

## Logs
Never log passwords, full tokens, encryption keys, session cookies, or full Restricted IDs.

## Exports
Sensitive exports require authorization, scope, audit event, private delivery, and expiration/deletion where appropriate.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
