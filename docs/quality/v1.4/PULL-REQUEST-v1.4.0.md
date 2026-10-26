<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->
# Pull request draft — VCGF v1.4.0 release candidate

Prepared locally for an independent, non-author review. Not pushed, not opened, not merged. When a maintainer with push rights decides to proceed:

```bash
git push origin develop/v1.4.0
```

```bash
gh pr create --base main --head develop/v1.4.0 --title "VCGF v1.4.0 release candidate: architecture, governance, context efficiency, verification and enforcement" --body-file docs/quality/v1.4/PULL-REQUEST-v1.4.0.md
```

---

## Title
VCGF v1.4.0 release candidate: architecture, governance, context efficiency, verification and enforcement

## Summary
Candidate code commit `d1e2c58`; the readiness-closure commits on top of it only add documentation and the validation record (the PR head is the authoritative reference). Branch `develop/v1.4.0` (33 commits over `main`, cut from `release/v1.3.1` at `08cd4cf`, itself cut from tag `v1.3.0`). The 84 v1.0 controls, their identifiers and texts, the frozen v1.0 schemas, the licence and the founder attribution are unchanged. The frozen Smart UI package (267 files) is unchanged.

### What changes
- **Routing and governance.** Canonical applicability matrix (`spec/applicability-matrix.yaml`) and an additive profile layer: every control is reachable for high-assurance, profiles are monotonic (baseline ⊆ production ⊆ high-assurance) and never load controls unrelated to the task; new capabilities and intents for release, operations, exceptions and governance changes; VCGF-REL-001 in the minimum set. User-experience domain VCGF-UX-001..004 bound to profiles, matrix and Smart UI standards.
- **Acceptance and compliance.** 395 acceptance definitions for all 88 controls with configurable parameters (thresholds are documented defaults, SHOULD is never MUST); 20 definitions executed against the framework itself with recorded results; `vcgf.py compliance` verifies a project's recorded results and hash-pinned evidence (COMPLIANT / FAILED / NOT_TESTED per control). Definitions never count as passed.
- **Context efficiency.** Derived control cards with a fidelity validator (every normative sentence, reference and control identifier verbatim), multi-intent routing, delta loading with hash invalidation, registry cache, token accounting (bytes measured, tokens estimated, reference tokenizer optional and labelled), compact CLI output, Smart UI requirement cards, signal inference, package denylist. Measured: route union bytes −47.2% versus the Phase 1 tree with identical control selection; no provider token cost is claimed.
- **Enforcement.** Enforcement matrix with honest statuses; governance-file guard and pre-commit hook that unlock only with a covering approval record (never an environment flag); Claude Code settings example (configurable, not exercised on the live platform).
- **Supply chain and CI.** Exact pins validated, SHA-pinned actions, Dependabot, pip-audit, SBOM artifact, CodeQL; full test matrix on Ubuntu and Windows; release workflow drafts only for a signed tag.
- **Compatibility.** Budget comparison moved from bytes to estimated tokens with explicit `budget_unit`, disclosure of a changed outcome and a migration tool; v1.1 contracts extended only with optional fields; cumulative compatibility record `docs/quality/v1.4/baseline-compatibility-v1.4.json` with a reason for every changed v1.0 original (44 files).

### Test results (local, Windows 11 / Python 3.14; CI green on the PR head `b1291d7`: 22 checks on ubuntu-latest and windows-latest, Python 3.12 and 3.13)
| Check | Result |
|---|---|
| Release quality gate (21 validators, 4 generators `--check`) | PASS |
| pytest, no deselection | 430 passed, 0 failed, 7 skipped (symlink privilege / POSIX-only module) |
| Framework self-acceptance | 20 / 20 PASS, recorded in `docs/quality/v1.4/self-acceptance-results.json` |
| Contract and compatibility suite | 100 / 100 |
| Benchmark (16 scenarios, same inputs on three trees) | `evidence` in the audit workspace; union bytes 2,800,412 → 1,480,014 |

### Findings register (audit of v1.3.0, 50 findings)
FIXED_LOCAL 31 · PARTIALLY_FIXED_LOCAL 13 · OPEN (inside the frozen Smart UI package) 4 · OPEN_EXTERNAL_ACTION 2. Release-blocking: V13-001 (signed tag and assets), V13-002 (independent review, branch protection). V13-114 cleared by the green CI run on the PR head. Everything else is scheduled (package revision 1.0.x, target-project actions, later minor).

### Residual risks for the reviewer
1. CI ran green on the PR head after two fixes found by the first run (an unresolvable action pin and a pytest import in a unittest job); keep watching the re-runs of later commits.
2. The agent-hook guard is tamper-evident, not tamper-proof: without a host-held identity adapter an agent with file access could forge an approval record. The matrix rates it `configurable` and the product hook was not exercised live.
3. Budget semantics changed to estimated tokens by default; legacy tasks receive an explicit warning and a migration tool exists, but projects tuned to bytes should review their budgets.
4. Signal inference for Smart UI loads more standards where the route indicates login, payment or sensitive screens (+21% UI bytes versus Phase 3) — deliberate relevance over minimal size; reviewers may prefer the inference table narrowed.
5. Four findings inside the frozen Smart UI package (duplicate requirement text, a template failing its own schema, version fields, pack NOTICE copyright line) remain until a package revision; none of those files is ever served into context.
6. 375 acceptance definitions describe target projects and are not executed here by design.

### Review focus suggested
`spec/applicability-matrix.yaml` triggers (22 hand-assigned), `spec/acceptance/*.yaml` parameters and SHOULD wording, `runtime/router.py` profile layer and delta loading, `scripts/hooks/guard-governance-files.py`, `runtime/compliance.py`, `platforms/enforcement-matrix.yaml` statuses.

### Checklist for merging
- [ ] All workflows green on the PR head (Test suite ubuntu+windows, Supply chain, Release quality gate, validate-*)
- [ ] Non-author approval; branch protection active
- [ ] No change to the 84 v1.0 controls, frozen schemas, licence, attribution (compatibility suite confirms)
- [ ] Release checklist `docs/quality/v1.4/release-checklist-v1.4.0.md` steps B1–B5 done before merge; B6–B9 after

🤖 Generated with [Claude Code](https://claude.com/claude-code)
