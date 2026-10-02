<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Lovable adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Workspace Knowledge, Project Knowledge, repository instruction files, built-in verification tools, and security-review surfaces documented by Lovable.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **LOVABLE-CLAIM-001 — VERIFIED:** Workspace Knowledge and Project Knowledge provide persistent instructions and context. (https://docs.lovable.dev/features/knowledge)
- **LOVABLE-CLAIM-002 — VERIFIED:** Lovable reads repository instruction files such as AGENTS.md or CLAUDE.md; root AGENTS.md is always read. (https://docs.lovable.dev/features/knowledge)
- **LOVABLE-CLAIM-003 — VERIFIED:** Lovable provides browser testing, frontend tests, and edge-function verification. (https://docs.lovable.dev/features/testing)
- **LOVABLE-CLAIM-004 — VERIFIED:** Lovable documents built-in security scans. (https://docs.lovable.dev/features/security)

## Limitations

- Knowledge and instruction files shape agent behavior; they are not an application-runtime enforcement boundary.
- Platform security scans are evidence inputs, not proof of complete VCGF conformance.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
