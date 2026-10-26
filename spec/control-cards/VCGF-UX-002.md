<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/user-experience/vcgf-ux-002-localization-and-bidirectional-text.md -->
# VCGF-UX-002 — Localization and Bidirectional Text
MUST · user-experience · profiles: high-assurance, production · full text: controls/user-experience/vcgf-ux-002-localization-and-bidirectional-text.md

## Requirement
Interfaces that support more than one language or a right-to-left language MUST set document and per-block language and direction structurally, use logical (start/end) layout properties for direction-sensitive styling, mirror only direction-meaning icons, isolate bidirectional runs such as identifiers, numbers and codes, render dates, numbers, currencies and calendars according to the user's locale (including a dual Gregorian/Hijri calendar where the product requires it) while storing canonical values, and MUST NOT lose, truncate or reorder meaning when the language is switched or when text is longer than the source language.

## Guidance
- Set `lang` and `dir` on the document and on any block whose language or direction differs; update them on locale change without a full rebuild assumption.
- Use logical CSS properties (`margin-inline-start`, `inset-inline-end`, `text-align: start`) for direction-sensitive layout; keep physical coordinates only where the physical axis is meaningful (maps, charts, drawn diagrams) and document those cases.
- Classify icons: mirror reading/navigation arrows in RTL; never mirror brand marks, numerals, phone handsets or domain-axis symbols; decide context-dependent icons case by case and test them.
- Isolate bidirectional runs (`bdi`, `unicode-bidi: isolate`) for identifiers, codes, numbers, email addresses and user-supplied names.
- Store canonical values (ISO 8601 instants with offsets, decimal amounts, Gregorian dates where the system of record is Gregorian); format for display per locale; convert between calendars with one shared engine and never change a stored value when the display calendar changes.
- Date pickers: expose month and year selection directly, distinguish the viewed period from the selected date, and support keyboard and assistive-technology use in both directions.
- Plan for text expansion and long names; test wrapping, truncation and tabular numerals in both languages.
- Translate security-relevant messages (errors, confirmations, consent) with the same precision as the source; never leave placeholders.

## References
- W3C Internationalization: structural markup for language and direction, inline bidirectional markup
- W3C Web Content Accessibility Guidelines (WCAG) 2.2
- Detailed UI standards: `packs/ux/smart-ui/governance/ACCESSIBILITY-RTL.md`, `packs/ux/smart-ui/external-standards/CALENDAR-GOVERNANCE-ADDENDUM.md`, `packs/ux/rtl-ltr.md`

## Applicability
Apply to every user-facing task in a product that declares more than one interface language or any right-to-left language. Required for the Production and High-Assurance profiles. Single-language left-to-right products record the control as not applicable with the declared language list as the reason.

## Verification Method
Switch the interface language and direction on each changed screen and verify layout, reading order, focus order, icon mirroring, numeric and date rendering, and absence of truncation; verify stored values are unchanged after display-locale or calendar changes; include screen-reader reading order in both directions for critical journeys.

## Required Evidence
A locale test record per changed screen covering both directions, screenshots or recordings for the two languages, and a check that stored canonical values are unaffected by presentation changes.

## Dependencies
VCGF-GOV-001, VCGF-GOV-004, VCGF-TEST-002, VCGF-UX-001.

## Related Controls
VCGF-SEC-001 (field validation of localized input), VCGF-SEC-005 (output encoding), VCGF-UX-004 (responsive strategy must hold in both directions).

## Platform Considerations
Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability; calendar and formatting libraries must be selected and version-pinned per project.

Common clauses (spec/control-cards/common-clauses.md): Exceptions[A]
