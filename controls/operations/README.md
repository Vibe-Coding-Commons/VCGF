<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Operations controls

This directory contains the canonical VCGF normative controls for the **Operations** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-OPS-001 | Environment Separation | MUST |
| VCGF-OPS-002 | Production Protection | MUST |
| VCGF-OPS-003 | Backup and Recovery Validation | MUST |
| VCGF-OPS-004 | Configuration Drift Control | SHOULD |
| VCGF-OPS-005 | Security Monitoring and Alerting | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
