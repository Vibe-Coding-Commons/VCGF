# Vue

افحص نسخة Vue وNuxt إن وجد وVue Router ونظام التصميم ومكتبات النماذج. لا تضف React لتطبيق معيار محايد. يمكن استخدام مكوّنات الإطار القائمة أو بديل موثق يحقق العقد؛ أسماء حزم React في الملفات أمثلة وليست إلزامًا.

حدد v-model أو نموذج props/events بصورة صريحة، وافصل watch effects عن طلبات الحفظ حتى لا يسبب تغيير اللغة أو mount إعادة تنفيذ أمر. إدارة Teleport والـfocus والـscroll تتبع نفس حدود Dialog وPopover في المعايير.

التحقق في العميل يعكس قواعد الخادم ولا يستبدلها. keys ثابتة للصفوف والعقد والتبويبات، وcache معزول بالحساب والمستأجر. عند Nuxt راجع SSR/hydration والـclient-only packages والوقت والمصادر.

اختبر القيمة الأولية والمحملة لاحقًا، والتبديل بين readonly وeditable، والـRTL، وحالة input أثناء IME. اختر مكتبة نماذج واحدة مناسبة بعد مراجعة مصادرها الحالية في المشروع؛ لا يعد هذا الدليل إثبات توافق إصدار بعينه.

## v0.4.0 — Smart Interaction Patterns
Use existing Vue state/composables/router/query capabilities where they satisfy the contract. Interaction Patterns are behavior specifications, not a mandate to add a state-machine dependency.


## v0.5.0 — Screen Composition & Adaptive UX

نفّذ Screen Composition كعقد تخطيط وسلوك قابل للتكيف، لا كقالب framework ثابت. حافظ على استقلال اختيار المكونات والتفاعلات، واجعل responsive transforms تحافظ على المهمة والسياق. لا تستنتج Authorization من الدور المرئي، ولا توسع data scope بسبب مساحة الشاشة. سجّل كيف يحقق الـAdapter Primary Composition والـModifiers والكثافة وProgressive Disclosure مع اختبارات للأجهزة المستهدفة.
