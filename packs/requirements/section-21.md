<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 21. Email Delivery Engine  بدل برمجة البريد بطريقة مختلفة لكل Feature، أريد **Provider Abstraction**.  يدعم على الأقل:  ```text Generic SMTP over TLS Microsoft 365 via OAuth 2.0 ```  ويفضل دعم:  ```text Microsoft Graph ```  عندما يكون مناسبًا.  لا يُنصح ببناء Integration حديث لـMicrosoft 365 اعتمادًا على Basic Authentication.  مرجع Microsoft:  [Microsoft Learn — OAuth for IMAP, POP and SMTP AUTH](https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth?utm_source=chatgpt.com)  كما يجب أن يشمل Email Delivery Engine عند الحاجة:  - Queue. - Retry. - Timeout. - Logs بدون كشف محتوى حساس. - Templates. - Localization. - From. - Reply-To. - Connection Test. - SPF. - DKIM. - DMARC ضمن Deployment Checklist.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
