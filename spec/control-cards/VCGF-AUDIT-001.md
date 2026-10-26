<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/logging-auditing/vcgf-audit-001-secure-errors-and-diagnostic-logging.md -->
# VCGF-AUDIT-001 — Secure Errors and Diagnostic Logging
MUST · logging-auditing · profiles: high-assurance, production · full text: controls/logging-auditing/vcgf-audit-001-secure-errors-and-diagnostic-logging.md

## Requirement
User-facing errors MUST avoid sensitive internals while trusted diagnostic logging preserves sufficient evidence without secrets or unnecessary personal data.

## Guidance
## User-facing errors
Never expose stack traces, SQL, filesystem paths, secret values, internal hostnames, or debug dumps.

## Server logs
Use correlation ID, operation, safe resource IDs, actor/tenant IDs where permitted.

## Security events
Log:
- repeated auth failure
- reset initiation/completion
- MFA changes
- role changes
- permission denials
- admin actions
- key/security configuration changes
- suspicious exports/downloads
- session revocations

Do not turn logs into a second sensitive-data store.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
