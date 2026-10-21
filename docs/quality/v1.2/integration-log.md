<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# سجل الدمج الفعلي وحدوده / Integration execution log

## 1. المصدر ومحاولة الفرع / Source and branch attempt

- Repository: `Vibe-Coding-Commons/VCGF`.
- Base commit: `419d8331e7b78c96b946d5815fbe886068dabfe5`.
- Base root tree: `225378370c6e368359cf0d07a542714f71def4a1`.
- Intended branch: `vcgf/v1.2-engine-integration-20261021`.
- GitHub result: **HTTP 403 — Resource not accessible by integration**.
- Remote branch/commit/PR/merge/release: **none created**.
- Branch protection: read rejected with 403; **settings unverified**, not classified as absent.

تم احترام فشل الصلاحيات ولم يُستخدم مسار بديل للالتفاف عليها. أثبتت القراءة النسخة الحالية؛ لم تثبت صلاحية الكتابة الفعلية. / The permission denial was respected; repository metadata did not establish effective connector write access.

## 2. ما دُمج محليًا / What was integrated locally

| نقطة الدمج / Integration point | التغيير / Change | التحقق / Verification |
|---|---|---|
| `scripts/vcgf.py` | إضافة توجيه مبكر لأربعة أوامر جديدة؛ نقل تحميل وحدات الأوامر القديمة إلى مسارها فقط / Add four opt-in commands without rewriting old handlers | استدعاء CLI فعلي في subprocess / Actual new-command subprocess tests |
| `runtime/adaptive/` | محركا الهندسة وUX، منسق، قراءة وعقود وتقييم قبول / Both engines, coordinator, bounded validation and release admission | اختبارات وحدات وتكامل محلية / Local unit/integration tests |
| `runtime/loader.py` | رفض البصمات المتعارضة للمسار المكرر / Reject conflicting duplicate hashes | إعادة إنتاج العيب ثم اختبارات انحدار محددة / Reproduced baseline and targeted regression |
| `capabilities/adaptive-*.yaml` | قدرتان إضافيتان تربطان الضوابط القائمة / Two additive capabilities | فحص البنية والمراجع المحلية؛ الموجّه الكامل لم ينفذ / Local structure/reference checks; full routing pending |
| `runtime/routing-policy.yaml` | تصنيف `design-review` دون حذف التصنيفات القائمة / Add intent without removing old ones | مقارنة الإضافات مع المصدر الموثق / Additive comparison against verified source |
| `runtime/pack-map.yaml` | تحميل حزمتين مختصرتين / Map compact packs | تشغيل المحمّل الأصلي مع 14 ضابطًا وملفي متطلبات / Real loader with 14 controls and two packs |
| `schemas/v1.2.0/` | خمسة عقود مستقلة / Five opt-in schemas | مدخلات صالحة وسلبية / Valid and invalid inputs |
| `examples/adaptive/` | مدخلات واضحة ومثال مزدوج بمصدر محلي وواجهة HTML / Explicit fixtures, paired source and HTML reference | تشغيل المنسق والمتصفح / Coordinator and Chromium |
| README/CHANGELOG/docs | توثيق ثنائي اللغة وحفظ حالة الإصدار / Bilingual status, usage and acceptance | مطابقة نصوص المصدر قبل التعديل، وفحص الملفات الجديدة / Baseline hashes and new-file checks |
| `.github/workflows/validate-adaptive.yml` | مصفوفة Python/Linux/Windows وانحدار قديم بإجراءات مثبتة / Pinned, least-privilege candidate CI | تعريف محلي؛ **لم ينفذ على GitHub** / Defined locally; not run remotely |

## 3. الاختبارات المنفذة / Executed checks

1. تشغيل اختبارات النموذج الأصلي: 71 ناجحة؛ معزولة عن نتائج VCGF الرسمي. / Original prototype: 71 passing tests, not official VCGF regression.
2. اختبارات المرشح: 154 ناجحة في التشغيل المسجل. / Candidate: 154 passed in the recorded run.
3. التغطية: نحو 86% ضمن `runtime.adaptive` فقط، لا كامل المستودع. / Approximately 86% combined statement/branch coverage for the new runtime layer only.
4. المتصفح: 171 تحققًا في Chromium على HTML اصطناعي؛ عرض AR/EN وستة أحجام، وحقول ومحتوى مختلط وتركيز وتفاصيل وتكبير نص. / 171 scoped static-reference Chromium assertions.
5. القياس: 100 تكرار و32 طلبًا بأربعة خيوط؛ نتائج وأزمنة خام محفوظة. / 100 warm iterations and 32 four-thread requests, with raw observations.

المخرجات الخام في مجلد [evidence](evidence/). يحتوي سجل التشغيل الأول على فشل تحقق استثناء أثناء بناء الاختبار؛ الإصلاح والتشغيل اللاحق محفوظان. لم تُحوّل أي نتيجة غير منفذة إلى نجاح. / Raw logs retain the initial exception-assertion failure and subsequent corrected run.

## 4. ما لم يُختبر / Not exercised

مسار `design-plan --task --context` يحتوي استدعاء حقيقيًا إلى `runtime.router.route`، وليس نسخة محاكاة منه، لكن ملفات Runtime وعقود v1.1 الكاملة لم تتوافر محليًا لتشغيله. اختُبر رفض تركيبة المدخلات الخاطئة، أما المرور الصحيح والمخاطر عبر الموجّه القائم فما زالا **unverified**.

The optional task/context path calls the real v1.1 router. A complete runtime and schemas were not locally available, so successful routing and retained risk gates must still be exercised on the full checkout. No mocked result is reported as equivalent integration evidence.

كذلك لم تنفذ الاختبارات القديمة كاملة، أو تطبيقات Laravel/React/Vue، أو مزودات البريد والنسخ والمضيف والمنصات المخولة. هذه قيود قبول معلنة وليست إلغاءً لمتطلبات المستخدم. / Full legacy, real target applications and inherited provider/host/platform acceptance remain open.

## 5. تطبيق الحزمة / Apply the change set

تتضمن الحزمة `candidate.patch` و`change-manifest.json` ومجلد `overlay/` والمثبّت `apply_candidate.py`. هي **حزمة تغييرات** وليست نسخة كاملة بديلة للمستودع.

The package is an overlay/patch against the pinned current commit, not a substitute repository. The guarded installer defaults to verification only:

```bash
python apply_candidate.py --repository /path/to/complete/VCGF
python apply_candidate.py --repository /path/to/complete/VCGF --apply
```

يتحقق المثبّت من HEAD ونظافة العمل وبصمات المصدر وحمولة التغيير، ومن أن الملفات الجديدة لا تتعارض مع ملفات موجودة، ثم يجري `git apply --check`. مع `--apply` ينشئ فرعًا محليًا جديدًا ويطبق التغيير. لا ينشئ Commit أو Push أو PR أو Release. لا تستخدم `--force` أو تغير معرّف الأساس لتجاوز اختلاف نسخة المستودع؛ أعد المراجعة على الأساس الجديد.

The installer checks HEAD, clean state, original/payload digests and path conflicts, then uses `git apply --check`. Apply mode creates a local branch and applies the patch. It does not commit, push, open a PR or release. If main has changed, reconcile against the new baseline rather than bypassing the guard.

## 6. أوامر النسخة الكاملة بعد التطبيق / Full-checkout follow-through

```bash
python -m pip install -r requirements-dev.txt -r requirements-quality.txt \
  -r examples/integrations/requirements.txt
python scripts/generate-runtime-registry.py
python scripts/generate-adapter-rules.py
python scripts/generate-repository-tree.py
python scripts/generate-file-manifest.py

git diff --stat
python scripts/release-quality-gate.py
python scripts/validate-runtime.py
python scripts/generate-runtime-registry.py --check
python scripts/generate-adapter-rules.py --check
python tests/contracts/test_phase1.py
python tests/scenarios/test_runtime.py
python tests/scenarios/test_gates.py
python tests/scenarios/test_adapters.py
python tests/scenarios/test_integrations.py
python -m coverage run --branch --source=runtime.adaptive -m pytest tests/adaptive -q
python -m coverage report
```

هذه أوامر متابعة على النسخة الكاملة، وليست سجلًا بأنها نُفذت كلها في هذه المراجعة. أي فشل توافق يعالج كتغيير مستقل قابل للمراجعة؛ لا تُمسح البصمات التاريخية أو تُستثنى ملفات محمية لتمرير الفاحص. / These are follow-through commands, not claims of execution here. Investigate compatibility failures without rewriting protected historical fixtures.

يلزم كذلك تشغيل السيناريو المزدوج مع سياق v1.1 صالح، ومصفوفة المشاريع الحقيقية، ثم PR ومراجعة مستقلة وبوابات القبول. لم يُنشأ رقم PR لأن العملية لم تحدث. / Real task/context routing, target matrices, reviewed PR and acceptance remain mandatory; no PR identifier was invented.

## 7. أثر التغيير والتراجع / Change impact and rollback

تبقى الوحدات الجديدة اختيارية، ولا تقوم بتعديل تطبيق العميل. يترك التغيير الضوابط وProfiles والحقوق وVERSION دون تعديل. تُراجع الملفات المشتقة بعد توليدها؛ التوليد ليس مصدر سياسات مستقلًا.

قبل اعتماد الفرع، يحتفظ المالك بنقطة الأساس وسجل التغييرات. يُراجع فرق الفرع ويستخدم تراجع Git عاديًا إذا لم يستوفِ القبول؛ لا تستخدم استبدالًا شاملًا لمجلد المستودع. لا توجد عملية قاعدة بيانات أو نشر إنتاجي ضمن هذه الحزمة تستدعي تنفيذ rollback تلقائي.

The extension is opt-in and does not modify target applications. Retain the baseline and review the branch diff. Use an ordinary reviewed Git revert when necessary, never wholesale replacement with the partial test checkout. No production database operation is included.

## 8. تغييرات قرار التنفيذ / Implementation decisions

- الأوامر المقترحة سابقًا توحدت إلى `advise-engineering` و`advise-ux` و`design-plan` و`release-readiness`؛ لا يوجد أمر قديم منشور أزيل. / New command names are explicit and additive.
- حقائق المشروع والجمهور والمهام تدخل كتصنيف قابل للمراجعة، لا كادعاء فهم لغوي ذاتي. / Inputs are reviewed classifications, not autonomous semantic understanding.
- الأمثلة والفحوص لا تؤهل مكتبة React أو Vue تلقائيًا. / Reference checks never certify a framework integration.
- جميع مهام ENG-B001..025 وUX-B001..026 محفوظة في [سجل النطاق](scope-register.json). / All 51 RFC tasks remain traceable.

**النتيجة: دمج محلي منفذ ومختبر ضمن نطاق محدد؛ دمج GitHub وقبول الإصدار الرسمي غير مكتملين. / Result: executed local integration within a bounded scope; GitHub merge and official release acceptance remain incomplete.**
