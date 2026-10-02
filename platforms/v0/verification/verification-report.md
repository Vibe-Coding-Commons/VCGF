<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# v0 adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

v0 Instructions, Plan Mode, Projects, environment-variable project settings, and GitHub-connected workflow documented by v0.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **V0-CLAIM-001 — VERIFIED:** v0 supports reusable custom Instructions and a Plan Mode that prepares a plan before code changes. (https://v0.app/docs/instructions)
- **V0-CLAIM-002 — VERIFIED:** v0 Projects share project settings including environment variables and GitHub integration. (https://v0.app/docs/projects)
- **V0-CLAIM-003 — VERIFIED:** v0 GitHub integration uses working branches and pull requests rather than pushing directly to main. (https://v0.app/docs/github)

## Limitations

- Instructions are behavioral controls and must be reinforced by code, tests, CI, and runtime authorization.
- Platform behavior outside the documented v0 project and Git surfaces is not assumed.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
