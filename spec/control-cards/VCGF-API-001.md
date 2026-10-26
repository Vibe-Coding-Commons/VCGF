<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/api/vcgf-api-001-api-and-server-function-security.md -->
# VCGF-API-001 — API and Server Function Security
MUST · api · profiles: baseline, high-assurance, production · full text: controls/api/vcgf-api-001-api-and-server-function-security.md

## Requirement
Every externally callable endpoint or server function MUST independently enforce authentication, authorization, validation, resource limits, and safe error handling as applicable.

## Guidance
Assume every endpoint is directly callable by an attacker.

## Per-endpoint checklist
- authentication
- operation-level authorization
- object-level authorization
- tenant validation
- request schema
- request/body size limit
- input validation
- safe query construction
- rate limiting/quotas
- replay/idempotency where relevant
- minimal response schema
- safe errors
- timeout
- external-call restrictions
- audit logging for sensitive actions

## Privileged DB clients
Use service/admin clients only in trusted server code and only after explicit application authorization.

Prefer user-scoped/RLS-scoped access when possible.

## Mass assignment
Do not pass request JSON directly to persistence for privileged models. Pick allowed fields explicitly.

## Output
Do not return full DB records by default. Use explicit response schemas.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
