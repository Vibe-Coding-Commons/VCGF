---
id: VCGF-DATA-003
title: Field-Level Encryption
domain: data-protection
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

# VCGF-DATA-003 - Field-Level Encryption

**Control ID:** VCGF-DATA-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Restricted recoverable data MUST use authenticated field-level encryption when the threat model requires protection beyond storage-layer encryption.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for field-level encryption.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Field-Level Encryption Policy

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
