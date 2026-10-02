---
id: VCGF-DB-001
title: Database Change Governance
domain: database
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

# VCGF-DB-001 - Database Change Governance

**Control ID:** VCGF-DB-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Schema and data migrations MUST be inspected for compatibility, integrity, authorization, rollback, data-loss, locking, and operational risk before execution.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for database change governance.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Database Change Policy

Database changes are high impact.

Before migration inspect:
- schema
- constraints
- relationships
- indexes
- RLS
- grants
- views
- functions/triggers
- application references
- reports/exports

Prefer additive, backward-compatible, reversible/staged changes.

Prohibited without explicit approval:
- DROP/TRUNCATE
- destructive rename
- broad policy removal
- making private data public
- permanently disabling integrity constraints

Backfill safely before enforcing new NOT NULL/constraints.

Document rollback or forward-fix plan before release.

## Verification Method

Inspect implementation and configuration, execute positive and negative tests appropriate to the control, and review evidence at the trusted enforcement layer.

## Required Evidence

At least one reproducible artifact such as a test result, code review, configuration record, security scan, migration review, or manual verification record.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, and applicable architecture or identity controls.

## Related Controls

See the domain index and selected profile.

## References

- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Change History

- 1.0.0: Initial VCGF control migrated and normalized from the previous framework.
