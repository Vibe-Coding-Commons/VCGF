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

# Validation and Injection Audit Prompt

Perform a read-only audit of:
- forms
- APIs
- route/query params
- headers/cookies
- imports
- uploads
- webhooks
- external payloads
- AI outputs

For each input document type/schema, length/range, allowlist, server validation, output encoding, DB use, command/template use, and URL fetch use.

Search for:
- raw SQL concatenation
- dynamic query fragments
- shell execution
- eval/new Function
- unsafe HTML
- weak rich-text sanitizer
- path traversal
- CRLF/header injection
- open redirects
- CSV formula injection
- SSRF
- NoSQL operator injection
- mass assignment

Do not fix yet. Rank by exploitability and impact.
