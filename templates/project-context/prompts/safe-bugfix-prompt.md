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

# Safe Bugfix Prompt

Fix the issue without speculative rewrites.

1. reproduce
2. capture error/log/network evidence
3. identify root cause
4. locate intended existing behavior
5. identify security impact
6. apply smallest targeted fix
7. rerun original scenario
8. regression tests
9. verify auth/validation/data exposure did not weaken

Never disable security to remove an error.

If root cause remains uncertain, report uncertainty instead of stacking guesses.
