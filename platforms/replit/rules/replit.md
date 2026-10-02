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

# VCGF Project Rules

You are operating under VCGF. Before implementation: understand the request, inspect the existing system, perform impact and risk analysis, and identify applicable controls.

Mandatory behavior:
- do not guess schemas, APIs, libraries, roles, secrets, or platform capabilities;
- do not perform unrelated refactoring;
- do not weaken security to make functionality work;
- validate untrusted input on a trusted layer;
- enforce authorization on a trusted layer;
- treat personal data according to classification and encryption requirements;
- keep secrets out of client code, source, logs, URLs, and prompts;
- do not perform destructive database, authentication, authorization, production, secret, payment, or infrastructure changes without required approval;
- test both positive and negative security paths;
- collect evidence before declaring a change complete.

Use canonical controls in `controls/`; this rule file is an adapter, not the source of policy.

## Replit project context

Keep architecture, conventions, important packages, and project-specific constraints concise and current.
