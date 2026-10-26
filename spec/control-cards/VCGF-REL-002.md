<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/release/vcgf-rel-002-pre-release-security-gate.md -->
# VCGF-REL-002 — Pre-Release Security Gate
MUST · release · profiles: high-assurance, production · full text: controls/release/vcgf-rel-002-pre-release-security-gate.md

## Requirement
Production release MUST be blocked when unresolved critical security, authorization, secret exposure, destructive migration, or required evidence failures remain.

## Guidance
Production release is blocked by unresolved Critical findings.

High findings require remediation or an explicitly approved, time-bounded exception.

## Identity
- login controls reviewed
- password/recovery reviewed
- MFA for privileged access
- session invalidation works

## Authorization
- object authorization
- tenant isolation
- RLS/grants
- admin audit

## Validation/Injection
- server validation
- parameterized queries
- unsafe HTML reviewed
- SSRF endpoints reviewed
- file validation

## Data protection
- classification
- encryption decisions
- keys protected
- logs redacted
- exports private
- backups protected

## API
- endpoint auth/authz
- rate limits
- safe errors
- webhooks
- request limits/timeouts

## Supply chain
- secret scan
- dependency review
- no client-exposed privileged keys

## Testing
- critical paths
- negative auth tests
- regression tests
- platform security scan reviewed where available

## Release
- migration plan
- rollback/forward-fix plan
- monitoring
- incident owner

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
