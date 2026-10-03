<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 25. Device-Bound Session  في **High-Assurance Mode** يمكن دعم تقنيات Device-Bound Session عندما تكون متاحة ومدعومة.  من الأمثلة المذكورة:  **Device Bound Session Credentials في Chrome**  والتي تربط استمرار الجلسة بمفتاح تشفيري خاص بالجهاز.  لكنها تقنية حديثة، لذلك:  - لا تُفرض على جميع المتصفحات. - تستخدم عند توفر الدعم. - يوجد Graceful Degradation. - تستخدم Risk-Based Session Binding عند عدم توفرها.  مرجع:  [Chrome for Developers — Device Bound Session Credentials](https://developer.chrome.com/docs/web-platform/device-bound-session-credentials?hl=ar&utm_source=chatgpt.com)  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
