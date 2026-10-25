<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Changelog

This project follows a Keep a Changelog-style release history and Semantic Versioning.

## [1.4.0] - Unreleased — Phase 1 architecture and governance (development — not released, not published, not signed)

### Added
- `spec/applicability-matrix.yaml`: canonical, machine-readable applicability for every control (trigger capabilities, always, load point, rationale). `scripts/validate-applicability.py` enforces that every non-deprecated control is reachable by the Task Router for the high-assurance profile from at least one intent, that the capability floor is never hidden and that no trigger names a capability no intent can select.
- Task Router profile layer (additive, monotonic): a control required by the confirmed profile joins the route when one of its trigger capabilities is selected for the task. For the same task baseline ⊆ production ⊆ high-assurance, the capability floor never shrinks and no profile loads a control unrelated to the task (`capability_id: profile-layer`, source `spec/applicability-matrix.yaml`).
- Capabilities `release`, `operations`, `exception` and `governance-change`; intents `release`, `backup`, `email`, `exception` and `governance-change` (routing policy 1.2.0). VCGF-REL-001 joins the minimum task-governance controls. The 19 controls no intent could reach before (VCGF-AI-007, ARCH-002, ARCH-005, AUDIT-003, DATA-003/004/005, DB-003/004, GOV-003/006, OPS-001/004/005, REL-001/002/004, SECR-002, TEST-004) are now reachable.
- User-experience control domain: VCGF-UX-001 Accessibility Conformance (MUST), VCGF-UX-002 Localization and Bidirectional Text (MUST), VCGF-UX-003 Interaction State Integrity (SHOULD), VCGF-UX-004 Responsive Strategy and Density (SHOULD). Production requires UX-001/002, high-assurance all four, baseline lists them as optional (profile_version 1.1.0). Control contract 1.4.0 superset under `schemas/v1.4.0/`; the frozen v1.0 schema is byte-identical and still validates every v1.0 control.
- `spec/acceptance/<domain>.yaml`: verifiable acceptance tests for all 88 controls (criterion, method, negative path, evidence type, automation hook), enforced by `scripts/validate-acceptance.py` and exposed by `vcgf.py acceptance <control-id>`.
- Governed Smart UI selection: `runtime/ui_select.py`, `runtime/ui-bindings.yaml`, contract `ui-selection` 1.1.0 and `vcgf.py ui-select <route> <screen-context>`. Smart UI layers load only for the user-experience controls present in the route, hash-pinned by the frozen package manifest, confined to the package directory and budgeted; standards selected by signals but not governed by a control in the route are reported as deferred and never loaded.
- Tests `tests/scenarios/test_profile_layer.py` and `tests/scenarios/test_ui_select.py`; fixtures `tests/fixtures/v1.1/screen-context.json` and `ui-selection.json`.
- Phase 2 (token efficiency and context optimisation): derived control cards `spec/control-cards/` with shared `common-clauses.md` (`scripts/generate-control-cards.py --check` in the gate); `lean`/`standard` routes load cards, `deep` routes load full controls (`context_detail`); the loader strips attribution comments from served Markdown.
- Multi-intent routing (`intents` on the task: union of capabilities, highest risk, one route) and delta loading (`loaded_context`: only unseen or changed items are sent; `reused_tokens`, `reused_context`; stale hashes are re-sent); registry cached per process while no canonical source changes.
- `runtime/tokens.py`: bytes measured, tokens estimated by a documented heuristic, observed only with an explicit `VCGF_TOKENIZER`; budgets enforced on tokens with `cost_bytes` reported; `ui-select` serves Smart UI requirement cards for lean/standard routes (`served_bytes`) and full standards for deep routes.
- CLI prints hash-pinned references by default (`--full` inlines text); `vcgf.py acceptance all` summarises definitions with execution state (always `not_executed` here).
- Acceptance tests follow the binding interpretation rules (`spec/acceptance/README.md`): numeric thresholds are documented `parameters`, SHOULD is never tested as MUST, requirement sources are ranked; `tests/scenarios/test_applicability_triggers.py` and `tests/scenarios/test_context_efficiency.py`.

### Changed
- `runtime/contracts.py` caches the known-control set by catalog content instead of re-parsing the catalog on every contract validation (registry build about 1.2 s → about 0.2 s on the reference machine).
- Adapter control mappings carry UNVERIFIED rows for the four user-experience controls; platform behaviour for UI governance is not claimed.
- `scripts/validate-version.py` accepts `release_status: development` for develop branches; the release workflow refuses it.
- Budget semantics: `limit_tokens` is now compared with estimated tokens of the served text instead of raw bytes (the declared contract); routes that were blocked only by the four-fold byte over-count now fit. Coverage is unchanged: a budget still blocks, never drops controls.
- Cumulative compatibility record `docs/quality/v1.4/baseline-compatibility-v1.4.json` (inherits v1.3.1). All 84 v1.0 controls, their identifiers, the frozen v1.0 schemas, licence and attribution are unchanged.

## [1.3.1] - 2026-10-24 — Integrity and governance hardening (release candidate — not published, not signed)

### Security
- Instruction-hierarchy clause added to all legacy always-on entry files and enforced by `scripts/validate-adapters.py`: repository, tool or generated content never overrides the host system and user authority chain.
- Development-agent safeguards made unconditional in the Task Router: context flags no longer drop VCGF-AI-002, VCGF-AI-004, VCGF-AI-006, VCGF-AI-008 or VCGF-AI-009 from a route.
- New `scripts/validate-package-integrity.py` verifies the frozen Smart UI `SHA256SUMS.txt` and `manifest.json` in the release gate and in CI.
- CI workflows run with least-privilege `permissions` and SHA-pinned actions.
- New release workflow that only drafts a release for a verifiable signed tag, attaching source archives, `SHA256SUMS.txt` and a CycloneDX SBOM; it never publishes on its own.

### Fixed
- Version identity made consistent across `runtime/bootstrap.md`, the seven platform guides, `VCGF-MANIFEST.yaml` adapters (supported and candidate) and contract schema versions, enforced by an extended `scripts/validate-version.py`.
- Generators and validators made read-only/portable: `--check` modes instead of silent rewrites, UTF-8 and LF enforced on every write.

### Changed
- Smart UI layer status aligned to `integration-candidate` in `packs/ux/catalog.yaml`; its runtime acceptance scenarios remain `not_run`.
- `VCGF-MANIFEST.yaml` gains `candidate_adapters`, `candidate_adapter_versions` and `contract_schema_versions`; `release_status` is `release-candidate` until publication.

### Release Status
Candidate prepared locally on a worktree cut from tag v1.3.0 (commit 43c617d). Publication requires independent review by a non-author and a verifiable tag signature; neither exists yet. v1.3.0 remains the latest published release. Production admission remains BLOCKED. All existing Control IDs, contracts, licensing and founder rights are preserved.

## [1.3.0] - 2026-10-24 — Smart UI & Adaptive Experience Orchestration (public framework release)

### Added
- VCGF Smart UI Components & Interaction Standards v1.0.0 as a selective UX capability pack.
- 36 Smart UI component standards with reuse-first selection and compatibility review.
- 24 Smart Interaction Patterns for stateful create/edit/delete/save/retry/conflict/session/offline behavior.
- 20 Screen Composition standards, including mobile-focused and large-screen modifiers.
- 18 Journey Patterns for cross-screen flow, deep links, return-to-origin, approvals, queues, offline sync and long-running work.
- Calendar month/year direct selection governance and centralized enterprise searchable-select binding.
- Smart UI governance for RTL/LTR, accessibility, responsive density, action hierarchy, information architecture, context continuity, explainability and evidence.

### Changed
- Adaptive UX can selectively load the Smart UI entrypoint and master policy without activating the entire catalog.
- Repository integration adds Smart UI traceability, schemas, tests, adapters and project-history evidence while preserving all existing Control IDs and Profiles.

### Release Status
Public framework source distribution authorized by the owner on 2026-10-24 after repository-native validation on the exact candidate. Production admission and target-application certification remain separate and BLOCKED unless their required evidence is accepted.


## [1.2.0] - 2026-10-21 — Adaptive Engineering & UX (public framework release)

### Added
- Adaptive Engineering Engine for architecture and design pattern recommendations.
- Adaptive UX Intelligence Engine for project-specific user experience decisions.
- Responsive mobile, tablet, and desktop design guidance.
- RTL/LTR component standards and bidirectional content support.
- Local WOFF2 typography and font performance guidelines.
- New validation contracts, automated tests, and 21 cumulative release acceptance gates.

### Improved
- Runtime integration with existing VCGF capabilities.
- Engineering decision traceability and evidence validation.
- Arabic and English documentation.
- Release governance and quality assurance.

### Release Status
Public framework release authorized by the owner following successful repository CI. Production admission remains BLOCKED pending target application, provider/host acceptance, independent review, and the outstanding 21 cumulative release gates. Existing controls, licensing, and founder rights are preserved. Fixes will use v1.2.1 onward.

## [Unreleased] — target 1.1.0

Historical v1.1 development checkpoint: at that time VERSION remained 1.0.0; v1.1 was not published independently. Its opt-in additions ship in the public v1.2.0 framework distribution, with open production acceptance boundaries.

### Added

- Seven opt-in versioned contracts and local validation.
- Task Router, bounded typed dependency resolution, selective control/pack loading, context freshness, handoff and budget checks.
- Scoped approval/evidence gates, required Profile coverage, artifact integrity, expiring exceptions and three evidence views.
- Reference CLI, 23 capability definitions, original sections 14–39 requirement packs and derived runtime registry.
- Executable TLS SMTP/OAuth email reference, encrypted outbox, SQLite unified backup/restore, and sandbox PostgreSQL/MySQL command adapters.
- Compact generated entries for seven existing adapters plus experimental ChatGPT, repository Skill source and local adapter tests.
- Local test evidence and context-size measurements, with explicit Unverified boundaries.

### Changed

- Updated English and Arabic README with current/target version, new uses, runnable examples and remaining acceptance work.
- Documented a narrowly approved exception for the three changed original documentation files in the compatibility check; canonical controls, Profiles and legal files remain pinned.

### Verification and remaining acceptance

- Prior development checkpoint: 178 local tests, 14 legacy validators and 36 context-size measurements; no claim of observed model tokens or full release acceptance.
- Live Microsoft 365, PostgreSQL/MySQL restore consistency, host authentication/enforcement, platform surfaces and remaining pack acceptance are still open.
- No changes to Control IDs, license or founder rights. No publication or production operation performed.

## [1.0.0] - 2026-10-02

### Added

- Human-first English and Arabic onboarding experience, daily user guide, and verified setup guides for all seven adapters.
- Vendor-neutral VCGF Core architecture and 84 normative controls.
- Baseline, Production, and High-Assurance profiles.
- Generic, Lovable, Claude Code, Bolt, v0, Replit, and Cursor adapters with independent versioning.
- Evidence, conformance, exception, risk, lifecycle, and human-approval models.
- Machine-readable control catalog, profiles, adapter manifests, mappings, verification-source registers, and JSON Schemas.
- Automated validators and GitHub Actions quality gates.
- English and Arabic canonical README documentation.
- Legal attribution, Apache-2.0 licensing, citation metadata, templates, checklists, examples, and operational playbooks.

### Changed
- Evolved the earlier Lovable Secure Vibe Coding Governance Framework into vendor-neutral VCGF.
- Normalized the pre-release secrets control namespace to the frozen `VCGF-SECR-*` namespace before the v1.0.0 ID freeze.

### Security
- Strengthened validation, injection defense, personal-data protection, field-level encryption, password recovery, supply-chain provenance, monitoring, and release artifact integrity.
