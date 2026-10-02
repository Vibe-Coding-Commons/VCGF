---
id: VCGF-IAM-007
title: Authorization, RBAC, ABAC and Data-Layer Enforcement
domain: identity-access
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

# VCGF-IAM-007 - Authorization, RBAC, ABAC and Data-Layer Enforcement

**Control ID:** VCGF-IAM-007  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Authorization MUST be enforced on trusted layers for every protected operation and object; UI visibility MUST NOT be treated as authorization.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for authorization, rbac, abac and data-layer enforcement.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# RBAC, ABAC, Object Authorization, and RLS Policy

Never trust role, user ID, tenant ID, owner ID, or permission flags supplied by the browser.

Derive security context from authenticated server/database identity.

## RBAC
Maintain a documented matrix:
Role → Resource → Read/Create/Update/Delete/Special Actions.

## ABAC/Object rules
Permissions may depend on ownership, tenant, department, state, assignment, or sensitivity. Evaluate trusted attributes, not client claims.

## Object-level authorization
Every request for a resource ID must verify access to that exact resource. A valid ID is not authorization.

## RLS
For exposed databases:
- enable RLS where applicable
- set least-privilege grants
- define operation-specific policies
- test allow/deny
- review views/functions that may bypass RLS
- keep privileged/bypass credentials server-side

## Multi-tenant
Every private tenant-scoped record needs an enforceable tenant model. Frontend-only filtering is prohibited.

## Admin
Admin access is explicit, audited, and separated from ordinary user behavior where feasible.

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
