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

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
