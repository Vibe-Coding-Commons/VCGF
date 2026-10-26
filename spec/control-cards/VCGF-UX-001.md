<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/user-experience/vcgf-ux-001-accessibility-conformance.md -->
# VCGF-UX-001 — Accessibility Conformance
MUST · user-experience · profiles: high-assurance, production · full text: controls/user-experience/vcgf-ux-001-accessibility-conformance.md

## Requirement
User-facing interfaces MUST conform to WCAG 2.2 Level AA for every critical user journey: all functionality operable by keyboard with visible focus, programmatic name/role/value and state for interactive elements, text contrast of at least 4.5:1 (3:1 for large text and UI components), reflow without horizontal scrolling at 320 CSS pixels, pointer targets of at least 24 by 24 CSS pixels unless an allowed exception applies, no information conveyed by color alone, and respect for the user's reduced-motion preference; conformance MUST be verified by automated scanning plus manual keyboard and assistive-technology testing of the critical journeys.

## Guidance
- Prefer native semantic elements (button, a, input, select, dialog) over scripted substitutes; when a custom widget is unavoidable, implement the complete WAI-ARIA pattern (roles, states, keyboard interaction) and test it.
- Every interactive element: reachable and operable by keyboard in a logical order, with a visible focus indicator that is never removed for aesthetics.
- Text alternatives for meaningful images and icons; decorative images hidden from assistive technology.
- Status messages (saving, saved, error, empty, loading) announced programmatically; never color-only.
- Respect `prefers-reduced-motion`; avoid content that flashes more than three times per second.
- Reflow and zoom: usable at 320 CSS pixels wide and at 200 percent zoom without loss of content or function.
- Target size: at least 24 by 24 CSS pixels for pointer targets, larger (44 by 44 is the common design target) for primary touch actions; document any WCAG exception used.
- Forms: labels programmatically associated, errors identified in text and linked to the field, required fields and formats stated before submission.
- Treat screen-reader reading order, focus order and clipboard behavior as test subjects, not assumptions.

## References
- W3C Web Content Accessibility Guidelines (WCAG) 2.2, Level AA
- W3C WAI-ARIA Authoring Practices patterns
- Detailed UI standards: `packs/ux/smart-ui/governance/ACCESSIBILITY-RTL.md` and the accessibility requirements (R10/AC10) of each component and interaction standard in `packs/ux/smart-ui/`

## Applicability
Apply to every task that creates or changes a user-facing interface (web, mobile web, kiosk or embedded UI). Required for the Production and High-Assurance profiles; recommended for Baseline. Not applicable to tasks with no user interface (an explicit `has_ui: false` screen context or a service-only change), which MUST be recorded as not applicable with a reason.

## Verification Method
Run an automated accessibility scan on each changed screen and treat every violation as a defect; perform manual keyboard-only and screen-reader walkthroughs of the critical journeys (authentication, recovery, consent, approval, checkout or the product's equivalents); verify reflow at 320 CSS pixels and 200 percent zoom; verify reduced-motion behavior. Record which journeys, browsers and assistive technologies were tested.

## Required Evidence
Automated scan report with zero unresolved violations for the changed screens, a manual test record listing journeys, assistive technologies and outcomes, and the list of WCAG exceptions claimed with justification.

## Exceptions
Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls (for example an accessible alternative path).

## Dependencies
VCGF-GOV-001, VCGF-GOV-004, VCGF-TEST-002, and VCGF-UX-002 for bidirectional and localized interfaces.

## Related Controls
VCGF-UX-003 (interaction states must be accessible), VCGF-UX-004 (responsive strategy preserves accessibility), VCGF-SEC-005 (output encoding of user content).

## Platform Considerations
Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability; automated scanners differ in coverage and never replace the manual verification required above.
