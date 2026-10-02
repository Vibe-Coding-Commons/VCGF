<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Platform compatibility

VCGF Core is vendor-neutral. Platform adapters are versioned and verified independently. Use the adapter only for the platform surface named in its manifest; do not infer behavior for other products from the same vendor.

| Adapter | Version | Framework compatibility | Status | Verified surface | Last verified | Setup guide |
|---|---|---|---|---|---|---|
| Generic | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Portable AI-assisted development workflow | 2026-10-02 | [Guide](platform-guides/generic.md) |
| Lovable | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Lovable web application builder and project repository context | 2026-10-02 | [Guide](platform-guides/lovable.md) |
| Claude Code | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Claude Code | 2026-10-02 | [Guide](platform-guides/claude.md) |
| Bolt | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Bolt web project agent | 2026-10-02 | [Guide](platform-guides/bolt.md) |
| v0 | 1.0.0 | `>=1.0.0 <2.0.0` | stable | v0 web agent and Projects | 2026-10-02 | [Guide](platform-guides/v0.md) |
| Replit | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Replit Agent project | 2026-10-02 | [Guide](platform-guides/replit.md) |
| Cursor | 1.0.0 | `>=1.0.0 <2.0.0` | stable | Cursor Agent / IDE project rules | 2026-10-02 | [Guide](platform-guides/cursor.md) |

## Enforcement model

Individual control mappings classify support as `NATIVE`, `CONFIGURABLE`, `PROMPT-ENFORCED`, `EXTERNAL`, `PARTIAL`, `UNSUPPORTED`, `NOT-APPLICABLE`, or `UNVERIFIED`. The canonical mapping is `platforms/<adapter>/control-mapping.yaml`.

## Verification sources

Each adapter keeps source-traceable claims in `platforms/<adapter>/verification/sources.yaml`. Vendor documentation is preferred for platform-specific behavior.

## If the platform is not listed

Use the [Generic guide](platform-guides/generic.md) rather than guessing that another adapter applies.
