<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/privacy/vcgf-priv-004-data-lifecycle-retention-and-secure-deletion.md -->
# VCGF-PRIV-004 — Data Lifecycle, Retention and Secure Deletion
MUST · privacy · profiles: high-assurance, production · full text: controls/privacy/vcgf-priv-004-data-lifecycle-retention-and-secure-deletion.md

## Requirement
Projects that store personal, confidential, or regulated data MUST define retention, archival, deletion, backup-expiry, and legal-hold behavior for that data.

## Guidance
Retention rules should be enforceable and testable. Deletion workflows must consider primary records, derived data, caches, search indexes, attachments, exports, replicas, and backups according to documented recovery windows. Secure deletion MUST NOT be represented as instantaneous when platform backups or immutable retention make that impossible; the documented lifecycle must state when data becomes inaccessible and when residual copies expire.

Common clauses (spec/control-cards/common-clauses.md): Applicability[C] Verification[C] Evidence[C] Exceptions[C] Dependencies[C] Related[C] Platform[C]
