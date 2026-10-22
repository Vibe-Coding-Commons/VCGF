<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.2.0 — Public Framework Release / الإصدار الرسمي العام

**Release date:** 2026-10-21  
**Release type:** Public framework source distribution (not certified for production deployments)  
**License:** Apache-2.0  
**Founder & Maintainer:** Eng. Hamada Sami

## العربية — ما الجديد؟

- **محرك Adaptive Engineering:** توصيات هندسية ومعمارية متناسبة مع متطلبات المشروع، وقرارات قابلة للتفسير والمراجعة
- **محرك Adaptive UX Intelligence:** مراعاة طبيعة المشروع والجمهور والمهام والأجهزة، ودعم اتجاهي RTL/LTR والخطوط المحلية والأداء
- **تنسيق المحركين:** ربط التوصيات الهندسية وتجربة المستخدم مع السياق والموافقات وحدود الصلاحية
- **إمكانات v1.1 المضمّنة:** توجيه المهام، الاعتماديات، التحميل الانتقائي، العقود، سجل الأدلة وتكاملات البريد والنسخ الاحتياطي المرجعية
- **الفحوص:** نجاح مصفوفة CI المنشورة لطلب الدمج PR #1 على Python 3.12/3.13 وWindows/Linux، مع حماية الضوابط والسجل التاريخي

## English — Highlights

Adaptive Engineering and Adaptive UX Intelligence deliver explainable, project-specific architecture and user experience guidance. This public release includes the unreleased v1.1 runtime capabilities and reference email/backup components, as well as bounded input validation, traceability and cross-platform CI tests. Existing 84 normative controls, Profiles, Control IDs, license and founder rights are retained.

## Important limitations / القيود

GitHub repository tests passing **does not** mean every external provider, supported editor, target Laravel/React/Vue application or trusted production host was tested. Real Microsoft 365 delivery, PostgreSQL/MySQL restore/attachment consistency, independent authorization, manual accessibility/usability, and the 21 cumulative admission gates remain open. **Production admission is BLOCKED**, even though the framework source itself is released publicly as v1.2.0.

Release users should inspect `docs/quality/v1.2/release-gates.md` and validate the intended application and host environment. Compatible fixes will use v1.2.1 onward.

## Links

- [English README](../../../README.md) · [Arabic README](../../../README.ar.md)
- [Release admission gates](release-gates.md) · [Release owner decision](public-release-decision.md)
- [Change history](../../../CHANGELOG.md)
