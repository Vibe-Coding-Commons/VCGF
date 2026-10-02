<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Implementation guide

VCGF is technology-neutral. Translate controls into implementation through architecture decisions, server-side validation, authorization policies, database constraints, cryptography/key management, secure secret storage, dependency controls, tests, CI, monitoring, and operational procedures appropriate to the project stack.

Do not implement security by hiding UI elements, trusting client-supplied roles/tenant IDs, disabling RLS/authorization to fix errors, placing secrets in frontend code, using reversible password encryption, or accepting AI-generated dependencies without provenance review.
