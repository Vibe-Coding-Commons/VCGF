<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED by scripts/generate-control-cards.py from controls/; do not edit -->
# Common control clauses
Shared verbatim by five or more controls. A control card cites the variant letter that applies to it; the full control text is normative.

## Applicability [A]
Apply when the project or change contains the relevant capability, data, trust boundary, or risk. Profile requirements may strengthen applicability.

## Applicability [B]
Apply according to project risk, selected profile, and affected trust boundaries.

## Applicability [C]
Apply according to the selected VCGF profile and whenever the capability or risk described by this control is present.

## Verification Method [A]
Inspect implementation and configuration, execute positive and negative tests appropriate to the control, and review evidence at the trusted enforcement layer.

## Verification Method [B]
Review the change, applicable configuration, test evidence, approval record, and platform mapping.

## Verification Method [C]
Inspect the relevant design, implementation, configuration, and evidence; run positive and negative tests where applicable; confirm that the control is enforced at a trusted layer.

## Required Evidence [A]
At least one reproducible artifact such as a test result, code review, configuration record, security scan, migration review, or manual verification record.

## Required Evidence [B]
A reproducible review, test, configuration record, or approval artifact appropriate to the control.

## Required Evidence [C]
A reproducible artifact such as a threat model, generated inventory, policy configuration, CI result, alert test, signed provenance record, review record, or release checksum, depending on the control.

## Exceptions [A]
Use the VCGF exception process. Exceptions must be risk-owned, approved, time-bounded, and accompanied by compensating controls.

## Exceptions [B]
Exceptions follow `spec/exception-management.md`.

## Exceptions [C]
Use the VCGF exception-management process. Exceptions must identify risk, owner, compensating controls, approval, expiry, and review date.

## Dependencies [A]
VCGF-GOV-001, VCGF-GOV-004, and applicable architecture or identity controls.

## Dependencies [B]
VCGF-GOV-001 and VCGF-GOV-004 where applicable.

## Dependencies [C]
VCGF-GOV-001, VCGF-GOV-002, VCGF-GOV-004, and the applicable security or architecture controls.

## Related Controls [A]
See the domain index and selected profile.

## Related Controls [B]
See the selected profile and control catalog.

## Related Controls [C]
See the selected profile and domain index for related requirements.

## Platform Considerations [A]
Platform-specific implementation belongs in `platforms/<adapter>/mappings/`. This control does not assume a vendor capability.

## Platform Considerations [B]
Adapters may classify enforcement as native, configurable, prompt-enforced, external, partial, unsupported, not-applicable, or unverified.

## Platform Considerations [C]
Platform adapters may identify native or configurable implementation surfaces. The normative requirement remains platform-independent.
