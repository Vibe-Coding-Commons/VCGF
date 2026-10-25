<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-004-trusted-layer-input-validation.md -->
# VCGF-SEC-004 — Trusted-Layer Input Validation
MUST · security · profiles: baseline, high-assurance, production · full text: controls/security/vcgf-sec-004-trusted-layer-input-validation.md

## Requirement
All data crossing a trust boundary MUST be parsed and validated on a trusted layer before it affects authorization, business logic, persistence, interpreters, or outbound requests.

## Guidance
Every value crossing a trust boundary must be validated on a trusted layer before it influences business logic, queries, authorization, files, or external requests.

Frontend validation improves UX but is never the authoritative security check.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
