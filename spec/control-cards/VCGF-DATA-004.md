<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/data-protection/vcgf-data-004-key-management-and-rotation.md -->
# VCGF-DATA-004 — Key Management and Rotation
MUST · data-protection · profiles: high-assurance, production · full text: controls/data-protection/vcgf-data-004-key-management-and-rotation.md

## Requirement
Cryptographic keys MUST be separated from protected data, least-privileged, versioned, rotatable, and recoverable under documented procedures.

## Guidance
Document the full key lifecycle:
- generation
- activation
- storage
- permitted services
- access logging
- rotation
- compromise response
- deactivation
- destruction

## Generation
Use CSPRNG/KMS. Never derive keys from project names or human-readable strings.

## Storage
Preferred:
- managed KMS
- HSM/virtual HSM
- cloud key vault
- dedicated secrets manager

Never commit keys to source or expose field-encryption keys to browser code.

## Separation
Do not reuse password peppers, HMAC lookup keys, token signing keys, and data-encryption keys.

## Rotation triggers
Rotate on scheduled policy, scope changes, suspected compromise, leakage, provider guidance, or improper environment cloning.

## Compromise
Treat as a security incident: issue new keys, stop old-key writes, identify affected data, re-encrypt where required, revoke access, preserve evidence.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
