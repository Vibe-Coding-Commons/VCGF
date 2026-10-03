<!--
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
-->

# إرسال نقطة التطوير عبر GitHub Desktop

1. فك الحزمة وانسخ محتويات مجلد `VCGF` إلى جذر نسختك الحالية من المستودع، حيث يوجد `README.md`. تجنب إنشاء مجلد `VCGF` متداخل.
2. افتح المستودع في GitHub Desktop، ويفضل استخدام فرع `development/v1.1`. راجع Changes، وبالأخص `README.md` و`README.ar.md` و`CHANGELOG.md`، قبل تحديد الملفات المراد إرسالها.
3. عند إرسال نقطة التطوير كاملة، انسخ النصين التاليين إلى Summary وDescription.

**Summary**

```text
feat: add VCGF v1.1 development checkpoint and bilingual docs
```

**Description**

```text
Add opt-in runtime routing, contracts and scoped evidence gates.
Include reference email and backup integrations and adapter candidates.
Update Arabic and English README with features, usage and version status.
Preserve canonical Control IDs, Profiles, license and founder rights.

Status: v1.1 development checkpoint; not a final release.
Live provider/platform verification and remaining acceptance are open.
```

إذا سبق إرسال بقية نقطة التطوير، استخدم بدلًا منه عنوانًا يصف فرق التوثيق فقط: `docs: update bilingual README and v1.1 development changelog`.

4. اضغط **Commit to [اسم الفرع]** لحفظ التغيير محليًا، ثم **Push origin** لإرساله إلى GitHub؛ وقد يظهر **Publish branch** إذا كان الفرع جديدًا. رفع الفرع لا ينشئ Release أو Tag تلقائيًا.

يبقى `VERSION` بالقيمة `1.0.0`، ويسجل `CHANGELOG.md` الهدف `1.1.0` تحت `Unreleased` إلى اكتمال قبول الإصدار. راجع سجل التحقق الحالي في `project-history/v1.1.0/documentation-test-evidence.json`.

مرجع: https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop
مرجع الالتزام والإرسال: https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop
