<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 19. Sensitive Settings Re-Authentication / Step-Up Authentication  لا يجب أن يكفي وجود Session مفتوحة للوصول إلى الإعدادات شديدة الحساسية.  يشمل ذلك صفحات مثل:  ```text Security Settings Users & Roles Authentication Settings Email Settings Backup Settings API Keys Secrets Password / MFA / Passkeys ```  يجب تقييم الحاجة إلى **Recent Authentication** باستخدام:  - Password. - Passkey. - MFA عند الحاجة.  وذلك خصوصًا للعمليات عالية الحساسية.  مرجع OWASP:  [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html?utm_source=chatgpt.com)  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
