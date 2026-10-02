---
id: VCGF-PRIV-002
title: Personal Data Protection
domain: privacy
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

# VCGF-PRIV-002 - Personal Data Protection

**Control ID:** VCGF-PRIV-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Personal data MUST be minimized, purpose-limited, access-controlled, protected in transit and at rest, and handled according to classification and retention requirements.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for personal data protection.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Personal Data / PII Protection Policy

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
