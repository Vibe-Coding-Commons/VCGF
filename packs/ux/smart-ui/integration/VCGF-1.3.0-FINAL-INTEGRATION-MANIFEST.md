# VCGF 1.3.0 — Smart UI Final Integration Manifest

**Smart UI Layer:** `v1.0.0`  
**Target framework:** `VCGF 1.3.0 development`  
**Status:** `final-integration-candidate`  
**Official VCGF baseline verified at freeze:** `1.2.0`

## 1. Scope delivered

The integration candidate closes the Smart UI specification layer through four independently selected governance layers:

1. **Smart Screen Composition & Adaptive UX Orchestration** — how the screen is organized.
2. **Smart UI Components** — what reusable UI capabilities are needed.
3. **Smart Interaction Patterns** — how screen state, actions and failures behave.
4. **Smart Journey Orchestration** — how users and context progress across screens and tasks.

Two mandatory bound standards remain independently governed:

- `CALENDAR-GOVERNANCE-ADDENDUM`
- `Enterprise Searchable Select & Combobox`

## 2. Frozen catalog scope

| Layer | Count | Core requirements | Core acceptance scenarios |
|---|---:|---:|---:|
| Smart UI Components | 36 | 432 | 432 |
| Smart Interaction Patterns | 24 | 288 | 288 |
| Screen Compositions | 20 | 240 | 240 |
| Journey Patterns | 18 | 216 | 216 |
| **Total** | **98** | **1176** | **1176** |

Additionally, Calendar Governance includes 14 direct navigation acceptance cases `CAL-NAV-AC01..CAL-NAV-AC14` for direct month/year selection and related date-picker behavior.

## 3. Selective-loading contract

The framework MUST NOT load or implement the whole catalog for every project.

The decision flow is:

`Understand → Inventory → Select Composition → Select Components → Select Interactions → Select Journeys → Reuse First → Review Compatibility → Load Minimum → Implement → Collect Evidence → Verify`

Selection signals remain independent:

- `composition_signals`
- `signals`
- `interaction_signals`
- `journey_signals`

Cross-layer auto-activation is prohibited. Dependencies and relationships are review evidence, not automatic implementation instructions.

## 4. Reuse-first decision order

`verify_first → reuse → extend → wrap → replace → build_new`

`build_new` is permitted only after the existing project inventory and reusable candidates have been evaluated with evidence appropriate to the change risk.

## 5. Final governance files

Adoption is governed by, at minimum:

- `governance/MASTER-POLICY.md`
- `governance/FINAL-ADOPTION-GATE.md`
- `governance/EVIDENCE-CONFORMANCE.md`
- `governance/DECISION-EXPLAINABILITY.md`
- `governance/SMART-UI-COMPONENT-SELECTION.md`
- `governance/SMART-INTERACTION-PATTERN-SELECTION.md`
- `governance/SMART-SCREEN-COMPOSITION-SELECTION.md`
- `governance/SMART-JOURNEY-SELECTION.md`
- `governance/EXPERIENCE-ORCHESTRATION.md`

## 6. Runtime boundary

Documentation, schemas, traceability, selectors, package integrity and deterministic selection tests can pass before application runtime exists. They MUST NOT be reported as proof that a target product has passed accessibility, performance, security, responsive, browser, integration or user-journey runtime acceptance.

The 1176 core acceptance scenarios remain `not_run` at application-runtime level until implementation evidence is attached. The same evidence rule applies to the 14 Calendar navigation cases when adopted by a target application.

## 7. Adoption sequence into VCGF Core

1. Create or use the approved VCGF 1.3.0 development branch.
2. Compare it against the repository baseline documented in `references/REPOSITORY-BASELINE.md`.
3. Place the Smart UI layer under the final repository paths without renumbering existing VCGF controls.
4. Run this package's final validator and integrity checks.
5. Run VCGF repository-native quality gates and compatibility tests.
6. Execute risk-based Pilot and applicable Runtime acceptance scenarios.
7. Collect evidence and resolve exceptions through the documented governance flow.
8. Update framework README/CHANGELOG/VERSION only through the official release decision.
9. Create Tag/Release only after the VCGF release gate approves it.

## 8. Freeze rule

After the final manifest and SHA-256 list are generated, any content change invalidates the freeze and requires rebuilding `manifest.json`, rebuilding `SHA256SUMS.txt`, rerunning final validation, and regenerating the delivery archive.
