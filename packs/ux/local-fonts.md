<!--
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
-->

# VCGF UXI — Local Web Fonts, Multilingual Typography & Performance Contract

**Proposal only. No font binaries are packaged or to be redistributed by this RFC.** Illustrative paths require the project team to obtain suitably licensed font assets and verify actual file availability before deployment.

## 1. Governance

1. Inspect existing `@font-face`, external font CSS domains, CSP, `link rel=preconnect/preload`, locale bundle and lockfiles **without reading secrets**.
2. Review font source/rights (OFL, Apache or applicable licensing), allowed self-hosting, modification/subsetting rights, copyright notices, and update provenance. Publicly available does not automatically mean unrestricted.
3. Default recommendation when appropriate: verified local WOFF2 served from project's own origin. Do **not** claim hosting alone proves GDPR compliance. Self-hosting reduces some third-party data transfers; it does not replace privacy assessment.
4. Prefer variable font only when real subsets, required weights, and total transferred bytes show a net benefit. A single large variable font can cost more than two small, language-specific static subsets.
5. Do not ship remote `@import` of Google Fonts on sensitive pages without an approved design/privacy reason. Do not copy code snippets that assume Google CDN hosts can never change.

## 2. Coverage and scripts

For Arabic, verify basic and extended Arabic glyphs used by actual content, contextual shaping, harakat and combining marks, diacritics, Arabic/Western digits, punctuation, Latin product names, ligatures and typical mixed identifiers. Check subsets with font-tools or a verified local glyph coverage test. `unicode-range` must match glyphs *in the binary* and cannot repair an incomplete file.

Create a font matrix per role, not one forced family for all projects:

| Text role | Arabic candidate | Latin candidate | Gate |
|---|---|---|---|
| Body/content | Licensed project-approved Arabic family | Licensed project-approved Latin family | Mixed-script legibility at 100/200/400% |
| Enterprise data grid | High-legibility numeric/tabular glyph support | Same design role | Arabic mixed numbers, dense tables, no clipping |
| Heading / brand | Approved branded family | Approved branded family | Same visual hierarchy, not identical pixel dimensions |
| Code / IDs | Accessible monospace with Arabic fallback | Accessible monospace | LTR identifiers remain stable in RTL context |

**There is no universally correct CSS declaration forcing Arabic to always be +1px, +2px or +15–25% line height.** Start from legibility, font x-height/glyph metrics and text spacing requirements. A typical initial body line-height may be 1.5–1.7 for Arabic and 1.45–1.6 for English, but these are review starting points, not mandates; headings and dense fields need separate measurements.

## 3. CSS illustration (only after font files and rights are confirmed)

```css
/* Example placeholder files: NOT PRESENT in this RFC ZIP */
@font-face {
  font-family: "VCGF Arabic UI";
  src: url("/assets/fonts/arabic-ui/ar-regular.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  /* Supply a verified unicode-range only after inspecting the actual font subset. */
}
@font-face {
  font-family: "VCGF Latin UI";
  src: url("/assets/fonts/latin-ui/en-regular.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}
:root {
  --ui-font-latin: "VCGF Latin UI", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --ui-font-arabic: "VCGF Arabic UI", system-ui, -apple-system, "Segoe UI", Tahoma, Arial, sans-serif;
  --ui-body-line-height-ar: 1.6; /* illustrative, tune for chosen font and product */
  --ui-body-line-height-en: 1.5;
}
html[dir="rtl"] { font-family: var(--ui-font-arabic); line-height: var(--ui-body-line-height-ar); }
html[dir="ltr"] { font-family: var(--ui-font-latin); line-height: var(--ui-body-line-height-en); }
.ui-accounting-number { font-variant-numeric: tabular-nums; }
```

**Variable font equivalent** may use `font-weight: 100 900;` only after verifying the actual included range; setting range in CSS does not magically add unsupported weights. Narrow unicode ranges are **not** provided as universal copy-paste because files and coverage are unknown.

## 4. Font preloading as an exception

If (and only if) field/lab measurement confirms that the requested local font is critical to the initial viewport, use a suitable per-locale preload:

```html
<!-- Only on pages where this verified font is needed immediately. -->
<link rel="preload" href="/assets/fonts/arabic-ui/ar-regular.woff2"
      as="font" type="font/woff2" crossorigin>
```

Unnecessary preload consumes bandwidth, can delay LCP resources, and may trigger unused-font downloads when language changes. `crossorigin` must be supplied for font preload, including self-hosted fonts. `font-display: swap` limits invisible text time but may introduce swap-induced layout shifts; consider `optional` when test evidence favours it. System fallback stacks and any metrics overrides must be verified across browsers.

## 5. Required implementation evidence

- Explicit font asset origin and **license** with attribution and right-to-host evidence.
- File formats/bundles and transfer size by AR/EN and device, cache policy, CSP, asset origin, and local failure fallback.
- Glyph coverage test with Arabic with harakat, mixed labels, punctuation, currency and identifiers; no missing-glyph boxes.
- Baseline vs final measured number of HTTP requests, CSS discovery waterfall, LCP/CLS/INP field where available; lab proxy clearly labeled, with p75 by device when available.
- Rendering at 320px / 375px / 768px / 1440px / 1920px / ultrawide, zoom 200/400%, low-bandwidth emulation and font asset blocked.
- Verify no host request to third-party font CDN **if local-only policy is chosen**.
- Provide remediation/rollback if typography adversely changes existing visual brand or breaks date/table density.

## 6. References

- https://web.dev/learn/performance/optimize-web-fonts
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40font-face
- https://web.dev/articles/vitals
