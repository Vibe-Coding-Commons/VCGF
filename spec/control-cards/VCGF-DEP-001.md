<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/dependencies/vcgf-dep-001-dependency-and-supply-chain-security.md -->
# VCGF-DEP-001 — Dependency and Supply-Chain Security
MUST · dependencies · profiles: baseline, high-assurance, production · full text: controls/dependencies/vcgf-dep-001-dependency-and-supply-chain-security.md

## Requirement
Dependencies MUST be justified, verified, locked where practical, reviewed for maintenance and security risk, and MUST NOT be invented by an AI agent.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
