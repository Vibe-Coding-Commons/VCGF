---
id: VCGF-DB-004
title: Row-Level Authorization Testing
domain: database
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

# VCGF-DB-004 - Row-Level Authorization Testing

**Control ID:** VCGF-DB-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Where row-level security or equivalent data-layer controls are used, allow and deny paths MUST be tested across anonymous, owner, non-owner, tenant, and privileged contexts as applicable.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for row-level authorization testing.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Row Level Security Testing Policy

Define grants and RLS deliberately for:
- SELECT
- INSERT
- UPDATE
- DELETE

Test:
- anonymous
- User A
- User B
- privileged/admin
- Tenant A
- Tenant B

Prove:
- A cannot access B private rows
- cross-tenant access fails
- client owner/tenant ID manipulation fails
- privileged server functions do not leak unscoped data

Review views and security-definer functions for bypass behavior.

Privileged/secret/service keys may bypass RLS; keep them server-side and authorize before use.

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
