<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/data-protection/vcgf-data-005-searchable-encrypted-data.md -->
# VCGF-DATA-005 — Searchable Encrypted Data
SHOULD · data-protection · profiles: high-assurance · full text: controls/data-protection/vcgf-data-005-searchable-encrypted-data.md

## Requirement
When exact-match search is required over encrypted low-entropy personal data, designs SHOULD use a keyed blind index or equivalent construction rather than an unsalted raw hash.

## Guidance
Separate index keys from encryption keys, normalize only according to an explicit field policy, version the index scheme, authorize lookup endpoints, and rate-limit enumeration-sensitive searches.

Common clauses (spec/control-cards/common-clauses.md): Applicability[B] Verification[B] Evidence[B] Exceptions[B] Dependencies[B] Related[B] Platform[B]
