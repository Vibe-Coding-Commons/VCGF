---
id: VCGF-SEC-003
title: Injection Defense
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

# VCGF-SEC-003 - Injection Defense

**Control ID:** VCGF-SEC-003  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Untrusted input MUST NOT be concatenated into interpreter contexts; context-appropriate parameterization, allowlisting, encoding, and isolation MUST be used.

## Purpose

Provide a stable, implementation-neutral VCGF requirement for injection defense.

## Risk Addressed

Security, privacy, integrity, availability, governance, or regression risk arising when this control is absent or bypassed.

## Rationale

AI-assisted development can accelerate unsafe assumptions and broad changes. This control creates a stable requirement that can be mapped consistently across tools and reviewed using evidence.

## Applicability

Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Implementation-Neutral Guidance

# Injection Defense Policy

Injection prevention keeps untrusted data separate from executable syntax.

## SQL Injection
- parameterized queries/prepared statements or safe ORM binding
- never concatenate raw input into SQL
- hard-map dynamic columns/sort directions through allowlists
- least-privilege database roles
- validation as secondary defense

Escaping input is not the primary SQL defense.

## NoSQL/Object Query Injection
- validate payload shape
- reject unexpected operators
- never pass request objects directly into query APIs
- construct filters explicitly

## OS Command Injection
Prefer APIs that do not invoke a shell.

If launching a process:
- fixed executable
- argument array
- allowlisted arguments
- no concatenated command strings

## Template Injection
Do not execute user-controlled template expressions or names.

## XSS
- framework auto-escaping for normal text
- context-specific encoding
- maintained HTML sanitizer for rich HTML
- avoid unsafe DOM sinks
- never use `eval`/`new Function` with untrusted data

## Path Traversal
Use server-generated names, canonicalize paths, enforce an allowed root, reject path separators when not required.

## Header/CRLF Injection
Never place raw user input in response headers. Reject control characters and use framework APIs.

## LDAP/XPath/XML
Use parameterized/safe APIs and disable dangerous XML entity behavior where applicable.

## CSV Formula Injection
Protect exported cells beginning with spreadsheet formula control characters.

## AI Prompt Injection
If the product uses LLMs/agents:
- treat user/retrieved content as data
- keep system/developer instructions separate
- allowlist tools
- validate tool arguments server-side
- require confirmation for destructive/high-impact side effects
- do not expose unnecessary secrets
- retrieved documents cannot override security policy

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
