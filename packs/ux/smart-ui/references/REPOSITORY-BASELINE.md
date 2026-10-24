# خط الأساس الرسمي لمستودع VCGF

**تاريخ التحقق:** 2026-10-24  
**المستودع:** `Vibe-Coding-Commons/VCGF`  
**الفرع:** `main`  
**حالة الاستخدام:** Read-only baseline verification for Smart UI Layer v1.0.0

## النسخة الرسمية الحالية

| البند | القيمة المتحققة |
|---|---|
| `VERSION` | `1.2.0` |
| `main` commit SHA | `f65336f87d97a6d9d0cb38a9838e41ec393ef756` |
| `VERSION` Git blob SHA | `26aaba0e86632e4d537006e45b0ec918d780b3b4` |
| آخر commit على `main` | `Merge pull request #2 from Vibe-Coding-Commons/release/v1.2.0-official` |
| تاريخ commit | `2026-10-22T12:34:48Z` |
| GitHub verification | Signed / verified |

## قرار الحالة

تستهدف هذه الحزمة **تطوير VCGF 1.3.0**، لكنها لا تدّعي أن VCGF 1.3.0 منشور أو مدمج في `main`.

الحالة الدقيقة للحزمة هي:

`VCGF Smart UI Components & Interaction Standards v1.0.0 — final-integration-candidate for VCGF 1.3.0 development`

ويظل الإصدار الرسمي المتحقق من المستودع وقت تجميد هذه الحزمة هو **VCGF 1.2.0**.

## قاعدة الدمج

عند اعتماد الحزمة داخل المستودع:

1. يبدأ الدمج من خط أساس VCGF الرسمي أو من branch تطوير 1.3.0 المعتمد وقت التنفيذ، وليس من نسخة ZIP قديمة.
2. تُراجع أي تغييرات طرأت على `main` بعد commit أعلاه قبل الدمج.
3. لا يُحدَّث `VERSION` إلى 1.3.0 ولا يُنشأ Tag أو Release لمجرد نجاح فحوص هذه الحزمة.
4. يجب تشغيل بوابات VCGF الأصلية بعد الدمج، إضافة إلى validators الحزمة.
5. تبقى حالات Runtime في `not_run` إلى أن تُنفذ على تطبيق أو Pilot فعلي وتُجمع Evidence قابلة للفحص.

## ملاحظة عن البصمات

Git blob SHA أعلاه يثبت نسخة الملف داخل Git، بينما بصمات ملفات حزمة التسليم نفسها موثقة بـSHA-256 داخل `manifest.json` و`SHA256SUMS.txt`.
