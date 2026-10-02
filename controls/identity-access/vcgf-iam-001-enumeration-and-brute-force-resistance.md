---
id: VCGF-IAM-001
title: Enumeration and Brute-Force Resistance
domain: identity-access
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

# VCGF-IAM-001 - Enumeration and Brute-Force Resistance

**Control ID:** VCGF-IAM-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Authentication and recovery flows MUST resist account enumeration, credential guessing, automated abuse, and excessive attempts.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for enumeration and brute-force resistance.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Account Enumeration, Brute Force, and Automation Defense

## Enumeration
Use generic responses for login failure, password reset, recovery, and sensitive invitation lookups.

Avoid meaningful timing differences.

## Rate limiting
Use layered controls based on:
- source
- account target
- device/session
- endpoint
- tenant
- API key

Do not rely only on IP.

## Lockout
Avoid designs allowing attackers to permanently lock victims out. Prefer progressive throttling, delays, risk challenges, and alerts.

## Credential stuffing
Use breached-password defenses, MFA, throttling, and anomaly controls where available.

## Logging
Record abuse signals without storing plaintext credentials or excessive PII.

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
