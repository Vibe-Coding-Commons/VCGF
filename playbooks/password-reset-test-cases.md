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

# Password Reset Security Test Cases

- Existing and non-existing accounts receive indistinguishable user-facing responses.
- Reset request is rate-limited.
- Token is unpredictable.
- Token expires.
- Token cannot be reused.
- Superseded-token behavior matches policy.
- Token is not logged.
- Reset URL uses trusted HTTPS origin.
- Redirect is allowlisted.
- Token grants only recovery capability.
- New password follows password policy.
- Password is securely hashed/provider-managed.
- No automatic login unless deliberately reviewed.
- Existing sessions are invalidated according to policy.
- Outstanding recovery tokens are invalidated.
- User receives security notification.
- Password reset does not disable MFA.
- Recovery channel changes require stronger verification.
