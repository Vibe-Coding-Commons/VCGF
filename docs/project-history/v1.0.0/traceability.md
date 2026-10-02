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

# Traceability

Traceability links prior package sources to VCGF 1.0.0 canonical destinations.

| Original Source | Canonical Destination | Platform Implementation |
|---|---|---|
| `00_Core/AI_ANTI_HALLUCINATION_POLICY.md` | `controls/ai-governance/vcgf-ai-001-inspect-before-generate.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `00_Core/CHANGE_IMPACT_POLICY.md` | `controls/governance/vcgf-gov-001-change-impact-analysis.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `00_Core/DEFINITION_OF_DONE.md` | `controls/release/vcgf-rel-001-definition-of-done.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `00_Core/MASTER_GOVERNANCE_CONSTITUTION.md` | `VCGF canonical documentation / control set` | N/A or destination-specific |
| `00_Core/SECURITY_EXCEPTION_PROCESS.md` | `controls/governance/vcgf-gov-003-security-exception-management.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `01_Input_Validation/CRITICAL_FIELD_VALIDATION_MATRIX.md` | `controls/security/vcgf-sec-001-critical-field-validation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `01_Input_Validation/FILE_AND_URL_VALIDATION.md` | `controls/security/vcgf-sec-002-file-and-url-validation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `01_Input_Validation/INJECTION_DEFENSE_POLICY.md` | `controls/security/vcgf-sec-003-injection-defense.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `01_Input_Validation/INPUT_VALIDATION_POLICY.md` | `controls/security/vcgf-sec-004-trusted-layer-input-validation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `01_Input_Validation/OUTPUT_ENCODING_SANITIZATION.md` | `controls/security/vcgf-sec-005-output-encoding-and-sanitization.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/BACKUP_EXPORT_SECURITY.md` | `controls/data-protection/vcgf-data-001-backup-and-export-protection.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/DATA_CLASSIFICATION_RETENTION.md` | `controls/data-protection/vcgf-data-002-data-classification-and-retention.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/FIELD_LEVEL_ENCRYPTION_POLICY.md` | `controls/data-protection/vcgf-data-003-field-level-encryption.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/KEY_MANAGEMENT_ROTATION.md` | `controls/data-protection/vcgf-data-004-key-management-and-rotation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/LOGGING_REDACTION_PRIVACY.md` | `controls/privacy/vcgf-priv-001-logging-redaction-and-privacy.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `02_Data_Protection/PII_DATA_PROTECTION_POLICY.md` | `controls/privacy/vcgf-priv-002-personal-data-protection.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/ACCOUNT_ENUMERATION_BRUTE_FORCE.md` | `controls/identity-access/vcgf-iam-001-enumeration-and-brute-force-resistance.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/AUTHENTICATION_POLICY.md` | `controls/identity-access/vcgf-iam-002-authentication-baseline.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/MFA_SESSION_SECURITY.md` | `controls/identity-access/vcgf-iam-003-mfa-and-session-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/PASSWORD_POLICY.md` | `controls/identity-access/vcgf-iam-004-password-storage-and-policy.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/PASSWORD_RESET_RECOVERY_POLICY.md` | `controls/identity-access/vcgf-iam-005-secure-password-reset-and-recovery.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/PRIVILEGED_ACCESS_ADMIN.md` | `controls/identity-access/vcgf-iam-006-privileged-access-administration.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `03_Identity_Access/RBAC_ABAC_RLS_POLICY.md` | `controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/API_EDGE_FUNCTION_SECURITY.md` | `controls/api/vcgf-api-001-api-and-server-function-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/BUSINESS_LOGIC_INTEGRITY.md` | `controls/api/vcgf-api-002-business-logic-integrity.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/MULTITENANCY_ISOLATION.md` | `controls/architecture/vcgf-arch-001-tenant-isolation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/RATE_LIMITING_ABUSE_PREVENTION.md` | `controls/api/vcgf-api-003-rate-limiting-and-abuse-prevention.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/SECURE_ERRORS_LOGGING.md` | `controls/logging-auditing/vcgf-audit-001-secure-errors-and-diagnostic-logging.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `04_Backend_API/SSRF_CSRF_CORS_WEBHOOKS.md` | `controls/api/vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `05_Database/DATABASE_CHANGE_POLICY.md` | `controls/database/vcgf-db-001-database-change-governance.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `05_Database/DATABASE_INTEGRITY_POLICY.md` | `controls/database/vcgf-db-002-database-integrity.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `05_Database/ENCRYPTION_IMPLEMENTATION_GUIDE.md` | `controls/database/vcgf-db-003-database-encryption-implementation.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `05_Database/RLS_TESTING_POLICY.md` | `controls/database/vcgf-db-004-row-level-authorization-testing.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `05_Database/SQL_QUERY_SECURITY.md` | `controls/database/vcgf-db-005-sql-query-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `06_Files_Secrets_SupplyChain/DEPENDENCY_SUPPLY_CHAIN_SECURITY.md` | `controls/dependencies/vcgf-dep-001-dependency-and-supply-chain-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `06_Files_Secrets_SupplyChain/FILE_UPLOAD_STORAGE_SECURITY.md` | `controls/file-handling/vcgf-file-001-file-upload-and-storage-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `06_Files_Secrets_SupplyChain/SECRETS_ENVIRONMENT_POLICY.md` | `controls/secrets/vcgf-secr-001-secrets-and-environment-protection.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `06_Files_Secrets_SupplyChain/THIRD_PARTY_INTEGRATION_SECURITY.md` | `controls/api/vcgf-api-005-third-party-integration-security.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/AUTHORIZATION_NEGATIVE_TEST_MATRIX.md` | `controls/testing/vcgf-test-001-authorization-negative-testing.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/INCIDENT_RESPONSE_MINIMUMS.md` | `controls/incident-response/vcgf-ir-001-incident-response-minimums.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/PRE_RELEASE_SECURITY_GATE.md` | `controls/release/vcgf-rel-002-pre-release-security-gate.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/SECURE_CODE_REVIEW_CHECKLIST.md` | `controls/testing/vcgf-test-002-secure-code-review.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/SECURITY_REGRESSION_CHECKLIST.md` | `controls/testing/vcgf-test-003-security-regression-review.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `07_Testing_Assurance/SECURITY_TEST_STRATEGY.md` | `controls/testing/vcgf-test-004-security-test-strategy.md` | Relevant `platforms/<adapter>/CONTROL-MAPPING.md` |
| `08_Prompts/AUTH_PASSWORD_RECOVERY_AUDIT_PROMPT.md` | `templates/project-context/prompts/auth-password-recovery-audit-prompt.md` | N/A or destination-specific |
| `08_Prompts/CHANGE_IMPACT_ANALYSIS_PROMPT.md` | `templates/project-context/prompts/change-impact-analysis-prompt.md` | N/A or destination-specific |
| `08_Prompts/DEPENDENCY_SUPPLY_CHAIN_AUDIT_PROMPT.md` | `templates/project-context/prompts/dependency-supply-chain-audit-prompt.md` | N/A or destination-specific |
| `08_Prompts/INITIAL_READ_ONLY_AUDIT_PROMPT.md` | `templates/project-context/prompts/initial-read-only-audit-prompt.md` | N/A or destination-specific |
| `08_Prompts/PII_ENCRYPTION_AUDIT_PROMPT.md` | `templates/project-context/prompts/pii-encryption-audit-prompt.md` | N/A or destination-specific |
| `08_Prompts/PRE_RELEASE_SECURITY_REVIEW_PROMPT.md` | `templates/project-context/prompts/pre-release-security-review-prompt.md` | N/A or destination-specific |
| `08_Prompts/SAFE_BUGFIX_PROMPT.md` | `templates/project-context/prompts/safe-bugfix-prompt.md` | N/A or destination-specific |
| `08_Prompts/SAFE_FEATURE_PROMPT.md` | `templates/project-context/prompts/safe-feature-prompt.md` | N/A or destination-specific |
| `08_Prompts/VALIDATION_INJECTION_AUDIT_PROMPT.md` | `templates/project-context/prompts/validation-injection-audit-prompt.md` | N/A or destination-specific |
| `09_Platform_Adapters/Bolt/BOLT_INSTALLATION_GUIDE.md` | `platforms/bolt/INSTALLATION.md` | N/A or destination-specific |
| `09_Platform_Adapters/Bolt/BOLT_PROJECT_KNOWLEDGE.md` | `platforms/bolt/rules/project-knowledge.md` | N/A or destination-specific |
| `09_Platform_Adapters/COMMON/PLATFORM_COMPATIBILITY_MATRIX.md` | `docs/platform-compatibility.md` | N/A or destination-specific |
| `09_Platform_Adapters/COMMON/PORTABLE_MASTER_PROMPT.md` | `docs/platform-compatibility.md` | N/A or destination-specific |
| `09_Platform_Adapters/Claude/CLAUDE_INSTALLATION_GUIDE.md` | `platforms/claude/INSTALLATION.md` | N/A or destination-specific |
| `09_Platform_Adapters/Claude/CLAUDE_PROJECT_INSTRUCTIONS.md` | `platforms/claude/rules/CLAUDE.md` | N/A or destination-specific |
| `09_Platform_Adapters/Lovable/LOVABLE_INSTALLATION_GUIDE.md` | `platforms/lovable/INSTALLATION.md` | N/A or destination-specific |
| `09_Platform_Adapters/Lovable/LOVABLE_PROJECT_KNOWLEDGE.md` | `platforms/lovable/rules/project-knowledge.md` | N/A or destination-specific |
| `09_Platform_Adapters/Lovable/LOVABLE_WORKSPACE_KNOWLEDGE.md` | `platforms/lovable/rules/project-knowledge.md` | N/A or destination-specific |
| `09_Platform_Adapters/Replit/REPLIT_INSTALLATION_GUIDE.md` | `platforms/replit/INSTALLATION.md` | N/A or destination-specific |
| `09_Platform_Adapters/v0/V0_INSTALLATION_GUIDE.md` | `platforms/v0/INSTALLATION.md` | N/A or destination-specific |
| `09_Platform_Adapters/v0/V0_PROJECT_INSTRUCTIONS.md` | `platforms/v0/rules/custom-instructions.md` | N/A or destination-specific |
| `10_Templates/DATA_CLASSIFICATION_TEMPLATE.md` | `templates/security/data-classification.md` | N/A or destination-specific |
| `10_Templates/ENCRYPTION_REGISTER_TEMPLATE.md` | `templates/security/encryption-register.md` | N/A or destination-specific |
| `10_Templates/FIELD_VALIDATION_MATRIX_TEMPLATE.md` | `templates/security/field-validation-matrix.md` | N/A or destination-specific |
| `10_Templates/PROJECT_SECURITY_PROFILE_TEMPLATE.md` | `templates/project-context/project-security-profile.md` | N/A or destination-specific |
| `10_Templates/REGULATORY_OVERLAY_TEMPLATE.md` | `templates/project-context/regulatory-overlay.md` | N/A or destination-specific |
| `10_Templates/ROLE_PERMISSION_MATRIX_TEMPLATE.md` | `templates/security/role-permission-matrix.md` | N/A or destination-specific |
| `10_Templates/SECURITY_DECISION_RECORD_TEMPLATE.md` | `templates/architecture/security-decision-record.md` | N/A or destination-specific |
| `10_Templates/SECURITY_EXCEPTION_TEMPLATE.md` | `templates/security/security-exception.md` | N/A or destination-specific |
| `10_Templates/SECURITY_TEST_EVIDENCE_TEMPLATE.md` | `templates/testing/security-test-evidence.md` | N/A or destination-specific |
| `10_Templates/THREAT_MODEL_TEMPLATE.md` | `templates/security/threat-model.md` | N/A or destination-specific |
| `11_References/MAPPING_TO_OWASP_ASVS_5.md` | `docs/references/owasp-asvs-5-mapping.md` | N/A or destination-specific |
| `11_References/SOURCES_AND_STANDARDS.md` | `docs/references/sources-and-standards.md` | N/A or destination-specific |
| `11_References/TERMINOLOGY.md` | `docs/terminology.md` | N/A or destination-specific |
| `12_Operational_Playbooks/EXISTING_PROJECT_HARDENING_PLAN.md` | `playbooks/existing-project-hardening-plan.md` | N/A or destination-specific |
| `12_Operational_Playbooks/KEY_ROTATION_PLAYBOOK.md` | `playbooks/key-rotation-playbook.md` | N/A or destination-specific |
| `12_Operational_Playbooks/NEW_PROJECT_SECURITY_BOOTSTRAP.md` | `playbooks/new-project-security-bootstrap.md` | N/A or destination-specific |
| `12_Operational_Playbooks/PASSWORD_RESET_TEST_CASES.md` | `playbooks/password-reset-test-cases.md` | N/A or destination-specific |
| `AGENTS.md` | `platforms/generic/rules/portable-project-rules.md` | N/A or destination-specific |
| `AUTHOR_AND_RIGHTS.md` | `AUTHORS.md` | N/A or destination-specific |
| `CHANGELOG.md` | `CHANGELOG.md` | N/A or destination-specific |
| `CLAUDE.md` | `platforms/claude/rules/CLAUDE.md` | N/A or destination-specific |
| `FILE_MANIFEST.md` | `FILE-MANIFEST.md` | N/A or destination-specific |
| `FRAMEWORK_OVERVIEW.md` | `README.md` | N/A or destination-specific |
| `LICENSE.md` | `LICENSE` | N/A or destination-specific |
| `MIGRATION_FROM_V1.md` | `docs/migration-guide.md` | N/A or destination-specific |
| `QUICK_START_AR.md` | `docs/quick-start.ar.md` | N/A or destination-specific |
| `README_AR.md` | `README.ar.md` | N/A or destination-specific |
| `replit.md` | `platforms/replit/rules/replit.md` | N/A or destination-specific |
