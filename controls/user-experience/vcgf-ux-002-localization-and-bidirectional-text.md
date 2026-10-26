---
id: VCGF-UX-002
title: Localization and Bidirectional Text
domain: user-experience
status: normative
requirement_level: MUST
framework_version_introduced: 1.4.0
profiles:
- high-assurance
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

# VCGF-UX-002 - Localization and Bidirectional Text

**Control ID:** VCGF-UX-002  
**Status:** Normative  
**Requirement Level:** MUST

## Requirement

Interfaces that support more than one language or a right-to-left language MUST set document and per-block language and direction structurally, use logical (start/end) layout properties for direction-sensitive styling, mirror only direction-meaning icons, isolate bidirectional runs such as identifiers, numbers and codes, render dates, numbers, currencies and calendars according to the user's locale (including a dual Gregorian/Hijri calendar where the product requires it) while storing canonical values, and MUST NOT lose, truncate or reorder meaning when the language is switched or when text is longer than the source language.

## Purpose

Prevent the two failure modes that dominate bilingual products: layouts that break when direction flips, and values whose meaning changes with their presentation.

## Risk Addressed

Mis-ordered or mirrored data (phone numbers, amounts, identifiers), unreadable mixed-direction text, wrong dates across calendars and time zones, and untranslated or truncated security-relevant messages.

## Rationale

Direction and locale are content semantics, not styling. Centralizing them in structure and formatting layers lets every component inherit correct behavior and makes the behavior testable per locale.

## Applicability

Apply to every user-facing task in a product that declares more than one interface language or any right-to-left language. Required for the Production and High-Assurance profiles. Single-language left-to-right products record the control as not applicable with the declared language list as the reason.

## Implementation-Neutral Guidance

# Localization and bidirectional text

- Set `lang` and `dir` on the document and on any block whose language or direction differs; update them on locale change without a full rebuild assumption.
- Use logical CSS properties (`margin-inline-start`, `inset-inline-end`, `text-align: start`) for direction-sensitive layout; keep physical coordinates only where the physical axis is meaningful (maps, charts, drawn diagrams) and document those cases.
- Classify icons: mirror reading/navigation arrows in RTL; never mirror brand marks, numerals, phone handsets or domain-axis symbols; decide context-dependent icons case by case and test them.
- Isolate bidirectional runs (`bdi`, `unicode-bidi: isolate`) for identifiers, codes, numbers, email addresses and user-supplied names.
- Store canonical values (ISO 8601 instants with offsets, decimal amounts, Gregorian dates where the system of record is Gregorian); format for display per locale; convert between calendars with one shared engine and never change a stored value when the display calendar changes.
- Date pickers: expose month and year selection directly, distinguish the viewed period from the selected date, and support keyboard and assistive-technology use in both directions.
- Time handling: store instants as ISO 8601 with an explicit offset (UTC preferred), convert to the user's zone only for display, compute durations across daylight-saving transitions from instants not wall clocks, and test the 29 February and the month-length differences of the Hijri calendar explicitly.
- Plan for text expansion and long names; test wrapping, truncation and tabular numerals in both languages.
- Translate security-relevant messages (errors, confirmations, consent) with the same precision as the source; never leave placeholders.

## Verification Method

Switch the interface language and direction on each changed screen and verify layout, reading order, focus order, icon mirroring, numeric and date rendering, and absence of truncation; verify stored values are unchanged after display-locale or calendar changes; include screen-reader reading order in both directions for critical journeys.

## Required Evidence

A locale test record per changed screen covering both directions, screenshots or recordings for the two languages, and a check that stored canonical values are unaffected by presentation changes.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, VCGF-TEST-002, VCGF-UX-001.

## Related Controls

VCGF-SEC-001 (field validation of localized input), VCGF-SEC-005 (output encoding), VCGF-UX-004 (responsive strategy must hold in both directions).

## References

- W3C Internationalization: structural markup for language and direction, inline bidirectional markup
- W3C Web Content Accessibility Guidelines (WCAG) 2.2
- Detailed UI standards: `packs/ux/smart-ui/governance/ACCESSIBILITY-RTL.md`, `packs/ux/smart-ui/external-standards/CALENDAR-GOVERNANCE-ADDENDUM.md`, `packs/ux/rtl-ltr.md`

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability; calendar and formatting libraries must be selected and version-pinned per project.

## Change History

- 1.4.0: Introduced to bind the bidirectional and calendar standards to a normative, profile-bindable control.
