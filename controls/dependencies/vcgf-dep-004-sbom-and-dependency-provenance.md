---
id: VCGF-DEP-004
title: SBOM and Dependency Provenance
domain: dependencies
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

# VCGF-DEP-004 - SBOM and Dependency Provenance

**Control ID:** VCGF-DEP-004  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Production and high-assurance projects MUST maintain dependency provenance and a machine-readable software bill of materials or equivalent inventory sufficient to identify shipped third-party components.

## Purpose

Establish a vendor-neutral governance requirement for sbom and dependency provenance in AI-assisted software development.

## Risk Addressed

Unidentified or unmanaged risk that can lead to security defects, privacy violations, supply-chain compromise, operational blind spots, or unverifiable releases.

## Rationale

AI-assisted development can accelerate changes faster than traditional review cycles. This control ensures that the relevant risk is explicitly analyzed, implemented, and evidenced rather than assumed.

## Applicability

Apply according to the selected VCGF profile and whenever the capability or risk described by this control is present.

## Implementation-Neutral Guidance

The dependency inventory should be reproducible from lockfiles or build metadata and should record package identity, version, source, and direct/transitive relationship where tooling permits. Release evidence SHOULD link the shipped artifact to its dependency inventory. Dependencies introduced by an AI agent require the same provenance and review as human-introduced dependencies. Unknown, typo-suspected, or unverifiable packages MUST NOT be added.

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
