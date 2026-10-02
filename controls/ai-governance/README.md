<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Ai Governance controls

This directory contains the canonical VCGF normative controls for the **Ai Governance** domain. Control files are the source of truth; `spec/control-catalog.yaml` is generated from their front matter.

| Control ID | Title | Requirement |
|---|---|---|
| VCGF-AI-001 | Inspect Before Generate | MUST |
| VCGF-AI-002 | No Silent Assumptions | MUST |
| VCGF-AI-003 | Architecture Drift Prevention | MUST |
| VCGF-AI-004 | Unauthorized Refactoring and Feature Change Prevention | MUST NOT |
| VCGF-AI-005 | Hallucinated API and Dependency Prevention | MUST |
| VCGF-AI-006 | Sensitive Change Guardrails | MUST |
| VCGF-AI-007 | Security Control Tamper Prevention | MUST NOT |
| VCGF-AI-008 | Prompt and Tool Injection Resilience | MUST |
| VCGF-AI-009 | Persistent Context Governance | SHOULD |

Control IDs are immutable after the v1.0.0 release. A retired control is marked Deprecated and its identifier is never reused.
