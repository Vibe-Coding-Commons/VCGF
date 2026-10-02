<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF adapter: Generic

**Adapter:** `generic`  
**Version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Status:** stable  
**Platform surface:** Portable AI-assisted development workflow

## Purpose

Reference adapter for tools without a dedicated VCGF adapter. It uses portable repository instructions, prompts, external CI, and runtime controls.

## Quick setup

Load the portable project rules into the persistent instruction mechanism of your tool, or paste them into governed sessions.

For a beginner-friendly, step-by-step installation, first-session prompt, activation test, examples, evidence/checklist usage, troubleshooting, and update process, use the full guide:

**→ [`../../docs/platform-guides/generic.md`](../../docs/platform-guides/generic.md)**

## Canonical adapter files

- `adapter.yaml` — identity, version, scope, capabilities, limitations, and compatibility.
- `control-mapping.yaml` — machine-readable mapping to VCGF controls.
- `CONTROL-MAPPING.md` — human-readable mapping.
- `verification/sources.yaml` — source-traceable platform claims.
- `CAPABILITIES.md` / `LIMITATIONS.md` — supported behavior and boundaries.
- `rules/` — platform-appropriate VCGF instruction assets.
- `prompts/` — supplemental review prompts.
- `tests/` — adapter verification guidance.

## Security boundary

The adapter explains how VCGF guidance reaches Generic. It does not automatically enforce application-runtime authentication, authorization, validation, encryption, secrets, database security, file access, or production controls unless a control mapping explicitly identifies verified platform enforcement.
