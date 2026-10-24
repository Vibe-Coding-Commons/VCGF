# Runtime Evidence & Conformance Model

نجاح وثائق VCGF لا يساوي نجاح التطبيق.

## حالات الأدلة
- `not_run`: لم ينفذ الاختبار في التطبيق.
- `pass`: دليل فعلي صالح ومؤرخ ومرتبط بإصدار التنفيذ.
- `fail`: دليل يثبت عدم تحقق الشرط.
- `blocked`: تعذر التنفيذ بسبب سبب موثق، ولا يعامل كنجاح.

## أنواع الأدلة
Unit، Integration، Contract، E2E، Accessibility manual/automated، Security، Performance، Visual/Responsive، Data migration.

كل Pass يحتاج Evidence Ref صالحًا؛ لا يسمح بتحويل `not_run` إلى `pass` لمجرد أن schema أو package validator نجح.
