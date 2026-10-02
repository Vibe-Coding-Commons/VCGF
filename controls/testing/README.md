<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Testing controls

This directory contains the canonical VCGF normative controls for the **Testing** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-TEST-001 | Authorization Negative Testing | MUST |
| VCGF-TEST-002 | Secure Code Review | MUST |
| VCGF-TEST-003 | Security Regression Review | MUST |
| VCGF-TEST-004 | Security Test Strategy | MUST |
| VCGF-TEST-005 | Validation and Injection Testing | MUST |
| VCGF-TEST-006 | Recovery Flow Testing | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
