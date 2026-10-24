# عقد التنفيذ المحايد للتقنية

**الحالة:** إرشادي؛ لا يوجد adapter برمجي منفذ في هذه الحزمة.

ابدأ من السلوك والعقود والبيانات لا من اسم مكتبة. لكل معيار مطلوب، عرّف value model وحالات المكوّن والأحداث ومصدر الإعدادات وحدود التفويض. قد يكون HTML أصلي ومكوّن صغير كافيين؛ لا تجعل حلًا تقنيًا واحدًا جزءًا من Core.

سجل framework/runtime/browser versions وملفات الحزم وعقد API الحقيقي. الأحداث المقترحة في المعيار أسماء دلالية وليست imports جاهزة؛ ثبت واجهتها typed حسب التقنية وأرفق أمثلة واختبارات.

اجعل central settings provider وpermission service وdate service قابلة للاستبدال. لا يعيد كل مكوّن تنفيذ الترجمة أو الصلاحيات أو تحليل التاريخ. يدعم Adapter الإعدادات المشتركة داخل حدود السياسة ويرفض القدرة غير المدعومة بدل الادعاء أنها تعمل.

أدلة adapter تشمل كيفية تحقيق كل REQ، والمعايير غير المنطبقة وسببها، وحدود المكتبة، واختبارات التكامل. لا تنسخ فقرة PASS من adapter آخر.

## v0.4.0 — Smart Interaction Patterns
Implement selected interaction patterns as explicit state and authority contracts. Do not map every pattern to a new framework or library. Existing controller/service/state code may be reused if evidence shows it satisfies the selected pattern.


## v0.5.0 — Screen Composition & Adaptive UX

نفّذ Screen Composition كعقد تخطيط وسلوك قابل للتكيف، لا كقالب framework ثابت. حافظ على استقلال اختيار المكونات والتفاعلات، واجعل responsive transforms تحافظ على المهمة والسياق. لا تستنتج Authorization من الدور المرئي، ولا توسع data scope بسبب مساحة الشاشة. سجّل كيف يحقق الـAdapter Primary Composition والـModifiers والكثافة وProgressive Disclosure مع اختبارات للأجهزة المستهدفة.
