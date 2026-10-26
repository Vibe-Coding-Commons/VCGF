<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-005-output-encoding-and-sanitization.md -->
# VCGF-SEC-005 — Output Encoding and Sanitization
MUST · security · profiles: baseline, high-assurance, production · full text: controls/security/vcgf-sec-005-output-encoding-and-sanitization.md

## Requirement
Untrusted data MUST be encoded or sanitized for its destination context before rendering or interpreter execution.

## Guidance
Validation and output encoding solve different problems.

## Plain text
Prefer framework mechanisms that render values as text rather than HTML.

Encode untrusted data for its exact output context:
- HTML body
- HTML attribute
- URL component
- JavaScript
- CSS
- CSV/spreadsheet
- shell/interpreter

No generic sanitizer is safe for every context.

## Rich HTML
When rich HTML is genuinely required, use a maintained allowlist sanitizer.

Never use raw HTML rendering such as `dangerouslySetInnerHTML` without a justified sanitization boundary.

Do not mutate sanitized HTML with unsafe string operations afterwards.

## URLs
Allow only expected schemes and validate redirect destinations.

## CSP
Content Security Policy is defense in depth, not a replacement for safe rendering.

## Spreadsheet exports
Neutralize user-controlled values that spreadsheet programs could treat as formulas.

## Logs
Secrets should be excluded/redacted, not "sanitized" into logs.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
