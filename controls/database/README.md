<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Database controls

This directory contains the canonical VCGF normative controls for the **Database** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-DB-001 | Database Change Governance | MUST |
| VCGF-DB-002 | Database Integrity | MUST |
| VCGF-DB-003 | Database Encryption Implementation | MUST |
| VCGF-DB-004 | Row-Level Authorization Testing | MUST |
| VCGF-DB-005 | SQL Query Security | MUST |
| VCGF-DB-006 | Transaction and Concurrency Integrity | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
