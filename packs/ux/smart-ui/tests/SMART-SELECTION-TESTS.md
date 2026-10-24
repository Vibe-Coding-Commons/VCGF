# SMART SELECTION TESTS — v1.0.0

الهدف إثبات أن الطبقات الأربع مستقلة وانتقائية.

- No UI → صفر من جميع الطبقات.
- Component signal only → لا يختار Interaction/Composition/Journey.
- Interaction signal only → لا يختار بقية الطبقات.
- Composition signal only → Primary واحد كحد أقصى + modifiers الصريحة فقط.
- Journey signal only → لا يفعّل شاشة أو مكوّنًا أو تفاعلًا.
- Birthdate → Form + SmartFormFields + explicit interactions + Create→Detail journey + Calendar/Searchable Select.
- Approval → Review composition + explicit approval interactions + Approve/Reject journeys حسب الإشارات.
- Bulk long-running → Bulk + Long-running journeys مع Review relationship فقط.
- Scope switch → Journey مستقل يعيد تقييم tenant/role/context.

يُنفذ المرجع آليًا بواسطة `scripts/validate_selection_layer.py`.
