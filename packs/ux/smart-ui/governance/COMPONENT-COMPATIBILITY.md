# VCGF Smart UI — Component Compatibility & Overlap Rules

## الهدف

بعض المكونات متكاملة، وبعضها بدائل لنفس طريقة عرض، وبعضها قد يعرض الحدث نفسه من منظور مختلف. لذلك يحتوي `catalog/compatibility-matrix.json` على علاقات تمنع الذكاء الاصطناعي من تجميع مكونات متشابهة بلا سبب.

## أنواع العلاقة

- `alternative`: غالبًا يختار أحد المكوّنين، ويمكن الجمع فقط إذا كان هناك View switch أو حاجة موثقة.
- `complementary`: لكل مكوّن مسؤولية مختلفة ويمكن أن يتعاونا.
- `authority-boundary`: قد يعرضان معلومات متشابهة لكن مصدر السلطة مختلف ويجب عدم خلطه.
- `specialization`: مكوّن متخصص يبني فوق معيار أعم.
- `mode-boundary`: يوضح حدود وضعين مثل القراءة والتحرير.

## قاعدة التحذير

إذا اختار محرك التقييم طرفي علاقة `alternative` أو `authority-boundary`، يجب أن يضيف `compatibility_review` وتحذير مراجعة. هذا ليس فشلًا آليًا؛ فقد يكون الجمع صحيحًا، لكنه يحتاج قرارًا صريحًا.

## أمثلة

- SmartDataGrid وSmartCollectionList: بديلان لعرض مجموعة سجلات غالبًا.
- AuditHistoryViewer وSmartActivityTimeline: الأول دليل تدقيقي، والثاني سرد تشغيلي للمستخدم.
- UnifiedFeedbackSystem وSmartNotificationCenter: الأول لحظي، والثاني Inbox مستمر.
- PermissionAwareActions وSmartContextualActionBar: الأول يحدد هل الإجراء مسموح، والثاني يحدد أين وكيف يظهر.
