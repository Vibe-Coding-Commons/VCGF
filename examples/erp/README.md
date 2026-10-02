<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# ERP adoption example

## Scenario
An ERP manages financial transactions, inventory, approvals, HR-related records, and business-critical state transitions.

## Recommended adoption
1. Use the **High-Assurance** profile when the ERP controls sensitive institutional or financial processes; otherwise use **Production**.
2. Model approval states and segregation of duties before coding workflows.
3. Validate money, currency, quantities, dates, identifiers, and cross-field invariants on trusted layers.
4. Enforce database constraints, transactional integrity, concurrency safety, and idempotency for critical posting operations.
5. Audit privileged adjustments, approvals, reversals, exports, and security-sensitive administration.
6. Require human approval and tested recovery for destructive migrations or changes to financial/business logic.

## Priority controls
`VCGF-API-002`, `VCGF-DB-002`, `VCGF-DB-006`, `VCGF-IAM-006`, `VCGF-IAM-007`, `VCGF-AUDIT-002`, `VCGF-GOV-002`, `VCGF-REL-003`.

## Verification evidence
- State-transition tests for draft, submitted, approved, rejected, posted, and reversed operations as applicable.
- Concurrency/idempotency tests for duplicate submission.
- Database migration review and recovery evidence.
- Privileged audit trail samples.
- Approval evidence for high-risk business-rule changes.

## Example release decision
A release is blocked when client-provided totals are trusted without server recalculation, when a posted transaction can be silently deleted, or when a destructive migration lacks validated recovery.
