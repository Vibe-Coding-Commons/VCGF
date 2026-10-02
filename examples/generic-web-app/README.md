<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Generic web application adoption example

## Scenario
A web application has authenticated and anonymous routes, API endpoints, forms, files, external URLs, a database, and routine deployment through CI/CD.

## Recommended adoption
1. Choose Baseline only for genuinely low-risk prototypes; use **Production** for real users, internet exposure, or business data.
2. Document trust boundaries and inspect the existing architecture before AI-generated changes.
3. Create a field-validation matrix and apply server-side validation plus context-appropriate output encoding.
4. Enforce authentication, object authorization, file access, and database integrity at trusted layers.
5. Keep secrets out of source/client code, review dependency provenance, and scan for injection and regression risks.
6. Collect release evidence and run the repository quality gate before declaring the release ready.

## Priority controls
`VCGF-AI-001`, `VCGF-GOV-001`, `VCGF-ARCH-005`, `VCGF-SEC-003`, `VCGF-IAM-007`, `VCGF-SECR-001`, `VCGF-DEP-001`, `VCGF-REL-002`.

## Verification evidence
- Change-impact record and threat model.
- Validation/injection tests.
- Authorization negative tests.
- Dependency and secret review output.
- CI result, release evidence, and monitoring plan.

## Example release decision
A release is blocked when the build passes but authorization negative tests fail, an unverified package was introduced, or a critical security finding remains unresolved without an approved exception.
