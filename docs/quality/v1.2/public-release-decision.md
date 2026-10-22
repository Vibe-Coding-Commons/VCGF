<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.2.0 — Owner public framework release decision / قرار النشر العام

**Date:** 2026-10-21  
**Decision:** Publish the VCGF **framework source distribution** as v1.2.0 after CI passes.  
**Separate decision:** Production admission, target application compliance and independent attestation remain **BLOCKED / NOT CERTIFIED** until their cumulative gates pass.

## العربية

بناء على قرار مالك المشروع الصريح في 2026-10-21، يتم اعتماد تسمية **v1.2.0** لإصدار عام رسمي من إطار VCGF ونشر الشيفرة والأدلة المتاحة؛ على أن تُعالج العيوب اللاحقة بإصدارات تصحيحية وفق Semantic Versioning.

**هذا قرار لنشر الإطار وليس إثباتاً لتأهيل كل مكون أو كل مشروع للإنتاج.** تحتفظ بوابات القبول الـ21 بحالتها الفعلية، ولا تُعتبر أي نتيجة غير منفذة PASS، ولا يسقط نطاق v1.1 أو متطلبات v1.2 السابقة. لم يتم تشغيل تطبيق عميل أو نشر خدمة إنتاجية بناءً على هذا القرار.

تم دمج PR #1 في main بالالتزام `782c642e85413bb14999c1b08ef0b747f967857c`، ونجحت فحوص GitHub المسجلة لذلك الدمج؛ ينبغي إعادة تشغيل CI لتغييرات إعداد الإصدار على الالتزام النهائي قبل إنشاء Tag `v1.2.0`.

## English

The owner elects to release the **VCGF v1.2.0 framework distribution** publicly with disclosed verification limits and a post-release bugfix policy. This is a distribution/version decision, not a waiver of application-specific production admission, authenticated review, dependency/provider acceptance, or the 21 cumulative gates. A green repository CI result is not a production compliance certificate. Future compatible fixes use v1.2.1, v1.2.2, etc.

The original v1.0 baseline hashes and the v1.1 historical approvals are preserved; independently reviewed v1.2 exceptions are declared in `baseline-compatibility-v1.2.json`. The founder’s attribution, Apache-2.0 license, original Control IDs, schemas and Profiles remain subject to their existing rules.

## Open validation boundaries / حدود التحقق المتبقية

- Real Laravel/React and Laravel/Vue application acceptance; supported browsers, manual accessibility and representative usability checks
- Live Microsoft 365 OAuth/delivery and PostgreSQL/MySQL backup/attachment restore acceptance
- Trusted production host identity, authority, auditing and independent approval
- Real live platform-adapter behavior, supply-chain/SBOM/dependency review and recovery exercises
- The remaining 21-gate evidence and inherited v1.1 scope; no failures or missing evidence may be silently relabeled successful

**Production admission remains BLOCKED.** Public distribution is provided under Apache-2.0 with the license disclaimers. Users must validate their target environment independently.

## References

- [Release gate policy](release-gates.md)
- [Candidate scope](scope-register.json)
- [Recorded local evaluation (historical snapshot)](executive-summary.md)
- [Release notes](release-notes-v1.2.0.md)
