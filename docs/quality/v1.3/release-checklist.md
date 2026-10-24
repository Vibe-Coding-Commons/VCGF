<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.3.0 — Official release checklist

1. Confirm repository is `Vibe-Coding-Commons/VCGF` and `main` is exactly the expected v1.2.0 baseline or review drift explicitly.
2. Create `release/v1.3.0` from the approved baseline.
3. Run `merge-ready/apply_vcgf_1_3_smart_ui.py <repo>` with no baseline bypass.
4. Review `git diff --check` and all changed files.
5. Run the repository-native `python scripts/release-quality-gate.py`.
6. Run Smart UI package validation and `tests/adaptive/test_smart_ui_pack.py`.
7. Run `finalize_v1_3_0.py <repo>`; it refuses to bump the version unless the pre-release gate passes.
8. Review generated VERSION / Manifest / Citation / Control Catalog / File Manifest / Repository Tree changes.
9. Run the final repository-native release quality gate again on VERSION=1.3.0.
10. Commit the release candidate and push the release branch.
11. Open/merge a reviewed PR into `main` and confirm CI on the exact merge commit.
12. Create signed/annotated tag `v1.3.0` on the exact approved `main` commit.
13. Publish GitHub Release using `RELEASE-NOTES-v1.3.0.md`.
14. Verify GitHub source archives/checksums and that `main`, tag and release all identify the same commit.
15. Keep target-product Production Admission separate; do not mark unexecuted evidence PASS.
