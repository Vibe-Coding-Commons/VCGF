<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF v1.0.0 Architecture Report

## Executive summary
VCGF v1.0.0 converts the earlier Lovable-centered governance package into a vendor-neutral, evidence-driven, machine-validatable framework. The logical Core is `spec/`, `controls/`, `profiles/`, and `schemas/`. Platform behavior is isolated in independently versioned adapters.

## Architecture decisions
- One canonical Control source per requirement.
- Core defines **what must be achieved**; adapters define **how a verified platform surface can support it**.
- Platform claims require traceable verification sources or an explicit unverified state.
- Framework, adapters, and schemas use independent versioning contracts.
- Generated catalogs/manifests are derived from canonical source data rather than maintained as competing sources of truth.
- Conformance is evidence-based and cannot be claimed merely by copying framework files.

## Core vs Adapter separation
The Core contains no Lovable-, Claude-, Bolt-, v0-, Replit-, Cursor-, or other vendor-specific implementation guidance. Dedicated adapters map Core controls using the controlled mapping vocabulary and document exact scope, limitations, evidence, and source claims.

## Control model
VCGF v1.0.0 contains **84 canonical normative controls across 17 domains**. Each control has an immutable v1 ID, YAML front matter, normative requirement level, verification method, required evidence, exceptions, dependencies, related controls, references, platform considerations, and change history.

The pre-v1 Secrets namespace was normalized from `VCGF-SEC-SECRET-*` to `VCGF-SECR-*` before the v1.0.0 ID freeze.

## Adapter model
Seven supported adapters ship in v1.0.0: Generic, Lovable, Claude Code, Bolt, v0, Replit, and Cursor. Each has a 1.0.0 adapter version, Core compatibility range, manifest, canonical machine-readable control mapping, human-readable mapping, capabilities, limitations, installation guidance, verification sources, test checklist, examples, and changelog.

## Security model
Coverage includes authentication, authorization, RBAC/ABAC, object and tenant isolation, sessions/MFA, password storage/recovery, input validation, injection defenses, files, APIs, database integrity, PII/privacy, encryption/key management, secrets, logging/audit, dependencies/SBOM, backups/recovery, monitoring, release integrity, and incident response.

## AI governance model
AI-specific controls cover inspect-before-generate, context governance, silent assumptions, architecture drift, unrequested refactoring/features, hallucinated APIs/packages, sensitive changes, security-control tampering, prompt/tool injection, and persistent instruction governance.

## Migration summary
The source inventory contained 93 migration inputs: **37 MOVE**, **43 GENERALIZE**, **12 MOVE-TO-ADAPTER**, and **1 MERGE** decisions. No security requirement was intentionally dropped. Final destinations are recorded in `migration-map.md` and `traceability.md`.

## Platform support
The v1 release includes Generic, Lovable, Claude Code, Bolt, v0, Replit, and Cursor. Vendor-specific capability claims are maintained under each adapter's `verification/` directory.

## Known limitations
VCGF cannot make behavioral AI instructions equivalent to runtime enforcement. Application security controls still require implementation at trusted code, database, identity, infrastructure, CI/CD, or operational boundaries. Platform capabilities can change after the adapter's `last_verified` date.

## Final architecture
The final release uses the repository architecture generated in the root `REPOSITORY-TREE.md`, with operational procedures under `playbooks/` and migration records retained under `docs/project-history/v1.0.0/`.
