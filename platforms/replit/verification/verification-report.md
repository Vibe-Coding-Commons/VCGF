<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Replit adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Replit Agent project instructions through root replit.md. Other Replit AI surfaces are not assumed.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **REPLIT-CLAIM-001 — VERIFIED:** Replit Agent reads a root replit.md file to understand project architecture, conventions, coding patterns, package managers, and dependencies. (https://docs.replit.com/features/project-setup/replit-dot-md)

## Limitations

- Agent may update replit.md, so governance changes to that file should be code-reviewed.
- Application runtime security remains an implementation responsibility.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
