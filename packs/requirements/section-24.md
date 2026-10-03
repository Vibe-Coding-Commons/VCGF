<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 24. Session Replay / Cookie Cloning Protection  يجب اعتبار:  # **Session Cookie Theft / Session Replay**  خطرًا مستقلًا.  ولا يجوز الادعاء بأن:  > HttpOnly يمنع Cookies Editor من نسخ Session Cookie.  هذا غير مضمون.  لذلك يجب إضافة مفهوم:  # **Session Replay Resistance**  ويتضمن عند توفر التقنية:  - Cryptographic Device / Session Binding. - Device-Bound Credentials. - New-Device Detection. - Risk Signals. - Session Rotation. - Server-Side Device / Session Record. - Re-authentication عند تغير الجهاز بشكل مشبوه.  ويستخدم **Browser Fingerprint** كـRisk Signal فقط، وليس كعامل وحيد لإبطال الجلسة.  ولا يُنصح بربط Session بشكل صارم بالـIP؛ لأن ذلك قد يسبب مشاكل للمستخدمين الشرعيين.  الهدف هو:  ```text Stolen Cookie ≠ Guaranteed Valid Session ```  وليس:  ```text Whoever owns Cookie = Logged In ```  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
