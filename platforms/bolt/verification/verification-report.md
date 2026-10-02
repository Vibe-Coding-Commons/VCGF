<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Bolt adapter verification report

**Adapter version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Verification date:** 2026-10-02  
**Status:** verified  

## Verified surface

Bolt Project Knowledge and project-context workflow documented in Bolt project settings. Runtime controls remain application responsibilities.

## Source policy

Platform-specific claims in this adapter are limited to claims recorded in `sources.yaml`. Runtime security controls that are not documented as native are mapped to `EXTERNAL` or `PARTIAL`, never inferred.

## Claims reviewed

- **BOLT-CLAIM-001 — VERIFIED:** Bolt Project Knowledge stores background instructions for goals, style, terminology, constraints, and workflows. (https://support.bolt.new/settings/project-settings)

## Limitations

- Project Knowledge guides the agent but does not replace trusted server/database controls.
- Capabilities not present in official documentation are not claimed by this adapter.

## Release decision

The adapter status reflects the verified instruction/configuration surface only. VCGF conformance still requires project-specific evidence for every required control.
