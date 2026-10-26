<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/ai-governance/vcgf-ai-004-unauthorized-refactoring-and-feature-change-prevention.md -->
# VCGF-AI-004 — Unauthorized Refactoring and Feature Change Prevention
MUST NOT · ai-governance · profiles: high-assurance, production · full text: controls/ai-governance/vcgf-ai-004-unauthorized-refactoring-and-feature-change-prevention.md

## Requirement
An AI agent MUST NOT remove, rewrite, refactor, rename, or expand unrelated behavior merely because an alternative implementation appears cleaner.

## Guidance
Treat existing working behavior as a contract. Any unrelated opportunity should be reported separately rather than bundled into the requested change.

## References
- VCGF core risk and evidence model
- OWASP guidance where security-relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
