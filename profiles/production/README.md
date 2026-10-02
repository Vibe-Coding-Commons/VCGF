<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Production profile

**Profile version:** 1.0.0  
**Framework compatibility:** >=1.0.0 <2.0.0  

VCGF profile for production applications handling real users, business data, or internet-facing services.

## Required controls

This profile requires **77** controls. The canonical list is `profile.yaml`; this README explains intent and must not be used as a second source of truth.

## Evidence expectation

- Automated test or equivalent reproducible evidence for required security controls.
- Release-gate evidence, threat model, dependency inventory, and operational monitoring evidence where applicable.

## Adoption

Validate the profile with `python scripts/validate-profiles.py`, record exceptions through `spec/exception-management.md`, and use the selected platform adapter only for platform-specific implementation guidance.
