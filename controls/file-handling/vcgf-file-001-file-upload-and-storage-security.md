---
id: VCGF-FILE-001
title: File Upload and Storage Security
domain: file-handling
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

# VCGF-FILE-001 - File Upload and Storage Security

**Control ID:** VCGF-FILE-001  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Uploaded files MUST be treated as untrusted and controlled by type, content, size, naming, authorization, storage visibility, and active-content or malware risk as applicable.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for file upload and storage security.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# File Upload and Storage Security

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
