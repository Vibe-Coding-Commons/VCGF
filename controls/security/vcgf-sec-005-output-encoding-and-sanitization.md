---
id: VCGF-SEC-005
title: Output Encoding and Sanitization
domain: security
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
- baseline
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

# VCGF-SEC-005 - Output Encoding and Sanitization

**Control ID:** VCGF-SEC-005  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Untrusted data MUST be encoded or sanitized for its destination context before rendering or interpreter execution.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for output encoding and sanitization.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Output Encoding and Sanitization

Validation and output encoding solve different problems.

## Plain text
Prefer framework mechanisms that render values as text rather than HTML.

Encode untrusted data for its exact output context:
- HTML body
- HTML attribute
- URL component
- JavaScript
- CSS
- CSV/spreadsheet
- shell/interpreter

No generic sanitizer is safe for every context.

## Rich HTML
When rich HTML is genuinely required, use a maintained allowlist sanitizer.

Never use raw HTML rendering such as `dangerouslySetInnerHTML` without a justified sanitization boundary.

Do not mutate sanitized HTML with unsafe string operations afterwards.

## URLs
Allow only expected schemes and validate redirect destinations.

## CSP
Content Security Policy is defense in depth, not a replacement for safe rendering.

## Spreadsheet exports
Neutralize user-controlled values that spreadsheet programs could treat as formulas.

## Logs
Secrets should be excluded/redacted, not "sanitized" into logs.

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
