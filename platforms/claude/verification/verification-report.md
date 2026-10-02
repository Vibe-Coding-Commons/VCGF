<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Claude adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Project instructions through CLAUDE.md and supported project-instruction mechanisms for Claude Code. This adapter does not claim behavior for Claude Web or the Claude API unless separately documented.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **CLAUDE-CLAIM-001 — VERIFIED:** Claude Code loads CLAUDE.md project instructions for coding standards, workflows, and project architecture. (https://code.claude.com/docs/en/memory)
- **CLAUDE-CLAIM-002 — VERIFIED:** Claude Code can read AGENTS.md under documented project-instruction conditions. (https://code.claude.com/docs/en/memory)
- **CLAUDE-CLAIM-003 — VERIFIED:** CLAUDE.md instructions shape behavior but are not hard enforcement; managed settings can enforce selected client constraints. (https://code.claude.com/docs/en/memory)

## Limitations

- Instructions can guide behavior but runtime and CI controls remain external.
- AGENTS.md loading semantics depend on Claude Code version and project-instruction configuration.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
