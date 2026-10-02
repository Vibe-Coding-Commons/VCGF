<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Versioning model

VCGF Core, each adapter, and machine-readable schemas use Semantic Versioning independently.

- **Core MAJOR**: breaking normative/schema/conformance change.
- **Core MINOR**: backward-compatible controls or capabilities.
- **Core PATCH**: compatible corrections/clarifications.
- **Adapter versions** change independently when platform behavior, mapping, or verification changes.
- **Control IDs** are immutable after v1.0.0. Deprecated IDs are never reused.

An adapter declares `framework_compatibility`; updating one adapter does not force a Core release when the Core contract is unchanged.
