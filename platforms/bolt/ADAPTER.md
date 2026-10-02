<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Bolt adapter specification

## Identity

- Adapter ID: `bolt`
- Adapter version: `1.0.0`
- Framework compatibility: `>=1.0.0 <2.0.0`
- Platform surface: Bolt web project agent

## Adapter law

This adapter MUST reference VCGF controls rather than restating them as independent policy. It MUST NOT claim a platform capability unless the claim is registered in `verification/sources.yaml` or marked `UNVERIFIED`. It MUST keep application-runtime controls external when the platform only provides behavioral instructions.

## Evidence

Adapter verification evidence is stored under `verification/`. Project conformance evidence is stored by the adopting project, not inside this adapter.
