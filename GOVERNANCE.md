<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Framework governance

## Control lifecycle

Control IDs become immutable at v1.0.0. A control may be clarified without changing its intended outcome in a compatible release. A materially changed normative outcome requires version impact analysis. Retired controls are marked `deprecated`; their IDs are never reused.

## Adapter governance

Adapters use independent SemVer. Acceptance requires exact platform scope, official-source verification where available, complete control mapping, limitations, installation guidance, tests, and a status consistent with evidence. Adapter deprecation does not automatically change the Core version.

## Maintainer responsibilities

The Founder & Maintainer protects vendor neutrality, control-ID integrity, source traceability, security-sensitive change review, release quality, and transparent changelogs. Contributions are reviewed for duplication, breaking changes, evidence quality, and licensing/attribution.

## Release process

A stable release requires passing repository validators, generated-file freshness, version consistency, documented warnings, and a final release report. Security-sensitive changes require explicit review and cannot bypass the quality gate.
