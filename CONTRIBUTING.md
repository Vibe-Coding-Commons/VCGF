<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Contributing to VCGF

## Before contributing

Read `GOVERNANCE.md`, `spec/VCGF-CORE.md`, and the relevant control/adapter documentation. Contributions must preserve vendor neutrality, stable IDs, SPDX attribution, and the single-source-of-truth model.

## Proposing a control

Search the catalog for overlapping outcomes. A proposal must explain risk, requirement level, applicability, verification method, evidence, dependencies, and why an existing control cannot cover the requirement.

## Proposing or updating an adapter

Start from `platforms/_adapter-template/`. Define exact platform surface, cite official documentation, update `verification/sources.yaml`, map every Control ID, document limitations, and run adapter validation. Unverified claims remain `UNVERIFIED`.

## Required checks

Install `requirements-dev.txt`, then run `python scripts/release-quality-gate.py`. Update documentation and changelogs when behavior or public structure changes. Pull requests must not introduce duplicate controls, stale generated files, missing SPDX, or unverified claims represented as facts.
