<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/testing/vcgf-test-004-security-test-strategy.md -->
# VCGF-TEST-004 — Security Test Strategy
MUST · testing · profiles: high-assurance, production · full text: controls/testing/vcgf-test-004-security-test-strategy.md

## Requirement
Projects MUST define a risk-based combination of automated, integration, browser, API, authorization, migration, and manual security verification.

## Guidance
Security testing accompanies functional testing.

## Layers
- static/type/lint
- unit
- integration
- API
- database/RLS
- browser/E2E
- dependency scanning
- secret scanning
- platform security scans
- manual secure code review
- penetration testing for higher-risk releases

## Mandatory negative tests
For sensitive operations test:
- unauthenticated
- wrong user
- wrong tenant
- insufficient role
- malformed input
- oversized input
- replay/duplicate where relevant
- invalid state transition

Every confirmed important security defect should gain a regression test where practical.

Preserve test evidence for sensitive releases.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
