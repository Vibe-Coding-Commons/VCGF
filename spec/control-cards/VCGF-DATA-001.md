<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/data-protection/vcgf-data-001-backup-and-export-protection.md -->
# VCGF-DATA-001 — Backup and Export Protection
MUST · data-protection · profiles: high-assurance, production · full text: controls/data-protection/vcgf-data-001-backup-and-export-protection.md

## Requirement
Backups and exports containing sensitive data MUST receive access control, encryption, retention, and audit protections appropriate to their classification.

## Guidance
## Backups
Sensitive backups must be encrypted and access-controlled.

Backup credentials must be separate from normal client credentials.

Test restore procedures without exposing data to unauthorized environments.

## Exports
Sensitive exports must:
- be generated server-side
- enforce authorization/scope
- create audit event
- use private storage
- use short-lived signed access where appropriate
- expire/delete after need
- avoid predictable public URLs

## Spreadsheet exports
Protect against formula injection.

## Restore
Restore is a privileged action requiring authentication, authorization, logging, and verification.

## References
- OWASP Application Security Verification Standard (ASVS) 5.0
- OWASP Cheat Sheet Series where relevant
- OWASP API Security guidance where relevant

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
