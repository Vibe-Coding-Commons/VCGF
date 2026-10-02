---
id: VCGF-SEC-001
title: Critical Field Validation
domain: security
status: normative
requirement_level: MUST
framework_version_introduced: 1.0.0
profiles:
- high-assurance
- baseline
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

# VCGF-SEC-001 - Critical Field Validation

**Control ID:** VCGF-SEC-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Security-sensitive and business-critical fields MUST have explicit trusted-layer validation rules for type, length, format, range, allowed values, and cross-field constraints.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for critical field validation.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Critical Field Validation Matrix

| Field type | Baseline validation | Security notes |
|---|---|---|
| Email | Parse with reliable library; trim outer whitespace; reasonable max length | PII; email existence is not authorization |
| Phone | Parse with phone library; normalize international form where possible | PII; rate-limit verification/recovery |
| Person name | Unicode-aware; allow legitimate spaces/hyphens/apostrophes; max length | Avoid ASCII-only rules |
| Username | Explicit allowed chars and length | Canonicalize consistently |
| Password | Long passphrases; no silent truncation; block common/breached values | Never log or reversibly encrypt |
| National/Resident ID | Country-specific format/checksum where available | Restricted PII; mask/encrypt when required |
| Passport | Document-specific rules where known | Restricted PII |
| Date of birth | Strict date + plausible range | Sensitive personal data |
| Money | Decimal/fixed-point + currency + bounds | Recalculate trusted totals server-side |
| Quantity | Explicit numeric type + bounds | Prevent negative/overflow |
| Percentage | Numeric explicit range | Server-authorize discounts |
| Role | Server-controlled enum | Never trust submitted role |
| Tenant ID | Strict identifier | Prefer deriving from auth context |
| Owner ID | Strict identifier | Never use without authorization |
| URL | Standard URL parser + scheme restrictions | SSRF controls for server fetches |
| Redirect URL | Exact allowlist or safe relative paths | Prevent open redirects |
| Rich text | Length + maintained HTML sanitizer | Do not raw-render unsanitized HTML |
| Plain text | Type/length | Contextual output encoding |
| File | Size, extension, MIME, magic signature | Scan higher-risk uploads |
| Enum/status | Exact allowlist | Validate allowed transitions |
| Search/filter | Length + supported operators | Never turn into raw query syntax |
| Sort | Map to fixed server columns/directions | Never concatenate raw identifiers |
| JSON | Schema, size/depth, unexpected-field checks | Prevent object/operator injection |
| OTP/PIN | Exact format + attempt limits | Expiring, single-use |
| Reset token | Opaque high-entropy value | Store securely/hashed; expiring, single-use |

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
