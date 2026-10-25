<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-006-privileged-access-administration.md -->
# VCGF-IAM-006 — Privileged Access Administration
MUST · identity-access · profiles: high-assurance, production · full text: controls/identity-access/vcgf-iam-006-privileged-access-administration.md

## Requirement
Privileged operations MUST use explicit authorization, least privilege, stronger authentication where appropriate, and auditable administrative actions.

## Guidance
Principles:
- least privilege
- separation of duties where practical
- MFA
- explicit admin actions
- full auditability
- short-lived elevation where possible

Prohibited:
- browser-controlled `admin=true`
- client-side-only admin checks
- shared admin accounts
- long-lived admin keys in browser code
- silent destructive operations

High-risk actions may require confirmation/step-up authentication:
- user deletion
- role elevation
- Restricted-data export
- RLS/security changes
- MFA reset for another user
- key rotation
- backup restore
- bulk deletion

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
