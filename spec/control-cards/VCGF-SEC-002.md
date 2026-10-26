<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-002-file-and-url-validation.md -->
# VCGF-SEC-002 — File and URL Validation
MUST · security · profiles: high-assurance, production · full text: controls/security/vcgf-sec-002-file-and-url-validation.md

## Requirement
Untrusted files and URLs MUST be validated before storage, parsing, rendering, fetching, redirecting, or downstream use.

## Guidance
## Files
Check independently:
- maximum size
- extension
- MIME type
- magic/content signature
- expected format structure
- upload count/rate
- authorization
- storage destination

Never trust original filenames. Generate server-side random object names.

Use malware scanning/quarantine for higher-risk uploads.

Keep parsing libraries patched and resource-limited.

## URLs displayed to users
Validate scheme and render safely.

## URLs fetched by server
Apply SSRF controls:
- standard URL parser
- HTTPS or explicit allowed schemes
- allowlist destinations where feasible
- resolve DNS and block loopback/private/link-local/cloud-metadata destinations
- revalidate redirects
- limit redirects/ports
- timeouts
- maximum response size
- do not forward internal credentials
- controlled egress where feasible

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
