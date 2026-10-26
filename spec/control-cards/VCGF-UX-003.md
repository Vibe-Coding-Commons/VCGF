<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/user-experience/vcgf-ux-003-interaction-state-integrity.md -->
# VCGF-UX-003 — Interaction State Integrity
SHOULD · user-experience · profiles: high-assurance · full text: controls/user-experience/vcgf-ux-003-interaction-state-integrity.md

## Requirement
Interactive screens SHOULD make every state explicit and recoverable: loading, empty, error and success states are rendered and announced; submissions are protected against duplicate execution by idempotent server-side handling and disabled or guarded controls; unsaved work is protected before navigation, refresh, language switch or session expiry; destructive or irreversible actions require an explicit confirmation that names the effect; concurrent edits are detected and resolved without silently overwriting; and the interface never reports an action as complete before the trusted layer confirms it.

## Guidance
- Model each screen's states explicitly: idle, loading, empty, partial, error, success, stale, offline where relevant; render each with text, not color alone.
- Submission: disable or guard the trigger while pending, send an idempotency key for payment-like or irreversible commands, and treat a timeout as unknown (query the trusted layer) rather than as failure or success.
- Unsaved changes: warn before leaving, keep drafts recoverable where the product allows, and never clear user input because of a refresh, a validation error or a language switch.
- Destructive actions: confirmation names the object and the effect, defaults to the safe choice, offers undo where feasible, and the server enforces authorization regardless of the confirmation.
- Concurrency: use versions or ETags, show the conflict with both versions, and never auto-merge without user decision.
- Session expiry and permission change: preserve the in-progress work, distinguish expired from forbidden, re-authenticate, and resume to the same context when still authorized.
- Completion feedback reflects the trusted layer's result; a toast or closed dialog is not a record.

## References
- W3C Web Content Accessibility Guidelines (WCAG) 2.2 (status messages, error identification)
- Detailed interaction standards: `packs/ux/smart-ui/interactions/` (VCGF-UI-INT-005 unsaved changes, INT-006 save and submit, INT-007 confirmation, INT-008 empty, INT-009 loading, INT-010 error and retry, INT-012 concurrency conflict, INT-016 session expiry, INT-019 idempotent submission)

## Applicability
Apply to tasks that create or change interactive screens, forms, workflows or background-job interfaces. Required for the High-Assurance profile and recommended for Production. Read-only presentation changes record the control as not applicable with a reason.

## Verification Method
For each changed interactive screen, exercise the state matrix (loading, empty, error, success, double submit, unsaved navigation, destructive confirmation, concurrent edit, expired session) with positive and negative cases; verify the server-side result after each case, not only the on-screen message.

## Required Evidence
A state-matrix test record for the changed screens with the trusted-layer outcome of each case, and the idempotency or conflict-handling tests for commands that money, approvals or irreversible changes depend on.

## Dependencies
VCGF-GOV-001, VCGF-GOV-004, VCGF-API-002, VCGF-UX-001.

## Related Controls
VCGF-IAM-003 (session security), VCGF-DB-006 (transaction and concurrency integrity), VCGF-GOV-002 (human approval gates), VCGF-AUDIT-002 (audit trail of privileged actions).

Common clauses (spec/control-cards/common-clauses.md): Exceptions[A] Platform[A]
