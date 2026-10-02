<!--
VCGF - Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Author: Eng. Hamada Sami
Mobile + WhatsApp: +966560000934
Email: i@hamada.io
LinkedIn: https://www.linkedin.com/in/hamadas/
GitHub: https://github.com/Vibe-Coding-Commons
-->

# PII and Encryption Audit Prompt

Perform a read-only personal-data audit.

Inventory each personal/sensitive field and classify:
Public / Internal / Confidential / Restricted.

For each field report:
- location
- purpose
- access
- storage
- transport protection
- logs
- URLs
- exports
- retention
- backup handling
- storage-at-rest
- field-encryption need
- search/index need

Flag:
- plaintext Restricted PII
- keys stored with data
- plaintext low-entropy lookup hashes
- browser-side decryption
- secrets in logs
- unnecessary collection
- excessive retention
- public exports/storage

Do not implement crypto automatically. Propose migration and key rotation first.
