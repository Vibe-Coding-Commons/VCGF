<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# E-commerce adoption example

## Scenario
An internet-facing commerce application handles accounts, carts, pricing, discounts, orders, payments through a provider, webhooks, and customer data.

## Recommended adoption
1. Select the **Production** profile and threat-model account takeover, price manipulation, webhook abuse, inventory races, and automated abuse.
2. Recalculate price, discount, tax, shipping, and order totals on trusted server-side logic; never trust client totals.
3. Rate-limit login, password recovery, coupon, checkout, and abuse-sensitive endpoints using risk-appropriate controls.
4. Keep payment-provider and integration secrets outside client code and validate webhook authenticity and replay protections supported by the provider.
5. Treat password recovery as an account-security flow with generic responses, strong single-use tokens, expiry, and session handling.
6. Minimize payment and identity data retained by the application.

## Priority controls
`VCGF-API-002`, `VCGF-API-003`, `VCGF-API-004`, `VCGF-IAM-001`, `VCGF-IAM-005`, `VCGF-SECR-001`, `VCGF-PRIV-003`, `VCGF-TEST-006`.

## Verification evidence
- Price-manipulation and duplicate-checkout tests.
- Password-reset and account-enumeration tests.
- Webhook signature/replay test evidence where provider capabilities exist.
- Secret-scanning and configuration evidence.
- Release monitoring for authentication, checkout, and payment failures.

## Example release decision
A release is blocked when changing a browser request can reduce the authoritative charge amount, reset tokens are reusable, or provider secrets reach public client bundles.
