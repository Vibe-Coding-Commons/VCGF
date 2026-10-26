<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/api/vcgf-api-002-business-logic-integrity.md -->
# VCGF-API-002 — Business Logic Integrity
MUST · api · profiles: high-assurance, production · full text: controls/api/vcgf-api-002-business-logic-integrity.md

## Requirement
Sensitive business state, calculations, approvals, prices, ownership, and transitions MUST be verified on a trusted layer and protected from replay and race conditions where relevant.

## Guidance
Attackers can submit valid-looking requests in invalid order.

Never trust client-calculated:
- price
- discount
- tax
- balance
- credit
- quota
- role
- approval state
- ownership
- tenant
- entitlement

Server recalculates or verifies these values.

## State machines
Document valid transitions and reject unauthorized transitions.

## Race conditions
Use transactions, locking/concurrency control, uniqueness, idempotency, and atomic updates where needed.

## Duplicate submissions
Payments, orders, approvals, emails, vouchers, and provisioning must be resilient to retries.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
