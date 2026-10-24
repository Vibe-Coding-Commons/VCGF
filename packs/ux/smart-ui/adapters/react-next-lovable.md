# React وNext.js وLovable

اقرأ lockfile وبنية المشروع قبل الاختيار. Lovable ليس اسم إطار خادم مضمون؛ تحقق هل المشروع React/Vite أو Next.js أو غير ذلك وما مصدر التخزين والمصادقة الحقيقي. لا تفترض وجود server actions أو Supabase أو API أو صلاحيات Row-Level Security دون دليل.

استخدم نظام التصميم الحالي؛ shadcn/ui أو Radix أو React Aria مرشحون عند الملاءمة، وليس المطلوب خلطهم جميعًا. TanStack Table وQuery وReact Hook Form أو بدائلها خيارات مرتبطة بالحاجة. حزم SSR وclient-only والـworkers تحتاج boundaries صحيحة وتهيئة مستقرة.

في Next.js حافظ على router الحالي وserver/client boundaries ولا تضف React Router افتراضيًا. في React/Vite استخدم router المثبت. عدم اختلاف التاريخ والاتجاه والمعرفات عند hydration يجب اختباره عندما يوجد SSR.

التفويض والتحقق والحسابات الدقيقة والعمليات الطويلة في خادم أو خدمات موثوقة؛ البيانات التجريبية لا تُقدّم كتكامل إنتاجي. اختبر keyboard وRTL وportal داخل Dialog والبحث الداخلي وطلبات الشبكة المتأخرة. لا تثبت dependencies كلها من سجل المرشحين.

## v0.4.0 — Smart Interaction Patterns
Model selected interactions with the project's existing state/query/form primitives first. Do not install a state-machine package solely because a VCGF pattern contains a state diagram. Use request cancellation/staleness guards, server authorization, and idempotency where required by the selected pattern.


## v0.5.0 — Screen Composition & Adaptive UX

نفّذ Screen Composition كعقد تخطيط وسلوك قابل للتكيف، لا كقالب framework ثابت. حافظ على استقلال اختيار المكونات والتفاعلات، واجعل responsive transforms تحافظ على المهمة والسياق. لا تستنتج Authorization من الدور المرئي، ولا توسع data scope بسبب مساحة الشاشة. سجّل كيف يحقق الـAdapter Primary Composition والـModifiers والكثافة وProgressive Disclosure مع اختبارات للأجهزة المستهدفة.
