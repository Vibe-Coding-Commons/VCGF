# توافق وتداخل أنماط التفاعل

المصفوفة التشغيلية في `catalog/interaction-compatibility-matrix.json`.

أنواع العلاقات:
- `complementary`: يمكن الجمع عند تحقق إشارات مستقلة.
- `alternative`: غالبًا يختار أحدهما أو يوثق سبب الجمع.
- `authority-boundary`: يجب حسم مصدر السلطة ومن يملك القرار.
- `specialization`: نمط متخصص يحل محل سلوك عام في جزء من الحالة.
- `mode-boundary`: الجمع ممكن لكن يحتاج حدودًا واضحة للحالة.

أمثلة حرجة:
- `ConfirmationDecisionPattern` و`UndoableActionPattern`: لا تستخدم الاثنين تلقائيًا. الإجراء القابل للعكس منخفض الخطورة قد يفضل Undo، أما الأثر غير القابل للعكس فيحتاج Confirmation أقوى.
- `OptimisticUpdateRollback` و`OfflineReconnectSynchronization`: يحتاجان مصدر ترتيب واحد للأوامر حتى لا تتصارع optimistic state مع offline queue.
- `ErrorRetryRecovery` و`IdempotentSubmissionProtection`: إعادة المحاولة في كتابة ذات أثر تحتاج ضمان عدم التكرار.
- `SessionExpiryReauthentication` و`SensitiveActionStepUp`: انتهاء الجلسة ليس هو رفع مستوى المصادقة لإجراء محدد.
