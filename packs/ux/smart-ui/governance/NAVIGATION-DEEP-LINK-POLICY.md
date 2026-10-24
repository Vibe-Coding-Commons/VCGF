# Navigation & Deep-Link Policy

- كل Route محمي يعيد التحقق من الهوية والنطاق والصلاحية.
- Deep Link لا يتجاوز prerequisties ولا يعتبر URL دليلاً على مرحلة العمل.
- Return-to-origin يستخدم معرف وجهة آمنًا أو route descriptor موثوقًا، وليس redirect URL حرًا.
- Back وCancel وFinish وReturn-to-origin معانٍ مستقلة.
- لا تنشئ الواجهة history entry لكل تغير محلي بسيط.
- عند انقضاء الجلسة يحتفظ النظام بنية آمنة فقط ثم يعيد تقييمها بعد المصادقة.
- عند تبديل tenant/role يتم إبطال origin وcache وpending requests غير الصالحة.
