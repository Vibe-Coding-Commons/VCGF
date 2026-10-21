<!--
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
-->

# VCGF UXI — Bidirectional Design System and Component Contract (AR/EN)

**Status: RFC proposal.** These are proposed implementation and test conditions. They do not prove that any official VCGF adapter can enforce browser behavior in its host environment.

## 1. Direction belongs to content semantics

Set `<html lang="ar" dir="rtl">` or `<html lang="en" dir="ltr">` in the rendered output, and update on locale change without a page rebuild assumption. A `lang` may not uniquely imply direction (e.g., mixed content); preserve per-block overrides using the `dir` attribute.

### Preferred logical CSS mappings

| Avoid for direction-sensitive code | Prefer | Scope |
|---|---|---|
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` | Direction-sensitive spacing |
| `padding-left` / `padding-right` | `padding-inline-start` / `padding-inline-end` | Direction-sensitive padding |
| `left:0` / `right:0` | `inset-inline-start:0` / `inset-inline-end:0` | Direction-sensitive positioned elements |
| `border-left` / `border-right` | `border-inline-start` / `border-inline-end` | Borders as leading / trailing indicators |
| `text-align:left/right` | `text-align:start/end` | Text aligned to reading flow |
| `margin-top/bottom` | `margin-block-start/end` | Writing-mode independence where useful |

Physical X/Y are **correct** where the physical coordinate itself is meaningful (maps, games, drawn diagrams, camera guides, charts with domain-fixed axes). Exceptions must be documented in component code. No global SVG mirroring rule.

### Reusable CSS illustration (tokens)

```css
:root {
  --ui-space-1: .25rem;
  --ui-space-2: .5rem;
  --ui-space-3: .75rem;
  --ui-space-4: 1rem;
  --ui-hit-target: 2.75rem; /* optional UX target, not a WCAG guarantee */
}
html[dir="rtl"] { --ui-reading-flow: rtl; }
html[dir="ltr"] { --ui-reading-flow: ltr; }
.ui-field { display: grid; gap: var(--ui-space-2); text-align: start; }
.ui-action-icon { margin-inline-start: var(--ui-space-2); }
.ui-drawer { position: fixed; inset-inline-start: 0; inset-block: 0; }
.ui-close { position: absolute; inset-block-start: var(--ui-space-3); inset-inline-end: var(--ui-space-3); }
.ui-table-text { text-align: start; }
.ui-table-number { text-align: end; font-variant-numeric: tabular-nums; }
.ui-identifier { direction: ltr; unicode-bidi: isolate; }
```

## 2. Per-icon direction decisions

Assign one of four metadata types to each symbolic icon:

| Classification | Common examples | Directional treatment |
|---|---|---|
| `reading_navigation` | Back, next, breadcrumb arrow, pagination arrow | Swap/mirror appropriate icon in RTL after semantic test |
| `brand_universal` | Logo, magnifier, settings cog, trash, camera | Never mirror merely due to RTL |
| `context_dependent` | Undo/redo, play/skip, slide motion, share or expand | Test actual meaning and platform conventions; do not assume |
| `domain_axis` | Spatial map, chart, anatomical, engineering diagrams | Preserve domain orientation unless data semantics require a different axis |

A full `scaleX(-1)` on the root or all icons is forbidden as an automatic RTL technique; it incorrectly mirrors letters, branding and meaning-bearing data.

## 3. Inputs / validation / data tables

- Field label, helper/error text and placeholder (where meaningful) align to `start` in inherited direction; prefixes and suffixes require case-by-case semantics, not universal CSS selectors.
- Use `type="tel"` with `dir="ltr"` for phone number entry when format is international, `dir="ltr"` for email, OTP and codes. Native `type="number"` can have localization and input behavior differences; choose text+inputmode+validation for identifiers/credit card where numeric arithmetic is not intended.
- Dynamic user names or free text: prefer `<bdi>` or `dir="auto"` when direction unknown. Known foreign phrases: `<bdi dir="ltr">...</bdi>` or equivalent.
- Numerical alignment: `text-align:end` plus `font-variant-numeric:tabular-nums` aids column scanning but does **not** guarantee decimal-point alignment. For accounting tables, test decimal columns across positive, negative, zero and localized currency.
- Dates and currencies: use locale-aware display, configurable numeral system and IANA time zones. Store canonical values independently, not formatted display strings.
- Sidebars/Drawers usually anchor to inline-start when serving the primary reading navigation; a context-specific bottom sheet or edge-specific physical panel can be different if documented and tested.
- Data-heavy RTL desktop tables and mobile cards MUST preserve the user's needed details. If a value moves into Details/Drawer, verify its keyboard, touch and screen reader path.

## 4. CSS and BiDi implementation exceptions

Common error: `dir="rtl"` on the root and `direction:ltr` globally for every numeric display. Real layouts often need mixed inline spans; wrap atomic tokens, not entire paragraphs.

### Reference HTML

```html
<html lang="ar" dir="rtl">
  <main>
    <p>رقم الطلب <bdi dir="ltr">CASE-2026-1042</bdi> قيد المعالجة</p>
    <label for="phone">رقم الهاتف</label>
    <input id="phone" type="tel" dir="ltr" inputmode="tel" autocomplete="tel" />
    <p>اسم مقدم الطلب <bdi>Sample English Name</bdi></p>
  </main>
</html>
```

## 5. Locale display policy

Digits are not inherently `latn` in an Arabic UI. The project owner may select `latn`, `arab`, or per-locale presentation. Where financial precision matters, numeric calculations must remain typed or decimal-safe in the backend; `Intl.NumberFormat` is **presentation**, not a money arithmetic engine.

```js
const formatSAR = (locale, numberingSystem, amount) =>
  new Intl.NumberFormat(locale, {style: 'currency', currency: 'SAR', numberingSystem}).format(amount);

// Example policies, not forced defaults for every project:
formatSAR('ar-SA', 'latn', 1234.56);
formatSAR('ar-SA', 'arab', 1234.56);
```

## 6. Acceptance gates

- RTL and LTR screenshots are supplementary; keyboard order, screen reader reading order, clipboard, truncation and text wrapping must be tested too.
- Interactive elements without touch/focus alternatives fail. Hover tooltips alone fail when essential data are otherwise unreachable.
- Test mixed Arabic + Latin values with parentheses, periods, slashes, plus signs, punctuation and embedded numbers.
- Test Screen Reader and logical focus order when switching language without navigation reload.
- WCAG 2.2 AA Target Size (Minimum) is 24x24 CSS pixels **or applicable exceptions**. A 44px visual/touch target may be an ergonomic design goal, **not an unconditional WCAG AA rule**.
- Automated tools do not certify all WCAG 2.2 AA provisions; record manual evidence separately.

## References

- https://www.w3.org/International/articles/inline-bidi-markup/
- https://www.w3.org/International/docs/bp-html-bidi/Overview
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
