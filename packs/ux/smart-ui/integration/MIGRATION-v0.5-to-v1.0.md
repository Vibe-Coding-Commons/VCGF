# Migration: Smart UI v0.5.0 → v1.0.0

## Screen Context
أضف الحقول المطلوبة: `journey_signals`, `entry_channel`, `completion_expectation`, `context_continuity`.

## Selection Plan
أضف: `journey_pattern_count`, `selected_journeys`, `journey_reviews`, `not_selected_journey_count`, `journey_status`, `experience_orchestration`.

لا تحول إشارات Interaction القديمة إلى Journey تلقائيًا؛ أضف Journey فقط عندما تكون المهمة متعددة الشاشات/المراحل مثبتة.

## Runtime
لا يحتاج التطبيق إلى تنفيذ كل الرحلات. حمّل فقط المسارات المذكورة في `standards_to_load`.
