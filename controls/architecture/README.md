<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Architecture controls

This directory contains the canonical VCGF normative controls for the **Architecture** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-ARCH-001 | Tenant Isolation | MUST |
| VCGF-ARCH-002 | Trust Boundary Separation | MUST |
| VCGF-ARCH-003 | Established System as Contract | MUST |
| VCGF-ARCH-004 | Separation of Concerns | SHOULD |
| VCGF-ARCH-005 | Threat Modeling | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
