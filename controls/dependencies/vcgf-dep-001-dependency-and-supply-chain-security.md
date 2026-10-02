---
id: VCGF-DEP-001
title: Dependency and Supply-Chain Security
domain: dependencies
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

# VCGF-DEP-001 - Dependency and Supply-Chain Security

**Control ID:** VCGF-DEP-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Dependencies MUST be justified, verified, locked where practical, reviewed for maintenance and security risk, and MUST NOT be invented by an AI agent.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for dependency and supply-chain security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Dependency and Software Supply Chain Security

Before adding a dependency ask:
- is it necessary?
- can existing platform/library functionality handle it?
- is it maintained?
- is the package name correct and not a typosquat?
- what runtime permissions does it need?
- how much attack surface does it add?

Use lockfiles and reproducible package management.

Do not casually delete lockfiles to fix conflicts.

Separate major upgrades from unrelated features when practical.

Review security advisories.

Treat install/postinstall scripts as higher risk.

Protect deployment tokens, build secrets, artifacts, and review gates.

AI must not invent packages merely because a name sounds plausible.

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
