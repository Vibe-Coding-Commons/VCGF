---
id: VCGF-REL-001
title: Definition of Done
domain: release
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

# VCGF-REL-001 - Definition of Done

**Control ID:** VCGF-REL-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

A change MUST NOT be declared complete until functional, security, regression, and evidence requirements applicable to its risk are satisfied.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for definition of done.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Definition of Done

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
