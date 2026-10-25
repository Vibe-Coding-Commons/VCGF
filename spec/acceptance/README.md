<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Control acceptance tests

One YAML file per control domain (`<domain>.yaml`) defines the acceptance tests that prove a control is satisfied in a target project. Control Markdown remains the normative text; these files add **verifiable** criteria, the method, the evidence and the automation hook. `scripts/validate-acceptance.py` enforces the format and completeness, and `scripts/vcgf.py acceptance <control-id>` shows the tests for a control.

## Format

```yaml
# SPDX header as in other YAML files
acceptance_version: 1.0.0
domain: identity-access            # must match the file name and the controls' domain
controls:
  VCGF-IAM-005:
    requirement_sources: [S17, S16]  # optional: requirement pack sections (S14..S39) or Smart UI standard IDs (VCGF-UI-*)
    tests:
      - id: VCGF-IAM-005-AT01        # <control id>-AT<two digits>, unique
        type: automated              # automated | manual | review
        criterion: >-                # ONE measurable statement specific to this control (not boilerplate)
          Requesting a reset for an unknown and a known account returns byte-identical responses
          and response times within 10 percent of each other over 50 samples.
        method: >-                   # how a reviewer or tool checks it
          Integration test issues 50 reset requests for each case and compares bodies, status codes and timing.
        negative_path: true          # does this test exercise a denied/failure/abuse path?
        evidence: [test-result]      # allowed: test-result, code-review, configuration-record, security-scan,
                                     #          migration-review, manual-verification, screenshot, log-sample,
                                     #          threat-model, inventory, approval-record, release-checksum
        automation:
          kind: ci                   # none | script | validator | hook | ci
          reference: tests/security/test_password_reset.py::test_enumeration_resistance
```

## Rules enforced by the validator

1. Every control in `spec/control-catalog.yaml` appears in exactly one domain file with **at least two** tests.
2. At least one test per control is `automated` or `review`; security, identity, data, database, API and file controls need at least one `negative_path: true` test.
3. `criterion` is specific: minimum 60 characters, must not be identical to another control's criterion, and must not consist only of the generic template phrases.
4. Test IDs follow `<control id>-AT\d\d` and are unique across all files.
5. `type`, `evidence` and `automation.kind` use the enumerations above; `automation.reference` is required unless `kind: none`.
6. `requirement_sources` entries must be known pack sections (`S14`…`S39` from `packs/index.yaml`) or Smart UI standard IDs (`VCGF-UI-COMP-###`, `VCGF-UI-INT-###`, `VCGF-UI-SCR-###`, `VCGF-UI-JRN-###`, or the two bound standards `CALENDAR-GOVERNANCE-ADDENDUM`, `UI-COMP-SEARCHABLE-SELECT`).
7. User-experience controls must reference at least one Smart UI standard.

## What these tests are and are not

They define **what a project must demonstrate**, with a method and evidence type, so that an evidence record can cite them (`evidence_refs`). They do not execute inside this repository; executing them is the target project's responsibility, and the VCGF evidence gate records whether they passed, failed or were not run.
