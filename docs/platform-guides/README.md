<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF platform setup guides

Choose the platform you actually use. Each guide explains what to copy, where the verified platform supports persistent instructions, how to prepare project context, what first message to send, how to verify VCGF is active, and what limitations remain.

> The VCGF Core is the same on every platform. The adapter changes **how the rules are delivered to the AI**, not the security requirement itself.

| Platform | Adapter status | Difficulty | Typical setup | Main rule asset(s) | Guide |
|---|---|---:|---:|---|---|
| Lovable | stable | Easy | 5–10 min | workspace-knowledge.md, project-knowledge.md, AGENTS.md | [lovable.md](lovable.md) |
| Claude Code | stable | Easy | 5–10 min | CLAUDE.md | [claude.md](claude.md) |
| Bolt | stable | Easy | 5–10 min | project-knowledge.md | [bolt.md](bolt.md) |
| v0 | stable | Easy | 5–10 min | custom-instructions.md | [v0.md](v0.md) |
| Replit | stable | Easy | 5–10 min | replit.md | [replit.md](replit.md) |
| Cursor | stable | Medium | 10–15 min | vcgf.mdc, AGENTS.md | [cursor.md](cursor.md) |
| Generic | stable | Easy | 5–10 min | portable-project-rules.md | [generic.md](generic.md) |

## If your platform is not listed

Use the [Generic adapter](generic.md). It is intentionally vendor-neutral and does not claim native enforcement.

## What to prepare before choosing a guide

1. Choose a [VCGF profile](../../profiles/).
2. Complete `templates/project-context/project-context.md`.
3. Know where your application code and database/security configuration live.
4. Do not place production secrets inside VCGF prompts or project-context documentation.

## Platform claims

The vendor-specific guides use only behavior recorded in each adapter's `verification/sources.yaml` or clearly label a step as a VCGF convention rather than a platform-native feature.
