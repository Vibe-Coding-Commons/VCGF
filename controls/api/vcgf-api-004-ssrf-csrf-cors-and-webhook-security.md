---
id: VCGF-API-004
title: SSRF, CSRF, CORS and Webhook Security
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

# VCGF-API-004 - SSRF, CSRF, CORS and Webhook Security

**Control ID:** VCGF-API-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Outbound fetches, browser state-changing requests, cross-origin access, and webhooks MUST use threat-appropriate controls for SSRF, CSRF, origin policy, signatures, replay, and schema validation.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for ssrf, csrf, cors and webhook security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# SSRF, CSRF, CORS, and Webhook Security

## SSRF
For server URL fetches:
- allowlist destinations where feasible
- block localhost/private/link-local/cloud-metadata networks
- validate DNS-resolved addresses
- re-check redirected destinations
- limit schemes/ports
- timeouts and response-size limits
- never forward internal credentials

## CSRF
For cookie-authenticated state changes, use framework CSRF protections and appropriate SameSite behavior.

Do not disable CSRF merely to fix integrations.

## CORS
CORS is not authentication.

Use exact trusted origins for credentialed requests. Avoid arbitrary Origin reflection.

## Webhooks
- verify provider signature
- use raw bytes when signature scheme requires
- validate timestamp/replay window where supported
- idempotent processing
- validate event type and schema
- secret-looking URLs alone are not trust

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
