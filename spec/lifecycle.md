<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF lifecycle

The required lifecycle for governed AI-assisted development is:

`Understand → Inspect → Impact Analysis → Risk Analysis → Plan → Human Approval When Required → Implement → Validate → Test → Security Review → Regression Review → Release Review → Release → Monitor`

LOW-risk changes may compress steps while retaining inspection, implementation, validation, and regression awareness. HIGH and CRITICAL changes must not jump directly from prompt to implementation. Human approval applies to authentication, authorization, destructive data changes, production secrets/configuration, infrastructure, personal-data processing, payments, security-control changes, dependency replacement, and major architecture changes.
