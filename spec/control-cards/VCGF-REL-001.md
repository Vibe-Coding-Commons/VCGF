<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/release/vcgf-rel-001-definition-of-done.md -->
# VCGF-REL-001 — Definition of Done
MUST · release · profiles: baseline, high-assurance, production · full text: controls/release/vcgf-rel-001-definition-of-done.md

## Requirement
A change MUST NOT be declared complete until functional, security, regression, and evidence requirements applicable to its risk are satisfied.

## Guidance
A change is not done because the preview looks correct.

Required:
- requirement implemented
- no unintended unrelated changes
- build/type/lint checks pass where applicable
- authoritative server-side validation exists
- error paths tested
- allowed and denied authorization tested
- tenant isolation tested where applicable
- sensitive data exposure reviewed
- logs reviewed for secrets/PII
- database/RLS/storage reviewed when relevant
- rate limiting considered for abuse-prone endpoints
- security scan findings reviewed where available
- regression test added for important defects where practical
- rollback path known for risky changes

Sensitive auth/encryption/admin/recovery/payment changes require preserved test evidence.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
