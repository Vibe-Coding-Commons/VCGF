<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Security controls

This directory contains the canonical VCGF normative controls for the **Security** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-SEC-001 | Critical Field Validation | MUST |
| VCGF-SEC-002 | File and URL Validation | MUST |
| VCGF-SEC-003 | Injection Defense | MUST |
| VCGF-SEC-004 | Trusted-Layer Input Validation | MUST |
| VCGF-SEC-005 | Output Encoding and Sanitization | MUST |
| VCGF-SEC-006 | Secure Defaults and Fail-Closed Behavior | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
