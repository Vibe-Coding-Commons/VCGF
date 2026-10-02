---
id: VCGF-API-005
title: Third-Party Integration Security
domain: api
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

# VCGF-API-005 - Third-Party Integration Security

**Control ID:** VCGF-API-005  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Third-party integrations MUST validate trust boundaries, credentials, scopes, payloads, callbacks, failures, timeouts, and data exposure.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for third-party integration security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Third-Party Integration Security

External providers are separate trust boundaries.

## Credentials
Use minimum scopes, keep private credentials server-side, rotate/revoke unused credentials.

## Incoming
Validate webhook signatures and payload schemas. Treat fields as untrusted.

## Outgoing
Send only minimum necessary personal/sensitive data and document third-party sharing.

## Failure
External API failures must not leave partial business transactions inconsistent. Use retries carefully and idempotency where needed.

## OAuth/OIDC
Use exact redirect URIs and protocol state/nonce protections. Do not implement protocol cryptography from scratch.

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
