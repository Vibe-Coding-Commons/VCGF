# السياسة الحاكمة النهائية — VCGF Smart UI v1.0.0

**الحالة:** `final-integration-candidate` — **المستهدف:** VCGF 1.3.0.

## 1. الطبقات الأربع

- **36 Smart UI Components**
- **24 Smart Interaction Patterns**
- **20 Smart Screen Compositions**: 18 Primary + 2 Modifiers
- **18 Smart Journey Patterns**
- **2 Bound Standards**: Calendar Governance وEnterprise Searchable Select

وجود معيار في الكتالوج لا يفعله. الإشارات مستقلة: `signals`, `interaction_signals`, `composition_signals`, `journey_signals`.

## 2. مسار القرار

`Understand → Inventory → Select Composition → Select Components → Select Interactions → Select Journeys → Reuse First → Review → Load Minimum → Implement → Evidence → Verify`

## 3. Reuse First

`reuse → extend → wrap → replace → build_new`، وعند نقص الدليل `verify_first`.

## 4. المصدر والسلطة

الواجهة لا تمنح صلاحية ولا تثبت أثرًا مستمرًا. الخادم/خدمة المجال مصدر التفويض وقواعد الأعمال والحالة النهائية.

## 5. الرحلات

Deep Link لا يتجاوز المراحل أو الصلاحية. Return-to-origin يتحقق من الأصل. تبديل tenant/role يبطل السياق غير الموافق.

## 6. الإعدادات

`System → Tenant → Allowed role/user preference → Temporary UI state`. لا يخفف مستوى أدنى قيدًا أمنيًا.

## 7. الأدلة

Package/Schema validation لا يساوي Runtime conformance. كل Acceptance تطبيقية تبقى `not_run` حتى Evidence فعلي.

## 8. الإصدار

هذه النسخة تكمل مواصفات Smart UI Layer، لكنها لا تغيّر VERSION أو Tag لـVCGF. الاعتماد الرسمي يتطلب `FINAL-ADOPTION-GATE.md` وبوابات المستودع.
