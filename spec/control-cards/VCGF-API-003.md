<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/api/vcgf-api-003-rate-limiting-and-abuse-prevention.md -->
# VCGF-API-003 — Rate Limiting and Abuse Prevention
MUST · api · profiles: high-assurance, production · full text: controls/api/vcgf-api-003-rate-limiting-and-abuse-prevention.md

## Requirement
Abuse-sensitive and resource-intensive endpoints MUST apply proportionate rate, quota, size, and concurrency protections.

## Guidance
Candidate endpoints:
- login
- password reset
- signup
- OTP/MFA
- search
- AI generation
- upload
- export
- webhooks
- email/SMS
- invitations
- expensive reports
- payments
- public APIs

Define:
- subject/key
- window
- burst limit
- sustained limit
- response behavior
- internal exceptions
- monitoring

Distributed apps need shared enforcement state.

Additional controls may include CAPTCHA/challenges, quotas, per-tenant limits, idempotency keys, queues, circuit breakers, and cost ceilings.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
