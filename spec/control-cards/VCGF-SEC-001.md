<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-001-critical-field-validation.md -->
# VCGF-SEC-001 — Critical Field Validation
MUST · security · profiles: baseline, high-assurance, production · full text: controls/security/vcgf-sec-001-critical-field-validation.md

## Requirement
Security-sensitive and business-critical fields MUST have explicit trusted-layer validation rules for type, length, format, range, allowed values, and cross-field constraints.

## Guidance
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

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
