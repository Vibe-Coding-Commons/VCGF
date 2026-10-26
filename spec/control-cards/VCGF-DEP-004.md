<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/dependencies/vcgf-dep-004-sbom-and-dependency-provenance.md -->
# VCGF-DEP-004 — SBOM and Dependency Provenance
MUST · dependencies · profiles: high-assurance, production · full text: controls/dependencies/vcgf-dep-004-sbom-and-dependency-provenance.md

## Requirement
Production and high-assurance projects MUST maintain dependency provenance and a machine-readable software bill of materials or equivalent inventory sufficient to identify shipped third-party components.

## Guidance
The dependency inventory should be reproducible from lockfiles or build metadata and should record package identity, version, source, and direct/transitive relationship where tooling permits. Release evidence SHOULD link the shipped artifact to its dependency inventory. Dependencies introduced by an AI agent require the same provenance and review as human-introduced dependencies. Unknown, typo-suspected, or unverifiable packages MUST NOT be added.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0 where applicable
- NIST Secure Software Development Framework (SSDF) where applicable
- Project-specific regulatory or contractual overlays where applicable

Common clauses (spec/control-cards/common-clauses.md): Applicability[C] Verification[C] Evidence[C] Exceptions[C] Dependencies[C] Related[C] Platform[C]
