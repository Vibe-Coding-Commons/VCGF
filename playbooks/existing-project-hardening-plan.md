<!--
VCGF - Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Author: Eng. Hamada Sami
Mobile + WhatsApp: +966560000934
Email: i@hamada.io
LinkedIn: https://www.linkedin.com/in/hamadas/
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Existing Project Hardening Plan

## Phase 1 — Read only
Run architecture/security audit.

## Phase 2 — Stop critical exposure
Prioritize:
- secret leaks
- public sensitive data
- broken auth
- tenant escape
- RLS bypass
- injection
- unsafe recovery

## Phase 3 — Data protection
Classify data and add encryption/redaction/retention where justified.

## Phase 4 — Validation
Centralize schemas and authoritative server validation.

## Phase 5 — Assurance
Add negative tests, scans, gates, and evidence.

Avoid a big-bang rewrite. Harden through controlled tested changes.
