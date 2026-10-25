<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md -->
# VCGF-IAM-007 — Authorization, RBAC, ABAC and Data-Layer Enforcement
MUST · identity-access · profiles: baseline, high-assurance, production · full text: controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md

## Requirement
Authorization MUST be enforced on trusted layers for every protected operation and object; UI visibility MUST NOT be treated as authorization.

## Guidance
Never trust role, user ID, tenant ID, owner ID, or permission flags supplied by the browser.

Derive security context from authenticated server/database identity.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
