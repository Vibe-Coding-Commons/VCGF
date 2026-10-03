<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 20. Strong Authentication Capability  عند وجود Authentication، يجب أن يستطيع VCGF تقييم ودعم:  ```text Password + TOTP 2FA + Passkeys / WebAuthn + Recovery Codes + Session Management ```  ## TOTP  يجب أن يكون TOTP معيارًا عامًا يعمل مع التطبيقات المتوافقة، مثل:  - Google Authenticator. - Microsoft Authenticator. - أي TOTP Application متوافق.  ولا يتم بناء Implementation مرتبطًا بجوجل فقط.  ## Passkeys  يتم تنفيذ Passkeys باستخدام:  ```text WebAuthn / FIDO2 ```  ويُفضل استخدامها عند توفرها للعمليات عالية الحساسية بسبب خصائصها المقاومة للتصيد.  المراجع المذكورة:  [W3C — Web Authentication Level 3](https://www.w3.org/news/2026/web-authentication-an-api-for-accessing-public-key-credentials-level-3-is-now-a-w3c-recommendation/?utm_source=chatgpt.com)  [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html?utm_source=chatgpt.com)  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
