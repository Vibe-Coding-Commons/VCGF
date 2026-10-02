<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Generic / Vendor-Neutral adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Reference adapter for tools without a dedicated VCGF adapter. It uses portable repository instructions, prompts, external CI, and runtime controls.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **GENERIC-CLAIM-001 — VERIFIED:** Reference adapter is defined by VCGF itself. (spec/VCGF-CORE.md)

## Limitations

- Behavioral instructions depend on the selected AI tool consuming the provided context.
- Runtime security and CI enforcement must be implemented by the project environment.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
