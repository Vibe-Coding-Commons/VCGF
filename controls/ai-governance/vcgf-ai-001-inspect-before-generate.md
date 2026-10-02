---
id: VCGF-AI-001
title: Inspect Before Generate
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

# VCGF-AI-001 - Inspect Before Generate

**Control ID:** VCGF-AI-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

AI-assisted changes MUST inspect relevant code, schema, dependencies, interfaces, and established project rules before implementation.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for inspect before generate.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# AI Anti-Hallucination and Change Discipline

Before changing an existing system, the AI must:
1. locate relevant implementation
2. identify database objects
3. identify validation
4. identify authorization
5. identify downstream consumers
6. identify tests
7. state assumptions
8. mark unknowns UNVERIFIED

The AI must not:
- create duplicates because existing code was not found immediately
- invent table/column names
- silently replace packages
- invent roles
- assume a field is public
- trust a browser user ID
- claim testing/scanning without evidence

Use evidence labels:
- VERIFIED
- INFERRED
- UNVERIFIED
- BLOCKED

After repeated failed fixes, stop speculative patching and return to root-cause analysis.

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
