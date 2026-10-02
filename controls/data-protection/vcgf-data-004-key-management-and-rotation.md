---
id: VCGF-DATA-004
title: Key Management and Rotation
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

# VCGF-DATA-004 - Key Management and Rotation

**Control ID:** VCGF-DATA-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Cryptographic keys MUST be separated from protected data, least-privileged, versioned, rotatable, and recoverable under documented procedures.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for key management and rotation.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Cryptographic Key Management and Rotation

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
