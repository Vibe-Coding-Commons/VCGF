<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 23. Single Active Session Policy  أريد دعم سياسة مثل:  ```yaml session_policy:   max_concurrent_sessions: 1   on_new_login: revoke_previous_sessions ```  خصوصًا في:  ```text Admin High-Assurance ```  مثال:  ```text Login من الجهاز A ↓ Session A Active  Login من الجهاز B ↓ Session B Active Session A Revoked Immediately ```  وعند محاولة الجهاز الأول تنفيذ Request:  ```text Session expired because your account was signed in from another device. ```  مع:  - Audit Log. - إمكانية إشعار المستخدم.  ويجب أن تكون السياسة Configurable:  ```yaml concurrent_sessions:   admin: 1   regular_user: configurable ```  لأن بعض التطبيقات تحتاج السماح للمستخدم العادي باستخدام أكثر من جهاز.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
