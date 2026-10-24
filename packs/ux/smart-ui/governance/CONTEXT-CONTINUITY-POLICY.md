# Context Continuity Policy

يحفظ VCGF فقط سياق المهمة الضروري للاستمرار: route scope، filters، sort، page/cursor، tab، selected record reference، step، draft reference عند السماح.

لا يحفظ كلمات مرور أو OTP أو tokens أو payload أعمال كاملًا داخل URL/history/local snapshots بلا ضرورة.

الاستعادة دائمًا `validate-then-restore`: يتحقق من صلاحية السجل والمرشح والصفحة والنطاق والنسخة قبل العرض أو الكتابة.

أي Snapshot يحمل `tenant/user/role/scope` binding أو ما يعادله حتى لا ينتقل بين نطاقات مختلفة.
