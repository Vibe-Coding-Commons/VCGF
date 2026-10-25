<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-004-row-level-authorization-testing.md -->
# VCGF-DB-004 — Row-Level Authorization Testing
MUST · database · profiles: high-assurance, production · full text: controls/database/vcgf-db-004-row-level-authorization-testing.md

## Requirement
Where row-level security or equivalent data-layer controls are used, allow and deny paths MUST be tested across anonymous, owner, non-owner, tenant, and privileged contexts as applicable.

## Guidance
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

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
