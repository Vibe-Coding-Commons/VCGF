<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF 1.4.0 — development notes (Phase 1: architecture and governance)

**Status:** development version on `develop/v1.4.0`, prepared locally. **Not released, not published, not tagged, not signed, not independently reviewed.** These notes describe the state of the develop branch; they are not release notes for a shipped version. The last public release is v1.3.0 and the local release candidate 1.3.1 (`release/v1.3.1`) is unchanged.

## What changed and why

| Area | Before (1.3.1) | Now (1.4.0 development) |
|---|---|---|
| Router reachability | 19 of 84 controls could not be loaded by any intent; profiles only produced a blocker | every one of the 88 controls is reachable for the high-assurance profile from at least one intent, enforced by `scripts/validate-applicability.py` |
| Profiles | identical selection for baseline, production and high-assurance | additive profile layer: baseline ⊆ production ⊆ high-assurance per task; nothing unrelated to the task is loaded |
| Applicability | implicit in capability files and router code | canonical `spec/applicability-matrix.yaml` with trigger capabilities, always flags and rationale per control |
| Acceptance | verification text only | `spec/acceptance/<domain>.yaml`: verifiable tests (criterion, method, negative path, evidence, automation) for all 88 controls, validated and exposed by the CLI |
| User experience | advisory packs | normative controls VCGF-UX-001..004 bound to profiles and to the Smart UI standards |
| Smart UI | frozen package reachable only through two pack-map documents | governed `ui-select`: layers load only for the user-experience controls in the route, hash-pinned, confined, budgeted; deferred standards are named, never loaded |
| Performance | registry build about 1.2 s (catalog re-parsed per contract validation) | about 0.2 s (content-keyed cache) |

## Compatibility

- The 84 v1.0 controls, their identifiers and requirement text are unchanged. New controls are additive (VCGF-UX-001..004, `framework_version_introduced: 1.4.0`).
- The frozen v1.0 schemas remain byte-identical; the control contract 1.4.0 (`schemas/v1.4.0/control.schema.json`) is a superset. The v1.1.0 `common.schema.json` control-id pattern accepts the `UX` prefix (widening only).
- Profile `required_controls` of 1.0.0 are preserved; the UX controls are appended (profile_version 1.1.0).
- Routing policy 1.2.0 adds intents and capabilities; existing intents keep their capabilities. VCGF-REL-001 is now a minimum control for every route.
- Cumulative compatibility record: `docs/quality/v1.4/baseline-compatibility-v1.4.json` (inherits v1.3.1).

## Verification performed locally

- Validators: full release quality gate including the new `validate-applicability.py` and `validate-acceptance.py`.
- Tests: `tests/scenarios/test_profile_layer.py` (reachability, monotonicity, no unrelated loading, new intents), `tests/scenarios/test_ui_select.py` (profile gating, hash pinning, budget, determinism, CLI), plus the existing contract and runtime suites.
- Measurements: before/after routing probe and token/byte benchmark recorded in the Phase 1 report (UTF-8 bytes measured; tokens estimated by a documented heuristic; no tokenizer measurement is claimed).

## What this is not

Not a release decision, not a conformance claim for any project or platform, and not a substitute for the independent review required before publication. The adapter mapping rows for the UX controls are UNVERIFIED.
