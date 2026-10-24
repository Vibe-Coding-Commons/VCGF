# ابدأ من هنا — VCGF Smart UI v1.0.0

1. اقرأ `governance/MASTER-POLICY.md`.
2. أنشئ Screen Context مطابقًا لـ`schemas/screen-context.schema.json`.
3. ضع إشارات كل طبقة بصورة مستقلة.
4. شغّل `python scripts/select_smart_ui.py <context.json>`.
5. حمّل فقط `standards_to_load`.
6. افحص Reuse First قبل أي بناء جديد.
7. نفذ التطبيق ثم اجمع Evidence للحالات المنطبقة.
8. شغّل `python scripts/validate_selection_layer.py` ثم `python scripts/validate_package.py --verify-manifest`.
9. قبل دمج VCGF الرسمي اتبع `governance/FINAL-ADOPTION-GATE.md`.

> لا تعتبر نجاح هذه الحزمة شهادة نجاح Runtime لأي تطبيق.
