<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->
# VCGF v1.4.0 — Release checklist (release candidate at `develop/v1.4.0`)

Local preparation is complete; every step below that is marked **EXTERNAL** needs an authority or an environment this repository does not hold. Nothing here is a release decision. Status values: DONE (verified locally), PREPARED (artefact exists, not yet exercised), EXTERNAL (requires an action outside this session), NOT_TESTED.

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
| B3 | Review the SBOM artifact and the pip-audit result; record the dependency licence inventory for the release | maintainer | EXTERNAL | artefacts attached to the PR |
| B4 | Exercise the Claude Code hook example (`platforms/claude/hooks/settings.example.json`) against the live product: blocked edit of a canonical file, blocked destructive command, allowed edit with a covering approval record; then raise the adapter rating from `configurable` only with that evidence | maintainer with Claude Code | EXTERNAL | recorded transcript or screenshots; matrix updated by a reviewed change |
| B5 | Independent human review by a non-author (controls/, runtime/, spec/, packs/, .github/) and branch protection requiring at least one approval; add a second maintainer or external reviewer to CODEOWNERS/SECURITY.md | repository owner | EXTERNAL | approval recorded on the PR; protection rule visible |
| B6 | Merge to `main` only after B2 and B5 | reviewer | EXTERNAL | merge commit on main |
| B7 | Enrol at least one release signer public key under `.github/release-keys/` (currently none) by a reviewed change | release maintainer | EXTERNAL | `*.asc` present on main |
| B8 | Create the annotated, signed tag `v1.4.0` on the merge commit (GPG or Sigstore gitsign) | release maintainer | EXTERNAL | `git tag -v v1.4.0` succeeds with an enrolled key |
| B9 | Let `release.yml` draft the release (verifies signature, VERSION, at least 7 successful checks, gate, release notes) and attach `SHA256SUMS.txt`, the source archives and the CycloneDX SBOM; publish only after a human reviews the draft | release maintainer | EXTERNAL | published release with assets and checksums |
| B10 | Post-release: Smart UI package revision 1.0.x for the four open package findings (V13-010, 017, 018, 019); hash-pinned lock file; coverage job across runtime/ and scripts/ | maintainers | scheduled | tracked as issues |

## C. Rules that apply to every step
- Prompt text enforces nothing; only validators, CI, hooks exercised on the platform and human review count as evidence.
- A local gate pass is not a CI pass; a local hook is not branch protection; an AI review is not an independent human review.
- Acceptance definitions are not executed tests; only the 20 framework self-checks are executed here.
- No step may modify the 84 v1.0 controls, the frozen v1.0 schemas, the licence or the attribution.
