---
id: VCGF-DB-003
title: Database Encryption Implementation
domain: database
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

# VCGF-DB-003 - Database Encryption Implementation

**Control ID:** VCGF-DB-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Database encryption implementations MUST use approved authenticated cryptography, documented key ownership, versioned ciphertext metadata, and trusted-side decryption.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for database encryption implementation.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Database / Field Encryption Implementation Guide

## Layer 1 — Storage encryption
Use provider/database/disk encryption at rest.

This may not protect against compromise of application/database privileges.

## Layer 2 — Field encryption
For selected Restricted fields:
1. classify
2. decide search need
3. encrypt before persistence in trusted server code
4. decrypt only after authorization
5. store key version/crypto metadata
6. audit access where needed

## Example logical model
For `national_id`:
- `national_id_ciphertext`
- `national_id_key_version`
- optional `national_id_lookup_hash` only if exact lookup is necessary
- masked display representation where justified

Never store original plaintext next to ciphertext.

## Search
For exact lookup, a keyed HMAC blind index may be used over a documented normalized representation.

Use a distinct HMAC key.

Do not use unsalted plain hashes for low-entropy values such as phone numbers or national IDs.

## Key access
Use KMS/vault/crypto service; never hardcode master keys.

## Backups
Ciphertext remains encrypted in backups, but key backup/recovery must be planned separately.

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
