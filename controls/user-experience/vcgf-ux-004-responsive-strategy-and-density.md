---
id: VCGF-UX-004
title: Responsive Strategy and Density
domain: user-experience
status: normative
requirement_level: SHOULD
framework_version_introduced: 1.4.0
profiles:
- high-assurance
---

<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF-UX-004 - Responsive Strategy and Density

**Control ID:** VCGF-UX-004  
**Status:** Normative  
**Requirement Level:** SHOULD

## Requirement

Each screen class SHOULD have an explicit, recorded responsive strategy (mobile-first, desktop-first or task-preserving adaptive) and density policy derived from its primary devices, task frequency and information density; layouts SHOULD transform across breakpoints without losing required information or actions (data moved into details or drawers remains reachable), SHOULD keep primary actions reachable without horizontal scrolling, and SHOULD size touch targets and spacing according to the declared input modality.

## Purpose

Replace ad-hoc breakpoints with a reviewable decision per screen class so that enterprise desktop workbenches and mobile task flows are each designed deliberately rather than degraded from the other.

## Risk Addressed

Hidden or unreachable actions and data on small screens, unusably sparse or dense enterprise workbenches, inconsistent behavior between screens of the same class, and accessibility regressions introduced by responsive transformations.

## Rationale

A single responsive rule rarely fits a login screen, a 40-column operational grid and a field task on a phone. Recording the strategy per screen class makes the trade-off explicit, testable and consistent.

## Applicability

Apply to tasks that compose, redesign or significantly restructure screens. Required for the High-Assurance profile and recommended for Production. Minor styling changes record the control as not applicable with a reason.

## Implementation-Neutral Guidance

# Responsive strategy and density

- Decide per screen class: primary devices, orientation, input modality (touch, keyboard, pointer), task frequency and information density; record the resulting strategy and density policy.
- Mobile-first for public self-service and field tasks; desktop-first for high-frequency operational workbenches; adaptive when roles use the same screen on different devices. Do not invert the decision silently.
- Transformations preserve information: tables become cards or list-detail with every required column still reachable; multi-pane layouts stack without dropping a pane's actions.
- Keep the primary action visible and reachable at every breakpoint; limit to one primary action per view.
- Density: comfortable for infrequent or public tasks, compact only for trained high-frequency users on large screens, never below the accessibility target-size policy.
- Large screens: use extra width for context (details, comparison, related records) rather than stretching a single column.
- Test at representative widths (for example 320, 390, 768, 1280, 1920 CSS pixels) in both text directions where VCGF-UX-002 applies.

## Verification Method

Review the recorded strategy and density decision for the screen class; exercise each changed screen at the representative widths and orientations, verifying that required data and actions remain reachable, that no horizontal scrolling is needed for primary tasks, and that target sizes meet the declared modality.

## Required Evidence

The screen-class strategy record and a responsive test record (widths, orientations, directions) with screenshots or recordings showing information preservation.

## Exceptions

Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Dependencies

VCGF-GOV-001, VCGF-GOV-004, VCGF-UX-001.

## Related Controls

VCGF-UX-002 (bidirectional layouts), VCGF-UX-003 (states must survive transformation), VCGF-ARCH-003 (established system as contract when redesigning).

## References

- W3C Web Content Accessibility Guidelines (WCAG) 2.2 (reflow, target size)
- Detailed screen-composition standards: `packs/ux/smart-ui/screen-compositions/` (VCGF-UI-SCR-019 mobile-focused task modifier, VCGF-UI-SCR-020 large-screen operations modifier), `packs/ux/smart-ui/governance/RESPONSIVE-DENSITY-POLICY.md`, `packs/ux/smart-ui/governance/ADAPTIVE-UX-ORCHESTRATION.md`

## Platform Considerations

Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Change History

- 1.4.0: Introduced to bind the Smart UI screen-composition orchestration to a normative control.
