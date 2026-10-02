<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Api controls

This directory contains the canonical VCGF normative controls for the **Api** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-API-001 | API and Server Function Security | MUST |
| VCGF-API-002 | Business Logic Integrity | MUST |
| VCGF-API-003 | Rate Limiting and Abuse Prevention | MUST |
| VCGF-API-004 | SSRF, CSRF, CORS and Webhook Security | MUST |
| VCGF-API-005 | Third-Party Integration Security | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
