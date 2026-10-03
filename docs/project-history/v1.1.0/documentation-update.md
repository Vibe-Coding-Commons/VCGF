<!--
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
-->

# تحديث التوثيق — 2026-10-03

استجابة لطلب المستخدم، أضيف إلى README.md وREADME.ar.md بيان الإصدار الحالي والهدف، وما الجديد واستخداماته وحدود التحقق، وأوامر Runtime، وروابط الأدلة والأعمال المفتوحة. أضيف قسم Unreleased إلى CHANGELOG.md ودليل GitHub Desktop في docs/github-desktop-update.ar.md.

نجحت ستة مدققات: documentation، internal-links، attribution، version، cross-references، license. ونجحت 97 حالة من tests/contracts/test_phase1.py. يسجل documentation-test-evidence.json الأوامر والمخرجات وبيئة Python وبصمة الاختبار. لا تعاد نسبة نتائج التكامل السابقة إلى هذا التعديل.

اختبار التوافق استثنى فقط ملفات التوثيق الأصلية الثلاثة المعتمدة، ببصمات محددة في documentation-approval.json. بقيت بصمات الملفات الأصلية الأخرى وعددها 380 كما هي، وبقيت نسخة المرجع المجمدة دون تعديل. لم يتغير كود Runtime أو Control IDs أو Profiles أو الترخيص أو حقوق المؤسس أو VERSION.

continuation-change-manifest.json وcontinuation-test-evidence.json سجلان تاريخيان لنقطة التطوير السابقة؛ لا يصفان بصمات هذا التحديث كاملة. يسجل documentation-change-manifest.json الفرق عن تلك النقطة، ويستثني نفسه من قائمته.

الأساس v1.0.0 والهدف v1.1.0 Unreleased. تبقى الأعمال المفتوحة في open-items.json دون تأجيلات جديدة. لم يحدث Push أو نشر إصدار في هذه المهمة.
