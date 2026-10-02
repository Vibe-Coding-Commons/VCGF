<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Identity Access controls

This directory contains the canonical VCGF normative controls for the **Identity Access** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-IAM-001 | Enumeration and Brute-Force Resistance | MUST |
| VCGF-IAM-002 | Authentication Baseline | MUST |
| VCGF-IAM-003 | MFA and Session Security | MUST |
| VCGF-IAM-004 | Password Storage and Policy | MUST |
| VCGF-IAM-005 | Secure Password Reset and Recovery | MUST |
| VCGF-IAM-006 | Privileged Access Administration | MUST |
| VCGF-IAM-007 | Authorization, RBAC, ABAC and Data-Layer Enforcement | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
