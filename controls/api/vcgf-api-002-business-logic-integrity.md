---
id: VCGF-API-002
title: Business Logic Integrity
domain: api
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

# VCGF-API-002 - Business Logic Integrity

**Control ID:** VCGF-API-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Sensitive business state, calculations, approvals, prices, ownership, and transitions MUST be verified on a trusted layer and protected from replay and race conditions where relevant.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for business logic integrity.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Business Logic Integrity

Attackers can submit valid-looking requests in invalid order.

Never trust client-calculated:
- price
- discount
- tax
- balance
- credit
- quota
- role
- approval state
- ownership
- tenant
- entitlement

Server recalculates or verifies these values.

## State machines
Document valid transitions and reject unauthorized transitions.

## Race conditions
Use transactions, locking/concurrency control, uniqueness, idempotency, and atomic updates where needed.

## Duplicate submissions
Payments, orders, approvals, emails, vouchers, and provisioning must be resilient to retries.

## Verification Method

Inspect implementation and configuration, execute positive and negative tests appropriate to the control, and review evidence at the trusted enforcement layer.

## Required Evidence

At least one reproducible artifact such as a test result, code review, configuration record, security scan, migration review, or manual verification record.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, and applicable architecture or identity controls.

## Related Controls

See the domain index and selected profile.

## References

- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Change History

- 1.0.0: Initial VCGF control migrated and normalized from the previous framework.
