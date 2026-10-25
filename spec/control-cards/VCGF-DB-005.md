<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/database/vcgf-db-005-sql-query-security.md -->
# VCGF-DB-005 — SQL Query Security
MUST · database · profiles: baseline, high-assurance, production · full text: controls/database/vcgf-db-005-sql-query-security.md

## Requirement
SQL queries MUST use parameterized interfaces for untrusted values and MUST NOT rely on string concatenation for data or authorization predicates.

## Guidance
Use prepared statements/parameterized queries or safe ORM binding.

Never concatenate untrusted strings into SQL.

For dynamic identifiers such as sort column/direction, map user choices to hardcoded server-side values.

Raw SQL requires review and must never receive untrusted query fragments.

Stored procedures are not automatically safe; review internal dynamic SQL and privileges.

Runtime DB credentials should use least privilege and differ from migration/admin credentials when architecture permits.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
