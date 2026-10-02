<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Data Protection controls

This directory contains the canonical VCGF normative controls for the **Data Protection** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-DATA-001 | Backup and Export Protection | MUST |
| VCGF-DATA-002 | Data Classification and Retention | MUST |
| VCGF-DATA-003 | Field-Level Encryption | MUST |
| VCGF-DATA-004 | Key Management and Rotation | MUST |
| VCGF-DATA-005 | Searchable Encrypted Data | SHOULD |
| VCGF-DATA-006 | Data in Transit Protection | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
