<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 14. Field Validation & Data Contract Governance  لا يكفي أن يقول VCGF للـAI:  > اعمل Validation.  كل حقل يتم إنشاؤه أو تعديله يجب أن يمتلك **Field Contract** يحدد عند الحاجة:  - Type. - Required / Optional. - Min / Max. - Length. - Allowlist / Enum. - Format. - Normalization. - Uniqueness. - Cross-field Rules. - Business Rules. - PII Classification. - Masking. - Encryption. - Retention. - Error Message.  ### مبادئ التنفيذ  - Client Validation لتحسين تجربة المستخدم. - Server Validation هو المرجع الأمني. - استخدام Database Constraints المناسبة. - رفض الحقول غير المتوقعة لمنع Mass Assignment. - استخدام Parameterized Queries. - إضافة Negative Tests. - إضافة Fuzz Tests للحقول الحساسة.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
