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

# Dependency and Supply Chain Audit Prompt

Perform a read-only review.

Identify:
- direct dependencies
- lockfile status
- vulnerable/outdated high-risk packages
- unused dependencies
- suspicious/typosquat names
- install/postinstall scripts
- broad runtime privileges
- libraries handling auth/crypto/files/parsing

Do not upgrade everything automatically.

Propose isolated upgrades with compatibility/test impact.
