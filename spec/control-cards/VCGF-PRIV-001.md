<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/privacy/vcgf-priv-001-logging-redaction-and-privacy.md -->
# VCGF-PRIV-001 — Logging Redaction and Privacy
MUST · privacy · profiles: high-assurance, production · full text: controls/privacy/vcgf-priv-001-logging-redaction-and-privacy.md

## Requirement
Logs, telemetry, analytics, URLs, and errors MUST minimize and redact personal, authentication, and secret data.

## Guidance
## Never log
- plaintext passwords
- password hashes
- session cookies
- access/refresh tokens
- API secret keys
- encryption keys
- full password-reset tokens/URLs
- MFA secrets
- unnecessary Restricted PII

## Prefer identifiers
Use request ID, actor ID, tenant ID, resource ID, and event type instead of full payloads.

## Central redaction
Redact authorization headers, cookies, known secret fields, tokens, and personal identifiers centrally.

## Audit logs
Record actor, action, resource, time, result, tenant/context, and correlation ID where appropriate.

Restrict and protect audit logs from tampering.

## Third-party error tools
Scrub sensitive request payloads before sending.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
