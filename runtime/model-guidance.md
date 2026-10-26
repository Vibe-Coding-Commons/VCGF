<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami | https://github.com/Vibe-Coding-Commons -->

# Model and reasoning-effort guidance (advisory)

This document is not loaded into any route. The Router emits a `model_guidance` block beside each route result; hosts and adapters may use it to choose a model tier or reasoning effort. Guidance never changes the selected controls, the approvals required or the evidence expected.

| Route | reasoning_effort | Why |
|---|---|---|
| risk HIGH or CRITICAL, or mode `deep` | `high` | approval-gated changes and deep reviews need the most careful reading of the full control text |
| risk MEDIUM | `standard` | ordinary feature work under lean/standard cards |
| risk LOW and mode lean/standard | `low` | small, reversible tasks; the minimum controls still apply |

Context-cache guidance: the first two served items of every route are identical across tasks (`runtime/bootstrap.md`, then `spec/control-cards/common-clauses.md` in lean/standard mode). Hosts that cache prompt prefixes keep them; `loaded_context` plus `loaded_context_policy_sha256` lets a session reuse everything it already holds and receive only the delta. Any change of a source file changes the hash and the registry fingerprint, so a cached prefix is never stale silently.

Not a cost claim: token figures are estimates (or a reference tokenizer when `VCGF_TOKENIZER` is set); actual billing depends on the target model's tokenizer and pricing, which VCGF does not measure.
