---
id: VCGF-AI-002
title: No Silent Assumptions
domain: ai-governance
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
- baseline
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

# VCGF-AI-002 - No Silent Assumptions

**Control ID:** VCGF-AI-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

An AI agent MUST distinguish verified project facts from assumptions and MUST NOT silently invent schemas, endpoints, roles, environment variables, integrations, libraries, or business rules.

## Purpose

Reduce AI-assisted engineering risk through a stable vendor-neutral requirement.

## Risk Addressed

Unauthorized change, security weakening, data exposure, architecture drift, integrity loss, or insufficient auditability.

## Rationale

VCGF separates normative policy from platform implementation so this requirement can be consistently enforced or evidenced across tools.

## Applicability

Apply according to project risk, selected profile, and affected trust boundaries.

## Implementation-Neutral Guidance

When a material fact cannot be verified, mark it UNVERIFIED or REQUIRES VERIFICATION and avoid destructive or security-sensitive implementation based on the assumption.

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
