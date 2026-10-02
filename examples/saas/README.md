<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# SaaS adoption example

## Scenario
A multi-tenant B2B SaaS application stores organization data, user profiles, attachments, and administrative configuration.

## Recommended adoption
1. Select the **Production** profile because the service has real users and business data.
2. Use the adapter matching the actual AI coding surface; use **Generic** when no dedicated adapter matches.
3. Define the tenant identifier, membership source, privileged roles, and trusted authorization layer before feature work.
4. Classify personal data and record retention, export, masking, and encryption decisions.
5. Model cross-tenant abuse paths before implementation and keep tenant authorization outside the client UI.
6. Require impact analysis and human approval for authentication, authorization, schema, secret, or production changes.

## Priority controls
`VCGF-ARCH-001`, `VCGF-ARCH-005`, `VCGF-IAM-007`, `VCGF-DB-004`, `VCGF-PRIV-002`, `VCGF-SECR-001`, `VCGF-TEST-001`, `VCGF-REL-002`.

## Verification evidence
- Tenant-isolation threat model.
- Negative tests proving Organization A cannot read or mutate Organization B data.
- Role/permission matrix and database/API authorization evidence.
- PII classification and encryption register where applicable.
- CI/security-test results and release approval record.

## Example release decision
A release is blocked when cross-tenant negative tests fail, an authorization control is implemented only in UI code, or a required exception has no owner and expiration date.
