# Changelog

## 1.0.0 — VCGF 1.3.1 integrity patch (2026-10-24)
- The package validator (`scripts/validate_final.py` / `scripts/validate_package.py`) no longer rewrites the example plans or any other file: it is read-only and platform-independent, with no CRLF side effects; stored `examples/*.plan.json` are compared against freshly generated plans (`Stored example plans match generated plans`).
- Integrity mismatches (manifest content, checksum entries, stored plan drift) are named in full; the offending-path list is no longer truncated.
- `manifest.json` and `SHA256SUMS.txt` regenerated for the patched validator and this changelog.
- No standard, catalog, schema, example or governance content changed.
- `scripts/build_manifest.py` made portable (POSIX path-part ordering, LF output on every platform); `reports/DOCUMENTATION-VALIDATION.*` regenerated to reflect the 73-check validator.

## 1.0.0 — Final Smart UI Integration Candidate
- Added 18 Smart Journey Patterns and cross-screen journey orchestration.
- Added Journey Contract, selection rules, compatibility matrix, schemas, traceability and examples.
- Added Deep-Link, Context Continuity, Return-to-Origin, Explainability, Evidence and Final Adoption policies.
- Upgraded Screen Context and selection plan schemas to 1.0.0.
- Final four-layer selective architecture: Composition + Components + Interactions + Journeys.
- Calendar year/month direct selection remains mandatory in the bound Calendar Governance standard.

## 0.5.0
- Added Smart Screen Composition & Adaptive UX Orchestration.

## 0.4.0
- Added 24 Smart Interaction Patterns.

## 0.3.0
- Expanded catalog to 36 components.

## 0.2.0
- Added selective selection/reuse governance and bound Calendar/Searchable Select standards.
