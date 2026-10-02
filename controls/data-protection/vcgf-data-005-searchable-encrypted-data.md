---
id: VCGF-DATA-005
title: Searchable Encrypted Data
domain: data-protection
status: normative
requirement_level: SHOULD
framework_version_introduced: 1.0.0
profiles:
- high-assurance
---

<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF-DATA-005 - Searchable Encrypted Data

**Control ID:** VCGF-DATA-005  
**Status:** Normative  
**Requirement Level:** SHOULD

## Requirement

When exact-match search is required over encrypted low-entropy personal data, designs SHOULD use a keyed blind index or equivalent construction rather than an unsalted raw hash.

## Purpose

Reduce AI-assisted engineering risk through a stable vendor-neutral requirement.

## Risk Addressed

Unauthorized change, security weakening, data exposure, architecture drift, integrity loss, or insufficient auditability.

## Rationale

VCGF separates normative policy from platform implementation so this requirement can be consistently enforced or evidenced across tools.

## Applicability

Apply according to project risk, selected profile, and affected trust boundaries.

## Implementation-Neutral Guidance

Separate index keys from encryption keys, normalize only according to an explicit field policy, version the index scheme, authorize lookup endpoints, and rate-limit enumeration-sensitive searches.

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
