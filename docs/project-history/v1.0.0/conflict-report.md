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

# Conflict Report

## CR-001 - License model

**Source A:** previous v2 file footers used `All Rights Reserved`.  
**Source B:** the VCGF master architecture requires Apache License 2.0 and explicitly distinguishes copyright ownership from license permissions.

**Impact:** retaining All Rights Reserved would conflict with the intended open-source contribution model and Apache-2.0 permissions.

**Resolution:** VCGF 1.0.0 uses Apache-2.0 while retaining Copyright (c) 2026 Eng. Hamada Sami and file-level attribution. Legacy restrictive footer text is not carried into canonical VCGF files.

## CR-002 - Vendor foundation

**Source A:** the historical framework originated around Lovable.  
**Source B:** the VCGF architecture requires a vendor-neutral core.

**Impact:** leaving platform mechanisms in core would prevent independent adapters and create duplicated policy.

**Resolution:** generic requirements are canonical controls; Lovable and every other product are adapters only.

## CR-003 - Signature scope

**Source A:** the architecture prompt requires name/email/GitHub in every file and phone/LinkedIn at least in key files.  
**Current explicit user requirement:** full signature including phone and LinkedIn in every file.

**Resolution:** the stricter current requirement wins. Every generated text/configuration file contains full attribution using format-safe comments or metadata.
