---
id: VCGF-PRIV-004
title: Data Lifecycle, Retention and Secure Deletion
domain: privacy
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

# VCGF-PRIV-004 - Data Lifecycle, Retention and Secure Deletion

**Control ID:** VCGF-PRIV-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Projects that store personal, confidential, or regulated data MUST define retention, archival, deletion, backup-expiry, and legal-hold behavior for that data.

## Purpose

Establish a vendor-neutral governance requirement for data lifecycle, retention and secure deletion in AI-assisted software development.

## Risk Addressed

Unidentified or unmanaged risk that can lead to security defects, privacy violations, supply-chain compromise, operational blind spots, or unverifiable releases.

## Rationale

AI-assisted development can accelerate changes faster than traditional review cycles. This control ensures that the relevant risk is explicitly analyzed, implemented, and evidenced rather than assumed.

## Applicability

Apply according to the selected VCGF profile and whenever the capability or risk described by this control is present.

## Implementation-Neutral Guidance

Retention rules should be enforceable and testable. Deletion workflows must consider primary records, derived data, caches, search indexes, attachments, exports, replicas, and backups according to documented recovery windows. Secure deletion MUST NOT be represented as instantaneous when platform backups or immutable retention make that impossible; the documented lifecycle must state when data becomes inaccessible and when residual copies expire.

## Verification Method

Inspect the relevant design, implementation, configuration, and evidence; run positive and negative tests where applicable; confirm that the control is enforced at a trusted layer.

## Required Evidence

A reproducible artifact such as a threat model, generated inventory, policy configuration, CI result, alert test, signed provenance record, review record, or release checksum, depending on the control.

## Exceptions

Use the VCGF exception-management process. Exceptions must identify risk, owner, compensating controls, approval, expiry, and review date.

## Dependencies

VCGF-GOV-001, VCGF-GOV-002, VCGF-GOV-004, and the applicable security or architecture controls.

## Related Controls

See the selected profile and domain index for related requirements.

## References

- OWASP Application Security Verification Standard (ASVS) 5.0 where applicable
- NIST Secure Software Development Framework (SSDF) where applicable
- Project-specific regulatory or contractual overlays where applicable

## Platform Considerations

Platform adapters may identify native or configurable implementation surfaces. The normative requirement remains platform-independent.

## Change History

- 1.0.0: Added before the v1.0.0 control-ID freeze.
