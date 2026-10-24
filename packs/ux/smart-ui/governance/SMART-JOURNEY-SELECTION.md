# Smart Journey Selection

يختار VCGF الرحلات من `journey_signals` الصريحة فقط.

## التسلسل

1. افهم نية المستخدم ونقطة الدخول ونقطة الاكتمال المتوقعة.
2. حدد هل المهمة تمتد عبر أكثر من شاشة/مرحلة.
3. طابق `journey_signals` مع `catalog/journey-rules.json`.
4. اختر أقل مجموعة رحلات لازمة.
5. راجع `journey-compatibility-matrix.json`.
6. لا تشغل شاشة أو مكوّن أو نمط تفاعل بسبب الرحلة وحدها.

## حالات القرار

- `selected`: توجد إشارة صريحة.
- `needs_review`: إشارات متعارضة أو ناقصة.
- `not_selected`: لا توجد رحلة متعددة النقاط مثبتة.
- `no_ui`: لا توجد واجهة.

## قاعدة عدم الاستنتاج

وجود Create Form لا يعني Create→Detail Journey. وجود Approval Button لا يعني Review→Approve→Complete. يجب أن يصف السياق الانتقال المطلوب صراحة.
