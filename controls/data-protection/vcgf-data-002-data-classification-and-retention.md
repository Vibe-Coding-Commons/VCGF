---
id: VCGF-DATA-002
title: Data Classification and Retention
domain: data-protection
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

# VCGF-DATA-002 - Data Classification and Retention

**Control ID:** VCGF-DATA-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Projects MUST classify data and define retention and deletion requirements proportionate to sensitivity and business need.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for data classification and retention.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Data Classification and Retention

Every persistent field should have:
- category
- classification
- purpose
- source
- owner
- retention
- deletion behavior
- backup behavior
- encryption requirement
- logging rule
- export rule

## Retention
Do not retain sensitive data indefinitely by default.

## Deletion scope
Consider:
- primary DB
- replicas
- search indexes
- object storage
- caches
- exports
- logs
- backups

If backups cannot delete individual records immediately, document how deleted data is prevented from being restored into active use.

## Test data
Do not copy production PII casually into development or demos. Prefer synthetic/de-identified data.

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
