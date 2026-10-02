<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Adapter model

A VCGF adapter maps Core requirements to one precisely scoped platform surface. It contains an independent version, compatibility range, capabilities, limitations, official-source claim register, machine-readable control mapping, installation assets, prompts/rules, examples, and tests.

Mapping states are: `NATIVE`, `CONFIGURABLE`, `PROMPT-ENFORCED`, `EXTERNAL`, `PARTIAL`, `UNSUPPORTED`, `NOT-APPLICABLE`, and `UNVERIFIED`. Behavioral instruction mechanisms are never labeled hard runtime enforcement.

Use `platforms/_adapter-template/` to create a new adapter.
