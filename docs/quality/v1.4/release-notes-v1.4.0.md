<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF 1.4.0 — Source release notes (architecture, governance, verification and context efficiency)

**Source status (2026-10-26):** v1.4.0 source merged to `main` via PR #4; `VERSION` is 1.4.0, manifest remains `release-candidate`. No signed `v1.4.0` tag or published GitHub Release was found during this review. The last published GitHub Release is v1.3.0. A merged source branch is not the same as a signed published release.

## Executive summary

v1.4.0 adds canonical control applicability, monotonic risk profiles, four UX controls, governed Smart UI selection, 395 acceptance definitions (20 framework self-tests executed; 375 target-project definitions not executed here), control-card fidelity verification, delta and multi-intent loading, evidence-backed compliance evaluation, and strengthened supply-chain and CI checks. The documented 16-scenario context comparison shows 47.2% fewer UTF-8 bytes with equivalent selected controls; this is not a measured reduction in billed provider tokens. GitHub PR #4 passed 22/22 checks on `f67ddeb` on Ubuntu/Windows with Python 3.12/3.13. This does not certify target applications.

See the [Arabic release notes](release-notes-v1.4.0.ar.md) and the bilingual READMEs for user-facing details.

## What changed and why

| Area | Before (1.3.1) | Now (1.4.0 development) |
|---|---|---|
| Router reachability | 19 of 84 controls could not be loaded by any intent; profiles only produced a blocker | every one of the 88 controls is reachable for the high-assurance profile from at least one intent, enforced by `scripts/validate-applicability.py` |
| Profiles | identical selection for baseline, production and high-assurance | additive profile layer: baseline ⊆ production ⊆ high-assurance per task; nothing unrelated to the task is loaded |
| Applicability | implicit in capability files and router code | canonical `spec/applicability-matrix.yaml` with trigger capabilities, always flags and rationale per control |
| Acceptance | verification text only | `spec/acceptance/<domain>.yaml`: verifiable tests (criterion, method, negative path, evidence, automation) for all 88 controls, validated and exposed by the CLI |
| User experience | advisory packs | normative controls VCGF-UX-001..004 bound to profiles and to the Smart UI standards |
| Smart UI | frozen package reachable only through two pack-map documents | governed `ui-select`: layers load only for the user-experience controls in the route, hash-pinned, confined, budgeted; deferred standards are named, never loaded |
| Performance | registry build about 1.2 s (catalog re-parsed per contract validation) | about 0.2 s (content-keyed cache); registry cached per process, second route about 50 ms |
| Context size (Phase 2) | full control Markdown per route; one route per intent; bytes compared with a token limit | derived control cards and shared clauses (about 37 percent of the control bytes) in lean/standard mode, full controls in deep mode; multi-intent routes; delta loading with hash invalidation; estimated tokens enforced with bytes reported |
| Tool output (Phase 2) | loaded text inline by default | hash-pinned references by default, `--full` for text; Smart UI requirement cards for lean/standard routes |
| Verification (Phase 3) | acceptance definitions only | `validate-control-cards.py` fidelity proof; executable self-acceptance for the framework (`framework_self`, recorded results) with target-project definitions kept `not_executed`; delta-loading hardening tests |
| Enforcement (Phase 3) | prompt text only | enforcement matrix with honest statuses, governance-file guard hook, pre-commit hook, Claude Code settings example (configurable, unverified) |
| Budget compatibility (Phase 3) | silent change of comparison unit | `budget_unit` tokens/bytes, disclosure of a changed outcome, migration tool |

## Compatibility

- The 84 v1.0 controls, their identifiers and requirement text are unchanged. New controls are additive (VCGF-UX-001..004, `framework_version_introduced: 1.4.0`).
- The frozen v1.0 schemas remain byte-identical; the control contract 1.4.0 (`schemas/v1.4.0/control.schema.json`) is a superset. The v1.1.0 `common.schema.json` control-id pattern accepts the `UX` prefix (widening only).
- Profile `required_controls` of 1.0.0 are preserved; the UX controls are appended (profile_version 1.1.0).
- Routing policy 1.2.0 adds intents and capabilities; existing intents keep their capabilities. VCGF-REL-001 is now a minimum control for every route.
- Cumulative compatibility record: `docs/quality/v1.4/baseline-compatibility-v1.4.json` (inherits v1.3.1).

Final documented 16-scenario comparison (same selected controls): 2,800,412 → 1,480,014 UTF-8 bytes (−47.2%). Reference tokenizer counts are not actual provider-billed tokens.

## Additional Phase 2–final consolidation capabilities

- Control Cards and shared clauses validated for normative fidelity, including subheadings, references and MUST/SHOULD statements.
- Multi-intent and hash-aware delta routing, explicit `budget_unit` compatibility and optional reference-tokenizer measurements.
- 20/20 executed framework self-acceptance checks; 375 target-project definitions require external project evidence.
- `vcgf.py compliance` verifies project-supplied results, hashes, reviewer requirements and freshness; no evidence means no verified pass.
- Approval-record-based governance guard, with a documented tamper-evident (not tamper-proof) trust boundary.
- GitHub PR #4: 22/22 checks green on commit `f67ddeb`, including Ubuntu, Windows, CodeQL, SBOM and supply-chain checks.
- Four findings inside the frozen Smart UI package remain scheduled for separate remediation; a manually reused schema-invalid template may still be affected.

## Verification performed locally

- Validators: full release quality gate including the new `validate-applicability.py` and `validate-acceptance.py`.
- Tests: `tests/scenarios/test_profile_layer.py` (reachability, monotonicity, no unrelated loading, new intents), `tests/scenarios/test_ui_select.py` (profile gating, hash pinning, budget, determinism, CLI), plus the existing contract and runtime suites.
- Measurements: before/after routing probe and token/byte benchmark recorded in the Phase 1 report (UTF-8 bytes measured; tokens estimated by a documented heuristic; no tokenizer measurement is claimed).

## What this is not

Not a release decision, not a conformance claim for any project or platform, and not a substitute for the independent review required before publication. The adapter mapping rows for the UX controls are UNVERIFIED.
