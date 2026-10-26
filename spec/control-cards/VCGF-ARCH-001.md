<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/architecture/vcgf-arch-001-tenant-isolation.md -->
# VCGF-ARCH-001 — Tenant Isolation
MUST · architecture · profiles: high-assurance, production · full text: controls/architecture/vcgf-arch-001-tenant-isolation.md

## Requirement
Multi-tenant systems MUST enforce tenant isolation on trusted layers and MUST include negative cross-tenant access tests.

## Guidance
Tenant identity must come from authenticated membership/trusted server context, not only request fields.

Tenant-scoped records require explicit tenant relationships.

Every private query enforces tenant scope; prefer DB policy/RLS for defense in depth.

Prevent cross-tenant foreign-key/business relationships unless explicitly designed.

Background jobs must carry/verify tenant context.

Tenant-specific caches need tenant-scoped cache keys.

Storage paths/policies must enforce tenant/user ownership.

Tests must prove Tenant A cannot read/write/delete Tenant B data.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
