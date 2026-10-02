<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Platform compatibility

| Adapter | Version | Framework compatibility | Status | Platform surface | Last verified | Native enforcement | Prompt enforcement | External enforcement | Known limitation |
|---|---|---|---|---|---|---|---|---|---|
| generic | 1.0.0 | >=1.0.0 <2.0.0 | stable | Portable AI-assisted development workflow | 2026-10-02 | None claimed globally | Yes | Yes | Behavioral instructions depend on the selected AI tool consuming the provided context. |
| lovable | 1.0.0 | >=1.0.0 <2.0.0 | stable | Lovable web application builder and project repository context | 2026-10-02 | None claimed globally | Yes | Yes | Knowledge and instruction files shape agent behavior; they are not an application-runtime enforcement boundary. |
| claude | 1.0.0 | >=1.0.0 <2.0.0 | stable | Claude Code | 2026-10-02 | None claimed globally | Yes | Yes | Instructions can guide behavior but runtime and CI controls remain external. |
| bolt | 1.0.0 | >=1.0.0 <2.0.0 | stable | Bolt web project agent | 2026-10-02 | None claimed globally | Yes | Yes | Project Knowledge guides the agent but does not replace trusted server/database controls. |
| v0 | 1.0.0 | >=1.0.0 <2.0.0 | stable | v0 web agent and Projects | 2026-10-02 | None claimed globally | Yes | Yes | Instructions are behavioral controls and must be reinforced by code, tests, CI, and runtime authorization. |
| replit | 1.0.0 | >=1.0.0 <2.0.0 | stable | Replit Agent project | 2026-10-02 | None claimed globally | Yes | Yes | Agent may update replit.md, so governance changes to that file should be code-reviewed. |
| cursor | 1.0.0 | >=1.0.0 <2.0.0 | stable | Cursor Agent / IDE project rules | 2026-10-02 | None claimed globally | Yes | Yes | Rule adherence is behavioral context; trusted runtime controls and CI remain external. |

Exact per-control mapping is in each adapter `control-mapping.yaml`.
