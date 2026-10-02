---
id: VCGF-AUDIT-001
title: Secure Errors and Diagnostic Logging
domain: logging-auditing
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

# VCGF-AUDIT-001 - Secure Errors and Diagnostic Logging

**Control ID:** VCGF-AUDIT-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

User-facing errors MUST avoid sensitive internals while trusted diagnostic logging preserves sufficient evidence without secrets or unnecessary personal data.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for secure errors and diagnostic logging.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Secure Errors and Security Logging

## User-facing errors
Never expose stack traces, SQL, filesystem paths, secret values, internal hostnames, or debug dumps.

## Server logs
Use correlation ID, operation, safe resource IDs, actor/tenant IDs where permitted.

## Security events
Log:
- repeated auth failure
- reset initiation/completion
- MFA changes
- role changes
- permission denials
- admin actions
- key/security configuration changes
- suspicious exports/downloads
- session revocations

Do not turn logs into a second sensitive-data store.

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
