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
│   ├── release-keys
│   │   ├── hamada-sami.asc
│   │   └── README.md
│   ├── workflows
│   │   ├── release-quality-gate.yml
│   │   ├── release.yml
│   │   ├── supply-chain.yml
│   │   ├── tests.yml
│   │   ├── validate-adapters.yml
│   │   ├── validate-adaptive.yml
│   │   ├── validate-framework.yml
│   │   ├── validate-links.yml
│   │   ├── validate-runtime.yml
│   │   └── validate-schemas.yml
│   ├── CODEOWNERS
│   ├── dependabot.yml
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
│   ├── exception.yaml
│   ├── fields.yaml
│   ├── files.yaml
│   ├── governance-change.yaml
│   ├── identity.yaml
│   ├── incident.yaml
│   ├── operations.yaml
│   ├── password-recovery.yaml
│   ├── payment.yaml
│   ├── privacy.yaml
│   ├── product-ai.yaml
│   ├── public-discovery.yaml
│   ├── release.yaml
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
│   ├── testing
│   │   ├── README.md
│   │   ├── vcgf-test-001-authorization-negative-testing.md
│   │   ├── vcgf-test-002-secure-code-review.md
│   │   ├── vcgf-test-003-security-regression-review.md
│   │   ├── vcgf-test-004-security-test-strategy.md
│   │   ├── vcgf-test-005-validation-and-injection-testing.md
│   │   └── vcgf-test-006-recovery-flow-testing.md
│   └── user-experience
│       ├── README.md
│       ├── vcgf-ux-001-accessibility-conformance.md
│       ├── vcgf-ux-002-localization-and-bidirectional-text.md
│       ├── vcgf-ux-003-interaction-state-integrity.md
│       └── vcgf-ux-004-responsive-strategy-and-density.md
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
│   │   ├── v1.1.0
│   │   │   ├── approval.md
│   │   │   ├── approved-analysis.md
│   │   │   ├── change-manifest.json
│   │   │   ├── continuation-approval.md
│   │   │   ├── continuation-change-manifest.json
│   │   │   ├── continuation-test-evidence.json
│   │   │   ├── CONTINUATION_REPORT_AR.md
│   │   │   ├── decisions.json
│   │   │   ├── documentation-approval.json
│   │   │   ├── documentation-change-manifest.json
│   │   │   ├── documentation-test-evidence.json
│   │   │   ├── documentation-update.md
│   │   │   ├── local-context-benchmark.json
│   │   │   ├── next-change-plan.json
│   │   │   ├── open-items.json
│   │   │   ├── PHASE1_REPORT_AR.md
│   │   │   ├── progress.json
│   │   │   ├── reference-stack.json
│   │   │   ├── scope-register.json
│   │   │   ├── skill-forward-test.json
│   │   │   └── test-evidence.json
│   │   ├── v1.3.0-smart-ui-integration.md
│   │   ├── v1.4.0-phase1-architecture-governance.md
│   │   ├── v1.4.0-phase2-token-efficiency.md
│   │   └── v1.4.0-phase3-verification-enforcement.md
│   ├── quality
│   │   ├── v1.2
│   │   │   ├── evidence
│   │   │   │   ├── browser
│   │   │   │   │   ├── browser-report.json
│   │   │   │   │   ├── crm-ar-1440.png
│   │   │   │   │   ├── crm-ar-390.png
│   │   │   │   │   ├── crm-en-1440.png
│   │   │   │   │   └── crm-en-390.png
│   │   │   │   ├── adaptive-benchmark.json
│   │   │   │   ├── adaptive-benchmark.log
│   │   │   │   ├── adaptive-browser.log
│   │   │   │   ├── adaptive-coverage.json
│   │   │   │   ├── adaptive-coverage.txt
│   │   │   │   ├── adaptive-coverage.xml
│   │   │   │   ├── adaptive-junit.xml
│   │   │   │   ├── adaptive-tests.log
│   │   │   │   ├── baseline-loader-duplicate.json
│   │   │   │   ├── baseline-verification.json
│   │   │   │   ├── candidate-tests-initial.log
│   │   │   │   ├── combined-plan-example.json
│   │   │   │   ├── engineering-smoke.json
│   │   │   │   ├── local-structure.json
│   │   │   │   ├── preview-baseline-tests.log
│   │   │   │   ├── preview-browser.log
│   │   │   │   ├── remote-attempts.json
│   │   │   │   ├── results-summary.json
│   │   │   │   ├── tested-code-snapshot.json
│   │   │   │   └── ux-smoke.json
│   │   │   ├── baseline-compatibility-v1.2.json
│   │   │   ├── environment-and-limitations.json
│   │   │   ├── evaluation-ar.md
│   │   │   ├── evaluation-en.md
│   │   │   ├── executive-summary.md
│   │   │   ├── HISTORICAL.md
│   │   │   ├── integration-log.md
│   │   │   ├── public-release-decision.md
│   │   │   ├── release-gates.md
│   │   │   ├── release-notes-v1.2.0.md
│   │   │   ├── scope-register.json
│   │   │   └── sources.json
│   │   ├── v1.3
│   │   │   ├── baseline-compatibility-v1.3.1.json
│   │   │   ├── baseline-compatibility-v1.3.json
│   │   │   ├── public-release-decision.md
│   │   │   ├── release-checklist-v1.3.1.md
│   │   │   ├── release-checklist.md
│   │   │   ├── release-notes-v1.3.0.md
│   │   │   ├── release-notes-v1.3.1.md
│   │   │   └── release-validation-local.json
│   │   └── v1.4
│   │       ├── baseline-compatibility-v1.4.json
│   │       ├── PULL-REQUEST-v1.4.0.md
│   │       ├── release-checklist-v1.4.0.md
│   │       ├── release-notes-v1.4.0.ar.md
│   │       ├── release-notes-v1.4.0.md
│   │       ├── release-validation-local.json
│   │       └── self-acceptance-results.json
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
│   │   ├── smart-ui
│   │   │   ├── adapters
│   │   │   │   ├── generic.md
│   │   │   │   ├── laravel-livewire.md
│   │   │   │   ├── react-next-lovable.md
│   │   │   │   ├── vanilla-legacy.md
│   │   │   │   └── vue.md
│   │   │   ├── catalog
│   │   │   │   ├── compatibility-matrix.json
│   │   │   │   ├── component-contracts.json
│   │   │   │   ├── interaction-compatibility-matrix.json
│   │   │   │   ├── interaction-contracts.json
│   │   │   │   ├── interaction-rules.json
│   │   │   │   ├── journey-compatibility-matrix.json
│   │   │   │   ├── journey-contracts.json
│   │   │   │   ├── journey-rules.json
│   │   │   │   ├── screen-composition-compatibility-matrix.json
│   │   │   │   ├── screen-composition-contracts.json
│   │   │   │   ├── screen-composition-rules.json
│   │   │   │   └── selection-rules.json
│   │   │   ├── config
│   │   │   │   ├── central-settings.example.json
│   │   │   │   ├── interaction-policy.example.json
│   │   │   │   └── screen-orchestration-policy.example.json
│   │   │   ├── examples
│   │   │   │   ├── alternative-presentation-screen.json
│   │   │   │   ├── alternative-presentation-screen.plan.json
│   │   │   │   ├── approval-workspace-screen.json
│   │   │   │   ├── approval-workspace-screen.plan.json
│   │   │   │   ├── binary-choice-screen.json
│   │   │   │   ├── binary-choice-screen.plan.json
│   │   │   │   ├── bulk-job-screen.json
│   │   │   │   ├── bulk-job-screen.plan.json
│   │   │   │   ├── document-sign-archive-journey.json
│   │   │   │   ├── document-sign-archive-journey.plan.json
│   │   │   │   ├── enterprise-operations-screen.json
│   │   │   │   ├── enterprise-operations-screen.plan.json
│   │   │   │   ├── executive-dashboard-screen.json
│   │   │   │   ├── executive-dashboard-screen.plan.json
│   │   │   │   ├── expired-session-draft-screen.json
│   │   │   │   ├── expired-session-draft-screen.plan.json
│   │   │   │   ├── master-detail-field-screen.json
│   │   │   │   ├── master-detail-field-screen.plan.json
│   │   │   │   ├── no-ui-service.json
│   │   │   │   ├── no-ui-service.plan.json
│   │   │   │   ├── offline-edit-screen.json
│   │   │   │   ├── offline-edit-screen.plan.json
│   │   │   │   ├── public-self-service-journey.json
│   │   │   │   ├── public-self-service-journey.plan.json
│   │   │   │   ├── record-collaboration-screen.json
│   │   │   │   ├── record-collaboration-screen.plan.json
│   │   │   │   ├── reversible-action-screen.json
│   │   │   │   ├── reversible-action-screen.plan.json
│   │   │   │   ├── safe-delete-screen.json
│   │   │   │   ├── safe-delete-screen.plan.json
│   │   │   │   ├── scope-switch-journey.json
│   │   │   │   ├── scope-switch-journey.plan.json
│   │   │   │   ├── secure-auth-screen.json
│   │   │   │   ├── secure-auth-screen.plan.json
│   │   │   │   ├── simple-birthdate-screen.json
│   │   │   │   ├── simple-birthdate-screen.plan.json
│   │   │   │   ├── simple-view-screen.json
│   │   │   │   └── simple-view-screen.plan.json
│   │   │   ├── external-standards
│   │   │   │   ├── CALENDAR-GOVERNANCE-ADDENDUM.md
│   │   │   │   └── ENTERPRISE-SEARCHABLE-SELECT-COMBOBOX.md
│   │   │   ├── governance
│   │   │   │   ├── ACCESSIBILITY-RTL.md
│   │   │   │   ├── ACTION-HIERARCHY-POLICY.md
│   │   │   │   ├── ADAPTIVE-UX-ORCHESTRATION.md
│   │   │   │   ├── CENTRAL-SETTINGS.md
│   │   │   │   ├── CHANGE-CONTROL.md
│   │   │   │   ├── COMPONENT-COMPATIBILITY.md
│   │   │   │   ├── COMPONENT-CONTRACT.md
│   │   │   │   ├── COMPONENT-LIFECYCLE.md
│   │   │   │   ├── CONTEXT-CONTINUITY-POLICY.md
│   │   │   │   ├── DECISION-EXPLAINABILITY.md
│   │   │   │   ├── EVIDENCE-CONFORMANCE.md
│   │   │   │   ├── EXPERIENCE-ORCHESTRATION.md
│   │   │   │   ├── EXTERNAL-STANDARDS-BINDINGS.md
│   │   │   │   ├── FINAL-ADOPTION-GATE.md
│   │   │   │   ├── GOLDEN-RULES.md
│   │   │   │   ├── INFORMATION-ARCHITECTURE-POLICY.md
│   │   │   │   ├── INTERACTION-COMPATIBILITY.md
│   │   │   │   ├── INTERACTION-CONTRACT.md
│   │   │   │   ├── INTERACTION-LIFECYCLE.md
│   │   │   │   ├── JOURNEY-CONTRACT.md
│   │   │   │   ├── MASTER-POLICY.md
│   │   │   │   ├── NAVIGATION-DEEP-LINK-POLICY.md
│   │   │   │   ├── PACKAGE-SELECTION.md
│   │   │   │   ├── PERFORMANCE-RESILIENCE.md
│   │   │   │   ├── QUALITY-GATES.md
│   │   │   │   ├── RESPONSIVE-DENSITY-POLICY.md
│   │   │   │   ├── RETURN-TO-ORIGIN-POLICY.md
│   │   │   │   ├── REUSE-FIRST-POLICY.md
│   │   │   │   ├── SCREEN-COMPOSITION-CONTRACT.md
│   │   │   │   ├── SCREEN-STATE-MODEL.md
│   │   │   │   ├── SECURITY-PRIVACY.md
│   │   │   │   ├── SMART-INTERACTION-GOLDEN-RULES.md
│   │   │   │   ├── SMART-INTERACTION-PATTERN-SELECTION.md
│   │   │   │   ├── SMART-JOURNEY-SELECTION.md
│   │   │   │   ├── SMART-SCREEN-COMPOSITION-SELECTION.md
│   │   │   │   └── SMART-UI-COMPONENT-SELECTION.md
│   │   │   ├── integration
│   │   │   │   ├── AGENTS.snippet.md
│   │   │   │   ├── FINAL-INTEGRATION-PROMPT.md
│   │   │   │   ├── IMPLEMENTATION-ROADMAP.md
│   │   │   │   ├── INTEGRATION-PLAN.md
│   │   │   │   ├── MASTER-IMPLEMENTATION-PROMPT.md
│   │   │   │   ├── MIGRATION-v0.5-to-v1.0.md
│   │   │   │   └── VCGF-1.3.0-FINAL-INTEGRATION-MANIFEST.md
│   │   │   ├── interactions
│   │   │   │   ├── VCGF-UI-INT-001-SmartCreateFlow.md
│   │   │   │   ├── VCGF-UI-INT-002-SmartEditFlow.md
│   │   │   │   ├── VCGF-UI-INT-003-SmartViewRefreshFlow.md
│   │   │   │   ├── VCGF-UI-INT-004-SafeDeleteFlow.md
│   │   │   │   ├── VCGF-UI-INT-005-UnsavedChangesProtection.md
│   │   │   │   ├── VCGF-UI-INT-006-SaveSubmitStateMachine.md
│   │   │   │   ├── VCGF-UI-INT-007-ConfirmationDecisionPattern.md
│   │   │   │   ├── VCGF-UI-INT-008-EmptyStateRecovery.md
│   │   │   │   ├── VCGF-UI-INT-009-LoadingProgressiveDisclosure.md
│   │   │   │   ├── VCGF-UI-INT-010-ErrorRetryRecovery.md
│   │   │   │   ├── VCGF-UI-INT-011-OptimisticUpdateRollback.md
│   │   │   │   ├── VCGF-UI-INT-012-ConcurrencyConflictResolution.md
│   │   │   │   ├── VCGF-UI-INT-013-BulkActionExecution.md
│   │   │   │   ├── VCGF-UI-INT-014-LongRunningOperationProgress.md
│   │   │   │   ├── VCGF-UI-INT-015-OfflineReconnectSynchronization.md
│   │   │   │   ├── VCGF-UI-INT-016-SessionExpiryReauthentication.md
│   │   │   │   ├── VCGF-UI-INT-017-PermissionChangeReaction.md
│   │   │   │   ├── VCGF-UI-INT-018-SensitiveActionStepUp.md
│   │   │   │   ├── VCGF-UI-INT-019-IdempotentSubmissionProtection.md
│   │   │   │   ├── VCGF-UI-INT-020-UndoableActionPattern.md
│   │   │   │   ├── VCGF-UI-INT-021-SearchFilterResultState.md
│   │   │   │   ├── VCGF-UI-INT-022-MultiStepTransactionOrchestration.md
│   │   │   │   ├── VCGF-UI-INT-023-DraftRecoveryResume.md
│   │   │   │   └── VCGF-UI-INT-024-NavigationContextPreservation.md
│   │   │   ├── journeys
│   │   │   │   ├── VCGF-UI-JRN-001-DiscoveryToDetailReturn.md
│   │   │   │   ├── VCGF-UI-JRN-002-CreateToDetailContinuation.md
│   │   │   │   ├── VCGF-UI-JRN-003-DraftReviewSubmit.md
│   │   │   │   ├── VCGF-UI-JRN-004-ReviewApproveComplete.md
│   │   │   │   ├── VCGF-UI-JRN-005-RejectReviseResubmit.md
│   │   │   │   ├── VCGF-UI-JRN-006-TaskQueueProcessNext.md
│   │   │   │   ├── VCGF-UI-JRN-007-BulkSelectActReview.md
│   │   │   │   ├── VCGF-UI-JRN-008-ImportValidateMapCommit.md
│   │   │   │   ├── VCGF-UI-JRN-009-DocumentReviewSignArchive.md
│   │   │   │   ├── VCGF-UI-JRN-010-ScheduleCreateRescheduleCancel.md
│   │   │   │   ├── VCGF-UI-JRN-011-PublicSubmitTrackRespond.md
│   │   │   │   ├── VCGF-UI-JRN-012-AuthenticateRecoverReturn.md
│   │   │   │   ├── VCGF-UI-JRN-013-DeepLinkAuthorizeReturnToOrigin.md
│   │   │   │   ├── VCGF-UI-JRN-014-CompareDecideAct.md
│   │   │   │   ├── VCGF-UI-JRN-015-ScopeSwitchResume.md
│   │   │   │   ├── VCGF-UI-JRN-016-OfflineCaptureSyncResolve.md
│   │   │   │   ├── VCGF-UI-JRN-017-LongRunningLeaveReturn.md
│   │   │   │   └── VCGF-UI-JRN-018-ConfigurePreviewPublish.md
│   │   │   ├── references
│   │   │   │   ├── package-register.json
│   │   │   │   ├── REPOSITORY-BASELINE.md
│   │   │   │   ├── source-register.json
│   │   │   │   └── SOURCES.md
│   │   │   ├── reports
│   │   │   │   ├── CONTENT-REVIEW.md
│   │   │   │   ├── DOCUMENTATION-VALIDATION.json
│   │   │   │   ├── DOCUMENTATION-VALIDATION.md
│   │   │   │   ├── FINAL-QUALITY-SUMMARY.md
│   │   │   │   ├── SMART-SELECTION-VALIDATION.md
│   │   │   │   └── SMART-SELECTION-VALIDATION.txt
│   │   │   ├── schemas
│   │   │   │   ├── catalog.schema.json
│   │   │   │   ├── central-settings.schema.json
│   │   │   │   ├── compatibility-matrix.schema.json
│   │   │   │   ├── component-contract.schema.json
│   │   │   │   ├── component-selection-plan.schema.json
│   │   │   │   ├── evidence-record.schema.json
│   │   │   │   ├── interaction-catalog.schema.json
│   │   │   │   ├── interaction-compatibility-matrix.schema.json
│   │   │   │   ├── interaction-contract.schema.json
│   │   │   │   ├── interaction-policy.schema.json
│   │   │   │   ├── journey-catalog.schema.json
│   │   │   │   ├── journey-compatibility-matrix.schema.json
│   │   │   │   ├── journey-contract.schema.json
│   │   │   │   ├── project-assessment.schema.json
│   │   │   │   ├── screen-composition-catalog.schema.json
│   │   │   │   ├── screen-composition-compatibility-matrix.schema.json
│   │   │   │   ├── screen-composition-contract.schema.json
│   │   │   │   ├── screen-context.schema.json
│   │   │   │   └── screen-orchestration-policy.schema.json
│   │   │   ├── screen-compositions
│   │   │   │   ├── VCGF-UI-SCR-001-DashboardOverview.md
│   │   │   │   ├── VCGF-UI-SCR-002-OperationalCollection.md
│   │   │   │   ├── VCGF-UI-SCR-003-RecordWorkspace.md
│   │   │   │   ├── VCGF-UI-SCR-004-FormTransaction.md
│   │   │   │   ├── VCGF-UI-SCR-005-GuidedWizard.md
│   │   │   │   ├── VCGF-UI-SCR-006-SearchDiscovery.md
│   │   │   │   ├── VCGF-UI-SCR-007-WorkQueueInbox.md
│   │   │   │   ├── VCGF-UI-SCR-008-ReviewApproval.md
│   │   │   │   ├── VCGF-UI-SCR-009-DocumentWorkspace.md
│   │   │   │   ├── VCGF-UI-SCR-010-SchedulingWorkspace.md
│   │   │   │   ├── VCGF-UI-SCR-011-AnalyticsReporting.md
│   │   │   │   ├── VCGF-UI-SCR-012-SettingsAdministration.md
│   │   │   │   ├── VCGF-UI-SCR-013-AuthenticationAccess.md
│   │   │   │   ├── VCGF-UI-SCR-014-CollaborationWorkspace.md
│   │   │   │   ├── VCGF-UI-SCR-015-MasterDetailExplorer.md
│   │   │   │   ├── VCGF-UI-SCR-016-ComparisonDecision.md
│   │   │   │   ├── VCGF-UI-SCR-017-ImportExportOperation.md
│   │   │   │   ├── VCGF-UI-SCR-018-PublicSelfService.md
│   │   │   │   ├── VCGF-UI-SCR-019-MobileFocusedTask.md
│   │   │   │   └── VCGF-UI-SCR-020-LargeScreenOperations.md
│   │   │   ├── scripts
│   │   │   │   ├── build_manifest.py
│   │   │   │   ├── report-labels.json
│   │   │   │   ├── select_components.py
│   │   │   │   ├── select_smart_ui.py
│   │   │   │   ├── validate_final.py
│   │   │   │   ├── validate_package.py
│   │   │   │   └── validate_selection_layer.py
│   │   │   ├── source-snapshots
│   │   │   │   ├── CALENDAR-GOVERNANCE-ADDENDUM.source.txt
│   │   │   │   └── ENTERPRISE-SEARCHABLE-SELECT.source.txt
│   │   │   ├── standards
│   │   │   │   ├── VCGF-UI-COMP-001-DesignSystemPrimitives.md
│   │   │   │   ├── VCGF-UI-COMP-002-SmartDataGrid.md
│   │   │   │   ├── VCGF-UI-COMP-003-SmartFormFields.md
│   │   │   │   ├── VCGF-UI-COMP-004-AdvancedFilterBuilder.md
│   │   │   │   ├── VCGF-UI-COMP-005-SmartFileUploader.md
│   │   │   │   ├── VCGF-UI-COMP-006-DocumentPreviewer.md
│   │   │   │   ├── VCGF-UI-COMP-007-AdaptiveOverlay.md
│   │   │   │   ├── VCGF-UI-COMP-008-UnifiedFeedbackSystem.md
│   │   │   │   ├── VCGF-UI-COMP-009-AdaptiveNavigation.md
│   │   │   │   ├── VCGF-UI-COMP-010-HierarchicalTreePicker.md
│   │   │   │   ├── VCGF-UI-COMP-011-SmartFormWizard.md
│   │   │   │   ├── VCGF-UI-COMP-012-PermissionAwareActions.md
│   │   │   │   ├── VCGF-UI-COMP-013-RichTextEditor.md
│   │   │   │   ├── VCGF-UI-COMP-014-GlobalSearchCommandPalette.md
│   │   │   │   ├── VCGF-UI-COMP-015-WorkflowApprovalTimeline.md
│   │   │   │   ├── VCGF-UI-COMP-016-AuditHistoryViewer.md
│   │   │   │   ├── VCGF-UI-COMP-017-SmartNumericInput.md
│   │   │   │   ├── VCGF-UI-COMP-018-SmartContactFields.md
│   │   │   │   ├── VCGF-UI-COMP-019-DataImportExportWizard.md
│   │   │   │   ├── VCGF-UI-COMP-020-SmartDashboardWidgets.md
│   │   │   │   ├── VCGF-UI-COMP-021-SmartKanbanBoard.md
│   │   │   │   ├── VCGF-UI-COMP-022-UnifiedScheduler.md
│   │   │   │   ├── VCGF-UI-COMP-023-DraftAutosaveManager.md
│   │   │   │   ├── VCGF-UI-COMP-024-AdaptiveContentPanels.md
│   │   │   │   ├── VCGF-UI-COMP-025-SmartRecordDetailView.md
│   │   │   │   ├── VCGF-UI-COMP-026-SmartCollectionList.md
│   │   │   │   ├── VCGF-UI-COMP-027-SmartActivityTimeline.md
│   │   │   │   ├── VCGF-UI-COMP-028-SmartCollaborationThread.md
│   │   │   │   ├── VCGF-UI-COMP-029-SmartNotificationCenter.md
│   │   │   │   ├── VCGF-UI-COMP-030-SmartSavedViewsManager.md
│   │   │   │   ├── VCGF-UI-COMP-031-SmartContextualActionBar.md
│   │   │   │   ├── VCGF-UI-COMP-032-SmartRelationshipPicker.md
│   │   │   │   ├── VCGF-UI-COMP-033-SmartAddressLocationFields.md
│   │   │   │   ├── VCGF-UI-COMP-034-SmartTaxonomyTagPicker.md
│   │   │   │   ├── VCGF-UI-COMP-035-SmartRulesExpressionBuilder.md
│   │   │   │   └── VCGF-UI-COMP-036-SmartSecureAuthenticationFlow.md
│   │   │   ├── templates
│   │   │   │   ├── ADR.md
│   │   │   │   ├── COMPONENT-IMPLEMENTATION.md
│   │   │   │   ├── component-selection-plan.example.json
│   │   │   │   ├── evidence-record.example.json
│   │   │   │   ├── EXCEPTION.md
│   │   │   │   ├── project-assessment.example.json
│   │   │   │   └── screen-context.example.json
│   │   │   ├── tests
│   │   │   │   ├── ACCEPTANCE-MATRIX.md
│   │   │   │   ├── interaction-traceability.json
│   │   │   │   ├── journey-traceability.json
│   │   │   │   ├── screen-composition-traceability.json
│   │   │   │   ├── SMART-SELECTION-TESTS.md
│   │   │   │   ├── TEST-PLAN.md
│   │   │   │   └── traceability.json
│   │   │   ├── CATALOG.html
│   │   │   ├── catalog.json
│   │   │   ├── CHANGELOG.md
│   │   │   ├── INDEX.md
│   │   │   ├── interaction-catalog.json
│   │   │   ├── journey-catalog.json
│   │   │   ├── LICENSE
│   │   │   ├── manifest.json
│   │   │   ├── NOTICE.md
│   │   │   ├── README.ar.md
│   │   │   ├── README.md
│   │   │   ├── requirements-validation.txt
│   │   │   ├── screen-composition-catalog.json
│   │   │   ├── SHA256SUMS.txt
│   │   │   └── START-HERE-AR.md
│   │   ├── adaptive.md
│   │   ├── catalog.yaml
│   │   ├── local-fonts.md
│   │   ├── rtl-ltr.md
│   │   └── SMART-UI-ATTRIBUTION.md
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
│   │   ├── hooks
│   │   │   └── settings.example.json
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
│   ├── v0
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── custom-instructions.md
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
│   └── enforcement-matrix.yaml
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
│   ├── acceptance.py
│   ├── approval.py
│   ├── bootstrap.md
│   ├── compliance.py
│   ├── context-policy.yaml
│   ├── context.py
│   ├── contracts.py
│   ├── evidence.py
│   ├── evidence_pack.py
│   ├── loader.py
│   ├── model-guidance.md
│   ├── pack-map.yaml
│   ├── preferences-policy.yaml
│   ├── registry.py
│   ├── resolver.py
│   ├── router.py
│   ├── routing-policy.yaml
│   ├── scope_guard.py
│   ├── tokens.py
│   ├── ui-bindings.yaml
│   └── ui_select.py
├── schemas
│   ├── v1.1.0
│   │   ├── acceptance-results.schema.json
│   │   ├── adapter-capabilities.schema.json
│   │   ├── approval.schema.json
│   │   ├── capability.schema.json
│   │   ├── common.schema.json
│   │   ├── context.schema.json
│   │   ├── evidence.schema.json
│   │   ├── preferences.schema.json
│   │   ├── route-result.schema.json
│   │   └── ui-selection.schema.json
│   ├── v1.2.0
│   │   ├── architecture-decision.schema.json
│   │   ├── project-fingerprint.schema.json
│   │   ├── release-evidence.schema.json
│   │   ├── ux-decision.schema.json
│   │   └── ux-discovery.schema.json
│   ├── v1.4.0
│   │   └── control.schema.json
│   ├── adapter.schema.json
│   ├── conformance.schema.json
│   ├── control.schema.json
│   └── profile.schema.json
├── scripts
│   ├── hooks
│   │   ├── guard-governance-files.py
│   │   └── pre-commit-vcgf.py
│   ├── benchmark-adaptive.py
│   ├── check-adapter-updates.py
│   ├── generate-adapter-rules.py
│   ├── generate-control-cards.py
│   ├── generate-control-catalog.py
│   ├── generate-file-manifest.py
│   ├── generate-repository-tree.py
│   ├── generate-runtime-registry.py
│   ├── generate-sbom.py
│   ├── migrate-task-budget.py
│   ├── record-release-validation.py
│   ├── release-quality-gate.py
│   ├── run-self-acceptance.py
│   ├── test-adaptive-browser.py
│   ├── validate-acceptance.py
│   ├── validate-adapters.py
│   ├── validate-applicability.py
│   ├── validate-attribution.py
│   ├── validate-contracts.py
│   ├── validate-control-cards.py
│   ├── validate-controls.py
│   ├── validate-cross-references.py
│   ├── validate-dependencies.py
│   ├── validate-documentation.py
│   ├── validate-enforcement.py
│   ├── validate-internal-links.py
│   ├── validate-license.py
│   ├── validate-operational-map.py
│   ├── validate-package-integrity.py
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
│   ├── acceptance
│   │   ├── ai-governance.yaml
│   │   ├── api.yaml
│   │   ├── architecture.yaml
│   │   ├── data-protection.yaml
│   │   ├── database.yaml
│   │   ├── dependencies.yaml
│   │   ├── file-handling.yaml
│   │   ├── governance.yaml
│   │   ├── identity-access.yaml
│   │   ├── incident-response.yaml
│   │   ├── logging-auditing.yaml
│   │   ├── operations.yaml
│   │   ├── privacy.yaml
│   │   ├── README.md
│   │   ├── release.yaml
│   │   ├── secrets.yaml
│   │   ├── security.yaml
│   │   ├── testing.yaml
│   │   └── user-experience.yaml
│   ├── control-cards
│   │   ├── common-clauses.md
│   │   ├── README.md
│   │   ├── VCGF-AI-001.md
│   │   ├── VCGF-AI-002.md
│   │   ├── VCGF-AI-003.md
│   │   ├── VCGF-AI-004.md
│   │   ├── VCGF-AI-005.md
│   │   ├── VCGF-AI-006.md
│   │   ├── VCGF-AI-007.md
│   │   ├── VCGF-AI-008.md
│   │   ├── VCGF-AI-009.md
│   │   ├── VCGF-API-001.md
│   │   ├── VCGF-API-002.md
│   │   ├── VCGF-API-003.md
│   │   ├── VCGF-API-004.md
│   │   ├── VCGF-API-005.md
│   │   ├── VCGF-ARCH-001.md
│   │   ├── VCGF-ARCH-002.md
│   │   ├── VCGF-ARCH-003.md
│   │   ├── VCGF-ARCH-004.md
│   │   ├── VCGF-ARCH-005.md
│   │   ├── VCGF-AUDIT-001.md
│   │   ├── VCGF-AUDIT-002.md
│   │   ├── VCGF-AUDIT-003.md
│   │   ├── VCGF-DATA-001.md
│   │   ├── VCGF-DATA-002.md
│   │   ├── VCGF-DATA-003.md
│   │   ├── VCGF-DATA-004.md
│   │   ├── VCGF-DATA-005.md
│   │   ├── VCGF-DATA-006.md
│   │   ├── VCGF-DB-001.md
│   │   ├── VCGF-DB-002.md
│   │   ├── VCGF-DB-003.md
│   │   ├── VCGF-DB-004.md
│   │   ├── VCGF-DB-005.md
│   │   ├── VCGF-DB-006.md
│   │   ├── VCGF-DEP-001.md
│   │   ├── VCGF-DEP-002.md
│   │   ├── VCGF-DEP-003.md
│   │   ├── VCGF-DEP-004.md
│   │   ├── VCGF-FILE-001.md
│   │   ├── VCGF-FILE-002.md
│   │   ├── VCGF-GOV-001.md
│   │   ├── VCGF-GOV-002.md
│   │   ├── VCGF-GOV-003.md
│   │   ├── VCGF-GOV-004.md
│   │   ├── VCGF-GOV-005.md
│   │   ├── VCGF-GOV-006.md
│   │   ├── VCGF-IAM-001.md
│   │   ├── VCGF-IAM-002.md
│   │   ├── VCGF-IAM-003.md
│   │   ├── VCGF-IAM-004.md
│   │   ├── VCGF-IAM-005.md
│   │   ├── VCGF-IAM-006.md
│   │   ├── VCGF-IAM-007.md
│   │   ├── VCGF-IR-001.md
│   │   ├── VCGF-IR-002.md
│   │   ├── VCGF-IR-003.md
│   │   ├── VCGF-OPS-001.md
│   │   ├── VCGF-OPS-002.md
│   │   ├── VCGF-OPS-003.md
│   │   ├── VCGF-OPS-004.md
│   │   ├── VCGF-OPS-005.md
│   │   ├── VCGF-PRIV-001.md
│   │   ├── VCGF-PRIV-002.md
│   │   ├── VCGF-PRIV-003.md
│   │   ├── VCGF-PRIV-004.md
│   │   ├── VCGF-REL-001.md
│   │   ├── VCGF-REL-002.md
│   │   ├── VCGF-REL-003.md
│   │   ├── VCGF-REL-004.md
│   │   ├── VCGF-REL-005.md
│   │   ├── VCGF-SEC-001.md
│   │   ├── VCGF-SEC-002.md
│   │   ├── VCGF-SEC-003.md
│   │   ├── VCGF-SEC-004.md
│   │   ├── VCGF-SEC-005.md
│   │   ├── VCGF-SEC-006.md
│   │   ├── VCGF-SECR-001.md
│   │   ├── VCGF-SECR-002.md
│   │   ├── VCGF-TEST-001.md
│   │   ├── VCGF-TEST-002.md
│   │   ├── VCGF-TEST-003.md
│   │   ├── VCGF-TEST-004.md
│   │   ├── VCGF-TEST-005.md
│   │   ├── VCGF-TEST-006.md
│   │   ├── VCGF-UX-001.md
│   │   ├── VCGF-UX-002.md
│   │   ├── VCGF-UX-003.md
│   │   └── VCGF-UX-004.md
│   ├── applicability-matrix.yaml
│   ├── conformance.md
│   ├── control-catalog.yaml
│   ├── evidence-model.md
│   ├── exception-management.md
│   ├── lifecycle.md
│   ├── normative-language.md
│   ├── operational-control-map.yaml
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
│   ├── acceptance
│   │   └── test_self_acceptance.py
│   ├── adaptive
│   │   ├── conftest.py
│   │   ├── test_engines.py
│   │   ├── test_inputs.py
│   │   ├── test_integration.py
│   │   ├── test_legacy_loader.py
│   │   ├── test_release.py
│   │   └── test_smart_ui_pack.py
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
│   │       ├── acceptance-results.json
│   │       ├── adapter-capabilities.json
│   │       ├── approval.json
│   │       ├── capability.json
│   │       ├── context.json
│   │       ├── evidence.json
│   │       ├── preferences.json
│   │       ├── route-result.json
│   │       ├── screen-context.json
│   │       └── ui-selection.json
│   └── scenarios
│       ├── test_adapters.py
│       ├── test_applicability_triggers.py
│       ├── test_compliance.py
│       ├── test_context_efficiency.py
│       ├── test_context_hardening.py
│       ├── test_enforcement.py
│       ├── test_final_consolidation.py
│       ├── test_gates.py
│       ├── test_integrations.py
│       ├── test_profile_layer.py
│       ├── test_runtime.py
│       └── test_ui_select.py
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
