<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 35. Automatic Pre-Migration Backup  عند قيام الـAI بعملية مثل:  ```text Destructive Migration Major Schema Change Bulk Data Update Production Migration ```  يجب على VCGF فحص:  > هل توجد Backup صالحة وحديثة؟  وفي المشاريع الحساسة:  ```text No Valid Backup ↓ Block Migration ↓ Create / Request Backup ↓ Verify ↓ Continue ```  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
