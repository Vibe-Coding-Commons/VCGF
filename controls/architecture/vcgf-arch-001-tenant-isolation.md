---
id: VCGF-ARCH-001
title: Tenant Isolation
domain: architecture
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

# VCGF-ARCH-001 - Tenant Isolation

**Control ID:** VCGF-ARCH-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Multi-tenant systems MUST enforce tenant isolation on trusted layers and MUST include negative cross-tenant access tests.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for tenant isolation.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Multi-Tenancy Isolation Policy

Tenant identity must come from authenticated membership/trusted server context, not only request fields.

Tenant-scoped records require explicit tenant relationships.

Every private query enforces tenant scope; prefer DB policy/RLS for defense in depth.

Prevent cross-tenant foreign-key/business relationships unless explicitly designed.

Background jobs must carry/verify tenant context.

Tenant-specific caches need tenant-scoped cache keys.

Storage paths/policies must enforce tenant/user ownership.

Tests must prove Tenant A cannot read/write/delete Tenant B data.

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
