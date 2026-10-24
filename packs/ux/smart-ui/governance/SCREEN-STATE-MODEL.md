# نموذج حالة الشاشة المرجعي

لا يفرض VCGF آلة حالات واحدة لكل الشاشات، لكنه يمنع اختزال الحالات المهمة في `loading/error` فقط عندما تكون المهمة أعقد.

الحالات الشائعة التي قد تظهر حسب السياق:
`idle`, `loading`, `ready`, `dirty`, `validating`, `saving`, `submitting`, `refreshing`, `stale`, `offline`, `syncing`, `conflict`, `forbidden`, `expired`, `retrying`, `rolling-back`, `completed`, `partial`, `error`.

## قواعد
- لا تضف حالة لا تؤثر في السلوك أو القرار.
- لا تدمج `forbidden` مع `error` إذا كانت طريقة التعافي مختلفة.
- لا تدمج `saved` مع `submitted` إذا كان الأثر مختلفًا.
- لا تعتبر `optimistic` حالة مؤكدة.
- اربط كل انتقال بحدث ومصدر سلطة وطريق فشل.
- اختبر الاستجابات القديمة وتغير السياق أثناء كل انتقال غير فوري.
