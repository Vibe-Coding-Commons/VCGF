# VCGF Smart UI, Interaction, Screen & Journey Standards

**إصدار الطبقة:** 1.0.0 · **الحالة:** `final-integration-candidate` · **المستهدف:** VCGF 1.3.0.

هذه النسخة تغلق التطوير المواصفاتي للطبقة الذكية بأربع طبقات انتقائية مستقلة:

1. **36 Components** — ما القدرة المرئية المطلوبة؟
2. **24 Interaction Patterns** — كيف تتصرف الحالة والبيانات؟
3. **20 Screen Compositions** — كيف تُركب الشاشة وفق المهمة والجهاز؟
4. **18 Journey Patterns** — كيف تستمر المهمة بين الشاشات والمراحل؟

بالإضافة إلى معيارَي Calendar Governance وEnterprise Searchable Select.

## القاعدة الحاكمة

**Understand → Inventory → Select Composition → Select Components → Select Interactions → Select Journeys → Reuse First → Load Minimum → Implement → Evidence → Verify**

لا ينشئ VCGF كل المكونات أو الأنماط أو الرحلات. الاختيار قائم على إشارات صريحة، والعلاقات Review-only.

## الأعداد النهائية

- 36 Component Standards
- 24 Interaction Patterns
- 20 Screen Compositions
- 18 Journey Patterns
- 2 Bound Standards
- 660 إعدادًا/سياسة مرجعية: 288 + 144 + 120 + 108
- 1176 Requirement
- 1176 Acceptance Scenario، وحالتها التطبيقية `not_run` حتى التنفيذ

## البدء

- [START-HERE-AR](START-HERE-AR.md)
- [CATALOG](CATALOG.html)
- [Master Policy](governance/MASTER-POLICY.md)
- [Experience Orchestration](governance/EXPERIENCE-ORCHESTRATION.md)
- [Journey Selection](governance/SMART-JOURNEY-SELECTION.md)
- [Final Adoption Gate](governance/FINAL-ADOPTION-GATE.md)

## التقويم

يبقى `CALENDAR-GOVERNANCE-ADDENDUM` إلزاميًا لكل موضع تاريخ. الضغط على السنة يفتح اختيار السنة والضغط على اسم الشهر يفتح اختيار الشهر، مع فصل `viewDate` عن `selectedDate`.

## حالة الإصدار

1.0.0 هنا يعني اكتمال **Smart UI Layer specification**، وليس نشر VCGF 1.3.0 رسميًا. الدمج النهائي بالمستودع والتجارب الفعلية وبوابات الإصدار ما زالت مطلوبة.
