<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/incident-response/vcgf-ir-001-incident-response-minimums.md -->
# VCGF-IR-001 — Incident Response Minimums
MUST · incident-response · profiles: high-assurance, production · full text: controls/incident-response/vcgf-ir-001-incident-response-minimums.md

## Requirement
Production systems MUST define minimum detection, containment, credential and key response, evidence preservation, communication, and recovery responsibilities.

## Guidance
Prepare:
- incident owner
- session/token revocation
- secret/key rotation
- useful audit logs
- backup/restore
- endpoint/feature disable path
- critical provider contacts

## Credential leak
Rotate/revoke, inspect usage, invalidate affected sessions/tokens, identify exposure, remove from code/history as required, add regression prevention.

## Data exposure
Preserve evidence, restrict access, identify affected data/tenants/users, determine cause, and follow applicable contractual/legal notification requirements.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
