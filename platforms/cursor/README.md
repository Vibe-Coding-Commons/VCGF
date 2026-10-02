<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF adapter: Cursor

**Adapter:** `cursor`  
**Version:** 1.0.0  
**Framework compatibility:** `>=1.0.0 <2.0.0`  
**Status:** stable  
**Surface:** Cursor Agent / IDE project rules  

## Scope

Cursor Project Rules under .cursor/rules and root AGENTS.md as documented for Cursor Agent. Runtime security controls remain project responsibilities.

## Use this adapter when

You are applying VCGF to the documented platform surface above. The Core defines what the project must achieve; this adapter explains how to carry VCGF instructions, prompts, evidence, and external-control mappings into Cursor.

## Install

Follow [`INSTALLATION.md`](INSTALLATION.md), then validate the adapter with `python scripts/validate-adapters.py` from the repository root.

## Canonical files

- `adapter.yaml`: adapter identity, version, scope, and capability declaration.
- `control-mapping.yaml`: machine-readable mapping to every VCGF control.
- `verification/sources.yaml`: verified platform claims and official sources.
- `rules/`: platform-appropriate instruction assets.
- `prompts/`: review prompts that supplement persistent rules.

## Security boundary

Agent instructions are never treated as a substitute for runtime authentication, authorization, validation, encryption, secret management, audit, or production controls unless the mapping explicitly identifies documented platform enforcement.
