# Laravel وLivewire وBlade

ابدأ من نسخ PHP وLaravel وLivewire المثبتة، ولا تفرض ترقية أو إعادة بناء الواجهة. استخدم Validation وPolicies وGates والعقود الحالية في طبقة موثوقة، وأضف مكونات Blade أو Livewire أو JavaScript حسب الحاجة.

عند دمج widget خارجي مع تحديث DOM احسم ملكية العنصر ودورة التهيئة والتنظيف؛ لا تنشئ عدة instances أو listeners بعد كل تحديث. `wire:ignore` أو بديله ليس حلًا عامًا؛ يحتاج مزامنة قيمة وخطأ وتعطيل وفك تهيئة موثقة وفق النسخة.

إعادة التحقق من المرفقات والصلاحيات وحجم الملفات والحسابات والتوقيت في الخادم إلزامية حسب انطباق المعيار. jobs والـqueues تحتاج تنفيذًا ومراقبة فعلية؛ تقدم الواجهة لا يثبت وجود عامل يعمل.

حافظ على name وvalue وإرسال النموذج وCSRF وحالات errors والمعرفات المحفوظة. لا تنقل قواعد التحقق إلى JavaScript وحده. لو كانت واجهة المشروع jQuery أو Bootstrap فأعد استخدام حل مناسب بعد فحص التوافق والترخيص بدل إدخال إطار جديد.

## v0.4.0 — Smart Interaction Patterns
Keep authorization, validation, idempotency, conflict detection, and persistent effects on the server. Livewire/UI state represents interaction progress but does not replace domain authority.


## v0.5.0 — Screen Composition & Adaptive UX

نفّذ Screen Composition كعقد تخطيط وسلوك قابل للتكيف، لا كقالب framework ثابت. حافظ على استقلال اختيار المكونات والتفاعلات، واجعل responsive transforms تحافظ على المهمة والسياق. لا تستنتج Authorization من الدور المرئي، ولا توسع data scope بسبب مساحة الشاشة. سجّل كيف يحقق الـAdapter Primary Composition والـModifiers والكثافة وProgressive Disclosure مع اختبارات للأجهزة المستهدفة.
