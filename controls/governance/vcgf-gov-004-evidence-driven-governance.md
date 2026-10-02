---
id: VCGF-GOV-004
title: Evidence-Driven Governance
domain: governance
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
- production
---

<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF-GOV-004 - Evidence-Driven Governance

**Control ID:** VCGF-GOV-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Conformance claims MUST be supported by evidence rather than by the presence of documentation alone.

## Purpose

Reduce AI-assisted engineering risk through a stable vendor-neutral requirement.

## Risk Addressed

Unauthorized change, security weakening, data exposure, architecture drift, integrity loss, or insufficient auditability.

## Rationale

VCGF separates normative policy from platform implementation so this requirement can be consistently enforced or evidenced across tools.

## Applicability

Apply according to project risk, selected profile, and affected trust boundaries.

## Implementation-Neutral Guidance

Evidence may include test output, CI status, code review, configuration snapshots, audit logs, scan results, migration dry-runs, or manual verification. Evidence must identify framework, profile, adapter, and control where practical.

## Verification Method

Review the change, applicable configuration, test evidence, approval record, and platform mapping.

## Required Evidence

A reproducible review, test, configuration record, or approval artifact appropriate to the control.

## Exceptions

Exceptions follow `spec/exception-management.md`.

## Dependencies

VCGF-GOV-001 and VCGF-GOV-004 where applicable.

## Related Controls

See the selected profile and control catalog.

## References

- VCGF core risk and evidence model
- OWASP guidance where security-relevant

## Platform Considerations

Adapters may classify enforcement as native, configurable, prompt-enforced, external, partial, unsupported, not-applicable, or unverified.

## Change History

- 1.0.0: Initial control.
