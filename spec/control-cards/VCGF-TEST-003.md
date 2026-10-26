<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/testing/vcgf-test-003-security-regression-review.md -->
# VCGF-TEST-003 — Security Regression Review
MUST · testing · profiles: high-assurance, production · full text: controls/testing/vcgf-test-003-security-regression-review.md

## Requirement
Changes MUST be checked for regression in authentication, authorization, validation, data isolation, security headers, secrets, logging, and critical workflows.

## Guidance
Verify the change did not:
- disable RLS/grants
- broaden roles
- expose secrets
- make storage public
- expose new API fields
- weaken validation
- remove rate limits
- weaken cookie/security headers
- create unprotected admin routes
- bypass tenant filters
- log PII/tokens
- allow unsafe redirects
- introduce raw SQL
- add risky dependencies
- expose reset tokens
- change encryption key handling unsafely

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
