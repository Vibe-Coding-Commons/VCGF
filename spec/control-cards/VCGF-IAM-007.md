<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md -->
# VCGF-IAM-007 — Authorization, RBAC, ABAC and Data-Layer Enforcement
MUST · identity-access · profiles: baseline, high-assurance, production · full text: controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md

## Requirement
Authorization MUST be enforced on trusted layers for every protected operation and object; UI visibility MUST NOT be treated as authorization.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
