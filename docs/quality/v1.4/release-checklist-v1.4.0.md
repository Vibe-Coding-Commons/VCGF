<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->
# VCGF v1.4.0 — Release checklist (released 2026-10-27: signed tag `v1.4.0` on `377e3eb`)

Section A was verified locally on the candidate tree before the pull request. Section B records what actually happened on GitHub, step by step, including the steps that were skipped by owner decision. Status values: DONE (verified; evidence named), PARTIAL (part of the step verified), NOT DONE (skipped; the finding it maps to stays open), EXTERNAL (still requires an action outside the repository), scheduled. A DONE here is a factual record, not an endorsement: steps B5 and the fingerprint confirmation in B7 were not performed, and the published release has had no independent non-author review.

## A. Local prerequisites (verified on the candidate tree)
| # | Check | Status | Evidence |
|---|---|---|---|
| A1 | VERSION 1.4.0, `release_status: release-candidate`, badges, CITATION, CHANGELOG heading, release notes present | DONE | `scripts/validate-version.py` PASS |
| A2 | Read-only release quality gate (21 validators, 4 generators in `--check`) | DONE | `scripts/release-quality-gate.py` PASS |
| A3 | Full test suite without deselection | DONE (Windows 11 / Python 3.14) | 430 passed, 0 failed, 7 skipped |
| A4 | Framework self-acceptance recorded and checked | DONE | `scripts/run-self-acceptance.py --check` 20/20 |
| A5 | Cumulative compatibility record v1.4 with a reason for every changed v1.0 original; frozen v1.0 schemas byte-identical; 84 controls unchanged | DONE | `tests/contracts/test_phase1.py` 100/100 |
| A6 | Frozen Smart UI package integrity (267 files) | DONE | `scripts/validate-package-integrity.py` PASS |
| A7 | Dependency pins exact, actions SHA-pinned, Dependabot present | DONE | `scripts/validate-dependencies.py` PASS |
| A8 | Local validation record bound to the commit and environment | DONE | `docs/quality/v1.4/release-validation-local.json` |
| A9 | Control cards semantically complete; enforcement matrix honest; operational files traced to controls | DONE | `validate-control-cards`, `validate-enforcement`, `validate-operational-map` PASS |

## B. External actions, in order
| # | Action | Owner | Status | Done when |
|---|---|---|---|---|
| B1 | Push `develop/v1.4.0` and open the pull request to `main` using `docs/quality/v1.4/PULL-REQUEST-v1.4.0.md` | maintainer with push rights | DONE (2026-10-26, PR #4) | PR exists; no self-merge |
| B2 | First real CI run: `Test suite` (ubuntu-latest, windows-latest; Python 3.12, 3.13), `Supply chain` (pins, pip-audit --strict, SBOM artifact, CodeQL), `Release quality gate`, `validate-*` workflows | GitHub Actions | DONE at `b1291d7` (22 checks green on ubuntu and windows after two fixes: unresolvable checkout pin, pytest-free skip) | every workflow green on the PR head; fix and re-run on failure |
| B3 | Review the SBOM artifact and the pip-audit result; record the dependency licence inventory for the release | maintainer | PARTIAL (2026-10-27: published `sbom.cdx.json` inspected, CycloneDX 1.5, component VCGF 1.4.0, 6 components; `pip-audit --strict` green in the Supply chain workflow on `377e3eb`; dependency licence inventory not recorded) | artefacts attached to the PR |
| B4 | Exercise the Claude Code hook example (`platforms/claude/hooks/settings.example.json`) against the live product: blocked edit of a canonical file, blocked destructive command, allowed edit with a covering approval record; then raise the adapter rating from `configurable` only with that evidence | maintainer with Claude Code | EXTERNAL | recorded transcript or screenshots; matrix updated by a reviewed change |
| B5 | Independent human review by a non-author (controls/, runtime/, spec/, packs/, .github/) and branch protection requiring at least one approval; add a second maintainer or external reviewer to CODEOWNERS/SECURITY.md | repository owner | NOT DONE (waived by owner decision on 2026-10-26; PR #4 has no review; no branch protection observed; audit finding V13-002 stays OPEN_EXTERNAL_ACTION) | approval recorded on the PR; protection rule visible |
| B6 | Merge to `main` only after B2 and B5 | reviewer | DONE (2026-10-26, merge commit `82bd70f`, after B2 but without B5, by owner decision) | merge commit on main |
| B7 | Enrol at least one release signer public key under `.github/release-keys/` by a reviewed change | release maintainer | DONE (2026-10-26, commit `73b41c3`: `hamada-sami.asc`, RSA-3072, fingerprint `34F67848A2007128D936894E0C5CE633105C6627`, public key only); pushed directly to `main`, so the independent fingerprint confirmation required by `.github/release-keys/README.md` was NOT DONE | `*.asc` present on main |
| B8 | Create the annotated, signed tag `v1.4.0` (GPG or Sigstore gitsign) | release maintainer | DONE (2026-10-27, GPG-signed tag on `377e3eb`, twelve documentation commits after the merge commit; `git tag -v` succeeds in an isolated keyring holding only the enrolled key; every check run on the tagged commit succeeded before and after the tag push) | `git tag -v v1.4.0` succeeds with an enrolled key |
| B9 | Let `release.yml` draft the release (verifies signature, VERSION, at least 7 successful checks, gate, release notes) and attach `SHA256SUMS.txt`, the source archives and the CycloneDX SBOM; publish only after a human reviews the draft | release maintainer | DONE with a deviation (2026-10-27): workflow run 40456591222 (manual dispatch) passed every verification step and drafted the release with the four assets; the draft was then published by workflow run 40456636356, started by a one-time `push` trigger the maintainer added to `release.yml` (commit `dafdafb`) and removed again (`2d04036`), without a human review of the draft. Assets verified after publication, see section D | published release with assets and checksums |
| B10 | Post-release: Smart UI package revision 1.0.x for the four open package findings (V13-010, 017, 018, 019); hash-pinned lock file; coverage job across runtime/ and scripts/; CI job that downloads the published archive and verifies it against `SHA256SUMS.txt`; per-file hashes in `FILE-MANIFEST.md`; independent fingerprint confirmation of the enrolled signer key | maintainers | scheduled | tracked as issues |

## D. Publication record (2026-10-27)
Release: <https://github.com/Vibe-Coding-Commons/VCGF/releases/tag/v1.4.0> (not a draft, not a pre-release, marked latest). Tag object `8039695433fab2337080606909df14c6df71855f` → commit `377e3eb382f7c89fea4a036c297ace83599bd316`. `VERSION` 1.4.0; `VCGF-MANIFEST.yaml` `release_status: release-candidate` at the tag (accepted by the workflow, which allows stable or release-candidate).

| Asset | SHA-256 (from `SHA256SUMS.txt`, matches the workflow log and an independent download) | Verification |
|---|---|---|
| `VCGF-v1.4.0.tar.gz` | `6e8e5fb08325e088fc7c13406debd442184fb4f3bda19c168755a0b907f79b48` | 1,132 files; every file byte-identical to the tag tree; nothing missing or extra |
| `VCGF-v1.4.0.zip` | `d6dd2ddded02cd50c670d1d218e430560e4d6a23eb197b527d25defb84fc3421` | 1,132 files; every file byte-identical to the tag tree; nothing missing or extra |
| `sbom.cdx.json` | `2c6e4a93031d7118ecbbcd4defeb9da98d4d5c8d87ac824a52aa65659ba4811a` | CycloneDX 1.5; component VCGF 1.4.0; 6 components |
| `SHA256SUMS.txt` | — | three entries, all matching |

Known deviations from this checklist, recorded rather than hidden: no non-author review (B5); signer key enrolled without independent fingerprint confirmation (B7); publication automated by a one-time trigger instead of a human review of the draft (B9); the published release body was edited after drafting (language switch line, publication status, absolute links) and therefore differs from `docs/quality/v1.4/release-notes-v1.4.0.md` at the tag in wording, not in technical content. The audit workspace keeps the raw evidence (`evidence/raw/final/release-publication-v1.4.0.json`).

## C. Rules that apply to every step
- Prompt text enforces nothing; only validators, CI, hooks exercised on the platform and human review count as evidence.
- A local gate pass is not a CI pass; a local hook is not branch protection; an AI review is not an independent human review.
- Acceptance definitions are not executed tests; only the 20 framework self-checks are executed here.
- No step may modify the 84 v1.0 controls, the frozen v1.0 schemas, the licence or the attribution.
