<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# إجراءات بوابات قبول الإصدار / Release acceptance procedure

**قبول الإنتاج: BLOCKED.** قرر المالك نشر إصدار عام من الشيفرة باسم v1.2.0 دون الادعاء باعتماد تطبيقات العملاء للإنتاج؛ تبقى البوابات الـ21 متطلبًا قائمًا. / **Production admission: BLOCKED.** The owner authorized public framework distribution as v1.2.0 without representing that 21 cumulative production gates passed.

## 0. قرار المالك بشأن الإصدار العام / Owner public distribution decision

يُسمح بتوزيع الشيفرة العامة وفق قرار المالك لعام 2026-10-21، مع الحفاظ على جميع بوابات قبول الإنتاج دون إغلاق صوري أو تنازل عن التزامات v1.1. لا يعني وصف النسخة بأنها رسمية أن التطبيقات والتكاملات في بيئات العملاء اجتازت تلك البوابات. / The owner authorized public versioned distribution; this is not technical production admission, does not waive v1.1 obligations, and does not relabel missing evidence as PASS. See [owner decision](public-release-decision.md).

## 1. الفصل بين أنواع النجاح / Separate types of success

| النوع / Type | ما يثبته / Meaning | ما لا يثبته / Not proof of |
|---|---|---|
| Schema valid | توافق بنية السجل / Structural validity | صحة البيانات أو هوية المراجع / Truth or reviewer identity |
| Unit/integration pass | نجاح سيناريوهات منفذة محددة / Executed scenario results | جميع البيئات أو التوافق الكامل / All environments or full conformance |
| Repository quality pass | اتساق ملفات وفحوص المستودع / Repository checks | قبول تطبيقات العملاء / Target-product acceptance |
| Release admission PASS | اكتمال الأدلة المطلوبة بعد مراجعة مضيف موثوق / Scoped authenticated evidence admission | إذن نشر ضمني أو تنفيذ نشر / Implicit deployment authority or actual publication |

## 2. عقد الأدلة / Evidence contract

العقد هو `schemas/v1.2.0/release-evidence.schema.json` والسياسة هي `packs/engineering/release-policy.json`. يلتزم السجل بما يلي:

1. `candidate_commit`: SHA كامل من 40 محرفًا، يطابق النسخة المراد اعتمادها. اسم الفرع غير كافٍ. / Exact 40-character candidate commit, never a mutable branch name.
2. `policy_sha256`: بصمة JSON المعيارية للسياسة الحالية. التعديل في المتطلبات يبطل الدليل السابق. / Canonical JSON digest of the required policy.
3. `created_at` و`valid_until`: تاريخان محددان بالمنطقة الزمنية؛ أقصى صلاحية سبعة أيام، ولا تُقبل أدلة مستقبلية أو منتهية. هذه مدة سياسة مقترحة للمشروع وليست قاعدة معيار عالمي. / Timezone-aware evidence window, at most seven days under this project policy.
4. `checks`: سجل واحد لكل بوابة، بالحالة والنطاق الصحيحين، ومرفقات محلية محددة وبصمات SHA-256 متطابقة. / One correctly scoped record per gate, with hash-matching artifacts.
5. مراجعة موثوقة: لا توجد قيمة JSON تستطيع المصادقة على صاحبها. يتحقق المضيف من الهوية والصلاحية والنطاق والإلغاء وحداثة التنفيذ. / No JSON field authenticates its own author; authority belongs to the trusted host.

يجب أن تكون ملفات السياسة والمراجع وقفل لقطة التنفيذ تحت إدارة المضيف، لا تحت تحكم مدخلات غير موثوقة. وظيفة Callback في اختبار وحدة ليست مواءمة هوية إنتاجية. ينبغي أن تمنع آلية المضيف إعادة التشغيل غير المخول وTOCTOU، وأن تربط نتيجة المراجعة بالنسخة والمرفقات وقت الاستخدام.

Policy, review authority and the execution snapshot must be host-controlled. Test callbacks are synthetic. The host must handle revocation, replay and concurrent replacement; the evaluator alone is not a universal tool broker.

## 3. البوابات التراكمية / Cumulative gates

| المعرّف / Gate | النطاق المطلوب / Scope | معيار الإغلاق والأدلة / Closure criteria |
|---|---|---|
| QG-BASELINE | full_repository | نسخة كاملة مثبتة الالتزام، بصمات الضوابط والحقوق محفوظة، وبيان التغييرات / Full checkout and protected-file evidence |
| QG-LEGACY | full_repository | نجاح جميع اختبارات وفاحصات v1.0/v1.1 المطلوبة، مع تفسير كل skip / All required legacy checks; explicit skips |
| QG-ADAPTIVE | full_repository | نجاح اختبارات المحركين والمنسق مع الموجّه القائم، ومدخلات سلبية، ومخرجات قابلة للتفسير / Both engines and real router integration |
| QG-PYTHON-MATRIX | full_repository | نجاح نسخ Python وأنظمة التشغيل المعلنة في الدعم، لا الاكتفاء بتعريف ملف CI / Executed supported runtime/OS matrix |
| QG-DEPENDENCIES | full_repository | تدقيق حديث للمباشر والانتقالي، ومراجعة التراخيص، وعدم بقاء نتيجة حرجة/عالية مؤثرة دون قرار موثق / Current vulnerability and license review |
| QG-SBOM | full_repository | قائمة مكونات وأقفال اعتمادية مرتبطة ببصمة النسخة / Candidate-bound dependency inventory and locks |
| QG-LARAVEL-REACT | target_project | تطبيق فعلي: إصدارات معلنة، build وAPI وتفويض ومعاملات وواجهات / Actual Laravel/React integration, not JSON fixtures |
| QG-LARAVEL-VUE | target_project | نفس المتطلبات على تطبيق Vue فعلي / Actual Laravel/Vue integration |
| QG-BROWSERS | target_project | مصفوفة المتصفحات والأجهزة واللغات المدعومة، وصفر عائق حرج يمنع المهمة / Supported browser/device/language journeys |
| QG-ACCESSIBILITY | manual_target_project | فحص يدوي وآلي للمعايير المنطبقة، ولوحة مفاتيح وقارئ شاشة وإعادة تدفق / Applicable WCAG evidence, keyboard and assistive technology |
| QG-USABILITY | manual_target_project | ثلاث مهام أساسية لكل دور ومعايير نجاح يقبلها المالك واختبار مستخدمين ممثلين / Approved top tasks and representative-user evidence |
| QG-PERFORMANCE | target_project | ميزانية زمن وأصول معتمدة للمشروع، وقياسات تحميل وبيانات واقعية / Project-approved latency/assets/load budgets |
| QG-FONTS | target_project | ترخيص ومحارف عربية/لاتينية وfallback وقياس التحميل؛ الأصول يحتفظ بها المشروع / Licensed project-owned fonts and glyph/loading checks |
| QG-M365 | authorized_sandbox | سيناريو OAuth وإرسال مخول فعلي حسب نطاق v1.1 / Authorized real v1.1 mail acceptance |
| QG-SQL-RESTORE | authorized_sandbox | استعادة PostgreSQL/MySQL واتساق البيانات والمرفقات وفحص التلاعب / Real SQL restore and attachment consistency |
| QG-PLATFORM-ADAPTERS | authorized_sandbox | أدلة المنصات الثماني المطلوبة؛ لا يساوي تطابق النص الإنفاذ الحي / Required live platform verification |
| QG-V11-SCOPE | full_repository | إغلاق النطاق الأصلي B001–B022 والحزم والالتزامات المسجلة دون حذف / Cumulative original scope without silent reduction |
| QG-HOST-TRUST | trusted_host | التحقق من الهوية والصلاحية والإلغاء والنطاق وقفل التنفيذ / Authenticated scoped review and execution lock |
| QG-REMOTE-REVIEW | trusted_host | PR مراجع مستقلًا ونتائج CI وربط النسخة بالموافقة / Reviewed PR, checks and commit-bound approval |
| QG-VERSION | full_repository | توافق VERSION وManifest وREADME وCHANGELOG والعقود وخريطة الترحيل / Consistent release metadata and migration |
| QG-RECOVERY | target_project | خطة تراجع/استعادة مجربة وآثارها على التطبيقات القائمة / Tested rollback/recovery |

لا تُستبدل `target_project` أو `trusted_host` بنتيجة `synthetic_fixture`. ولا يسمح العقد باستثناء N/A تلقائي. تغيير النطاق نفسه يحتاج قرارًا مستقلًا ومراجعة للسياسة؛ لا يُستخدم لتجاوز التزامات سابقة. / Synthetic fixtures cannot substitute for target or trusted-host scopes. No automatic N/A or scope waiver is supported.

## 4. تسلسل التنفيذ / Execution sequence

**أ. التثبيت:** تثبيت الالتزام والبيئة ونطاق الإصدار والمصفوفة والمسؤولين، ومنع تغير الملفات أثناء الفحص الحساس. / Pin candidate, environment, scope and ownership; protect the snapshot.

**ب. فحص المستودع:** إعادة توليد المشتقات في فرع العمل، وفحص اختلافها، وتشغيل الانحدار القديم والجديد والاعتماديات. لا يجوز حذف فشل أو تعديل بصمة تاريخية لتمرير الفحص. / Regenerate and inspect derived files, run old/new tests and dependency checks without suppressing failures.

**ج. فحص المشاريع:** تنفيذ سيناريوهات React/Vue والأجهزة واللغات والإتاحة والمعاملات في بيئات مخولة. بيانات حساسة أو بريد خارجي أو تكاليف خدمة تحتاج تفويضًا خاصًا. / Run actual target scenarios in authorized environments; do not infer permission for production data, external mail or charges.

**د. جمع الأدلة:** حفظ الأمر والبيئة وبصمة الشيفرة والنتيجة والمخرجات والأوقات، وربط كل بوابة بمرفقاتها. عدّ التحققات لا يكفي؛ يجب بيان ما اختُبر. / Record commands, environment, code digest, timestamps and outputs with scope.

**هـ. المراجعة:** يراجع مالك الإصدار الأدلة وصلاحية المراجع المستقل والاستثناءات المقررة خارج هذه السياسة. تُعاد الاختبارات المتأثرة بعد كل تعديل. / Independently review and rerun affected checks after changes.

**و. القرار:** تقييم العقد مع مزود الهوية الموثوق. عند أي نقص تكون النتيجة BLOCKED. حتى PASS لا ينفذ النشر. / Evaluate through the trusted host; missing evidence blocks. PASS does not deploy.

## 5. الأوامر / Commands

```bash
python scripts/vcgf.py release-readiness evidence.json \
  --artifact-root approved-evidence --candidate EXACT_COMMIT_SHA
```

CLI لا يملك مزود هوية، ولذلك لا يعطي اعتمادًا رسميًا حتى لو كانت جميع القيم `passed`. لا تضف خيارًا من نوع `--assume-approved` أو Callback يقرأ الموافقة من المشروع غير الموثوق. / The CLI has no authority provider and cannot approve a release. Do not add `--assume-approved` or trust project-supplied approval code.

يُستدعى API `runtime.adaptive.release.assess` من المضيف الموثوق مع `trusted_review`، بعد تكامل هوية خاضع للتدقيق. اختبارات الوحدة تستخدم Callback اصطناعيًا فقط للتحقق من ترتيب المنطق وحالات الرفض. / Only an audited host supplies the trusted callback; unit-test callbacks are not deployment integrations.

## 6. حالة هذه المراجعة / Status of this review

المثبت محليًا: اختبار الخوارزمية والحالات السلبية، وربط الملفات والبصمات، ورفض الأدلة الناقصة والمنتهية والمتعارضة، ورفض النجاح الذاتي. / Locally verified: algorithm behavior, negative tests, scope/hash/time binding and rejection of self-approval.

غير المثبت: إغلاق البوابات الإحدى والعشرين على مستودع كامل ومشاريع فعلية ومضيف ومنصات مخولة. جميعها تحتفظ بحالة قبول معلقة؛ ولا تُرفع حالة النشر لمجرد نجاح الاختبارات الجزئية. / Not verified: completion of all gates on the full repository, real applications and authorized providers/hosts/platforms.

**قرار توزيع الإطار: v1.2.0 إصدار عام يقرره المالك، بينما اعتماد الإنتاج BLOCKED حتى إغلاق أدلة جميع البوابات. / Framework distribution: owner-authorized v1.2.0 public release; production admission remains BLOCKED until all required evidence is accepted.**
