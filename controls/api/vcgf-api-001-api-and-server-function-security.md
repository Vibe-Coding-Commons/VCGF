---
id: VCGF-API-001
title: API and Server Function Security
domain: api
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

# VCGF-API-001 - API and Server Function Security

**Control ID:** VCGF-API-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Every externally callable endpoint or server function MUST independently enforce authentication, authorization, validation, resource limits, and safe error handling as applicable.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for api and server function security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# API and Edge Function Security

Assume every endpoint is directly callable by an attacker.

## Per-endpoint checklist
- authentication
- operation-level authorization
- object-level authorization
- tenant validation
- request schema
- request/body size limit
- input validation
- safe query construction
- rate limiting/quotas
- replay/idempotency where relevant
- minimal response schema
- safe errors
- timeout
- external-call restrictions
- audit logging for sensitive actions

## Privileged DB clients
Use service/admin clients only in trusted server code and only after explicit application authorization.

Prefer user-scoped/RLS-scoped access when possible.

## Mass assignment
Do not pass request JSON directly to persistence for privileged models. Pick allowed fields explicitly.

## Output
Do not return full DB records by default. Use explicit response schemas.

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
