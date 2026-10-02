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

# File Inventory

Inventory of the previous multi-platform package used as migration input.

| Current File | Purpose / Category | Vendor Specific | Security Relevance | Recommended Action | New Location |
|---|---|---|---|---|---|
| `00_Core/AI_ANTI_HALLUCINATION_POLICY.md` | AI ANTI HALLUCINATION POLICY | No | Medium | GENERALIZE | `controls/ai-governance/vcgf-ai-001-inspect-before-generate.md` |
| `00_Core/CHANGE_IMPACT_POLICY.md` | CHANGE IMPACT POLICY | No | Medium | GENERALIZE | `controls/governance/vcgf-gov-001-change-impact-analysis.md` |
| `00_Core/DEFINITION_OF_DONE.md` | DEFINITION OF DONE | No | Medium | GENERALIZE | `controls/release/vcgf-rel-001-definition-of-done.md` |
| `00_Core/MASTER_GOVERNANCE_CONSTITUTION.md` | MASTER GOVERNANCE CONSTITUTION | No | Medium | MERGE | `VCGF canonical documentation / control set` |
| `00_Core/SECURITY_EXCEPTION_PROCESS.md` | SECURITY EXCEPTION PROCESS | No | Medium | GENERALIZE | `controls/governance/vcgf-gov-003-security-exception-management.md` |
| `01_Input_Validation/CRITICAL_FIELD_VALIDATION_MATRIX.md` | CRITICAL FIELD VALIDATION MATRIX | No | High | GENERALIZE | `controls/security/vcgf-sec-001-critical-field-validation.md` |
| `01_Input_Validation/FILE_AND_URL_VALIDATION.md` | FILE AND URL VALIDATION | No | High | GENERALIZE | `controls/security/vcgf-sec-002-file-and-url-validation.md` |
| `01_Input_Validation/INJECTION_DEFENSE_POLICY.md` | INJECTION DEFENSE POLICY | No | High | GENERALIZE | `controls/security/vcgf-sec-003-injection-defense.md` |
| `01_Input_Validation/INPUT_VALIDATION_POLICY.md` | INPUT VALIDATION POLICY | No | High | GENERALIZE | `controls/security/vcgf-sec-004-trusted-layer-input-validation.md` |
| `01_Input_Validation/OUTPUT_ENCODING_SANITIZATION.md` | OUTPUT ENCODING SANITIZATION | No | High | GENERALIZE | `controls/security/vcgf-sec-005-output-encoding-and-sanitization.md` |
| `02_Data_Protection/BACKUP_EXPORT_SECURITY.md` | BACKUP EXPORT SECURITY | No | High | GENERALIZE | `controls/data-protection/vcgf-data-001-backup-and-export-protection.md` |
| `02_Data_Protection/DATA_CLASSIFICATION_RETENTION.md` | DATA CLASSIFICATION RETENTION | No | High | GENERALIZE | `controls/data-protection/vcgf-data-002-data-classification-and-retention.md` |
| `02_Data_Protection/FIELD_LEVEL_ENCRYPTION_POLICY.md` | FIELD LEVEL ENCRYPTION POLICY | No | High | GENERALIZE | `controls/data-protection/vcgf-data-003-field-level-encryption.md` |
| `02_Data_Protection/KEY_MANAGEMENT_ROTATION.md` | KEY MANAGEMENT ROTATION | No | High | GENERALIZE | `controls/data-protection/vcgf-data-004-key-management-and-rotation.md` |
| `02_Data_Protection/LOGGING_REDACTION_PRIVACY.md` | LOGGING REDACTION PRIVACY | No | High | GENERALIZE | `controls/privacy/vcgf-priv-001-logging-redaction-and-privacy.md` |
| `02_Data_Protection/PII_DATA_PROTECTION_POLICY.md` | PII DATA PROTECTION POLICY | No | High | GENERALIZE | `controls/privacy/vcgf-priv-002-personal-data-protection.md` |
| `03_Identity_Access/ACCOUNT_ENUMERATION_BRUTE_FORCE.md` | ACCOUNT ENUMERATION BRUTE FORCE | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-001-enumeration-and-brute-force-resistance.md` |
| `03_Identity_Access/AUTHENTICATION_POLICY.md` | AUTHENTICATION POLICY | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-002-authentication-baseline.md` |
| `03_Identity_Access/MFA_SESSION_SECURITY.md` | MFA SESSION SECURITY | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-003-mfa-and-session-security.md` |
| `03_Identity_Access/PASSWORD_POLICY.md` | PASSWORD POLICY | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-004-password-storage-and-policy.md` |
| `03_Identity_Access/PASSWORD_RESET_RECOVERY_POLICY.md` | PASSWORD RESET RECOVERY POLICY | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-005-secure-password-reset-and-recovery.md` |
| `03_Identity_Access/PRIVILEGED_ACCESS_ADMIN.md` | PRIVILEGED ACCESS ADMIN | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-006-privileged-access-administration.md` |
| `03_Identity_Access/RBAC_ABAC_RLS_POLICY.md` | RBAC ABAC RLS POLICY | No | High | GENERALIZE | `controls/identity-access/vcgf-iam-007-authorization-rbac-abac-and-data-layer-enforcement.md` |
| `04_Backend_API/API_EDGE_FUNCTION_SECURITY.md` | API EDGE FUNCTION SECURITY | No | High | GENERALIZE | `controls/api/vcgf-api-001-api-and-server-function-security.md` |
| `04_Backend_API/BUSINESS_LOGIC_INTEGRITY.md` | BUSINESS LOGIC INTEGRITY | No | High | GENERALIZE | `controls/api/vcgf-api-002-business-logic-integrity.md` |
| `04_Backend_API/MULTITENANCY_ISOLATION.md` | MULTITENANCY ISOLATION | No | High | GENERALIZE | `controls/architecture/vcgf-arch-001-tenant-isolation.md` |
| `04_Backend_API/RATE_LIMITING_ABUSE_PREVENTION.md` | RATE LIMITING ABUSE PREVENTION | No | High | GENERALIZE | `controls/api/vcgf-api-003-rate-limiting-and-abuse-prevention.md` |
| `04_Backend_API/SECURE_ERRORS_LOGGING.md` | SECURE ERRORS LOGGING | No | High | GENERALIZE | `controls/logging-auditing/vcgf-audit-001-secure-errors-and-diagnostic-logging.md` |
| `04_Backend_API/SSRF_CSRF_CORS_WEBHOOKS.md` | SSRF CSRF CORS WEBHOOKS | No | High | GENERALIZE | `controls/api/vcgf-api-004-ssrf-csrf-cors-and-webhook-security.md` |
| `05_Database/DATABASE_CHANGE_POLICY.md` | DATABASE CHANGE POLICY | No | High | GENERALIZE | `controls/database/vcgf-db-001-database-change-governance.md` |
| `05_Database/DATABASE_INTEGRITY_POLICY.md` | DATABASE INTEGRITY POLICY | No | High | GENERALIZE | `controls/database/vcgf-db-002-database-integrity.md` |
| `05_Database/ENCRYPTION_IMPLEMENTATION_GUIDE.md` | ENCRYPTION IMPLEMENTATION GUIDE | No | High | GENERALIZE | `controls/database/vcgf-db-003-database-encryption-implementation.md` |
| `05_Database/RLS_TESTING_POLICY.md` | RLS TESTING POLICY | No | High | GENERALIZE | `controls/database/vcgf-db-004-row-level-authorization-testing.md` |
| `05_Database/SQL_QUERY_SECURITY.md` | SQL QUERY SECURITY | No | High | GENERALIZE | `controls/database/vcgf-db-005-sql-query-security.md` |
| `06_Files_Secrets_SupplyChain/DEPENDENCY_SUPPLY_CHAIN_SECURITY.md` | DEPENDENCY SUPPLY CHAIN SECURITY | No | High | GENERALIZE | `controls/dependencies/vcgf-dep-001-dependency-and-supply-chain-security.md` |
| `06_Files_Secrets_SupplyChain/FILE_UPLOAD_STORAGE_SECURITY.md` | FILE UPLOAD STORAGE SECURITY | No | High | GENERALIZE | `controls/file-handling/vcgf-file-001-file-upload-and-storage-security.md` |
| `06_Files_Secrets_SupplyChain/SECRETS_ENVIRONMENT_POLICY.md` | SECRETS ENVIRONMENT POLICY | No | High | GENERALIZE | `controls/secrets/vcgf-secr-001-secrets-and-environment-protection.md` |
| `06_Files_Secrets_SupplyChain/THIRD_PARTY_INTEGRATION_SECURITY.md` | THIRD PARTY INTEGRATION SECURITY | No | High | GENERALIZE | `controls/api/vcgf-api-005-third-party-integration-security.md` |
| `07_Testing_Assurance/AUTHORIZATION_NEGATIVE_TEST_MATRIX.md` | AUTHORIZATION NEGATIVE TEST MATRIX | No | High | GENERALIZE | `controls/testing/vcgf-test-001-authorization-negative-testing.md` |
| `07_Testing_Assurance/INCIDENT_RESPONSE_MINIMUMS.md` | INCIDENT RESPONSE MINIMUMS | No | High | GENERALIZE | `controls/incident-response/vcgf-ir-001-incident-response-minimums.md` |
| `07_Testing_Assurance/PRE_RELEASE_SECURITY_GATE.md` | PRE RELEASE SECURITY GATE | No | High | GENERALIZE | `controls/release/vcgf-rel-002-pre-release-security-gate.md` |
| `07_Testing_Assurance/SECURE_CODE_REVIEW_CHECKLIST.md` | SECURE CODE REVIEW CHECKLIST | No | High | GENERALIZE | `controls/testing/vcgf-test-002-secure-code-review.md` |
| `07_Testing_Assurance/SECURITY_REGRESSION_CHECKLIST.md` | SECURITY REGRESSION CHECKLIST | No | High | GENERALIZE | `controls/testing/vcgf-test-003-security-regression-review.md` |
| `07_Testing_Assurance/SECURITY_TEST_STRATEGY.md` | SECURITY TEST STRATEGY | No | High | GENERALIZE | `controls/testing/vcgf-test-004-security-test-strategy.md` |
| `08_Prompts/AUTH_PASSWORD_RECOVERY_AUDIT_PROMPT.md` | AUTH PASSWORD RECOVERY AUDIT PROMPT | No | Medium | MOVE | `templates/project-context/prompts/auth-password-recovery-audit-prompt.md` |
| `08_Prompts/CHANGE_IMPACT_ANALYSIS_PROMPT.md` | CHANGE IMPACT ANALYSIS PROMPT | No | Medium | MOVE | `templates/project-context/prompts/change-impact-analysis-prompt.md` |
| `08_Prompts/DEPENDENCY_SUPPLY_CHAIN_AUDIT_PROMPT.md` | DEPENDENCY SUPPLY CHAIN AUDIT PROMPT | No | Medium | MOVE | `templates/project-context/prompts/dependency-supply-chain-audit-prompt.md` |
| `08_Prompts/INITIAL_READ_ONLY_AUDIT_PROMPT.md` | INITIAL READ ONLY AUDIT PROMPT | No | Medium | MOVE | `templates/project-context/prompts/initial-read-only-audit-prompt.md` |
| `08_Prompts/PII_ENCRYPTION_AUDIT_PROMPT.md` | PII ENCRYPTION AUDIT PROMPT | No | Medium | MOVE | `templates/project-context/prompts/pii-encryption-audit-prompt.md` |
| `08_Prompts/PRE_RELEASE_SECURITY_REVIEW_PROMPT.md` | PRE RELEASE SECURITY REVIEW PROMPT | No | Medium | MOVE | `templates/project-context/prompts/pre-release-security-review-prompt.md` |
| `08_Prompts/SAFE_BUGFIX_PROMPT.md` | SAFE BUGFIX PROMPT | No | Medium | MOVE | `templates/project-context/prompts/safe-bugfix-prompt.md` |
| `08_Prompts/SAFE_FEATURE_PROMPT.md` | SAFE FEATURE PROMPT | No | Medium | MOVE | `templates/project-context/prompts/safe-feature-prompt.md` |
| `08_Prompts/VALIDATION_INJECTION_AUDIT_PROMPT.md` | VALIDATION INJECTION AUDIT PROMPT | No | Medium | MOVE | `templates/project-context/prompts/validation-injection-audit-prompt.md` |
| `09_Platform_Adapters/Bolt/BOLT_INSTALLATION_GUIDE.md` | BOLT INSTALLATION GUIDE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/bolt/INSTALLATION.md` |
| `09_Platform_Adapters/Bolt/BOLT_PROJECT_KNOWLEDGE.md` | BOLT PROJECT KNOWLEDGE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/bolt/rules/project-knowledge.md` |
| `09_Platform_Adapters/COMMON/PLATFORM_COMPATIBILITY_MATRIX.md` | PLATFORM COMPATIBILITY MATRIX | Yes | Medium | MOVE-TO-ADAPTER | `docs/platform-compatibility.md` |
| `09_Platform_Adapters/COMMON/PORTABLE_MASTER_PROMPT.md` | PORTABLE MASTER PROMPT | Yes | Medium | MOVE-TO-ADAPTER | `docs/platform-compatibility.md` |
| `09_Platform_Adapters/Claude/CLAUDE_INSTALLATION_GUIDE.md` | CLAUDE INSTALLATION GUIDE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/claude/INSTALLATION.md` |
| `09_Platform_Adapters/Claude/CLAUDE_PROJECT_INSTRUCTIONS.md` | CLAUDE PROJECT INSTRUCTIONS | Yes | Medium | MOVE-TO-ADAPTER | `platforms/claude/rules/CLAUDE.md` |
| `09_Platform_Adapters/Lovable/LOVABLE_INSTALLATION_GUIDE.md` | LOVABLE INSTALLATION GUIDE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/lovable/INSTALLATION.md` |
| `09_Platform_Adapters/Lovable/LOVABLE_PROJECT_KNOWLEDGE.md` | LOVABLE PROJECT KNOWLEDGE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/lovable/rules/project-knowledge.md` |
| `09_Platform_Adapters/Lovable/LOVABLE_WORKSPACE_KNOWLEDGE.md` | LOVABLE WORKSPACE KNOWLEDGE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/lovable/rules/project-knowledge.md` |
| `09_Platform_Adapters/Replit/REPLIT_INSTALLATION_GUIDE.md` | REPLIT INSTALLATION GUIDE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/replit/INSTALLATION.md` |
| `09_Platform_Adapters/v0/V0_INSTALLATION_GUIDE.md` | V0 INSTALLATION GUIDE | Yes | Medium | MOVE-TO-ADAPTER | `platforms/v0/INSTALLATION.md` |
| `09_Platform_Adapters/v0/V0_PROJECT_INSTRUCTIONS.md` | V0 PROJECT INSTRUCTIONS | Yes | Medium | MOVE-TO-ADAPTER | `platforms/v0/rules/custom-instructions.md` |
| `10_Templates/DATA_CLASSIFICATION_TEMPLATE.md` | DATA CLASSIFICATION TEMPLATE | No | Medium | MOVE | `templates/security/data-classification.md` |
| `10_Templates/ENCRYPTION_REGISTER_TEMPLATE.md` | ENCRYPTION REGISTER TEMPLATE | No | Medium | MOVE | `templates/security/encryption-register.md` |
| `10_Templates/FIELD_VALIDATION_MATRIX_TEMPLATE.md` | FIELD VALIDATION MATRIX TEMPLATE | No | Medium | MOVE | `templates/security/field-validation-matrix.md` |
| `10_Templates/PROJECT_SECURITY_PROFILE_TEMPLATE.md` | PROJECT SECURITY PROFILE TEMPLATE | No | Medium | MOVE | `templates/project-context/project-security-profile.md` |
| `10_Templates/REGULATORY_OVERLAY_TEMPLATE.md` | REGULATORY OVERLAY TEMPLATE | No | Medium | MOVE | `templates/project-context/regulatory-overlay.md` |
| `10_Templates/ROLE_PERMISSION_MATRIX_TEMPLATE.md` | ROLE PERMISSION MATRIX TEMPLATE | No | Medium | MOVE | `templates/security/role-permission-matrix.md` |
| `10_Templates/SECURITY_DECISION_RECORD_TEMPLATE.md` | SECURITY DECISION RECORD TEMPLATE | No | Medium | MOVE | `templates/architecture/security-decision-record.md` |
| `10_Templates/SECURITY_EXCEPTION_TEMPLATE.md` | SECURITY EXCEPTION TEMPLATE | No | Medium | MOVE | `templates/security/security-exception.md` |
| `10_Templates/SECURITY_TEST_EVIDENCE_TEMPLATE.md` | SECURITY TEST EVIDENCE TEMPLATE | No | Medium | MOVE | `templates/testing/security-test-evidence.md` |
| `10_Templates/THREAT_MODEL_TEMPLATE.md` | THREAT MODEL TEMPLATE | No | Medium | MOVE | `templates/security/threat-model.md` |
| `11_References/MAPPING_TO_OWASP_ASVS_5.md` | MAPPING TO OWASP ASVS 5 | No | Medium | MOVE | `docs/references/owasp-asvs-5-mapping.md` |
| `11_References/SOURCES_AND_STANDARDS.md` | SOURCES AND STANDARDS | No | Medium | MOVE | `docs/references/sources-and-standards.md` |
| `11_References/TERMINOLOGY.md` | TERMINOLOGY | No | Medium | MOVE | `docs/terminology.md` |
| `12_Operational_Playbooks/EXISTING_PROJECT_HARDENING_PLAN.md` | EXISTING PROJECT HARDENING PLAN | No | Medium | MOVE | `playbooks/existing-project-hardening-plan.md` |
| `12_Operational_Playbooks/KEY_ROTATION_PLAYBOOK.md` | KEY ROTATION PLAYBOOK | No | Medium | MOVE | `playbooks/key-rotation-playbook.md` |
| `12_Operational_Playbooks/NEW_PROJECT_SECURITY_BOOTSTRAP.md` | NEW PROJECT SECURITY BOOTSTRAP | No | Medium | MOVE | `playbooks/new-project-security-bootstrap.md` |
| `12_Operational_Playbooks/PASSWORD_RESET_TEST_CASES.md` | PASSWORD RESET TEST CASES | No | Medium | MOVE | `playbooks/password-reset-test-cases.md` |
| `AGENTS.md` | AGENTS | No | Medium | MOVE | `platforms/generic/rules/portable-project-rules.md` |
| `AUTHOR_AND_RIGHTS.md` | AUTHOR AND RIGHTS | No | Medium | MOVE | `AUTHORS.md` |
| `CHANGELOG.md` | CHANGELOG | No | Medium | MOVE | `CHANGELOG.md` |
| `CLAUDE.md` | CLAUDE | Yes | Medium | MOVE | `platforms/claude/rules/CLAUDE.md` |
| `FILE_MANIFEST.md` | FILE MANIFEST | No | Medium | MOVE | `FILE-MANIFEST.md` |
| `FRAMEWORK_OVERVIEW.md` | FRAMEWORK OVERVIEW | No | Medium | MOVE | `README.md` |
| `LICENSE.md` | LICENSE | No | Medium | MOVE | `LICENSE` |
| `MIGRATION_FROM_V1.md` | MIGRATION FROM V1 | No | Medium | MOVE | `docs/migration-guide.md` |
| `QUICK_START_AR.md` | QUICK START AR | No | Medium | MOVE | `docs/quick-start.ar.md` |
| `README_AR.md` | README AR | No | Medium | MOVE | `README.ar.md` |
| `replit.md` | replit | Yes | Medium | MOVE | `platforms/replit/rules/replit.md` |
