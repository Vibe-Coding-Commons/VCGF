# سياسة اختيار أنماط التفاعل الذكية

**الإصدار:** 0.5.0 — **الحالة:** integration-candidate — **المستهدف:** VCGF 1.3.0

هذه السياسة تضيف طبقة **Smart Interaction Patterns** إلى VCGF. المكوّن يحدد ما الذي يظهر للمستخدم، بينما نمط التفاعل يحدد كيف تتصرف الحالة والبيانات والانتقالات والفشل والتعافي.

## القاعدة الأساسية

لا تُفعّل أي Interaction Pattern لمجرد وجود مكوّن مرتبط أو لأن الشاشة اسمها Create أو Edit. يجب أن توجد **إشارة تفاعل صريحة** في `interaction_signals` أو قاعدة مجال موثقة تثبت الحاجة.

تسلسل القرار:

`Understand task → Detect interaction risks → Match explicit signals → Reuse existing behavior → Select minimum patterns → Review compatibility → Load only selected standards → Implement → Verify`

## أمثلة

- نموذج إنشاء بسيط قد يختار `SmartCreateFlow` و`IdempotentSubmissionProtection` فقط إذا كانت عملية الإنشاء معرضة للتكرار.
- نموذج تعديل طويل قد يختار `SmartEditFlow + UnsavedChangesProtection + ConcurrencyConflictResolution`.
- شاشة قراءة فقط لا تحتاج `EditFlow` أو `UnsavedChangesProtection`.
- وجود Toast لا يعني تفعيل `ErrorRetryRecovery`.
- وجود جدول لا يعني تفعيل `BulkActionExecution` إلا إذا كانت هناك أوامر جماعية فعلًا.
- فقد الاتصال لا يعني تفعيل Offline؛ النمط يحتاج `offline_required` صريحًا.

## فصل الإشارات

`signals` تخص قدرات الواجهة والمكوّنات.

`interaction_signals` تخص انتقالات الحالة والمخاطر والسلوك.

يمكن أن تستخدم الشاشة الاثنين معًا، لكن لا يشتق أحدهما آليًا من الآخر.

## عدم التفعيل التلقائي

علاقات `review_components` وCompatibility هي روابط مراجعة فقط. لا يفعّل Interaction Pattern مكوّنًا، ولا يفعّل Pattern Pattern آخر. أي نمط إضافي يحتاج إشارة مستقلة أو قرارًا موثقًا في تقييم المشروع.

## الأدلة

لكل نمط مختار سجّل:
- الإشارات المطابقة.
- سبب الانطباق.
- مصدر السلطة.
- مخطط الحالة المقصود.
- ما إذا كان السلوك موجودًا ويمكن `reuse/extend/wrap/replace/build_new/verify_first`.
- حالات الفشل والتعارض والصلاحية.
- اختبارات القبول والأدلة بعد التنفيذ.

راجع [عقد النمط](INTERACTION-CONTRACT.md) و[مصفوفة التوافق](INTERACTION-COMPATIBILITY.md).


## فصل Screen Composition

`composition_signals` لا تفعّل Interaction Patterns. فاختيار `ReviewApproval` لا يثبت وجود `Confirmation`, `StepUp`, أو `ConcurrencyConflict`; كل نمط يحتاج `interaction_signals` الخاصة به. والعكس صحيح: وجود Conflict Resolution لا يفرض Archetype معينًا.

التركيب يحدد أين وكيف تظهر الحالة ضمن المهمة، بينما Interaction Pattern يحدد آلة الحالة والسلطة والفشل والتعافي.
