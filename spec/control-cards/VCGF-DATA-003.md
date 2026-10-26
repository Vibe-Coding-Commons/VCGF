<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/data-protection/vcgf-data-003-field-level-encryption.md -->
# VCGF-DATA-003 — Field-Level Encryption
MUST · data-protection · profiles: high-assurance, production · full text: controls/data-protection/vcgf-data-003-field-level-encryption.md

## Requirement
Restricted recoverable data MUST use authenticated field-level encryption when the threat model requires protection beyond storage-layer encryption.

## Guidance
## When to use
Use application-level or controlled database field encryption when the threat model requires protection beyond disk/database-at-rest encryption.

Do not encrypt every column blindly; encryption affects search, indexes, uniqueness, analytics, migrations, and rotation.

## Approved design principles
Use established cryptographic libraries.

Prefer authenticated encryption:
- AES-256-GCM
- ChaCha20-Poly1305 when appropriate

Never design custom cryptography.

Use safe unique nonces/IVs according to algorithm/library requirements.

Persist necessary metadata:
- algorithm/version
- key version
- nonce/IV
- ciphertext
- authentication tag where applicable

## Key separation
Keys should not live alongside encrypted business data such that one SQL compromise exposes both.

Use KMS/HSM/vault/managed secrets.

Separate:
- DEK — Data Encryption Key
- KEK — Key Encryption Key

Envelope encryption is preferred for mature systems.

## Environment separation
Development, staging, and production must not share encryption keys.

## Tenant separation
Higher-assurance multi-tenant systems may use per-tenant/per-domain DEKs when justified.

## Associated data
Where supported, bind ciphertext to non-secret context such as tenant ID, record type, or field identifier.

## Searchable sensitive fields
Avoid deterministic encryption for convenience.

For exact-match lookup, consider a separate keyed HMAC/blind index over a carefully normalized value with a key distinct from the encryption key.

Document that equality/search indexes leak equality information.

## Rotation
Every ciphertext design must support key versioning.

Rotation supports new writes, old reads during migration, controlled re-encryption, retirement, and emergency compromise rotation.

## Decryption
Decrypt only in trusted server-side code after authorization.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
