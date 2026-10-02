---
id: VCGF-PRIV-001
title: Logging Redaction and Privacy
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

# VCGF-PRIV-001 - Logging Redaction and Privacy

**Control ID:** VCGF-PRIV-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Logs, telemetry, analytics, URLs, and errors MUST minimize and redact personal, authentication, and secret data.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for logging redaction and privacy.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Logging, Redaction, and Privacy

## Never log
- plaintext passwords
- password hashes
- session cookies
- access/refresh tokens
- API secret keys
- encryption keys
- full password-reset tokens/URLs
- MFA secrets
- unnecessary Restricted PII

## Prefer identifiers
Use request ID, actor ID, tenant ID, resource ID, and event type instead of full payloads.

## Central redaction
Redact authorization headers, cookies, known secret fields, tokens, and personal identifiers centrally.

## Audit logs
Record actor, action, resource, time, result, tenant/context, and correlation ID where appropriate.

Restrict and protect audit logs from tampering.

## Third-party error tools
Scrub sensitive request payloads before sending.

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
