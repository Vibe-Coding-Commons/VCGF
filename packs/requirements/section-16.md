<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 16. Authentication Capability Dependency Engine  إذا كان المشروع يستخدم:  # **Local Password Authentication**  فلا يعتبر Login مكتملًا دون تقييم **Password Reset** المناسب.  عندها يجب أن يتمكن VCGF من تحميل ما يلزم من:  ```text Authentication Session Security Rate Limiting Email Audit Password Recovery Validation UX ```  أما إذا كان المشروع يستخدم:  ```text Microsoft Entra SSO only ```  فلا يجب اختراع Password Reset محلي.  بل يتم تطبيق Recovery المناسب لموفر الهوية.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
