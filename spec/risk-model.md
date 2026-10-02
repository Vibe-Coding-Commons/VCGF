<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Risk model

| Level | Typical change | Governance expectation |
|---|---|---|
| LOW | Copy, styling, non-sensitive presentation | Inspect, implement, verify regression |
| MEDIUM | Normal feature or schema-additive change | Impact analysis, tests, review |
| HIGH | Authentication, authorization, sensitive data, external integration, production behavior | Formal plan, human approval, security evidence |
| CRITICAL | Destructive migration, production secrets/infrastructure, security-control disablement, high-impact payment/identity change | Explicit owner approval, rollback/recovery, independent evidence where practical |

Risk is raised by blast radius, data sensitivity, privilege, irreversibility, internet exposure, financial impact, and uncertainty.
