<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/file-handling/vcgf-file-001-file-upload-and-storage-security.md -->
# VCGF-FILE-001 — File Upload and Storage Security
MUST · file-handling · profiles: baseline, high-assurance, production · full text: controls/file-handling/vcgf-file-001-file-upload-and-storage-security.md

## Requirement
Uploaded files MUST be treated as untrusted and controlled by type, content, size, naming, authorization, storage visibility, and active-content or malware risk as applicable.

## Guidance
## Upload
Require:
- authenticated/authorized uploader where appropriate
- count/size limits
- extension allowlist
- MIME validation
- content signature validation
- server-generated filename
- metadata validation
- rate limits

## Storage
Private by default.

Do not make a bucket public to solve an access error.

Use authorization-controlled downloads or short-lived signed URLs.

## Processing
Keep image/document parsing libraries patched, set CPU/memory/time limits, isolate risky parsers where appropriate, and malware-scan higher-risk files.

## Serving
Use safe content type/disposition and avoid executing uploaded HTML/SVG/script-capable formats unless explicitly required and sandboxed.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
