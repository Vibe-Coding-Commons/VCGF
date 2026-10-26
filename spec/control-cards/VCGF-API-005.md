<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/api/vcgf-api-005-third-party-integration-security.md -->
# VCGF-API-005 — Third-Party Integration Security
MUST · api · profiles: high-assurance, production · full text: controls/api/vcgf-api-005-third-party-integration-security.md

## Requirement
Third-party integrations MUST validate trust boundaries, credentials, scopes, payloads, callbacks, failures, timeouts, and data exposure.

## Guidance
External providers are separate trust boundaries.

## Credentials
Use minimum scopes, keep private credentials server-side, rotate/revoke unused credentials.

## Incoming
Validate webhook signatures and payload schemas. Treat fields as untrusted.

## Outgoing
Send only minimum necessary personal/sensitive data and document third-party sharing.

## Failure
External API failures must not leave partial business transactions inconsistent. Use retries carefully and idempotency where needed.

## OAuth/OIDC
Use exact redirect URIs and protocol state/nonce protections. Do not implement protocol cryptography from scratch.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
