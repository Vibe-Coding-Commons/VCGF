<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/ai-governance/vcgf-ai-001-inspect-before-generate.md -->
# VCGF-AI-001 — Inspect Before Generate
MUST · ai-governance · profiles: baseline, high-assurance, production · full text: controls/ai-governance/vcgf-ai-001-inspect-before-generate.md

## Requirement
AI-assisted changes MUST inspect relevant code, schema, dependencies, interfaces, and established project rules before implementation.

## Guidance
Before changing an existing system, the AI must:
1. locate relevant implementation
2. identify database objects
3. identify validation
4. identify authorization
5. identify downstream consumers
6. identify tests
7. state assumptions
8. mark unknowns UNVERIFIED

The AI must not:
- create duplicates because existing code was not found immediately
- invent table/column names
- silently replace packages
- invent roles
- assume a field is public
- trust a browser user ID
- claim testing/scanning without evidence

Use evidence labels:
- VERIFIED
- INFERRED
- UNVERIFIED
- BLOCKED

After repeated failed fixes, stop speculative patching and return to root-cause analysis.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
