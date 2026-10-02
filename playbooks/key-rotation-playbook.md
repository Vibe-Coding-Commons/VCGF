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

# Key Rotation Playbook

1. inventory affected encrypted fields
2. create new key/version in approved KMS/vault
3. send new writes to new key
4. retain controlled old-key reads
5. re-encrypt in bounded batches
6. verify counts/integrity
7. monitor failures
8. stop old-key writes
9. retire old key after verification/rollback window
10. record completion

Suspected compromise accelerates the process and is treated as an incident.
