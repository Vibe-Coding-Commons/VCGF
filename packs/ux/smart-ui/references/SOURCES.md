# المصادر الرسمية وسجل المراجعة

راجعت هوية المكتبات ووثائقها الرسمية ذات الصلة بتاريخ 23 أكتوبر 2026. لا يُقصد بذلك اعتماد أحدث نسخة أو تدقيق أمني أو ترخيص نهائي؛ تثبيت النسخة المناسبة وفحصها مسؤولية مرحلة التنفيذ. كل رابط أدناه مصدر للقدرات والحدود التقنية، أما الإعدادات والسياسات المقترحة فهي قرارات تصميم في هذه الحزمة.

## مراجع مشتركة

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) - Accessibility criteria; conformance requires project evidence.
- [WAI-ARIA Authoring Practices patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) - Interaction patterns, not a substitute for testing.
- [W3C structural direction markup](https://www.w3.org/International/questions/qa-html-dir) - Document and inline text direction.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) - Trusted-layer authorization.
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) - Upload validation and storage boundaries.
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) - Untrusted content and rendering boundaries.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) - Logging, redaction, and data minimization.
- [Playwright accessibility testing guide](https://playwright.dev/docs/accessibility-testing) - Automated testing support; manual checks remain required.

## مرشحو المكتبات — 44 مرجعًا

| ID | المكتبة أو المنتج | الدور المقترح | الحدود والتنبيهات |
|---|---|---|---|
| `SHADCN` | [shadcn/ui](https://ui.shadcn.com/docs/components) | مكوّنات قابلة للتخصيص ضمن نظام تصميم React مناسب. | افحص primitive والبنية في الإصدار الفعلي؛ لا تفترض أن كل Combobox يضع البحث داخل النافذة، ولا تثبّت كل المكوّنات دفعة واحدة. |
| `RADIX` | [Radix UI Primitives](https://www.radix-ui.com/primitives/docs/components) | عناصر تفاعل غير منسقة تشمل Dialog وPopover وTabs وDropdown Menu. | اختبار التركيب وإدارة التركيز يظل مطلوبًا؛ اختيارها لا يمنح التطبيق شهادة وصولية تلقائية. |
| `REACT_ARIA` | [React Aria Components](https://react-aria.adobe.com/Tree) | بديل لمكوّنات تفاعلية مع اهتمام بالدلالات ولوحة المفاتيح. | اختر النمط الموافق للبنية ولا تركب primitives متضاربة؛ راجع وثائق المكوّن والإصدار المستعمل. |
| `TANSTACK_TABLE` | [TanStack Table / @tanstack/react-table](https://tanstack.com/table/v8/docs/introduction) | أساس headless لبناء سلوك الجداول وتركيب الواجهة حسب الهوية. | ليس جدولًا مكتمل التصميم ولا خدمة استعلام؛ virtualization والتفويض والفرز الخادمي تحتاج دمجًا واختبارًا. |
| `TANSTACK_QUERY` | [TanStack Query / @tanstack/react-query](https://tanstack.com/query/latest/docs/framework/react/overview) | تنسيق حالة البيانات والطلبات وcache وإعادة الجلب. | اضبط query keys وإبطال البيانات حسب المستأجر والصلاحيات؛ ليست محرك تفويض أو قاعدة بيانات. |
| `AG_GRID` | [AG Grid](https://www.ag-grid.com/license-pricing/) | بديل جدول غني عند الحاجة إلى قدرات جاهزة متقدمة. | راجع الفرق بين Community وEnterprise وترخيص كل خاصية في تاريخ اعتماد المشروع؛ لا تفترض إتاحة جميع القدرات مجانًا. |
| `REACT_HOOK_FORM` | [React Hook Form](https://github.com/react-hook-form/react-hook-form) | إدارة حالة الحقول والنماذج والتحقق في React. | التحقق في العميل لا يستبدل تحقق الخادم؛ وثائق الموقع المباشرة حجبت الجلب فاستُخدم مستودع المشروع الرسمي. |
| `ZOD` | [Zod](https://zod.dev/) | مخططات للتحقق من مدخلات TypeScript واستنتاج أنواعها. | تحقق من توافق resolver والإصدار؛ لا تفترض تطابقًا تلقائيًا مع قواعد خادم بلغة أخرى. |
| `TANSTACK_FORM` | [TanStack Form](https://tanstack.com/form/latest) | بديل لإدارة نماذج ذات احتياج إلى تحكم وتحقق منظم. | اختره أو حل النماذج المناسب الموجود؛ لا تجمع محركي نماذج لنفس النموذج بلا حاجة. |
| `NUQS` | [nuqs](https://nuqs.dev/) | ربط حالة غير حساسة بمعلمات البحث في URL مع أنواع واضحة. | تحتاج مراجعة adapter الخاص بإطار المشروع وقائمة سماح؛ لا تضع بيانات شخصية في الرابط تلقائيًا. |
| `UPPY` | [Uppy / @uppy/core](https://uppy.io/docs/) | أساس رفع ملفات قابل للتركيب مع نقل ومصادر وواجهات اختيارية. | استئناف tus يتطلب ناقلًا وخادمًا متوافقين؛ الفحص والربط والصلاحيات ليست ميزات أمان مكتملة بالواجهة. |
| `FILEPOND` | [FilePond](https://pqina.nl/filepond/docs/) | بديل لإدارة اختيار الملفات وتجربة الرفع مع adapters متعددة. | تحقق من إضافات المشروع وخدمة النقل وسياسة التحقق في الخادم قبل إعلان الدعم. |
| `REACT_DROPZONE` | [react-dropzone](https://react-dropzone.js.org/) | اختيار الملفات والسحب والإفلات في React. | ليس uploader خادميًا ولا فحصًا أمنيًا؛ اربطه بناقل وخدمة ملفات مستقلين. |
| `PDFJS` | [PDF.js / pdfjs-dist](https://mozilla.github.io/pdf.js/) | تحليل ورندر PDF وفق تقنيات الويب. | لا يوفر تحويل صيغ Office أو تنقيحًا آمنًا أو توقيعًا بمجرد استخدامه؛ راجع worker والتوافق ومصادره. |
| `REACT_PDF` | [React-PDF / react-pdf](https://github.com/wojtekmaj/react-pdf) | ربط معاينة PDF داخل React باستخدام مشروع العرض المخصص. | المقصود مكتبة wojtekmaj للعرض وليس @react-pdf/renderer المخصص لإنشاء ملفات؛ راجع توافق PDF.js والـworker. |
| `SONNER` | [Sonner](https://sonner.emilkowal.ski/) | إشعارات Toast في تطبيقات React. | ليست مركز إشعارات دائمًا أو سجل تدقيق؛ راجع المدة والتركيز والإعلانات حسب نوع الرسالة. |
| `REACT_ROUTER` | [React Router](https://reactrouter.com/) | توجيه مناسب عندما يكون هو الموجّه المعتمد في تطبيق React. | لا تضفه بجانب Router الإطار دون حاجة؛ Next.js يستخدم توجيهه المعتمد حسب بنية المشروع. |
| `REACT_ARIA_TREE` | [React Aria Tree](https://react-aria.adobe.com/Tree) | أساس لشجرة تفاعلية باختيار وتوسيع منظمين. | انتشار اختيار الأب والصلاحيات والتحميل الكسول قواعد تكامل تُختبر ولا تفترضها من اسم المكوّن. |
| `MUI_TREE` | [MUI X Tree View](https://mui.com/x/react-tree-view/) | بديل للشجرة ضمن مشروع يعتمد MUI. | تحقق من قدرات Simple وRich وPro وترخيص الميزات المطلوبة وتوافق نظام التصميم. |
| `XSTATE` | [XState](https://stately.ai/docs/xstate) | نمذجة حالات وانتقالات عندما تبررها تفرعات أو تعقيد التفاعل. | لا يمنح وحده استمرارية مؤسسية ومؤقتات موزعة وتفويضًا وتخزينًا دائمًا؛ هذه عقود تنفيذ مستقلة. |
| `CASL` | [CASL](https://github.com/stalniy/casl) | نمذجة قدرات أو قواعد تفويض عندما تلائم لغة وبنية المشروع. | استخدامه في الواجهة لا يحمي API؛ أي قواعد مرسلة للعميل يعاد فرضها في طبقة موثوقة. |
| `LARAVEL_AUTH` | [Laravel Gates and Policies](https://laravel.com/docs/authorization) | آليات تفويض خادمية للمشاريع التي تستخدم Laravel. | هذه قدرة في الإطار وليست حزمة واجهة جديدة؛ استخدم إصدار الوثائق المطابق للمشروع دون ترقية إجبارية. |
| `TIPTAP` | [Tiptap / @tiptap/react](https://tiptap.dev/docs/editor/getting-started/overview) | أساس محرر محتوى قابل للتوسعة والتخصيص. | افحص تراخيص الامتدادات والخدمات وحدود التعاون؛ التعقيم والإصدارات والتصدير مسؤوليات تكامل مستقلة. |
| `LEXICAL` | [Lexical](https://lexical.dev/docs/intro) | بديل لمحرك تحرير محتوى مع نموذج منظم وامتدادات. | لا تفترض أنه محرر جاهز بكل الأدوات؛ ربط النموذج والتنقية والواجهة واختبارات العربية مطلوب. |
| `CKEDITOR` | [CKEditor 5](https://github.com/ckeditor/ckeditor5) | بديل محرر غني عندما تناسبه متطلبات المشروع. | راجع الترخيص ونطاق الميزات والخدمات قبل التثبيت؛ لا تفترض أن كل القدرات متاحة بنفس الرخصة. |
| `CMDK` | [cmdk](https://github.com/dip/cmdk) | مكوّن قائمة أوامر قابل للتخصيص في React. | لا يوفر فهرس بحث أو ACL أو تنفيذ أوامر موثوقًا؛ تحقّق من نمط الوصولية في التركيب المختار. |
| `REACT_FLOW` | [React Flow / @xyflow/react](https://reactflow.dev/) | بناء واجهات عقد وروابط ومحررات مخططات عند الحاجة. | المخطط ليس محرك Workflow، والتعريفات يجب أن تُتحقق وتنفذ في خدمات الأعمال. |
| `JSONDIFFPATCH` | [jsondiffpatch](https://github.com/benjamine/jsondiffpatch) | حساب وعرض فروق كائنات JSON ضمن سياسة المجال. | ليس سجل تدقيق أو آلية نزاهة؛ لا تمرر patches غير موثوقة مباشرة إلى بيانات الأعمال. |
| `REACT_NUMBER_FORMAT` | [react-number-format](https://s-yadav.github.io/react-number-format/docs/intro/) | تنسيق مدخلات رقمية مع إدارة موضع المؤشر. | ليس محرك حساب مالي؛ القيمة المعيارية والدقة والتحقق الخادمي تبقى مستقلة. |
| `DECIMALJS` | [decimal.js](https://mikemcl.github.io/decimal.js/) | حساب عشري عند الحاجة إلى دقة محددة. | تحديد precision وrounding وتمرير سلاسل دقيقة مطلوب؛ لا يصلح فقد الدقة الذي حدث قبل دخوله. |
| `PHONE_INPUT` | [react-phone-number-input](https://catamphetamine.gitlab.io/react-phone-number-input/) | واجهة إدخال هاتف دولي في React. | تنسيق رقم لا يثبت نشاطه أو ملكيته؛ تحقق من بيانات المناطق والامتدادات وسياسة التخزين. |
| `LIBPHONENUMBER` | [libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) | تحليل وتنسيق والتحقق البنيوي من الهواتف ضمن بيانات المكتبة. | بيانات الترقيم تحتاج تحديثًا وتوافقًا؛ لا تثبت صلاحية التسليم أو هوية المتلقي. |
| `INPUT_OTP` | [input-otp](https://input-otp.rodz.dev/) | إدخال رمز تحقق في React مع قابلية تخصيص العرض. | لا ينشئ أو يرسل أو يتحقق من الرمز في الخادم؛ طبقة الأمان والمهلات والمحاولات مستقلة. |
| `PAPA_PARSE` | [Papa Parse](https://www.papaparse.com/docs) | تحليل وتصدير CSV مع خيارات ترميز وفواصل مناسبة. | لا يستبدل تحقق الأعمال ولا يعالج Excel بذاته؛ اختبر منع حقن الصيغ وفق العميل المستهدف. |
| `EXCELJS` | [ExcelJS](https://github.com/exceljs/exceljs) | التعامل مع ملفات workbook في البيئات والميزات المدعومة. | اختبر حجم الملف وأنواع الخلايا والتواريخ؛ لا تستخدمه لتقييم صيغ أو macros غير موثوقة. |
| `LARAVEL_EXCEL` | [Laravel Excel](https://docs.laravel-excel.com/) | تكامل استيراد وتصدير مناسب لبعض مشاريع Laravel. | راجع إصدار PHP وLaravel والمكتبة وسياسة معالجة الصفوف والمهام، ولا تفترض توافق جميع الإصدارات. |
| `ECHARTS` | [Apache ECharts](https://echarts.apache.org/en/index.html) | رسم مرئيات متنوعة عند الحاجة إلى مرونة وتحكم. | لا يحسب حقيقة KPI ولا يمنح الوصولية كاملة دون بديل نصي؛ اختبر canvas أو SVG بحسب الحجم. |
| `RECHARTS` | [Recharts](https://recharts.github.io/) | خيار رسوم مناسب لمشروعات React. | تحقق من إصدار المشروع ودلالات الرسوم والبديل النصي؛ لا تجمع مكتبات رسم متعددة بلا مبرر. |
| `CHARTJS` | [Chart.js](https://www.chartjs.org/docs/latest/) | بديل رسوم JavaScript يدمج مع إطار الواجهة المناسب. | حدد wrapper إن احتاجه المشروع واختبر الأداء والبديل المتاح للبيانات. |
| `DNDKIT` | [dnd kit](https://dndkit.com/) | أساس للسحب والإفلات مع adapters بحسب التقنية والإصدار. | أسماء الحزم وواجهاتها تختلف عبر الأجيال؛ اختر adapter الموثق للإصدار المثبت ولا تخلط أمثلة أجيال مختلفة. |
| `FULLCALENDAR` | [FullCalendar](https://fullcalendar.io/docs) | واجهة تقويم وجدولة مع عروض وملحقات متعددة. | راجع رخصة الموارد وTimeline والقدرات المتقدمة؛ العربية ليست إثبات أم القرى أو التكرار الهجري. |
| `REACT_BIG_CALENDAR` | [React Big Calendar](https://github.com/bigcalendar/react-big-calendar) | بديل عرض مواعيد لتطبيقات React. | localizer وإدارة المناطق والتكرار والتعارض مسؤوليات تكامل؛ لا تفترض دعم أم القرى المطلوب. |
| `IDB` | [idb](https://github.com/jakearchibald/idb) | واجهة Promise للعمل مع IndexedDB عند اعتماد تخزين محلي. | لا توفر وحدها تشفيرًا أو تفويضًا أو مزامنة، ولا تُستخدم للمحتوى الحساس دون سياسة. |
| `RESIZABLE_PANELS` | [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) | لوحات قابلة لتغيير الحجم في React. | اختبر الفاصل باللمس ولوحة المفاتيح وحدود الأحجام وحفظ التخطيط قبل الاعتماد. |
