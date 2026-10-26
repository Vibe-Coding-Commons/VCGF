<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/identity-access/vcgf-iam-001-enumeration-and-brute-force-resistance.md -->
# VCGF-IAM-001 — Enumeration and Brute-Force Resistance
MUST · identity-access · profiles: high-assurance, production · full text: controls/identity-access/vcgf-iam-001-enumeration-and-brute-force-resistance.md

## Requirement
Authentication and recovery flows MUST resist account enumeration, credential guessing, automated abuse, and excessive attempts.

## Guidance
## Enumeration
Use generic responses for login failure, password reset, recovery, and sensitive invitation lookups.

Avoid meaningful timing differences.

## Rate limiting
Use layered controls based on:
- source
- account target
- device/session
- endpoint
- tenant
- API key

Do not rely only on IP.

## Lockout
Avoid designs allowing attackers to permanently lock victims out. Prefer progressive throttling, delays, risk challenges, and alerts.

## Credential stuffing
Use breached-password defenses, MFA, throttling, and anomaly controls where available.

## Logging
Record abuse signals without storing plaintext credentials or excessive PII.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
