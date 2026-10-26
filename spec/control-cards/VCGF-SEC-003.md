<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/security/vcgf-sec-003-injection-defense.md -->
# VCGF-SEC-003 — Injection Defense
MUST · security · profiles: baseline, high-assurance, production · full text: controls/security/vcgf-sec-003-injection-defense.md

## Requirement
Untrusted input MUST NOT be concatenated into interpreter contexts; context-appropriate parameterization, allowlisting, encoding, and isolation MUST be used.

## Guidance
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

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
