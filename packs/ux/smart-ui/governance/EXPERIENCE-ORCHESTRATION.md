# VCGF Experience Orchestration — Final Layer Model

## الطبقات الأربع

1. **Screen Composition** — كيف تنظم الشاشة.
2. **Components** — ما القدرات المرئية المطلوبة.
3. **Interactions** — كيف تتصرف الحالة داخل المهمة.
4. **Journeys** — كيف تنتقل المهمة بين الشاشات والمراحل.

كل طبقة لها إشارات مستقلة. لا توجد Auto Activation عبر الطبقات.

## ترتيب العمل

`Understand → Inventory → Select Composition → Select Components → Select Interactions → Select Journeys → Reuse First → Review Compatibility → Load Minimum → Implement → Evidence → Verify`

## الحد الأدنى

لا يحمّل الوكيل Catalog Dump. يستخدم `standards_to_load` الناتجة عن الخطة.

## الثقة

إذا كانت الإشارات ناقصة، يخرج `needs_review` ولا يخترع رحلة أو مكوّنًا احترازيًا.
