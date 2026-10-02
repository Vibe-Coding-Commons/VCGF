<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# VCGF user guide — day-to-day use

This guide explains how to use VCGF **after installation**. It is written for developers, product owners, technical founders, and power users of AI coding tools.

[← Main README](../README.md) · [Platform setup guides](platform-guides/README.md) · [Control catalog](../spec/control-catalog.yaml)

## 1. The daily mental model

VCGF does not ask you to become a security engineer before every prompt. It changes the conversation from “make this change” to a controlled engineering loop:

1. **Understand** — restate the requested outcome and constraints.
2. **Inspect** — read the relevant existing code, schema, roles, APIs, and tests.
3. **Impact analysis** — identify what may change or break.
4. **Risk analysis** — classify the change LOW, MEDIUM, HIGH, or CRITICAL.
5. **Plan** — describe the minimum safe change and tests.
6. **Approval when required** — stop before sensitive work.
7. **Implement** — change only the approved scope.
8. **Validate and test** — include negative/security paths where relevant.
9. **Security and regression review** — confirm existing protections still work.
10. **Evidence** — keep proof of what was tested or reviewed.
11. **Release review** — use the release checklist before shipping.

## 2. Before your first task of the day

Confirm that the AI can identify:

- VCGF version (`1.0.0` for this release);
- selected profile;
- platform adapter;
- project-context source;
- relevant persistent rule/instruction file;
- changes that require human approval.

If it cannot, fix context before asking for implementation.

## 3. Universal first-session message

```text
Read the active VCGF project rules and project context before changing anything. Confirm the VCGF version, selected profile, adapter, project constraints, relevant controls, and any approval gate. Inspect the existing implementation first. Do not modify code yet.
```

Use your platform guide for a more specific version.

## 4. How to request a feature

### Good request

```text
Add profile-photo upload for authenticated users. Follow VCGF. Inspect the current storage, authorization, validation, and file-access design first. Show the impact/risk plan and tests before implementation, and wait for approval if required.
```

### What the AI should do

- inspect existing upload/storage patterns;
- identify affected UI, API, storage, permissions, and database records;
- validate file type/size/name and access model;
- avoid public storage unless the requirement calls for it and the risk is accepted;
- test allowed and denied access;
- keep evidence before declaring completion.

## 5. How to request a bug fix

### Example

```text
The user can see another user's record under some conditions. Reproduce the problem first. Treat it as an authorization/data-isolation issue, identify the root cause, make the minimum safe fix, add regression tests for both allowed and denied access, and show the evidence.
```

For a security bug, do not ask the AI to “make the error disappear.” Require root-cause analysis and a negative test.

## 6. How to request a database change

### Example

```text
Add a national ID field to the customer profile. Before changing the schema, classify the data, define validation/access/encryption/retention requirements, inspect existing records and indexes, propose a backward-compatible migration, and show rollback/test steps. Wait for approval before a destructive or high-risk change.
```

Use:

- `templates/database/migration-review.md`
- `checklists/database-change/database-change.md`
- `templates/security/data-classification.md`
- `templates/security/encryption-register.md` when encryption is applicable.

## 7. How to request an authentication change

### Example

```text
Add Google sign-in. Inspect the existing authentication, account-linking, session, MFA, recovery, and authorization flows. Identify account-takeover or duplicate-account risks, propose the plan and tests, then wait for approval before changing the authentication boundary.
```

Authentication and recovery changes are not UI-only work. Expect HIGH/CRITICAL governance when the blast radius justifies it.

## 8. How to ask for a security review

```text
Run a VCGF security review of this change. Map the affected controls, test positive and negative authorization/validation paths, check secrets and data exposure, identify remaining findings, and produce security-test evidence. Do not claim conformance from a scan alone.
```

Use `checklists/security-review/security-review.md` and `templates/testing/security-test-evidence.md`.

## 9. How to review the AI plan

Before approving, check five things:

1. **Scope** — does the plan change only what you asked for?
2. **Impact** — does it list database, APIs, auth, roles, files, integrations, tests, and deployment surfaces that may be affected?
3. **Risk** — is the risk classification believable?
4. **Controls** — are the relevant VCGF protections represented?
5. **Verification** — does the plan say how success and failure/denied paths will be tested?

If the plan says “refactor the whole module” for a small feature, ask for a smaller plan.

## 10. How to approve

Approval should be scoped. A useful approval message is:

```text
Approved for the plan you described only. Do not expand scope. Preserve existing behavior outside the listed components. Run the stated tests and return evidence and remaining findings when complete.
```

## 11. How to reject or narrow a plan

```text
Do not implement this plan. It changes more than the requested feature. Re-plan using the minimum safe change, keep the current authentication/database architecture intact, and explain any remaining trade-offs.
```

## 12. When approval is expected

Expect an approval stop for sensitive changes such as:

- authentication, sessions, MFA, password recovery;
- authorization, RBAC/ABAC, tenant isolation, admin privileges;
- destructive database migration or data deletion;
- secrets, production configuration, infrastructure;
- payment or financial flows;
- new processing of sensitive/personal data;
- security-control weakening or exception;
- major architecture or dependency replacement.

## 13. What evidence looks like

Evidence is the proof that a requirement was actually checked. Examples:

- automated test output;
- negative authorization test;
- browser/user-flow verification;
- CI result;
- security scan finding and remediation result;
- configuration review;
- migration dry run;
- threat model;
- code review;
- release checksum or signed/provenance record where applicable.

Evidence should be reproducible when practical. “The AI says it works” is not sufficient evidence.

## 14. How to use checklists

| Stage | Checklist |
|---|---|
| Project start | `checklists/project-initiation/project-initiation.md` |
| Before development | `checklists/pre-development/pre-development.md` |
| Before commit/review | `checklists/pre-commit/pre-commit.md` |
| Security-sensitive review | `checklists/security-review/security-review.md` |
| Database change | `checklists/database-change/database-change.md` |
| Before release | `checklists/pre-release/pre-release.md` |
| Production release | `checklists/production-release/production-release.md` |

## 15. How to use templates

| Need | Template |
|---|---|
| Project overview/context | `templates/project-context/project-context.md` |
| Security posture | `templates/project-context/project-security-profile.md` |
| Impact analysis | `templates/architecture/change-impact-analysis.md` |
| Architecture/security decision | `templates/architecture/security-decision-record.md` |
| Threat model | `templates/security/threat-model.md` |
| Roles/permissions | `templates/security/role-permission-matrix.md` |
| Important-field validation | `templates/security/field-validation-matrix.md` |
| Data classification | `templates/security/data-classification.md` |
| Encryption decisions | `templates/security/encryption-register.md` |
| Security exception | `templates/security/security-exception.md` |
| Database migration | `templates/database/migration-review.md` |
| Security test evidence | `templates/testing/security-test-evidence.md` |
| Release evidence | `templates/release/release-evidence.md` |

## 16. How to choose a profile

**Baseline** — use for low-risk prototypes or experiments. It still enforces core inspection, access-control, input, injection, secret, database, and regression protections.

**Production** — use for applications with real users, business data, internet exposure, or production obligations. It requires most VCGF controls and stronger release/operational evidence.

**High-Assurance** — use for sensitive institutional, regulated, or high-impact systems. It requires every VCGF v1.0.0 control and stronger evidence/review expectations.

## 17. How to handle an exception

If a required control cannot be implemented:

1. do not silently ignore it;
2. document the Control ID and reason;
3. describe the risk and owner;
4. define compensating control(s);
5. obtain approval;
6. set expiration and review dates;
7. track the exception status.

Use `templates/security/security-exception.md` and `spec/exception-management.md`.

## 18. How to prepare a release

Before release:

- run relevant tests and security tests;
- resolve or document findings;
- confirm database migrations and rollback readiness;
- review secrets/config/environment separation;
- verify monitoring/recovery where required by the profile;
- complete `checklists/pre-release/pre-release.md`;
- retain release evidence;
- if using the VCGF repository itself, run `python scripts/release-quality-gate.py`.

## 19. Example requests and expected VCGF behavior

| Request | What VCGF should add to the conversation |
|---|---|
| “Add a profile photo.” | file validation, storage/access model, authorization, tests |
| “User A can see User B's data.” | authorization/tenant isolation investigation, negative tests, regression evidence |
| “Add national ID.” | minimization, classification, validation, encryption/access/retention review |
| “Add Google login.” | authentication/account-linking/session/recovery impact and approval gate |
| “Install this npm package.” | necessity, provenance, vulnerability/supply-chain review, lockfile impact |
| “Change this table.” | migration impact, integrity, indexes/constraints, rollback and data compatibility |
| “Ship to production.” | release checklist, tests, findings, environment/config, rollback, evidence |

## 20. How to know a task is complete

A VCGF-governed task is not complete only because the preview looks correct. Completion should include, as applicable:

- requested behavior implemented;
- no unintended scope expansion;
- build/type/lint checks relevant to the project;
- positive and negative tests;
- authorization/data-isolation verification;
- database integrity/migration verification;
- security review for sensitive surfaces;
- evidence retained;
- remaining findings or exceptions clearly stated.

## 21. Updating VCGF in a project

When a new VCGF or adapter release appears:

1. read framework and adapter changelogs;
2. check compatibility ranges;
3. compare persistent rule files before replacing them;
4. review profile/control changes;
5. update project context if architecture changed;
6. rerun the platform activation test;
7. keep evidence of significant governance changes when required.

## 22. Common failure modes

**The AI ignores the rules.** Start a fresh session and verify the platform-specific instruction is loaded.

**The AI invents an API or package.** Require source/code inspection and apply the hallucinated API/dependency control; do not install an unverified package just to satisfy generated code.

**The AI wants to disable RLS/authorization/validation to fix an error.** Reject the plan. Security controls must not be weakened as a shortcut.

**The AI changes unrelated code.** Ask it to revert unrelated changes and re-plan using Minimum Safe Change.

**The platform cannot enforce a control natively.** Use an external project/runtime/CI control or document an approved exception. Do not relabel an unsupported capability as compliant.

## 23. Where to go next

- [Choose your platform guide](platform-guides/README.md)
- [VCGF lifecycle](../spec/lifecycle.md)
- [Control model](control-model.md)
- [Evidence model](../spec/evidence-model.md)
- [Conformance](../spec/conformance.md)
- [Control catalog](../spec/control-catalog.yaml)
