<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Installation

1. Copy `rules/portable-project-rules.md` into the instruction mechanism supported by your AI coding tool.
2. Use `prompts/pre-change-impact-review.md` before MEDIUM, HIGH, or CRITICAL changes.
3. Implement runtime security and release gates outside the AI prompt.
4. Record any tool-specific behavior as project evidence or create a dedicated VCGF adapter.

## Verification

Run `python scripts/validate-adapters.py` and confirm project-specific controls with the selected profile.
