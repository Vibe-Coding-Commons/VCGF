<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/release/vcgf-rel-005-release-artifact-integrity-and-provenance.md -->
# VCGF-REL-005 — Release Artifact Integrity and Provenance
MUST · release · profiles: high-assurance, production · full text: controls/release/vcgf-rel-005-release-artifact-integrity-and-provenance.md

## Requirement
Production release artifacts MUST be traceable to reviewed source and SHOULD use integrity or provenance mechanisms appropriate to the delivery channel.

## Guidance
Release evidence should record source revision, build workflow, dependency state, test/security gate results, and artifact checksum or platform-native immutable identifier. High-assurance releases SHOULD use signed commits, signed artifacts, attestations, or equivalent provenance where supported. Generated artifacts must not be substituted after approval without re-running the applicable release gate.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0 where applicable
- NIST Secure Software Development Framework (SSDF) where applicable
- Project-specific regulatory or contractual overlays where applicable

Common clauses (spec/control-cards/common-clauses.md): Applicability[C] Verification[C] Evidence[C] Exceptions[C] Dependencies[C] Related[C] Platform[C]
