<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF adapter: Replit

**Adapter:** `replit`  
**Version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Status:** stable  
**Platform surface:** Replit Agent project

## Purpose

Replit Agent project instructions through root replit.md. Other Replit AI surfaces are not assumed.

## Quick setup

Copy the supplied `replit.md` to the project root.

For a beginner-friendly, step-by-step installation, first-session prompt, activation test, examples, evidence/checklist usage, troubleshooting, and update process, use the full guide:

**→ [`../../docs/platform-guides/replit.md`](../../docs/platform-guides/replit.md)**

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

The adapter explains how VCGF guidance reaches Replit. It does not automatically enforce application-runtime authentication, authorization, validation, encryption, secrets, database security, file access, or production controls unless a control mapping explicitly identifies verified platform enforcement.
