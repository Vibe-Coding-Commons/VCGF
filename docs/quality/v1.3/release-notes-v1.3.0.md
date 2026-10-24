<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 -->
# VCGF v1.3.0 — Smart UI & Adaptive Experience Orchestration

**Release date:** 2026-10-24
**Release type:** Public framework source distribution
**License:** Apache-2.0
**Founder & Maintainer:** Eng. Hamada Sami

## العربية — ما الجديد؟

VCGF v1.3.0 يضيف طبقة **VCGF Smart UI Components & Interaction Standards v1.0.0** كامتداد متوافق مع إصدارات v1.x، مع الحفاظ على جميع Control IDs والـProfiles والترخيص وحقوق المؤسس دون تغيير.

أبرز الإضافات:

- **36 Smart UI Component Standards** للاختيار الانتقائي حسب سياق الشاشة والمهمة، وليس لإنشاء جميع المكونات في كل مشروع.
- **24 Smart Interaction Patterns** لسلوك الإنشاء والتعديل والحذف والحفظ والتعارض والجلسة والصلاحيات والانقطاع وإعادة المحاولة وغيرها.
- **20 Smart Screen Composition Standards** تشمل 18 تركيب شاشة أساسيًا و2 Adaptive Modifiers للموبايل والشاشات الكبيرة.
- **18 Smart Journey Patterns** لتنظيم الرحلات بين الشاشات، Deep Links، Return-to-Origin، Queue Processing، Approval، Offline Sync، وغيرها.
- **Reuse-First governance** بمسار `reuse → extend → wrap → replace → build_new` مع `verify_first` عند نقص دليل الملاءمة.
- **Selective Loading**: لا تُفعّل Dependencies أو الطبقات المتقاطعة تلقائيًا، ولا يُحمّل الكتالوج كاملًا دون حاجة.
- **Calendar governance enhancement**: الضغط على السنة يفتح اختيار السنة والضغط على اسم الشهر يفتح اختيار الشهر، مع فصل `viewDate` عن `selectedDate` وعدم تغيير القيمة حتى اختيار يوم صالح.
- **Enterprise Searchable Select & Combobox** كمعيار مرتبط مركزيًا مع عدم فرض البحث على القوائم القصيرة التي لا تحتاجه.
- سياسات مستقلة لـRTL/LTR، Accessibility، Responsive Density، Action Hierarchy، Information Architecture، Context Continuity، Deep Links، Decision Explainability، Evidence Conformance، وFinal Adoption Gate.

## English — Highlights

VCGF v1.3.0 adds the **VCGF Smart UI Components & Interaction Standards v1.0.0** layer as a backwards-compatible v1.x capability. It adds selective component, interaction, screen-composition and journey orchestration while preserving the existing 84 normative Control IDs, Profiles, licensing and founder attribution.

The Smart UI layer is evidence-bound and reuse-first. It does not authorize implementation, install packages automatically, activate dependencies implicitly, or claim product/runtime acceptance from documentation or schema validation.

## Verification boundary / حدود التحقق

This release decision is for the **framework source distribution**. Repository validation and Smart UI package checks must pass on the exact release commit before tagging. Target-application acceptance, trusted-host enforcement, provider integrations, independent attestation and the cumulative production gates remain separate.

**Production admission remains BLOCKED unless its required evidence is accepted.** A public framework release is not a production compliance certificate for every application.
