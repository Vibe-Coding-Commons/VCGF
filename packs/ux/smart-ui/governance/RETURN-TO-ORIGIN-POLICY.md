# Return-to-Origin Policy

Return-to-origin هو عقد مهمة وليس مجرد `history.back()`.

الأولوية المرجعية:
1. أصل موثق وصالح من نفس نطاق المهمة.
2. وجهة fallback خاصة بالمهمة مثل queue/list/detail.
3. Home آمن فقط عند عدم وجود بديل.

يجب الحفاظ على filters/page/scroll/focus عندما تكون صالحة، وعدم إعادة المستخدم إلى كيان أو tenant لم يعد مخولًا له.
