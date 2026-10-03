<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami -->

# 37. Attachment Folder Organization  يفضل تنظيم الملفات باستخدام Tenant / Workspace قبل التاريخ.  مثال:  ```text attachments/ └── tenant-id/     └── workspace-id/         └── 2026/             └── 10/                 └── 03/                     ├── uuid-1.pdf                     ├── uuid-2.jpg                     └── uuid-3.docx ```  بدلًا من:  ```text 2026/10/03/original-file-name.pdf ```  ويفضل أن يكون اسم التخزين:  ```text UUID ```  مع حفظ الاسم الأصلي داخل Metadata / Database.  مثال:  ```text stored_name: original_name: mime_type: size: checksum: owner_id: workspace_id: uploaded_at: ```  هذا يقلل مشكلات:  - Name Collision. - Path Traversal. - أسماء الملفات الخطرة. - كشف أسماء ملفات المستخدمين.  لكن:  > تنظيم `Year/Month/Day` جيد للإدارة والحفظ، لكنه ليس Security Boundary بحد ذاته.  ---  

## Verification boundary

This file preserves original requirements. Each requirement needs applicable implementation evidence or a justified N/A. Presence of this document is not implementation or successful testing. D10 and D12 in continuation approval govern email/backup and recovery objectives.
