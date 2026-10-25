<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/secrets/vcgf-secr-001-secrets-and-environment-protection.md -->
# VCGF-SECR-001 — Secrets and Environment Protection
MUST · secrets · profiles: baseline, high-assurance, production · full text: controls/secrets/vcgf-secr-001-secrets-and-environment-protection.md

## Requirement
Secrets MUST remain out of client bundles, source control, logs, URLs, and unsafe configuration, and MUST be isolated by environment with least privilege.

## Guidance
Secrets include API keys, DB secrets, privileged platform keys, encryption/signing keys, webhook secrets, OAuth client secrets, SMTP credentials, and private certificates.

Never place secrets in:
- frontend bundles
- source code
- public env vars
- Git history
- browser localStorage
- URLs
- logs
- screenshots/docs

Use platform secret managers or a dedicated vault.

Scope by environment/service and prefer narrowly scoped credentials.

Document owner, usage, expiry/rotation, and emergency revocation.

A suspected leak requires rotation; deleting from the latest commit is not enough.

Common clauses (spec/control-cards/common-clauses.md): Applicability[A] Verification[A] Evidence[A] Exceptions[A] Dependencies[A] Related[A] Platform[A]
