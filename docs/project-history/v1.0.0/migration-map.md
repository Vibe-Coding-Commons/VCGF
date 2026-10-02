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

# Migration Map

| Old File | New File / Area | Action | Reason |
|---|---|---|---|
| `00_Core/AI_ANTI_HALLUCINATION_POLICY.md` | `controls/ai-governance/vcgf-ai-001-inspect-before-generate.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `00_Core/CHANGE_IMPACT_POLICY.md` | `controls/governance/vcgf-gov-001-change-impact-analysis.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `00_Core/DEFINITION_OF_DONE.md` | `controls/release/vcgf-rel-001-definition-of-done.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `00_Core/MASTER_GOVERNANCE_CONSTITUTION.md` | `VCGF canonical documentation / control set` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `00_Core/SECURITY_EXCEPTION_PROCESS.md` | `controls/governance/vcgf-gov-003-security-exception-management.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `01_Input_Validation/CRITICAL_FIELD_VALIDATION_MATRIX.md` | `controls/security/vcgf-sec-001-critical-field-validation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `01_Input_Validation/FILE_AND_URL_VALIDATION.md` | `controls/security/vcgf-sec-002-file-and-url-validation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `01_Input_Validation/INJECTION_DEFENSE_POLICY.md` | `controls/security/vcgf-sec-003-injection-defense.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `01_Input_Validation/INPUT_VALIDATION_POLICY.md` | `controls/security/vcgf-sec-004-trusted-layer-input-validation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `01_Input_Validation/OUTPUT_ENCODING_SANITIZATION.md` | `controls/security/vcgf-sec-005-output-encoding-and-sanitization.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/BACKUP_EXPORT_SECURITY.md` | `controls/data-protection/vcgf-data-001-backup-and-export-protection.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/DATA_CLASSIFICATION_RETENTION.md` | `controls/data-protection/vcgf-data-002-data-classification-and-retention.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/FIELD_LEVEL_ENCRYPTION_POLICY.md` | `controls/data-protection/vcgf-data-003-field-level-encryption.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/KEY_MANAGEMENT_ROTATION.md` | `controls/data-protection/vcgf-data-004-key-management-and-rotation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/LOGGING_REDACTION_PRIVACY.md` | `controls/privacy/vcgf-priv-001-logging-redaction-and-privacy.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `02_Data_Protection/PII_DATA_PROTECTION_POLICY.md` | `controls/privacy/vcgf-priv-002-personal-data-protection.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/ACCOUNT_ENUMERATION_BRUTE_FORCE.md` | `controls/identity-access/vcgf-iam-001-enumeration-and-brute-force-resistance.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/AUTHENTICATION_POLICY.md` | `controls/identity-access/vcgf-iam-002-authentication-baseline.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/MFA_SESSION_SECURITY.md` | `controls/identity-access/vcgf-iam-003-mfa-and-session-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/PASSWORD_POLICY.md` | `controls/identity-access/vcgf-iam-004-password-storage-and-policy.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/PASSWORD_RESET_RECOVERY_POLICY.md` | `controls/identity-access/vcgf-iam-005-secure-password-reset-and-recovery.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/PRIVILEGED_ACCESS_ADMIN.md` | `controls/identity-access/vcgf-iam-006-privileged-access-administration.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `03_Identity_Access/RBAC_ABAC_RLS_POLICY.md` | `controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/API_EDGE_FUNCTION_SECURITY.md` | `controls/api/vcgf-api-001-api-and-server-function-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/BUSINESS_LOGIC_INTEGRITY.md` | `controls/api/vcgf-api-002-business-logic-integrity.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/MULTITENANCY_ISOLATION.md` | `controls/architecture/vcgf-arch-001-tenant-isolation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/RATE_LIMITING_ABUSE_PREVENTION.md` | `controls/api/vcgf-api-003-rate-limiting-and-abuse-prevention.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/SECURE_ERRORS_LOGGING.md` | `controls/logging-auditing/vcgf-audit-001-secure-errors-and-diagnostic-logging.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `04_Backend_API/SSRF_CSRF_CORS_WEBHOOKS.md` | `controls/api/vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `05_Database/DATABASE_CHANGE_POLICY.md` | `controls/database/vcgf-db-001-database-change-governance.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `05_Database/DATABASE_INTEGRITY_POLICY.md` | `controls/database/vcgf-db-002-database-integrity.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `05_Database/ENCRYPTION_IMPLEMENTATION_GUIDE.md` | `controls/database/vcgf-db-003-database-encryption-implementation.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `05_Database/RLS_TESTING_POLICY.md` | `controls/database/vcgf-db-004-row-level-authorization-testing.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `05_Database/SQL_QUERY_SECURITY.md` | `controls/database/vcgf-db-005-sql-query-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `06_Files_Secrets_SupplyChain/DEPENDENCY_SUPPLY_CHAIN_SECURITY.md` | `controls/dependencies/vcgf-dep-001-dependency-and-supply-chain-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `06_Files_Secrets_SupplyChain/FILE_UPLOAD_STORAGE_SECURITY.md` | `controls/file-handling/vcgf-file-001-file-upload-and-storage-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `06_Files_Secrets_SupplyChain/SECRETS_ENVIRONMENT_POLICY.md` | `controls/secrets/vcgf-secr-001-secrets-and-environment-protection.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `06_Files_Secrets_SupplyChain/THIRD_PARTY_INTEGRATION_SECURITY.md` | `controls/api/vcgf-api-005-third-party-integration-security.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/AUTHORIZATION_NEGATIVE_TEST_MATRIX.md` | `controls/testing/vcgf-test-001-authorization-negative-testing.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/INCIDENT_RESPONSE_MINIMUMS.md` | `controls/incident-response/vcgf-ir-001-incident-response-minimums.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/PRE_RELEASE_SECURITY_GATE.md` | `controls/release/vcgf-rel-002-pre-release-security-gate.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/SECURE_CODE_REVIEW_CHECKLIST.md` | `controls/testing/vcgf-test-002-secure-code-review.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/SECURITY_REGRESSION_CHECKLIST.md` | `controls/testing/vcgf-test-003-security-regression-review.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `07_Testing_Assurance/SECURITY_TEST_STRATEGY.md` | `controls/testing/vcgf-test-004-security-test-strategy.md` | GENERALIZE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/AUTH_PASSWORD_RECOVERY_AUDIT_PROMPT.md` | `templates/project-context/prompts/auth-password-recovery-audit-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/CHANGE_IMPACT_ANALYSIS_PROMPT.md` | `templates/project-context/prompts/change-impact-analysis-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/DEPENDENCY_SUPPLY_CHAIN_AUDIT_PROMPT.md` | `templates/project-context/prompts/dependency-supply-chain-audit-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/INITIAL_READ_ONLY_AUDIT_PROMPT.md` | `templates/project-context/prompts/initial-read-only-audit-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/PII_ENCRYPTION_AUDIT_PROMPT.md` | `templates/project-context/prompts/pii-encryption-audit-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/PRE_RELEASE_SECURITY_REVIEW_PROMPT.md` | `templates/project-context/prompts/pre-release-security-review-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/SAFE_BUGFIX_PROMPT.md` | `templates/project-context/prompts/safe-bugfix-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/SAFE_FEATURE_PROMPT.md` | `templates/project-context/prompts/safe-feature-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `08_Prompts/VALIDATION_INJECTION_AUDIT_PROMPT.md` | `templates/project-context/prompts/validation-injection-audit-prompt.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `09_Platform_Adapters/Bolt/BOLT_INSTALLATION_GUIDE.md` | `platforms/bolt/INSTALLATION.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Bolt/BOLT_PROJECT_KNOWLEDGE.md` | `platforms/bolt/rules/project-knowledge.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/COMMON/PLATFORM_COMPATIBILITY_MATRIX.md` | `docs/platform-compatibility.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/COMMON/PORTABLE_MASTER_PROMPT.md` | `docs/platform-compatibility.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Claude/CLAUDE_INSTALLATION_GUIDE.md` | `platforms/claude/INSTALLATION.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Claude/CLAUDE_PROJECT_INSTRUCTIONS.md` | `platforms/claude/rules/CLAUDE.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Lovable/LOVABLE_INSTALLATION_GUIDE.md` | `platforms/lovable/INSTALLATION.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Lovable/LOVABLE_PROJECT_KNOWLEDGE.md` | `platforms/lovable/rules/project-knowledge.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Lovable/LOVABLE_WORKSPACE_KNOWLEDGE.md` | `platforms/lovable/rules/project-knowledge.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/Replit/REPLIT_INSTALLATION_GUIDE.md` | `platforms/replit/INSTALLATION.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/v0/V0_INSTALLATION_GUIDE.md` | `platforms/v0/INSTALLATION.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `09_Platform_Adapters/v0/V0_PROJECT_INSTRUCTIONS.md` | `platforms/v0/rules/custom-instructions.md` | MOVE-TO-ADAPTER | Separate vendor implementation from core policy. |
| `10_Templates/DATA_CLASSIFICATION_TEMPLATE.md` | `templates/security/data-classification.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/ENCRYPTION_REGISTER_TEMPLATE.md` | `templates/security/encryption-register.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/FIELD_VALIDATION_MATRIX_TEMPLATE.md` | `templates/security/field-validation-matrix.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/PROJECT_SECURITY_PROFILE_TEMPLATE.md` | `templates/project-context/project-security-profile.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/REGULATORY_OVERLAY_TEMPLATE.md` | `templates/project-context/regulatory-overlay.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/ROLE_PERMISSION_MATRIX_TEMPLATE.md` | `templates/security/role-permission-matrix.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/SECURITY_DECISION_RECORD_TEMPLATE.md` | `templates/architecture/security-decision-record.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/SECURITY_EXCEPTION_TEMPLATE.md` | `templates/security/security-exception.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/SECURITY_TEST_EVIDENCE_TEMPLATE.md` | `templates/testing/security-test-evidence.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `10_Templates/THREAT_MODEL_TEMPLATE.md` | `templates/security/threat-model.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `11_References/MAPPING_TO_OWASP_ASVS_5.md` | `docs/references/owasp-asvs-5-mapping.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `11_References/SOURCES_AND_STANDARDS.md` | `docs/references/sources-and-standards.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `11_References/TERMINOLOGY.md` | `docs/terminology.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `12_Operational_Playbooks/EXISTING_PROJECT_HARDENING_PLAN.md` | `playbooks/existing-project-hardening-plan.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `12_Operational_Playbooks/KEY_ROTATION_PLAYBOOK.md` | `playbooks/key-rotation-playbook.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `12_Operational_Playbooks/NEW_PROJECT_SECURITY_BOOTSTRAP.md` | `playbooks/new-project-security-bootstrap.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `12_Operational_Playbooks/PASSWORD_RESET_TEST_CASES.md` | `playbooks/password-reset-test-cases.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `AGENTS.md` | `platforms/generic/rules/portable-project-rules.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `AUTHOR_AND_RIGHTS.md` | `AUTHORS.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `CHANGELOG.md` | `CHANGELOG.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `CLAUDE.md` | `platforms/claude/rules/CLAUDE.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `FILE_MANIFEST.md` | `FILE-MANIFEST.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `FRAMEWORK_OVERVIEW.md` | `README.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `LICENSE.md` | `LICENSE` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `MIGRATION_FROM_V1.md` | `docs/migration-guide.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `QUICK_START_AR.md` | `docs/quick-start.ar.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `README_AR.md` | `README.ar.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
| `replit.md` | `platforms/replit/rules/replit.md` | MOVE/MERGE | Normalize content into the vendor-neutral VCGF architecture while preserving requirement intent. |
