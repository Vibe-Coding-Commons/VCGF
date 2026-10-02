---
id: VCGF-SECR-001
title: Secrets and Environment Protection
domain: secrets
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

# VCGF-SECR-001 - Secrets and Environment Protection

**Control ID:** VCGF-SECR-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Secrets MUST remain out of client bundles, source control, logs, URLs, and unsafe configuration, and MUST be isolated by environment with least privilege.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for secrets and environment protection.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Secrets and Environment Policy

Secrets include API keys, DB secrets, privileged platform keys, encryption/signing keys, webhook secrets, OAuth client secrets, SMTP credentials, and private certificates.

Never place secrets in:
- frontend bundles
- source code
- public env vars
- Git history
- browser localStorage
- URLs
- logs
- screenshots/docs

Use platform secret managers or a dedicated vault.

Scope by environment/service and prefer narrowly scoped credentials.

Document owner, usage, expiry/rotation, and emergency revocation.

A suspected leak requires rotation; deleting from the latest commit is not enough.

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
