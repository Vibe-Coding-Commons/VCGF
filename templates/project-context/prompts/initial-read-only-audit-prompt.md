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

# Initial Read-Only Architecture & Security Audit Prompt

Before making ANY changes, perform a comprehensive READ-ONLY audit.

DO NOT modify code, schema, RLS, storage, secrets, dependencies, or configuration.

Inspect:
1. architecture/routes
2. schema/relationships/constraints/indexes
3. authentication
4. authorization/roles
5. RLS/grants
6. APIs/functions
7. secrets
8. file/storage
9. validation
10. SQL/NoSQL/command/template/XSS risk
11. SSRF/external URLs
12. password reset/recovery
13. MFA/session
14. PII/sensitive data
15. encryption/key management
16. logs/error tracking
17. dependencies
18. tenant isolation
19. tests
20. deployment/release controls

For each finding:
- ID
- severity
- verified evidence
- affected component
- scenario
- recommended correction
- regression risk

Label unsupported assumptions UNVERIFIED.

Do not automatically fix findings.
