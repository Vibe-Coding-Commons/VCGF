<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-003-database-encryption-implementation.md -->
# VCGF-DB-003 — Database Encryption Implementation
MUST · database · profiles: high-assurance, production · full text: controls/database/vcgf-db-003-database-encryption-implementation.md

## Requirement
Database encryption implementations MUST use approved authenticated cryptography, documented key ownership, versioned ciphertext metadata, and trusted-side decryption.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
