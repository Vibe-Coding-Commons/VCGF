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
