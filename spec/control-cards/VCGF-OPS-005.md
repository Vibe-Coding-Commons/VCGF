<!-- SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | DERIVED control card; normative text: controls/operations/vcgf-ops-005-security-monitoring-and-alerting.md -->
# VCGF-OPS-005 — Security Monitoring and Alerting
MUST · operations · profiles: high-assurance, production · full text: controls/operations/vcgf-ops-005-security-monitoring-and-alerting.md

## Requirement
Production and high-assurance systems MUST monitor security-relevant events and define actionable alerting for events whose timely detection materially reduces risk.

## Guidance
Monitoring should cover authentication abuse, privileged actions, repeated authorization failures, secret/key incidents, suspicious API or file activity, integrity failures, and security-control degradation where applicable. Alerts need an owner, severity, routing path, suppression strategy, and response playbook. Monitoring data must follow privacy and log-redaction controls.

Common clauses (spec/control-cards/common-clauses.md): Applicability[C] Verification[C] Evidence[C] Exceptions[C] Dependencies[C] Related[C] Platform[C]
