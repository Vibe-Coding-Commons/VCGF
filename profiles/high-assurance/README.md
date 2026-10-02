<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# High Assurance profile

**Profile version:** 1.0.0  
**Framework compatibility:** >=1.0.0 <2.0.0  

Strengthened VCGF profile for sensitive, institutional, regulated, or high-impact systems.

## Required controls

This profile requires **84** controls. The canonical list is `profile.yaml`; this README explains intent and must not be used as a second source of truth.

## Evidence expectation

- Independent or dual-person review for high-risk controls where practical.
- Comprehensive security test evidence, threat model, provenance, monitoring, recovery, and approved exceptions.

## Adoption

Validate the profile with `python scripts/validate-profiles.py`, record exceptions through `spec/exception-management.md`, and use the selected platform adapter only for platform-specific implementation guidance.
