<!--
VCGF | SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0 | Founder & Maintainer: Eng. Hamada Sami | Email: i@hamada.io | GitHub: https://github.com/Vibe-Coding-Commons
-->

# Opt-in VCGF 1.1 contract layer

Historical phase-1 boundary below describes `validate_contract` only. Later `runtime/router.py`, `runtime/approval.py` and `runtime/evidence.py` add separate opt-in behavior; see docs/runtime-guide.md. Contract acceptance alone remains insufficient.

Seven entry contracts (capability, context, route-result, approval, evidence, preferences, adapter-capabilities) plus one shared definitions schema live under schemas/v1.1.0. There are seven instance entry points; common is not an instance contract. They do not replace the four v1.0 schemas. Only contract_version 1.1.0 is accepted by the new validator. The repository VERSION remains 1.0.0 in this intermediate checkpoint.

Use `python scripts/validate-contracts.py NAME FILE.json` with the pinned requirements-dev.txt dependencies. Validation uses local, allowlisted schemas and explicit FormatChecker; it never retrieves schema URLs or executes condition text, test commands, artifact references or approval actions. JSON output and exit status are suitable for local checks: 0 accepted, 1 rejected, 2 input/tool usage error. Accepted means structurally/locally coherent, never tested runtime or conformant project.

Canonical controls/Profiles/mappings remain untouched. Control references are checked against spec/control-catalog.yaml. Names, required evidence references and dates must be coherent. Unknown facts are null with reasons. Conditions have a small declarative vocabulary and are not evaluated in this phase. Graph cycles, fallback resolution, context loading, cost measurement and condition evaluation belong to phase 2.

## Contracts and boundaries

| Contract | Data guaranteed by local validation | Still requires later execution/evidence |
|---|---|---|
| capability | typed dependencies, stable control references, no executable conditions | graph resolution, applicability and provider implementation |
| context | source/hash/timestamps, known vs unknown, independent agent/product flags | verifying source contents and actual freshness at use time |
| route-result | selected/loaded/excluded relationships, inspection reference, reasons, blocked state | generating a route, observing actual load and tokens |
| approval | scoped action/resources/environment/digests, decision identity metadata and ordering | authenticating signer/role, revocation/current validity and preventing the effect |
| evidence | scoped records, known control IDs, artifact/exception links and timestamp ordering | executing tests, validating artifact hashes/content, current freshness, full profile coverage and conformance decision |
| preferences | first-run confirmation flag, language/code convention separation | asking the user and persistent platform storage |
| adapter-capabilities | separate maturity/support/mechanism/test metadata | platform experiment, evidence truth and actual capabilities |

No remote artifacts are fetched. No empty exception or passed control without referenced evidence is accepted. A task may list only affected required controls; required_control_ids is the declared set, not independently inferred. The new validator does NOT yet prove that a release/project declares every required Profile control; conformance claims remain prohibited until the later coverage/evidence gate is implemented. A record with `verification=passed` is a reported result whose truth still requires review; schema acceptance is not a verified result produced by VCGF.

## Compatibility

Legacy records are validated with their original schema and retained as legacy, with missing verification metadata unknown. No automatic PASS conversion or mutation is performed. Frozen fixtures cover all 84 control headers, all three Profiles, all seven Adapters and a synthetic legacy conformance record. Old contract permissiveness is recorded, not silently rewritten. New contracts are explicitly opt-in and versioned; no v1.0 required fields, enums, profiles or IDs are changed.

## Field semantics

Timestamps use an RFC3339 subset with mandatory timezone offsets, no leap seconds and at most six fractional digits. The validator registers an explicit standard-library calendar/offset checker because the optional date-time dependency of jsonschema is not guaranteed by requirements-dev.txt. Invalid dates are rejected even when that optional dependency is absent. Date order is checked relative to the record, not today's clock; expired historical records can be archived but must be rejected as authority by a future current-time enforcement check. `snapshot_id` and hashes are supplied content digests, not signatures. `source.kind=repository` never grants authority. Budget `unavailable` uses null cost, not zero. `profile_selection=proposed` cannot yield ready_to_plan. Support and mechanism are separate from implementation and verification; behavioral support cannot claim technical enforcement. N/A needs a reason and cannot be a passed applicable control. Every evidence record's declared required set must match its control records; deciding whether that declared set is complete for a Profile remains a later phase.

## Future pack acceptance fixed by approval

Before phase 4 begins, record technology/engine/storage/provider versions, environments and tests. Email minimum: Generic SMTP over TLS and Microsoft 365 OAuth 2.0; Graph preferred when appropriate. Real authorized sandbox integrations must supplement mocks. Database and attachments require restore and coordinated consistency proof. Unavailable resources are blockers/Unverified, never success or automatic deferral. D12 requires justified recovery objectives or reasoned N/A for persistent production data, with no unapproved defaults. Discovery/Readiness is a separate planned scope. No live email or costs are authorized by this checkpoint.
