<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Cursor adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Cursor Project Rules under .cursor/rules and root AGENTS.md as documented for Cursor Agent. Runtime security controls remain project responsibilities.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **CURSOR-CLAIM-001 — VERIFIED:** Cursor Project Rules are stored under .cursor/rules and provide persistent scoped instructions. (https://cursor.com/docs/rules)
- **CURSOR-CLAIM-002 — VERIFIED:** Cursor supports root AGENTS.md as a simple project instruction format. (https://cursor.com/docs/rules)

## Limitations

- Rule adherence is behavioral context; trusted runtime controls and CI remain external.
- Legacy .cursorrules is not used as the preferred VCGF mechanism.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
