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

# Change Impact Analysis Prompt

Analyze the requested change before implementation. Do not write code yet.

Report:
1. current implementation
2. affected files/components
3. database objects
4. APIs
5. roles/permissions
6. personal/sensitive data impact
7. validation requirements
8. injection/SSRF/file risks
9. encryption/key impact
10. compatibility
11. migration
12. test plan
13. rollback
14. minimum safe implementation

Mark unknowns UNVERIFIED.

If the change can weaken security or destroy data, state it before implementation.
