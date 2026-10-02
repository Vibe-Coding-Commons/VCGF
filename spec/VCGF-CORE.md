<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF Core specification

VCGF is an open, vendor-neutral, evidence-driven governance, security, privacy, and engineering framework for controlled AI-assisted software development.

## Architectural law

`Core → Normative Controls → Profiles → Platform Adapter → Platform-Specific Implementation`

The logical Core is `spec/`, `controls/`, `profiles/`, and `schemas/`. Controls define **what must be achieved**. Platform adapters define **how the requirement can be carried into a verified platform surface**. An adapter never creates a competing copy of a Core policy.

## Single source of truth

Each normative requirement has one immutable Control ID after v1.0.0. Control Markdown front matter is canonical. `spec/control-catalog.yaml` is generated from that front matter. Profile YAML and adapter mapping YAML are canonical for their respective machine-readable domains.

## Conformance boundary

Copying VCGF files does not create conformance. A conformant project identifies framework version, profile, adapter/version, required controls, evidence, exceptions, unsupported/external controls, outstanding findings, and validation date.

## Security boundary

Prompt or instruction compliance is behavioral. Runtime authentication, authorization, validation, cryptography, database policy, monitoring, and deployment controls must be enforced at trusted technical layers unless a documented adapter mapping identifies equivalent native enforcement.
