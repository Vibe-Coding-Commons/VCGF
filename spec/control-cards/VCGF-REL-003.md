<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/release/vcgf-rel-003-rollback-and-recovery-readiness.md -->
# VCGF-REL-003 — Rollback and Recovery Readiness
MUST · release · profiles: high-assurance, production · full text: controls/release/vcgf-rel-003-rollback-and-recovery-readiness.md

## Requirement
High-risk releases MUST define how code, configuration, schema, and operational state can be recovered if validation fails after deployment.

## Guidance
For irreversible data migrations, use backups, staged rollout, expand-contract patterns, or other documented recovery measures as applicable.

## References
- VCGF core risk and evidence model
- OWASP guidance where security-relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
