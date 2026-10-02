---
id: VCGF-REL-005
title: Release Artifact Integrity and Provenance
domain: release
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

# VCGF-REL-005 - Release Artifact Integrity and Provenance

**Control ID:** VCGF-REL-005  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Production release artifacts MUST be traceable to reviewed source and SHOULD use integrity or provenance mechanisms appropriate to the delivery channel.

## Purpose

Establish a vendor-neutral governance requirement for release artifact integrity and provenance in AI-assisted software development.

## Risk Addressed

Unidentified or unmanaged risk that can lead to security defects, privacy violations, supply-chain compromise, operational blind spots, or unverifiable releases.

## Rationale

AI-assisted development can accelerate changes faster than traditional review cycles. This control ensures that the relevant risk is explicitly analyzed, implemented, and evidenced rather than assumed.

## Applicability

Apply according to the selected VCGF profile and whenever the capability or risk described by this control is present.

## Implementation-Neutral Guidance

Release evidence should record source revision, build workflow, dependency state, test/security gate results, and artifact checksum or platform-native immutable identifier. High-assurance releases SHOULD use signed commits, signed artifacts, attestations, or equivalent provenance where supported. Generated artifacts must not be substituted after approval without re-running the applicable release gate.

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
