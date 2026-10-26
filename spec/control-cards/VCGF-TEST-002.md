<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/testing/vcgf-test-002-secure-code-review.md -->
# VCGF-TEST-002 — Secure Code Review
MUST · testing · profiles: baseline, high-assurance, production · full text: controls/testing/vcgf-test-002-secure-code-review.md

## Requirement
Security-relevant changes MUST receive structured review of trust boundaries, validation, authorization, secrets, data handling, dependencies, errors, and tests.

## Guidance
Ask:
- Is every untrusted input validated on a trusted layer?
- Are queries parameterized?
- Are dynamic identifiers allowlisted?
- Is authorization checked on the exact object/action?
- Can user/tenant IDs be manipulated?
- Are privileged clients necessary?
- Are secrets exposed?
- Is sensitive data logged?
- Is output safely encoded?
- Are unsafe HTML sinks present?
- Can server URL fetches reach internal networks?
- Are files treated as untrusted?
- Is rate limiting needed?
- Are state transitions validated?
- Are money/discounts recalculated server-side?
- Is cryptography standard with managed keys?
- Is password recovery safe?
- Are negative tests included?

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
