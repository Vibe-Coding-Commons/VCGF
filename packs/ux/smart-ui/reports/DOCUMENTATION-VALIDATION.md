# فحص VCGF Smart UI v1.0.0

**PASS**

- Components: 36
- Interactions: 24
- Screen Compositions: 20
- Journeys: 18
- Requirements / Acceptance: 1176 / 1176
- Checks: 72/72
- Local links: 2449
- Negative schema tests: 12/12 rejected

> الفحص يثبت سلامة الحزمة والمخططات والاختيار والتتبع فقط. Runtime tests للتطبيقات تبقى `not_run`.

| الفحص | الحالة | التفاصيل |
|---|---|---|
| Package catalog counts | pass | 36/24/20/18 |
| Screen composition split | pass | 18 primary + 2 modifiers expected |
| Unique standard IDs | pass | 98 IDs |
| Package metadata final candidate | pass | catalog package metadata |
| Component rule coverage | pass | 36/36 |
| Interaction rule coverage | pass | 24/24 |
| Composition rule coverage | pass | 20/20 |
| Journey rule coverage | pass | 18/18 |
| External bindings exactly two | pass | Calendar + Searchable Select |
| Calendar source snapshot digest | pass |  |
| Searchable source snapshot digest | pass |  |
| Calendar direct navigation: اختيار السنة مباشرة | pass |  |
| Calendar direct navigation: اختيار الشهر مباشرة | pass |  |
| Calendar direct navigation: viewDate | pass |  |
| Calendar direct navigation: selectedDate | pass |  |
| Calendar direct navigation: birthDate | pass |  |
| Calendar direct navigation: CAL-NAV-AC14 | pass |  |
| Searchable Select contract: embedded, auto-focused search input | pass |  |
| Searchable Select contract: أول صف داخل القائمة | pass |  |
| Searchable Select contract: التركيز تلقائيًا | pass |  |
| Searchable Select contract: لا تفرض مكوّنًا معقدًا على كل اختيار | pass |  |
| Component document contracts | pass | OK |
| Interaction document contracts | pass | OK |
| Screen document contracts | pass | OK |
| Journey document contracts | pass | OK |
| Total requirements | pass | 1176 |
| Total acceptance scenarios | pass | 1176 |
| Reference settings/policies | pass | 288+144+120+108=660 |
| Journey traceability count | pass | 216 |
| Acceptance matrix total | pass | 1176 rows |
| Component catalog schema | pass | valid |
| Interaction catalog schema | pass | valid |
| Screen catalog schema | pass | valid |
| Journey catalog schema | pass | valid |
| Component contracts schema | pass | valid |
| Interaction contracts schema | pass | valid |
| Screen contracts schema | pass | valid |
| Journey contracts schema | pass | valid |
| Component compatibility schema | pass | valid |
| Interaction compatibility schema | pass | valid |
| Screen compatibility schema | pass | valid |
| Journey compatibility schema | pass | valid |
| Central settings schema | pass | valid |
| Interaction policy schema | pass | valid |
| Screen orchestration schema | pass | valid |
| Screen context template schema | pass | valid |
| Project assessment schema | pass | valid |
| Evidence record schema | pass | valid |
| All example contexts validate | pass | OK |
| All generated plans validate | pass | OK |
| No-UI selects zero | pass |  |
| Birthdate selective component | pass |  |
| Birthdate journey | pass |  |
| Birthdate bound standards | pass |  |
| Enterprise remains selective | pass | 11/11/2/1 |
| Bulk + long-running journey selection | pass |  |
| Bulk journey compatibility review | pass |  |
| Approval dual branch journeys | pass |  |
| Approval branch review emitted | pass |  |
| Scope switch journey only expected | pass |  |
| Document lifecycle journey | pass |  |
| Public self-service journey | pass |  |
| Component-only guard | pass |  |
| Interaction-only guard | pass |  |
| Composition-only guard | pass |  |
| Journey-only guard | pass |  |
| Interactive catalog covers all 98 core standards | pass | OK |
| Interactive catalog includes bound standards | pass |  |
| Markdown code fences balanced | pass | OK |
| Local links and anchors resolve | pass | 2449 checked |
| Negative schema tests | pass | 12/12 rejected |
| Manifest and SHA-256 integrity | pass | OK |
