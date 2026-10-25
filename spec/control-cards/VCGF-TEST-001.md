<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/testing/vcgf-test-001-authorization-negative-testing.md -->
# VCGF-TEST-001 — Authorization Negative Testing
MUST · testing · profiles: high-assurance, production · full text: controls/testing/vcgf-test-001-authorization-negative-testing.md

## Requirement
Protected features MUST test both allowed and denied access, including object-level and tenant-level negative cases where applicable.

## Guidance
| Actor | Read | Create | Update | Delete | Special action |
|---|---|---|---|---|---|
| Anonymous | Deny unless public | Deny unless designed | Deny | Deny | Deny |
| User A owner | Expected policy | Expected | Expected | Expected | Expected |
| User B non-owner | Deny private | Controlled | Deny | Deny | Deny |
| Tenant A | Tenant A only | Tenant A only | Tenant A only | Tenant A only | Scoped |
| Tenant B against A | Deny | Deny | Deny | Deny | Deny |
| Privileged | Explicit | Explicit | Explicit | Explicit | Audited |

Also test:
- modified `user_id`
- modified `tenant_id`
- direct API calls
- guessed IDs
- bulk endpoints
- exports
- storage URLs
- privileged server functions

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
