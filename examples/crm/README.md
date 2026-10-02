<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# CRM adoption example

## Scenario
A CRM stores contacts, account notes, sales activities, attachments, exports, and third-party messaging or enrichment integrations.

## Recommended adoption
1. Select the **Production** profile for customer-facing or internal production use.
2. Classify contact and account fields by purpose and sensitivity; do not collect data without a defined business purpose.
3. Validate email, phone, identifiers, URLs, notes, imports, and exported spreadsheet content at trusted boundaries.
4. Restrict bulk export, merge, delete, and administrative actions through explicit roles and server-side authorization.
5. Protect webhooks and integrations with least-privilege credentials, signature checks where supported, and safe outbound URL handling.
6. Redact sensitive fields from diagnostic logs and audit privileged exports or mass changes.

## Priority controls
`VCGF-SEC-001`, `VCGF-SEC-003`, `VCGF-PRIV-003`, `VCGF-IAM-007`, `VCGF-API-004`, `VCGF-API-005`, `VCGF-AUDIT-002`, `VCGF-DATA-001`.

## Verification evidence
- Field-validation matrix covering contact imports and exports.
- Permission tests for sales, manager, and administrator actors.
- Webhook/integration configuration evidence.
- Audit events for bulk export and privileged data changes.
- Data-retention and deletion evidence.

## Example release decision
A release is blocked when export authorization can be bypassed by changing a client-supplied account ID, or when integration secrets are exposed to browser code.
