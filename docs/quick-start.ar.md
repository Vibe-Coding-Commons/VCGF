<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# البدء السريع

1. اختر Profile مناسبًا: `baseline` أو `production` أو `high-assurance`.
2. اختر Adapter المنصة أو `generic` عند عدم وجود Adapter مخصص.
3. ثبّت ملفات التعليمات الخاصة بالمنصة كما هو موضح في `platforms/<adapter>/INSTALLATION.md`.
4. أكمل قوالب سياق المشروع والصلاحيات وتصنيف البيانات والـValidation والـThreat Model حسب النطاق.
5. اتبع دورة VCGF: Understand → Inspect → Impact/Risk Analysis → Plan → Approval → Implement → Validate/Test → Security/Regression/Release Review → Release → Monitor.
6. نفذ `python scripts/release-quality-gate.py` للتحقق من Repository الخاص بـVCGF عند المساهمة في الإطار.
7. لا تدّع Conformance لمشروعك إلا بوجود Evidence وExceptions صحيحة لكل Controls المطلوبة.
