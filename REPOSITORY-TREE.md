<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Repository tree

> AUTO-GENERATED — DO NOT EDIT MANUALLY

```text
VCGF/
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── adapter-request.md
│   │   ├── bug-report.md
│   │   ├── config.yml
│   │   ├── control-proposal.md
│   │   └── documentation-issue.md
│   ├── workflows
│   │   ├── release-quality-gate.yml
│   │   ├── validate-adapters.yml
│   │   ├── validate-adaptive.yml
│   │   ├── validate-framework.yml
│   │   ├── validate-links.yml
│   │   ├── validate-runtime.yml
│   │   └── validate-schemas.yml
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── assets
│   └── brand
│       └── brand-guidelines.md
├── capabilities
│   ├── adaptive-engineering.yaml
│   ├── adaptive-ux.yaml
│   ├── admin.yaml
│   ├── api.yaml
│   ├── audit.yaml
│   ├── authorization.yaml
│   ├── backup-restore.yaml
│   ├── database.yaml
│   ├── deletion.yaml
│   ├── development-agent.yaml
│   ├── email.yaml
│   ├── fields.yaml
│   ├── files.yaml
│   ├── identity.yaml
│   ├── incident.yaml
│   ├── password-recovery.yaml
│   ├── payment.yaml
│   ├── privacy.yaml
│   ├── product-ai.yaml
│   ├── public-discovery.yaml
│   ├── script-protection.yaml
│   ├── sessions.yaml
│   ├── step-up.yaml
│   ├── strong-auth.yaml
│   └── ux-accessibility.yaml
├── checklists
│   ├── database-change
│   │   └── database-change.md
│   ├── pre-commit
│   │   └── pre-commit.md
│   ├── pre-development
│   │   └── pre-development.md
│   ├── pre-release
│   │   └── pre-release.md
│   ├── production-release
│   │   └── production-release.md
│   ├── project-initiation
│   │   └── project-initiation.md
│   └── security-review
│       └── security-review.md
├── controls
│   ├── ai-governance
│   │   ├── README.md
│   │   ├── vcgf-ai-001-inspect-before-generate.md
│   │   ├── vcgf-ai-002-no-silent-assumptions.md
│   │   ├── vcgf-ai-003-architecture-drift-prevention.md
│   │   ├── vcgf-ai-004-unauthorized-refactoring-and-feature-change-prevention.md
│   │   ├── vcgf-ai-005-hallucinated-api-and-dependency-prevention.md
│   │   ├── vcgf-ai-006-sensitive-change-guardrails.md
│   │   ├── vcgf-ai-007-security-control-tamper-prevention.md
│   │   ├── vcgf-ai-008-prompt-and-tool-injection-resilience.md
│   │   └── vcgf-ai-009-persistent-context-governance.md
│   ├── api
│   │   ├── README.md
│   │   ├── vcgf-api-001-api-and-server-function-security.md
│   │   ├── vcgf-api-002-business-logic-integrity.md
│   │   ├── vcgf-api-003-rate-limiting-and-abuse-prevention.md
│   │   ├── vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md
│   │   └── vcgf-api-005-third-party-integration-security.md
│   ├── architecture
│   │   ├── README.md
│   │   ├── vcgf-arch-001-tenant-isolation.md
│   │   ├── vcgf-arch-002-trust-boundary-separation.md
│   │   ├── vcgf-arch-003-established-system-as-contract.md
│   │   ├── vcgf-arch-004-separation-of-concerns.md
│   │   └── vcgf-arch-005-threat-modeling.md
│   ├── data-protection
│   │   ├── README.md
│   │   ├── vcgf-data-001-backup-and-export-protection.md
│   │   ├── vcgf-data-002-data-classification-and-retention.md
│   │   ├── vcgf-data-003-field-level-encryption.md
│   │   ├── vcgf-data-004-key-management-and-rotation.md
│   │   ├── vcgf-data-005-searchable-encrypted-data.md
│   │   └── vcgf-data-006-data-in-transit-protection.md
│   ├── database
│   │   ├── README.md
│   │   ├── vcgf-db-001-database-change-governance.md
│   │   ├── vcgf-db-002-database-integrity.md
│   │   ├── vcgf-db-003-database-encryption-implementation.md
│   │   ├── vcgf-db-004-row-level-authorization-testing.md
│   │   ├── vcgf-db-005-sql-query-security.md
│   │   └── vcgf-db-006-transaction-and-concurrency-integrity.md
│   ├── dependencies
│   │   ├── README.md
│   │   ├── vcgf-dep-001-dependency-and-supply-chain-security.md
│   │   ├── vcgf-dep-002-locked-and-reproducible-dependencies.md
│   │   ├── vcgf-dep-003-dependency-vulnerability-review.md
│   │   └── vcgf-dep-004-sbom-and-dependency-provenance.md
│   ├── file-handling
│   │   ├── README.md
│   │   ├── vcgf-file-001-file-upload-and-storage-security.md
│   │   └── vcgf-file-002-private-by-default-file-access.md
│   ├── governance
│   │   ├── README.md
│   │   ├── vcgf-gov-001-change-impact-analysis.md
│   │   ├── vcgf-gov-002-human-approval-gates.md
│   │   ├── vcgf-gov-003-security-exception-management.md
│   │   ├── vcgf-gov-004-evidence-driven-governance.md
│   │   ├── vcgf-gov-005-minimum-safe-change.md
│   │   └── vcgf-gov-006-single-source-of-truth-for-controls.md
│   ├── identity-access
│   │   ├── README.md
│   │   ├── vcgf-iam-001-enumeration-and-brute-force-resistance.md
│   │   ├── vcgf-iam-002-authentication-baseline.md
│   │   ├── vcgf-iam-003-mfa-and-session-security.md
│   │   ├── vcgf-iam-004-password-storage-and-policy.md
│   │   ├── vcgf-iam-005-secure-password-reset-and-recovery.md
│   │   ├── vcgf-iam-006-privileged-access-administration.md
│   │   └── vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md
│   ├── incident-response
│   │   ├── README.md
│   │   ├── vcgf-ir-001-incident-response-minimums.md
│   │   ├── vcgf-ir-002-credential-and-key-compromise-response.md
│   │   └── vcgf-ir-003-personal-data-incident-handling.md
│   ├── logging-auditing
│   │   ├── README.md
│   │   ├── vcgf-audit-001-secure-errors-and-diagnostic-logging.md
│   │   ├── vcgf-audit-002-privileged-and-business-audit-trail.md
│   │   └── vcgf-audit-003-audit-tamper-resistance.md
│   ├── operations
│   │   ├── README.md
│   │   ├── vcgf-ops-001-environment-separation.md
│   │   ├── vcgf-ops-002-production-protection.md
│   │   ├── vcgf-ops-003-backup-and-recovery-validation.md
│   │   ├── vcgf-ops-004-configuration-drift-control.md
│   │   └── vcgf-ops-005-security-monitoring-and-alerting.md
│   ├── privacy
│   │   ├── README.md
│   │   ├── vcgf-priv-001-logging-redaction-and-privacy.md
│   │   ├── vcgf-priv-002-personal-data-protection.md
│   │   ├── vcgf-priv-003-data-minimization-and-purpose-limitation.md
│   │   └── vcgf-priv-004-data-lifecycle-retention-and-secure-deletion.md
│   ├── release
│   │   ├── README.md
│   │   ├── vcgf-rel-001-definition-of-done.md
│   │   ├── vcgf-rel-002-pre-release-security-gate.md
│   │   ├── vcgf-rel-003-rollback-and-recovery-readiness.md
│   │   ├── vcgf-rel-004-post-release-monitoring.md
│   │   └── vcgf-rel-005-release-artifact-integrity-and-provenance.md
│   ├── secrets
│   │   ├── README.md
│   │   ├── vcgf-secr-001-secrets-and-environment-protection.md
│   │   └── vcgf-secr-002-secret-rotation-and-compromise-response.md
│   ├── security
│   │   ├── README.md
│   │   ├── vcgf-sec-001-critical-field-validation.md
│   │   ├── vcgf-sec-002-file-and-url-validation.md
│   │   ├── vcgf-sec-003-injection-defense.md
│   │   ├── vcgf-sec-004-trusted-layer-input-validation.md
│   │   ├── vcgf-sec-005-output-encoding-and-sanitization.md
│   │   └── vcgf-sec-006-secure-defaults-and-fail-closed-behavior.md
│   └── testing
│       ├── README.md
│       ├── vcgf-test-001-authorization-negative-testing.md
│       ├── vcgf-test-002-secure-code-review.md
│       ├── vcgf-test-003-security-regression-review.md
│       ├── vcgf-test-004-security-test-strategy.md
│       ├── vcgf-test-005-validation-and-injection-testing.md
│       └── vcgf-test-006-recovery-flow-testing.md
├── docs
│   ├── platform-guides
│   │   ├── bolt.md
│   │   ├── claude.md
│   │   ├── cursor.md
│   │   ├── generic.md
│   │   ├── lovable.md
│   │   ├── README.md
│   │   ├── replit.md
│   │   └── v0.md
│   ├── project-history
│   │   ├── v1.0.0
│   │   │   ├── architecture-report.md
│   │   │   ├── conflict-report.md
│   │   │   ├── file-inventory.md
│   │   │   ├── final-qa-audit.md
│   │   │   ├── final-release-report.md
│   │   │   ├── migration-map.md
│   │   │   └── traceability.md
│   │   └── v1.1.0
│   │       ├── approval.md
│   │       ├── approved-analysis.md
│   │       ├── change-manifest.json
│   │       ├── continuation-approval.md
│   │       ├── continuation-change-manifest.json
│   │       ├── continuation-test-evidence.json
│   │       ├── CONTINUATION_REPORT_AR.md
│   │       ├── decisions.json
│   │       ├── documentation-approval.json
│   │       ├── documentation-change-manifest.json
│   │       ├── documentation-test-evidence.json
│   │       ├── documentation-update.md
│   │       ├── local-context-benchmark.json
│   │       ├── next-change-plan.json
│   │       ├── open-items.json
│   │       ├── PHASE1_REPORT_AR.md
│   │       ├── progress.json
│   │       ├── reference-stack.json
│   │       ├── scope-register.json
│   │       ├── skill-forward-test.json
│   │       └── test-evidence.json
│   ├── quality
│   │   └── v1.2
│   │       ├── evidence
│   │       │   ├── browser
│   │       │   │   ├── browser-report.json
│   │       │   │   ├── crm-ar-1440.png
│   │       │   │   ├── crm-ar-390.png
│   │       │   │   ├── crm-en-1440.png
│   │       │   │   └── crm-en-390.png
│   │       │   ├── adaptive-benchmark.json
│   │       │   ├── adaptive-benchmark.log
│   │       │   ├── adaptive-browser.log
│   │       │   ├── adaptive-coverage.json
│   │       │   ├── adaptive-coverage.txt
│   │       │   ├── adaptive-coverage.xml
│   │       │   ├── adaptive-junit.xml
│   │       │   ├── adaptive-tests.log
│   │       │   ├── baseline-loader-duplicate.json
│   │       │   ├── baseline-verification.json
│   │       │   ├── candidate-tests-initial.log
│   │       │   ├── combined-plan-example.json
│   │       │   ├── engineering-smoke.json
│   │       │   ├── local-structure.json
│   │       │   ├── preview-baseline-tests.log
│   │       │   ├── preview-browser.log
│   │       │   ├── remote-attempts.json
│   │       │   ├── results-summary.json
│   │       │   ├── tested-code-snapshot.json
│   │       │   └── ux-smoke.json
│   │       ├── baseline-compatibility-v1.2.json
│   │       ├── environment-and-limitations.json
│   │       ├── evaluation-ar.md
│   │       ├── evaluation-en.md
│   │       ├── executive-summary.md
│   │       ├── integration-log.md
│   │       ├── public-release-decision.md
│   │       ├── release-gates.md
│   │       ├── release-notes-v1.2.0.md
│   │       ├── scope-register.json
│   │       └── sources.json
│   ├── references
│   │   ├── owasp-asvs-5-mapping.md
│   │   └── sources-and-standards.md
│   ├── adapter-model.md
│   ├── adoption-guide.md
│   ├── architecture.md
│   ├── contracts-v1.1.md
│   ├── control-model.md
│   ├── github-desktop-update.ar.md
│   ├── implementation-guide.md
│   ├── migration-guide.md
│   ├── platform-compatibility.md
│   ├── principles.md
│   ├── quick-start.ar.md
│   ├── runtime-guide.md
│   ├── terminology.md
│   ├── user-guide.md
│   └── versioning-model.md
├── examples
│   ├── adaptive
│   │   ├── example-project
│   │   │   ├── brief.md
│   │   │   ├── discovery.json
│   │   │   └── fingerprint.json
│   │   ├── fingerprint-enterprise.json
│   │   ├── fingerprint-laravel.json
│   │   ├── rtl-ltr-crm.html
│   │   ├── ux-crm.json
│   │   ├── ux-editorial.json
│   │   └── ux-service.json
│   ├── crm
│   │   └── README.md
│   ├── ecommerce
│   │   └── README.md
│   ├── erp
│   │   └── README.md
│   ├── generic-web-app
│   │   └── README.md
│   ├── integrations
│   │   ├── backup
│   │   │   ├── operations.py
│   │   │   ├── sql_engines.py
│   │   │   └── unified.py
│   │   ├── email
│   │   │   ├── delivery.py
│   │   │   └── queue.py
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── runtime
│   │   ├── admin
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── api
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── authorization
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── deletion
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── dependency
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── emergency
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── login
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── migration
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── payment
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── pii
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   ├── reset
│   │   │   ├── config.json
│   │   │   ├── context.json
│   │   │   └── task.json
│   │   └── upload
│   │       ├── config.json
│   │       ├── context.json
│   │       └── task.json
│   └── saas
│       └── README.md
├── legal
│   ├── attribution.md
│   ├── third-party-notices.md
│   └── trademark-policy.md
├── packs
│   ├── engineering
│   │   ├── adaptive.md
│   │   ├── catalog.yaml
│   │   └── release-policy.json
│   ├── requirements
│   │   ├── section-14.md
│   │   ├── section-15.md
│   │   ├── section-16.md
│   │   ├── section-17.md
│   │   ├── section-18.md
│   │   ├── section-19.md
│   │   ├── section-20.md
│   │   ├── section-21.md
│   │   ├── section-22.md
│   │   ├── section-23.md
│   │   ├── section-24.md
│   │   ├── section-25.md
│   │   ├── section-26.md
│   │   ├── section-27.md
│   │   ├── section-28.md
│   │   ├── section-29.md
│   │   ├── section-30.md
│   │   ├── section-31.md
│   │   ├── section-32.md
│   │   ├── section-33.md
│   │   ├── section-34.md
│   │   ├── section-35.md
│   │   ├── section-36.md
│   │   ├── section-37.md
│   │   ├── section-38.md
│   │   └── section-39.md
│   ├── ux
│   │   ├── adaptive.md
│   │   ├── catalog.yaml
│   │   ├── local-fonts.md
│   │   └── rtl-ltr.md
│   └── index.yaml
├── platforms
│   ├── _adapter-template
│   │   ├── examples
│   │   │   └── README.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── README.md
│   │   ├── rules
│   │   │   └── README.md
│   │   ├── templates
│   │   │   └── README.md
│   │   ├── tests
│   │   │   └── README.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   └── README.md
│   ├── bolt
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── project-knowledge.md
│   │   │   └── runtime.generated.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── chatgpt
│   │   ├── examples
│   │   │   └── README.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── README.md
│   │   ├── rules
│   │   │   ├── README.md
│   │   │   └── runtime.generated.md
│   │   ├── skills
│   │   │   └── vcgf
│   │   │       └── SKILL.md
│   │   ├── templates
│   │   │   └── README.md
│   │   ├── tests
│   │   │   ├── README.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── claude
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── CLAUDE.md
│   │   │   └── runtime.generated.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── cursor
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── AGENTS.md
│   │   │   ├── runtime.generated.md
│   │   │   └── vcgf.mdc
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── generic
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── portable-project-rules.md
│   │   │   └── runtime.generated.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── lovable
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── AGENTS.md
│   │   │   ├── project-knowledge.md
│   │   │   ├── runtime.generated.md
│   │   │   └── workspace-knowledge.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   ├── replit
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── replit.md
│   │   │   └── runtime.generated.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   ├── adapter-verification.md
│   │   │   └── runtime-canary.md
│   │   ├── verification
│   │   │   ├── sources.yaml
│   │   │   └── verification-report.md
│   │   ├── ADAPTER.md
│   │   ├── adapter.yaml
│   │   ├── CAPABILITIES.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTROL-MAPPING.md
│   │   ├── control-mapping.yaml
│   │   ├── INSTALLATION.md
│   │   ├── LIMITATIONS.md
│   │   ├── README.md
│   │   ├── runtime-capabilities.yaml
│   │   └── RUNTIME-INSTALLATION.md
│   └── v0
│       ├── examples
│       │   └── example-adoption.md
│       ├── mappings
│       │   └── README.md
│       ├── prompts
│       │   └── pre-change-impact-review.md
│       ├── rules
│       │   ├── custom-instructions.md
│       │   └── runtime.generated.md
│       ├── templates
│       │   └── project-context.md
│       ├── tests
│       │   ├── adapter-verification.md
│       │   └── runtime-canary.md
│       ├── verification
│       │   ├── sources.yaml
│       │   └── verification-report.md
│       ├── ADAPTER.md
│       ├── adapter.yaml
│       ├── CAPABILITIES.md
│       ├── CHANGELOG.md
│       ├── CONTROL-MAPPING.md
│       ├── control-mapping.yaml
│       ├── INSTALLATION.md
│       ├── LIMITATIONS.md
│       ├── README.md
│       ├── runtime-capabilities.yaml
│       └── RUNTIME-INSTALLATION.md
├── playbooks
│   ├── existing-project-hardening-plan.md
│   ├── key-rotation-playbook.md
│   ├── new-project-security-bootstrap.md
│   └── password-reset-test-cases.md
├── profiles
│   ├── baseline
│   │   ├── profile.yaml
│   │   └── README.md
│   ├── high-assurance
│   │   ├── profile.yaml
│   │   └── README.md
│   └── production
│       ├── profile.yaml
│       └── README.md
├── references
│   └── source-registry.yaml
├── runtime
│   ├── adaptive
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── common.py
│   │   ├── coordinator.py
│   │   ├── engineering.py
│   │   ├── release.py
│   │   ├── schools.py
│   │   └── ux.py
│   ├── __init__.py
│   ├── approval.py
│   ├── bootstrap.md
│   ├── context-policy.yaml
│   ├── context.py
│   ├── contracts.py
│   ├── evidence.py
│   ├── evidence_pack.py
│   ├── loader.py
│   ├── pack-map.yaml
│   ├── preferences-policy.yaml
│   ├── registry.py
│   ├── resolver.py
│   ├── router.py
│   ├── routing-policy.yaml
│   └── scope_guard.py
├── schemas
│   ├── v1.1.0
│   │   ├── adapter-capabilities.schema.json
│   │   ├── approval.schema.json
│   │   ├── capability.schema.json
│   │   ├── common.schema.json
│   │   ├── context.schema.json
│   │   ├── evidence.schema.json
│   │   ├── preferences.schema.json
│   │   └── route-result.schema.json
│   ├── v1.2.0
│   │   ├── architecture-decision.schema.json
│   │   ├── project-fingerprint.schema.json
│   │   ├── release-evidence.schema.json
│   │   ├── ux-decision.schema.json
│   │   └── ux-discovery.schema.json
│   ├── adapter.schema.json
│   ├── conformance.schema.json
│   ├── control.schema.json
│   └── profile.schema.json
├── scripts
│   ├── benchmark-adaptive.py
│   ├── check-adapter-updates.py
│   ├── generate-adapter-rules.py
│   ├── generate-control-catalog.py
│   ├── generate-file-manifest.py
│   ├── generate-repository-tree.py
│   ├── generate-runtime-registry.py
│   ├── release-quality-gate.py
│   ├── test-adaptive-browser.py
│   ├── validate-adapters.py
│   ├── validate-attribution.py
│   ├── validate-contracts.py
│   ├── validate-controls.py
│   ├── validate-cross-references.py
│   ├── validate-documentation.py
│   ├── validate-internal-links.py
│   ├── validate-license.py
│   ├── validate-placeholders.py
│   ├── validate-profiles.py
│   ├── validate-repository-structure.py
│   ├── validate-runtime.py
│   ├── validate-schemas.py
│   ├── validate-vendor-neutral-core.py
│   ├── validate-version.py
│   ├── validate-yaml.py
│   ├── vcgf.py
│   └── vcgf_lib.py
├── spec
│   ├── conformance.md
│   ├── control-catalog.yaml
│   ├── evidence-model.md
│   ├── exception-management.md
│   ├── lifecycle.md
│   ├── normative-language.md
│   ├── risk-model.md
│   ├── runtime-registry.json
│   └── VCGF-CORE.md
├── templates
│   ├── adapters
│   │   └── runtime-rules.template.md
│   ├── architecture
│   │   ├── change-impact-analysis.md
│   │   └── security-decision-record.md
│   ├── database
│   │   └── migration-review.md
│   ├── project-context
│   │   ├── prompts
│   │   │   ├── auth-password-recovery-audit-prompt.md
│   │   │   ├── change-impact-analysis-prompt.md
│   │   │   ├── dependency-supply-chain-audit-prompt.md
│   │   │   ├── initial-read-only-audit-prompt.md
│   │   │   ├── pii-encryption-audit-prompt.md
│   │   │   ├── pre-release-security-review-prompt.md
│   │   │   ├── safe-bugfix-prompt.md
│   │   │   ├── safe-feature-prompt.md
│   │   │   └── validation-injection-audit-prompt.md
│   │   ├── project-context.md
│   │   ├── project-security-profile.md
│   │   └── regulatory-overlay.md
│   ├── release
│   │   └── release-evidence.md
│   ├── security
│   │   ├── data-classification.md
│   │   ├── encryption-register.md
│   │   ├── field-validation-matrix.md
│   │   ├── role-permission-matrix.md
│   │   ├── security-exception.md
│   │   └── threat-model.md
│   └── testing
│       └── security-test-evidence.md
├── tests
│   ├── adaptive
│   │   ├── conftest.py
│   │   ├── test_engines.py
│   │   ├── test_inputs.py
│   │   ├── test_integration.py
│   │   ├── test_legacy_loader.py
│   │   └── test_release.py
│   ├── benchmarks
│   │   └── measure_context.py
│   ├── contracts
│   │   └── test_phase1.py
│   ├── fixtures
│   │   ├── v1.0
│   │   │   ├── schemas
│   │   │   │   ├── adapter.schema.json
│   │   │   │   ├── conformance.schema.json
│   │   │   │   ├── control.schema.json
│   │   │   │   └── profile.schema.json
│   │   │   ├── baseline-hashes.json
│   │   │   └── records.json
│   │   └── v1.1
│   │       ├── adapter-capabilities.json
│   │       ├── approval.json
│   │       ├── capability.json
│   │       ├── context.json
│   │       ├── evidence.json
│   │       ├── preferences.json
│   │       └── route-result.json
│   └── scenarios
│       ├── test_adapters.py
│       ├── test_gates.py
│       ├── test_integrations.py
│       └── test_runtime.py
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── COPYRIGHT.md
├── FILE-MANIFEST.md
├── GOVERNANCE.md
├── LICENSE
├── NOTICE.md
├── README.ar.md
├── README.md
├── REPOSITORY-TREE.md
├── requirements-dev.txt
├── requirements-quality.txt
├── ROADMAP.md
├── SECURITY.md
├── VCGF-MANIFEST.yaml
└── VERSION
```
