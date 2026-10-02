<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Security policy

Report security issues in the **VCGF repository itself** privately to **i@hamada.io**. Do not publish exploitable repository/tooling vulnerabilities, leaked credentials, or sensitive reporter data in a public issue before coordinated review.

## Scope

Security reports may cover validator bypasses, unsafe release automation, malicious or misleading platform mapping, secret exposure in repository assets, or a VCGF requirement whose wording creates a concrete security risk. Vulnerabilities in third-party platforms should be reported to those vendors through their own channels.

## Reporting content

Include the affected version/path, impact, reproducible steps, and a safe proof of concept when appropriate. Never test systems you do not own or lack permission to assess.

## Handling

Confirmed issues are triaged for control impact, adapter impact, backward compatibility, and release severity. Stable Control IDs are preserved unless the project is still before the relevant version freeze.
