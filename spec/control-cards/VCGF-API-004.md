<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/api/vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md -->
# VCGF-API-004 — SSRF, CSRF, CORS and Webhook Security
MUST · api · profiles: high-assurance, production · full text: controls/api/vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md

## Requirement
Outbound fetches, browser state-changing requests, cross-origin access, and webhooks MUST use threat-appropriate controls for SSRF, CSRF, origin policy, signatures, replay, and schema validation.

## Guidance
## SSRF
For server URL fetches:
- allowlist destinations where feasible
- block localhost/private/link-local/cloud-metadata networks
- validate DNS-resolved addresses
- re-check redirected destinations
- limit schemes/ports
- timeouts and response-size limits
- never forward internal credentials

## CSRF
For cookie-authenticated state changes, use framework CSRF protections and appropriate SameSite behavior.

Do not disable CSRF merely to fix integrations.

## CORS
CORS is not authentication.

Use exact trusted origins for credentialed requests. Avoid arbitrary Origin reflection.

## Webhooks
- verify provider signature
- use raw bytes when signature scheme requires
- validate timestamp/replay window where supported
- idempotent processing
- validate event type and schema
- secret-looking URLs alone are not trust

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
