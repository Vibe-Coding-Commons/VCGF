<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/ai-governance/vcgf-ai-002-no-silent-assumptions.md -->
# VCGF-AI-002 — No Silent Assumptions
MUST · ai-governance · profiles: baseline, high-assurance, production · full text: controls/ai-governance/vcgf-ai-002-no-silent-assumptions.md

## Requirement
An AI agent MUST distinguish verified project facts from assumptions and MUST NOT silently invent schemas, endpoints, roles, environment variables, integrations, libraries, or business rules.

## Guidance
When a material fact cannot be verified, mark it UNVERIFIED or REQUIRES VERIFICATION and avoid destructive or security-sensitive implementation based on the assumption.

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
