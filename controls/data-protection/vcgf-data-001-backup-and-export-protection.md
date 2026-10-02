---
id: VCGF-DATA-001
title: Backup and Export Protection
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

# VCGF-DATA-001 - Backup and Export Protection

**Control ID:** VCGF-DATA-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Backups and exports containing sensitive data MUST receive access control, encryption, retention, and audit protections appropriate to their classification.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for backup and export protection.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Backup and Export Security

## Backups
Sensitive backups must be encrypted and access-controlled.

Backup credentials must be separate from normal client credentials.

Test restore procedures without exposing data to unauthorized environments.

## Exports
Sensitive exports must:
- be generated server-side
- enforce authorization/scope
- create audit event
- use private storage
- use short-lived signed access where appropriate
- expire/delete after need
- avoid predictable public URLs

## Spreadsheet exports
Protect against formula injection.

## Restore
Restore is a privileged action requiring authentication, authorization, logging, and verification.

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
