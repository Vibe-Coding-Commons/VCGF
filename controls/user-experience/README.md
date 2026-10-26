<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# User Experience controls

This directory contains the canonical VCGF normative controls for the **User Experience** domain, introduced in framework version 1.4.0. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter. The detailed component, interaction, screen-composition and journey standards live in `packs/ux/smart-ui/` and are bound to these controls through `spec/applicability-matrix.yaml`, `spec/acceptance/user-experience.yaml` and the governed `ui-select` command; they are loaded selectively, never as permanent context.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-UX-001 | Accessibility Conformance | MUST |
| VCGF-UX-002 | Localization and Bidirectional Text | MUST |
| VCGF-UX-003 | Interaction State Integrity | SHOULD |
| VCGF-UX-004 | Responsive Strategy and Density | SHOULD |

Control IDs are immutable once released. A retired control is marked Deprecated and its identifier is never reused.
