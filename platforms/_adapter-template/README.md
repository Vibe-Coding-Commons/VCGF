<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# How to build a VCGF adapter

Use this directory as the normative authoring template for a new platform adapter.

## Required process

1. Define the exact platform surface; a vendor name alone is insufficient.
2. Create `adapter.yaml` and keep adapter SemVer independent from VCGF Core.
3. Inventory platform capabilities using official documentation first.
4. Record every material claim in `verification/sources.yaml`.
5. Map every canonical control in `control-mapping.yaml` using only the approved status vocabulary.
6. Keep Core policy out of the adapter; reference Control IDs and describe platform implementation only.
7. Document unsupported and external controls without hiding limitations.
8. Add rules, prompts, examples, templates, and tests that are actually useful for the platform surface.
9. Run `python scripts/validate-adapters.py` and `python scripts/release-quality-gate.py`.
10. Release the adapter only when its declared status matches its verification quality.

## Required files

`README.md`, `ADAPTER.md`, `adapter.yaml`, `control-mapping.yaml`, `CONTROL-MAPPING.md`, `CAPABILITIES.md`, `LIMITATIONS.md`, `INSTALLATION.md`, `CHANGELOG.md`, `verification/sources.yaml`, `verification/verification-report.md`, and meaningful content under `rules/`, `prompts/`, `mappings/`, `templates/`, `examples/`, and `tests/`.
