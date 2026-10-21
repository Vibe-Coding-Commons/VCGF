<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF quality evaluation and local integration review

Review date: 2026-10-21. Decision: **BLOCKED for official release**. Deliverable: a tested local integration candidate and guarded change set, not a remote merge.

## Executive assessment

VCGF has an explicit vendor-neutral policy architecture, immutable control identifiers, separate assurance Profiles, attribution, contribution/security documents and evidence-oriented runtime boundaries. These are observable organizational strengths, not proof of successful operation in every target application.

The Engineering and UX prototypes were moved into `runtime/adaptive/`, connected to the actual VCGF CLI and canonical loader, hardened at input/source boundaries, and provided with a cumulative release evidence evaluator. These are executable local changes. Branch creation through the connected GitHub integration was denied with HTTP 403. No remote branch, PR, merge, deployment or published release was produced.

Production acceptance is blocked by missing full-checkout regression, unexecuted legacy-router integration, real Laravel/React/Vue application tests and outstanding v1.1 provider/host/platform acceptance. Local green tests cannot waive those requirements.

## Evidence scope

The source baseline is commit `419d8331e7b78c96b946d5815fbe886068dabfe5`. Current Git tree hashes were matched for canonical controls, Profiles, legal files, checklists, playbooks and assets. Existing changed files were matched individually against current Git blob hashes, including both READMEs and CHANGELOG. Historical archive content was reused only when its hash matched current repository content. The testing checkout is deliberately labelled **partial**, not a complete repository.

See [baseline evidence](evidence/baseline-verification.json) and [environment details](environment-and-limitations.json). The proposal does not overwrite v1.1 with v1.0. VERSION, all 84 existing control definitions, Profile membership and legal attribution are unchanged.

## Findings and corrective actions

| Finding | Priority | Evidence and action | Status |
|---|---|---|---|
| F-001: conflicting duplicate loader digests | P1 | Reproduced on the actual old loader; the second conflicting digest was ignored. Added an explicit rejection while retaining identical-record deduplication | Fixed locally; full legacy suite remains required |
| F-002: asserted sources are not byte-verified evidence | P1 | Coordinator now verifies explicit local source hashes, freshness, duplicate consistency and a second snapshot read | Locally tested; interpretation truth still requires review |
| F-003: density overrides workflow semantics | P1 | Restricted workbench override to browsing, preserving form, approval, monitoring and kiosk semantics | Locally tested |
| F-004: category-only school selection is insufficient | P1 | Added explicit goal outcomes/weights, task-frequency and audience contributions with deterministic ranking | Locally tested; no autonomous NLP claim |
| F-005: unknown and contradictory facts | P1 | Block necessary unresolved architecture facts and contradictory risk declarations | Locally tested |
| F-006: unsafe or excessive input | P1 | Bounded JSON, duplicate-key/non-finite rejection, offline schemas, safe explicit local reads, symlink/path restrictions | Locally tested on Linux; cross-OS acceptance pending |
| F-007: green evidence cannot authenticate itself | P1 | Candidate/policy/expiry/scope/artifact binding plus mandatory trusted-host callback across 21 cumulative gates | Algorithm tested; actual host authentication unavailable |
| F-008: explicit script direction | P2 | Script tags take precedence over language defaults; unsupported direction remains unresolved | Locally tested |
| F-009: unsupported device claims | P2 | Per-workflow device applicability, wide-screen context and explicit kiosk outcome | Locally tested |
| F-010: focus/disclosure loss in static demo | P2 | Retain action focus and expanded details after rendering; announce changes through a live status region | Chromium reference checks passed |
| F-011: calendar changes on language switch | P2 | Keep a documented Gregorian calendar in this example only; retain per-project calendar choice | Chromium reference checks passed |
| F-012: repeated policy parsing and shared mutation | P2 | Content-keyed caches invalidate on edits; mutable catalog values are returned as copies | Locally tested and benchmarked |
| F-013: repository write unavailable | P0 acceptance | GitHub create_branch returned 403; no workaround bypassed permissions | Blocked; owner action required |
| F-014: incomplete target and inherited acceptance | P0 acceptance | No full checkout, actual applications, provider environments or trusted-host integration | Explicitly blocked, not silently deferred |

P0 denotes a release blocker, not a claim that a critical exploitable production vulnerability was discovered. No CVE or exploitation claim is made for the duplicate-record consistency defect.

## Tests and performance

The original RFC prototype ran 71 passing unit tests before modification. These are not official v1.1 tests and are not added to candidate results to inflate totals.

The candidate recorded **154 passing automated tests**, covering both engines, coordinator, invalid data, release admission rules, concurrency and targeted tests of the actual original loader. Combined statement/branch coverage was approximately **86% for `runtime.adaptive` only**. The release evaluator's branches were exercised with synthetic callbacks; that does not authenticate a real release authority.

The static reference recorded **171 Chromium assertions** across Arabic/English at 320, 390, 768, 1280, 1440 and 1920 CSS pixels. Checks covered direction, visible layouts, data access, search/empty states, keyboard disclosure, focus retention, status announcements, calendar consistency, identifier isolation and no external requests. Some checks used 200% text sizing. This is neither physical-device validation nor whole-WCAG conformance nor browser-zoom certification. Other browser engines and manual assistive technology remain open.

A 100-iteration synthetic microbenchmark recorded warm p50 **8.728 ms**, p95 **12.243 ms**, maximum **16.016 ms** and cold-call **129.38 ms**. A 32-request/four-thread exercise was deterministic without blocked results. Peak traced Python allocation for one warm call was **1,184,491 bytes**, not full process RSS. These observations are tied to the supplied environment and are not production SLOs or before/after performance improvements.

The initial test run exposed an imprecise exception-message assertion. The boundary was normalized to a structured input error and tests were rerun; initial failure evidence is retained rather than presented as success.

## Robustness and security boundaries

Invalid or stale observations, conflicting projects, insufficient budget and unsafe paths block planning. Required control identifiers are retained even when context cannot be loaded. Quiet presentation does not suppress blockers. No command from a supplied JSON record is executed.

Reads are explicit and bounded to 1 MiB; JSON is bounded to depth 32 and 20,000 nodes. Common sensitive paths are rejected, but this is not comprehensive secret detection. POSIX descriptor-based reads reject symlinks beneath the project root. Other operating systems and concurrent file replacement require separate host-owned snapshot locking and validation. Hash equality verifies bytes, not the correctness of an AI or human interpretation.

The v1.1 schema semantics remain unchanged. Two additive capability definitions and a `design-review` intent bridge to new versioned contracts. The actual optional legacy-router execution path was not exercised because required runtime files/schemas were not available in the partial local source set. Its absence is a blocker, not an implicit success or equivalent mock.

## Organizational and leadership-control assessment

The repository documents maintainer identity, ownership, license, immutable controls, contributions, security, versioning and evidence. Those establish a useful organizational baseline. Branch protection, enforced independent review, remote checks and authenticated approval settings were not verified. The protection read also returned 403; lack of access is not proof of missing protection.

A least-privilege, pinned-action and time-bounded CI definition was added locally. It has not run remotely and does not alter repository protection settings. The scope register retains all 51 Engineering/UX RFC tasks and marks remaining work explicitly. There is insufficient evidence to evaluate individual leadership competence or team delivery metrics such as change-failure rate or review lead time.

## Prioritized completion plan

Effort is indicative engineering time after access and suitable sandboxes become available, not a delivery promise or background schedule. Independent tracks can run in parallel.

| Work | Priority | Owner | Indicative effort | Closure evidence |
|---|---|---|---|---|
| Restore scoped connector write and inspect protection | P0 | Repository owner | 0.5-1 day | Authorized branch/PR plus settings evidence |
| Apply candidate, regenerate derived artifacts and run full regression | P0 | Maintainer + QA | 1-2 days | Old and new checks pass; protected content unchanged |
| Exercise real v1.1 task/context routing | P0 | Runtime engineer | 0.5-1 day | Correct capabilities and retained risk/context blockers |
| Real Laravel + React and Laravel + Vue projects | P0 | Application engineers + QA | 2-4 days | Pinned environments, build/API/auth/transaction/UI evidence |
| Browser/device/manual accessibility matrix | P0 | QA + accessibility specialist | 2-3 days | No unresolved critical task barriers in supported AR/EN journeys |
| User tasks and usability outcomes | P1 | Product owner + UX | 1-3 days | Approved top-three tasks per role and representative-user findings |
| Font license, glyphs and delivery performance | P1 | Frontend + UX | 1-2 days | Licensed project-owned assets and measured fallback/loading behavior |
| Outstanding v1.1 provider/backup/host/platform acceptance | P0 | Integrations + security + owner | 3-7 days after sandbox access | Original accepted scenarios completed without scope reduction |
| Dependency/SBOM/recovery/release review | P0 | Security + release owner | 1-2 days | Current reports, tested recovery and authenticated approval |

These durations should not be mechanically summed into a release date. Re-estimate after the first complete regression run.

## Acceptance metrics and standards

Require zero failed mandatory tests, explicit treatment of skipped/not-run checks, all applicable required controls, negative tests at trust boundaries and no loss of essential task data across supported layouts. Define application-specific latency and asset budgets; do not copy the reference microbenchmark into a product SLO.

An 85% combined coverage regression floor for the new layer is a proposed project threshold, supplemented by behavioral tests of critical branches. It is not mandated by NIST or W3C. Real WCAG 2.2 assessment requires the applicable criteria and suitable manual/automated evidence, not an aggregate tool score.

References: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use), [NIST SSDF](https://csrc.nist.gov/Projects/ssdf). These informed recommendations; no external certification or full standards-mapping claim is made.

## Deliverables

[Arabic report](evaluation-ar.md), [integration log](integration-log.md), [release procedure](release-gates.md), [scope register](scope-register.json), [executive summary](executive-summary.md), updated root READMEs and CHANGELOG, executable candidate modules, tests, browser reference and a guarded patch package.
