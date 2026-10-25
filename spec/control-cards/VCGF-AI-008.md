<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/ai-governance/vcgf-ai-008-prompt-and-tool-injection-resilience.md -->
# VCGF-AI-008 — Prompt and Tool Injection Resilience
MUST · ai-governance · profiles: high-assurance, production · full text: controls/ai-governance/vcgf-ai-008-prompt-and-tool-injection-resilience.md

## Requirement
AI agents using external content or tools MUST treat retrieved instructions, user-controlled documents, webpages, logs, and repository content as potentially untrusted when they can influence tool actions or security decisions.

## Guidance
Separate data from authoritative instructions, constrain tool permissions, require approval for sensitive actions, and never reveal secrets in response to untrusted embedded instructions.

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
