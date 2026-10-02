<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Release controls

This directory contains the canonical VCGF normative controls for the **Release** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-REL-001 | Definition of Done | MUST |
| VCGF-REL-002 | Pre-Release Security Gate | MUST |
| VCGF-REL-003 | Rollback and Recovery Readiness | MUST |
| VCGF-REL-004 | Post-Release Monitoring | SHOULD |
| VCGF-REL-005 | Release Artifact Integrity and Provenance | MUST |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
