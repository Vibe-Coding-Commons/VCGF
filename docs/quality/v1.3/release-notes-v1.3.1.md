<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.3.1 — Integrity and governance hardening

**Status:** Release candidate — prepared locally, not published, not signed, not independently reviewed
**Candidate date:** 2026-10-24
**Release type:** Patch release (integrity and governance hardening; no new controls, no contract or schema changes)
**Base:** tag `v1.3.0` (commit `43c617d`) — the latest published release; this candidate does not modify it
**License:** Apache-2.0
**Founder & Maintainer:** Eng. Hamada Sami

## العربية — حالة الإصدار وما الذي تغيّر

**الحالة:** مرشح إصدار أُعدّ محليًا على فرع `release/v1.3.1` المتفرع من Tag `v1.3.0`. لم يُنشر، ولم يُوقَّع، ولم يُراجَع من طرف مستقل. يبقى v1.3.0 هو آخر إصدار منشور، ويبقى اعتماد الإنتاج (Production Admission) محجوبًا (BLOCKED).

هذا إصدار تصحيحي يعالج نتائج التدقيق المؤسسي لـ v1.3.0 دون إضافة Controls جديدة أو تغيير أي عقد (Contract) أو Schema. جميع Control IDs والـProfiles والترخيص وحقوق المؤسس محفوظة دون تغيير.

ما الذي تغيّر:

- **تسلسل التعليمات (Instruction hierarchy):** أُضيف بند صريح إلى جميع ملفات الدخول القديمة الدائمة التفعيل (always-on entry files) يؤكد أن محتوى المستودع أو الأدوات أو المحتوى المُولَّد لا يتجاوز سلطة النظام المضيف والمستخدم، ويفرضه `scripts/validate-adapters.py`.
- **ضوابط وكيل التطوير غير مشروطة:** لم يعد Task Router يُسقط VCGF-AI-002 وVCGF-AI-004 وVCGF-AI-006 وVCGF-AI-008 وVCGF-AI-009 بناءً على أعلام السياق (context flags).
- **سلامة حزمة Smart UI:** مدقق جديد `scripts/validate-package-integrity.py` يتحقق حتميًا من `SHA256SUMS.txt` و`manifest.json` المجمّدين داخل بوابة الإصدار وفي CI.
- **اتساق هوية الإصدار:** توحيد الإصدار في `runtime/bootstrap.md` وأدلة المنصات السبعة و`VCGF-MANIFEST.yaml` (المحوّلات المدعومة والمرشحة وإصدارات Schemas للعقود) مع توسيع `scripts/validate-version.py` لفرض ذلك.
- **المولّدات والمدققات للقراءة فقط:** أوضاع `--check` بدل إعادة الكتابة الصامتة، مع فرض UTF-8 وLF في كل كتابة.
- **حماية CI والنشر:** صلاحيات بأقل امتياز وتثبيت Actions بـSHA، وسير عمل إصدار يُعدّ مسودة إصدار فقط لـTag موقّع يمكن التحقق منه، مع أرشيفات المصدر و`SHA256SUMS.txt` وSBOM بصيغة CycloneDX؛ ولا ينشر تلقائيًا.
- **حالة طبقة Smart UI:** تغيّرت إلى `integration-candidate` في `packs/ux/catalog.yaml`؛ سيناريوهات القبول التشغيلي ما تزال `not_run`.

## English — Release status and what changed

**Status:** release candidate prepared locally on branch `release/v1.3.1`, cut from tag `v1.3.0`. It is not published, not signed and not independently reviewed. v1.3.0 remains the latest published release and production admission remains BLOCKED.

This is a patch release addressing the enterprise audit findings for v1.3.0. It adds no controls and changes no contract or schema. All Control IDs, Profiles, licensing and founder attribution are preserved unchanged.

What changed:

- **Instruction hierarchy:** an explicit clause added to every legacy always-on entry file states that repository, tool or generated content never overrides the host system and user authority chain; `scripts/validate-adapters.py` enforces its presence.
- **Unconditional development-agent safeguards:** the Task Router no longer drops VCGF-AI-002, VCGF-AI-004, VCGF-AI-006, VCGF-AI-008 or VCGF-AI-009 based on context flags.
- **Smart UI package integrity:** new `scripts/validate-package-integrity.py` deterministically verifies the frozen `SHA256SUMS.txt` and `manifest.json` in the release gate and in CI.
- **Version identity:** `runtime/bootstrap.md`, the seven platform guides and `VCGF-MANIFEST.yaml` (supported and candidate adapters, contract schema versions) now agree with `VERSION`; an extended `scripts/validate-version.py` enforces it.
- **Read-only, portable generators and validators:** `--check` modes instead of silent rewrites; UTF-8 and LF enforced on every write.
- **CI and release protection:** least-privilege `permissions`, SHA-pinned actions, and a release workflow that only drafts a release for a verifiable signed tag with source archives, `SHA256SUMS.txt` and a CycloneDX SBOM; nothing is published automatically.
- **Smart UI layer status:** aligned to `integration-candidate` in `packs/ux/catalog.yaml`; runtime acceptance scenarios remain `not_run`.

Full entry: [CHANGELOG.md](../../../CHANGELOG.md).

## Verification boundary / حدود التحقق

- Repository-native validators and targeted tests were run locally on the candidate working tree. They validate the framework source distribution only.
- Independent review by a non-author has **not** been performed. Nothing in this document counts as that review.
- No tag `v1.3.1` exists; no signature exists; no release assets exist. Any claim that v1.3.1 is signed or published is false until the steps in [release-checklist-v1.3.1.md](release-checklist-v1.3.1.md) are executed and recorded.
- Smart UI runtime acceptance scenarios are `not_run`; the layer ships as a selectively loadable specification candidate (layer v1.0.0).
- Target-application acceptance, trusted-host enforcement, provider integrations, independent attestation and the cumulative production gates remain separate. **Production admission remains BLOCKED.**

## How to verify once published / كيفية التحقق بعد النشر

1. **Signed tag:** `git fetch --tags && git tag -v v1.3.1` must report a good signature from a maintainer key listed in `.github/release-keys`, and the tagged commit must equal the `main` merge commit named in the release.
2. **Checksums:** download the release assets, then run `sha256sum -c SHA256SUMS.txt` (or `Get-FileHash` on Windows) against the source archives; every line must report `OK`.
3. **SBOM:** `sbom.cdx.json` must be a CycloneDX document whose component version is `1.3.1` and whose listed files match the archive contents.
4. **Repository identity:** inside the archive, `VERSION`, `VCGF-MANIFEST.yaml`, `CITATION.cff`, `spec/control-catalog.yaml` and the first `CHANGELOG.md` heading must all state `1.3.1`; `python scripts/validate-version.py` must print `PASS validate-version`.
5. **Smart UI package:** `python scripts/validate-package-integrity.py` must pass against the frozen `packs/ux/smart-ui/SHA256SUMS.txt`.

Until these checks succeed on published assets, treat v1.3.1 as an unreleased local candidate.
