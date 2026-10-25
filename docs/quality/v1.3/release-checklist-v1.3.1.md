<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.3.1 — Release checklist (release candidate)

**Execution status: none of the steps below has been executed.** This checklist was prepared locally on branch `release/v1.3.1`, a worktree cut from tag `v1.3.0` (commit `43c617d`). Preparing it does not modify tag `v1.3.0`, does not publish anything and does not sign anything. v1.3.0 remains the latest published release until every step is complete and recorded.

| # | Step | Required evidence | Status |
|---|------|-------------------|--------|
| 1 | Independent review of the `release/v1.3.1` pull request by a reviewer who authored none of its commits. | Approval recorded in the PR by the non-author reviewer, naming the reviewed merge commit. | NOT EXECUTED |
| 2 | CI green on the exact merge commit, including the test workflows (`validate-framework`, `validate-adapters`, `validate-schemas`, `validate-links`, `validate-runtime`, `validate-adaptive`, `release-quality-gate`). | Workflow run URLs for the merge commit, all successful. | NOT EXECUTED |
| 3 | Signed annotated tag `v1.3.1` created by a maintainer on the exact merge commit, using a key listed in `.github/release-keys`. | `git tag -v v1.3.1` output showing a good signature from a listed key. | NOT EXECUTED |
| 4 | Draft release produced by `.github/workflows/release.yml` for the verified tag, with source archives, `SHA256SUMS.txt` and `sbom.cdx.json` attached. | Workflow run URL and the draft release asset list. | NOT EXECUTED |
| 5 | Independent verification of the draft assets: checksums (`sha256sum -c SHA256SUMS.txt`), SBOM contents and tag signature, by someone other than the tag author. | Verification record (who, when, commands, results) attached to the PR or release discussion. | NOT EXECUTED |
| 6 | Publish the release. | Public release URL identifying the same commit as `main` and tag `v1.3.1`. | NOT EXECUTED |

## Rules that apply to every step

- No step may be marked done without the evidence named for it. A statement that a step "will be" or "should be" done is not evidence.
- Tag `v1.3.0` is immutable; nothing in this release moves, re-signs or deletes it.
- Publication requires a publication authorization that is independent of the authors of the change set.
- If any step fails, the candidate stays unpublished; fixes land as new commits and the checklist restarts from step 1.
- Target-product production admission is a separate decision and remains BLOCKED; this checklist covers the framework source distribution only.

See [release-notes-v1.3.1.md](release-notes-v1.3.1.md) for what the candidate contains and how to verify it once published.
