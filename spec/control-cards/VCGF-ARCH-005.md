<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/architecture/vcgf-arch-005-threat-modeling.md -->
# VCGF-ARCH-005 — Threat Modeling
MUST · architecture · profiles: baseline, high-assurance, production · full text: controls/architecture/vcgf-arch-005-threat-modeling.md

## Requirement
Projects and HIGH or CRITICAL changes MUST identify assets, trust boundaries, threat actors, abuse cases, security assumptions, and planned mitigations before implementation proceeds.

## Guidance
Use a lightweight threat model for small changes and a structured model for major features or systems. At minimum document: protected assets; entry points; identities and trust boundaries; data flows; attacker capabilities; abuse cases; threats affecting confidentiality, integrity, availability, privacy, and authorization; mitigations; residual risk; and an owner. Revisit the model when authentication, authorization, sensitive data, infrastructure, integrations, or trust boundaries materially change.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0 where applicable
- NIST Secure Software Development Framework (SSDF) where applicable
- Project-specific regulatory or contractual overlays where applicable

Common clauses (spec/control-cards/common-clauses.md): Applicability[C] Verification[C] Evidence[C] Exceptions[C] Dependencies[C] Related[C] Platform[C]
