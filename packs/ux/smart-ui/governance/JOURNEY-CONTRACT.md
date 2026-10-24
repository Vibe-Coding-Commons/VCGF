# VCGF Smart Journey Contract

**الإصدار:** 1.0.0 — **الحالة:** `final-integration-candidate`

## المبدأ

Journey Standard يصف انتقالًا متعدد النقاط بين شاشات أو مراحل. لا يصف زرًا ولا مكوّنًا ولا صفحة منفردة. وجود Journey في الكتالوج لا يفعله تلقائيًا.

## العقد الإلزامي

كل رحلة تعرف: `entry`, `stages`, `authority`, `context`, `success`, `failure`, `cancel`, `resume`, `completion`, `return`. يجب أن تكون نقطة الاستمرار قابلة للتحقق، والعودة لا تعتمد على browser history وحده عندما يكون أصل المهمة مهمًا.

## استقلال الطبقات

- Journey لا يفعّل Screen Composition.
- Journey لا يفعّل Component.
- Journey لا يفعّل Interaction Pattern.
- العلاقات في العقد Review hints فقط.

## الأمان

الرابط العميق لا يثبت الصلاحية، وReturn URL لا يقبل open redirect، وتبديل tenant أو role يبطل السياق غير الموافق.

## الأدلة

تبقى `application_tests: not_run` حتى تنفيذ الرحلة في تطبيق مستهدف وجمع Evidence عبر Integration/E2E/Accessibility/Security حسب الخطر.
