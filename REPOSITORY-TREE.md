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
│   │   ├── validate-framework.yml
│   │   ├── validate-links.yml
│   │   └── validate-schemas.yml
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── assets
│   └── brand
│       └── brand-guidelines.md
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
│   │   └── v1.0.0
│   │       ├── architecture-report.md
│   │       ├── conflict-report.md
│   │       ├── file-inventory.md
│   │       ├── final-qa-audit.md
│   │       ├── final-release-report.md
│   │       ├── migration-map.md
│   │       └── traceability.md
│   ├── references
│   │   ├── owasp-asvs-5-mapping.md
│   │   └── sources-and-standards.md
│   ├── adapter-model.md
│   ├── adoption-guide.md
│   ├── architecture.md
│   ├── control-model.md
│   ├── implementation-guide.md
│   ├── migration-guide.md
│   ├── platform-compatibility.md
│   ├── principles.md
│   ├── quick-start.ar.md
│   ├── terminology.md
│   ├── user-guide.md
│   └── versioning-model.md
├── examples
│   ├── crm
│   │   └── README.md
│   ├── ecommerce
│   │   └── README.md
│   ├── erp
│   │   └── README.md
│   ├── generic-web-app
│   │   └── README.md
│   └── saas
│       └── README.md
├── legal
│   ├── attribution.md
│   ├── third-party-notices.md
│   └── trademark-policy.md
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
│   │   │   └── project-knowledge.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   ├── claude
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   └── CLAUDE.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   ├── cursor
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   ├── AGENTS.md
│   │   │   └── vcgf.mdc
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   ├── generic
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   └── portable-project-rules.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   │   │   └── workspace-knowledge.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   ├── replit
│   │   ├── examples
│   │   │   └── example-adoption.md
│   │   ├── mappings
│   │   │   └── README.md
│   │   ├── prompts
│   │   │   └── pre-change-impact-review.md
│   │   ├── rules
│   │   │   └── replit.md
│   │   ├── templates
│   │   │   └── project-context.md
│   │   ├── tests
│   │   │   └── adapter-verification.md
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
│   └── v0
│       ├── examples
│       │   └── example-adoption.md
│       ├── mappings
│       │   └── README.md
│       ├── prompts
│       │   └── pre-change-impact-review.md
│       ├── rules
│       │   └── custom-instructions.md
│       ├── templates
│       │   └── project-context.md
│       ├── tests
│       │   └── adapter-verification.md
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
│       └── README.md
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
├── schemas
│   ├── adapter.schema.json
│   ├── conformance.schema.json
│   ├── control.schema.json
│   └── profile.schema.json
├── scripts
│   ├── generate-control-catalog.py
│   ├── generate-file-manifest.py
│   ├── generate-repository-tree.py
│   ├── release-quality-gate.py
│   ├── validate-adapters.py
│   ├── validate-attribution.py
│   ├── validate-controls.py
│   ├── validate-cross-references.py
│   ├── validate-documentation.py
│   ├── validate-internal-links.py
│   ├── validate-license.py
│   ├── validate-placeholders.py
│   ├── validate-profiles.py
│   ├── validate-repository-structure.py
│   ├── validate-schemas.py
│   ├── validate-vendor-neutral-core.py
│   ├── validate-version.py
│   ├── validate-yaml.py
│   └── vcgf_lib.py
├── spec
│   ├── conformance.md
│   ├── control-catalog.yaml
│   ├── evidence-model.md
│   ├── exception-management.md
│   ├── lifecycle.md
│   ├── normative-language.md
│   ├── risk-model.md
│   └── VCGF-CORE.md
├── templates
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
├── ROADMAP.md
├── SECURITY.md
├── VCGF-MANIFEST.yaml
└── VERSION
```
