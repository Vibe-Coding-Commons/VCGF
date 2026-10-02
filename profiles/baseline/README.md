<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Baseline profile

**Profile version:** 1.0.0  
**Framework compatibility:** >=1.0.0 <2.0.0  

Minimum VCGF governance for prototypes and low-risk applications.

## Required controls

This profile requires **25** controls. The canonical list is `profile.yaml`; this README explains intent and must not be used as a second source of truth.

## Evidence expectation

- Implementation or review evidence for every required MUST/MUST NOT control.
- Negative-test evidence for authentication, authorization, validation, and injection controls when those capabilities exist.

## Adoption

Validate the profile with `python scripts/validate-profiles.py`, record exceptions through `spec/exception-management.md`, and use the selected platform adapter only for platform-specific implementation guidance.
