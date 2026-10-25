---
id: VCGF-UX-003
title: Interaction State Integrity
domain: user-experience
status: normative
requirement_level: SHOULD
framework_version_introduced: 1.4.0
profiles:
- high-assurance
---

<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF-UX-003 - Interaction State Integrity

**Control ID:** VCGF-UX-003  
**Status:** Normative  
**Requirement Level:** SHOULD

## Requirement

Interactive screens SHOULD make every state explicit and recoverable: loading, empty, error and success states are rendered and announced; submissions are protected against duplicate execution by idempotent server-side handling and disabled or guarded controls; unsaved work is protected before navigation, refresh, language switch or session expiry; destructive or irreversible actions require an explicit confirmation that names the effect; concurrent edits are detected and resolved without silently overwriting; and the interface never reports an action as complete before the trusted layer confirms it.

## Purpose

Interaction state is where user intent meets business state; mishandled states silently corrupt data or double-execute privileged actions.

## Risk Addressed

Duplicate payments or approvals, lost user work, silent overwrites in concurrent editing, misleading success feedback, and unsafe destructive actions triggered without informed confirmation.

## Rationale

Most interaction defects are not visual; they are state-machine defects. Defining the states and transitions as a requirement makes them testable and prevents client-side optimism from masquerading as completion.

## Applicability

Apply to tasks that create or change interactive screens, forms, workflows or background-job interfaces. Required for the High-Assurance profile and recommended for Production. Read-only presentation changes record the control as not applicable with a reason.

## Implementation-Neutral Guidance

# Interaction state integrity

- Model each screen's states explicitly: idle, loading, empty, partial, error, success, stale, offline where relevant; render each with text, not color alone.
- Submission: disable or guard the trigger while pending, send an idempotency key for payment-like or irreversible commands, and treat a timeout as unknown (query the trusted layer) rather than as failure or success.
- Unsaved changes: warn before leaving, keep drafts recoverable where the product allows, and never clear user input because of a refresh, a validation error or a language switch.
- Destructive actions: confirmation names the object and the effect, defaults to the safe choice, offers undo where feasible, and the server enforces authorization regardless of the confirmation.
- Concurrency: use versions or ETags, show the conflict with both versions, and never auto-merge without user decision.
- Session expiry and permission change: preserve the in-progress work, distinguish expired from forbidden, re-authenticate, and resume to the same context when still authorized.
- Completion feedback reflects the trusted layer's result; a toast or closed dialog is not a record.

## Verification Method

For each changed interactive screen, exercise the state matrix (loading, empty, error, success, double submit, unsaved navigation, destructive confirmation, concurrent edit, expired session) with positive and negative cases; verify the server-side result after each case, not only the on-screen message.

## Required Evidence

A state-matrix test record for the changed screens with the trusted-layer outcome of each case, and the idempotency or conflict-handling tests for commands that money, approvals or irreversible changes depend on.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, VCGF-API-002, VCGF-UX-001.

## Related Controls

VCGF-IAM-003 (session security), VCGF-DB-006 (transaction and concurrency integrity), VCGF-GOV-002 (human approval gates), VCGF-AUDIT-002 (audit trail of privileged actions).

## References

- W3C Web Content Accessibility Guidelines (WCAG) 2.2 (status messages, error identification)
- Detailed interaction standards: `packs/ux/smart-ui/interactions/` (VCGF-UI-INT-005 unsaved changes, INT-006 save and submit, INT-007 confirmation, INT-008 empty, INT-009 loading, INT-010 error and retry, INT-012 concurrency conflict, INT-016 session expiry, INT-019 idempotent submission)

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Change History

- 1.4.0: Introduced to bind the Smart UI interaction patterns to a normative control.
