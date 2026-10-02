<!--
VCGF - Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Author: Eng. Hamada Sami
Mobile + WhatsApp: +966560000934
Email: i@hamada.io
LinkedIn: https://www.linkedin.com/in/hamadas/
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Authentication and Password Recovery Audit Prompt

Perform a read-only audit of:
- login
- rate limiting
- enumeration
- password policy
- password hashing/provider
- signup/verification
- reset request
- reset token generation/storage/expiry/single-use
- reset URL origin/redirect
- reset page token leakage
- session invalidation
- notifications
- recovery channel changes
- MFA enrollment/change/recovery
- admin recovery
- active sessions

Flag flows that:
- reveal account existence
- store plaintext reset tokens unnecessarily
- use predictable tokens
- auto-login after reset without deliberate design
- disable MFA through reset
- trust Host header for reset origin
- lack rate limits
- log reset URLs/tokens
