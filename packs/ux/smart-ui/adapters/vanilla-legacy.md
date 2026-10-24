# JavaScript الأصلي والأنظمة القائمة

الاستهداف هو تحسين آمن متدرج لا إعادة كتابة تلقائية. افحص المتصفحات المدعومة وإصدار Bootstrap أو jQuery والحزم المثبتة قبل إضافة أي widget. عنصر HTML أصلي يحقق المهمة أفضل من بديل أثقل لا يحافظ على form submission والوصولية.

عند التحسين progressive enhancement حافظ على labels وname وvalue وrequired وdisabled والقيم المبدئية. المكوّن المحسن يتزامن مع العقد الحقيقي ولا ينشئ حقلين متناقضين. وفّر teardown وتهيئة idempotent عند إعادة فتح Modal أو استبدال DOM.

لا تخلط plugins متنافسة على نفس العنصر أو تكرر ملفات CSS/JS. استخدام مكتبة قديمة قائمة يحتاج مراجعة دعم وثغرات وتوافق في وقت التغيير، ولا تعني المحافظة على الموجود تجاهل خطر موثق.

اختبر السلوك بدون JavaScript عندما يسمح التطبيق بذلك، ومع تحميل متأخر وفشل مورد وعدم وجود بيانات. يظل الخادم مرجع القيمة والتفويض؛ واجهة محسنة لا تعني نظامًا أكثر أمانًا وحدها.

## v0.4.0 — Smart Interaction Patterns
For legacy interfaces, implement the smallest selected state transitions explicitly and centralize guards against duplicate submission, stale responses, and permission changes. Do not rewrite the application just to match a modern library.


## v0.5.0 — Screen Composition & Adaptive UX

نفّذ Screen Composition كعقد تخطيط وسلوك قابل للتكيف، لا كقالب framework ثابت. حافظ على استقلال اختيار المكونات والتفاعلات، واجعل responsive transforms تحافظ على المهمة والسياق. لا تستنتج Authorization من الدور المرئي، ولا توسع data scope بسبب مساحة الشاشة. سجّل كيف يحقق الـAdapter Primary Composition والـModifiers والكثافة وProgressive Disclosure مع اختبارات للأجهزة المستهدفة.
