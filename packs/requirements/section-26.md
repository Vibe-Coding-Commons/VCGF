<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 26. Script & Application Protection Pack  لا يجب اعتبار:  ```text Obfuscation ```  حماية أمنية حقيقية بحد ذاتها.  JavaScript الذي يصل إلى المتصفح لا يمكن اعتباره Secret.  يجب أن تشمل الحماية الفعلية عند انطباقها:  - عدم وجود Secrets في Client. - CSP قوية. - SRI للسكريبتات الخارجية المناسبة. - Dependency Pinning. - Lockfile Integrity. - SBOM. - Dependency Scanning. - Trusted Types حيث يناسب. - Security Headers. - التحكم في Source Maps في Production. - Signed Release Artifacts. - Hashed Release Artifacts. - Provenance. - File Integrity. - منع الـAI من إضافة CDN أو Script أو Package جديد دون فحص.  يمكن استخدام:  ```text Obfuscation Minification ```  كطبقة إضافية فقط، وليس كـSecurity Control أساسي.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
