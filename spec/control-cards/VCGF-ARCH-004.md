<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/architecture/vcgf-arch-004-separation-of-concerns.md -->
# VCGF-ARCH-004 — Separation of Concerns
SHOULD · architecture · profiles: high-assurance · full text: controls/architecture/vcgf-arch-004-separation-of-concerns.md

## Requirement
Projects SHOULD maintain clear separation among presentation, state, business logic, security decisions, integration boundaries, and persistence.

## Guidance
Avoid embedding authorization, database migration logic, privileged credentials, or irreversible business decisions only in presentation components.

## References
- VCGF core risk and evidence model
- OWASP guidance where security-relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
