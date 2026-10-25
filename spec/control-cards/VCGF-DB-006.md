<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-006-transaction-and-concurrency-integrity.md -->
# VCGF-DB-006 — Transaction and Concurrency Integrity
MUST · database · profiles: high-assurance, production · full text: controls/database/vcgf-db-006-transaction-and-concurrency-integrity.md

## Requirement
Multi-step operations that can produce inconsistent security or business state MUST use suitable atomicity, locking, idempotency, or concurrency controls.

## Guidance
Identify race-sensitive transitions such as approvals, balances, inventory, one-time tokens, quota consumption, and duplicate submissions.

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
