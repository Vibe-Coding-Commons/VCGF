# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Synthetic contract tests, not platform or application security verification."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from runtime.contracts import NAMES, validate_contract, load_schemas, _offline_only


def fixture(name):
    return json.loads((ROOT / "tests/fixtures/v1.1" / (name + ".json")).read_text())["record"]


def put(path, value):
    def mutate(record):
        at = record
        for key in path[:-1]:
            at = at[key]
        at[path[-1]] = value
    return mutate


def delete(path):
    def mutate(record):
        at = record
        for key in path[:-1]:
            at = at[key]
        del at[path[-1]]
    return mutate


class ContractTests(unittest.TestCase):
    def test_all_local_schemas_are_valid(self):
        docs, _ = load_schemas()
        self.assertEqual(set(docs), set(NAMES) | {"common"})

    def test_remote_schema_resolution_is_denied(self):
        with self.assertRaises(ValueError):
            _offline_only("https://untrusted.example/schema")

    def test_unknown_contract_name_rejected(self):
        self.assertTrue(validate_contract("../../other", {}))

    def test_context_arbitrary_fact_data_not_interpreted_as_controls(self):
        record = fixture("context")
        record["facts"][0]["value"] = {"control_id": "customer-business-field"}
        self.assertEqual(validate_contract("context", record), [])

    def test_lowercase_rfc3339_is_accepted(self):
        record = fixture("approval")
        record["issued_at"] = record["issued_at"].lower()
        self.assertEqual(validate_contract("approval", record), [])

    def test_blocked_route_preserves_missing_context(self):
        record = fixture("route-result")
        record.update(decision="blocked", loaded_control_ids=[], blockers=["Context unavailable"])
        self.assertEqual(validate_contract("route-result", record), [])

    def test_unknown_fact_is_not_false(self):
        record = fixture("context")
        record["facts"][0].update(state="unknown", value=None, reason="Inspection needed")
        self.assertEqual(validate_contract("context", record), [])

    def test_unknown_evidence_not_claimed_as_pass(self):
        record = fixture("evidence")
        record["controls"][0].update(applicability="unknown", implementation="unknown",
                                     verification="not_run", evidence_refs=[], reason="Not inspected")
        self.assertEqual(validate_contract("evidence", record), [])

    def test_na_reasoned_record_can_be_archived(self):
        record = fixture("evidence")
        record["controls"][0].update(applicability="not_applicable", support="not_applicable",
                                     verification="not_run", evidence_refs=[], reason="Synthetic N/A")
        self.assertEqual(validate_contract("evidence", record), [])

    def test_commands_are_data_not_executed(self):
        record = fixture("evidence")
        record["artifacts"][0]["test"]["command"] = "FORBIDDEN command text"
        with patch("subprocess.run", side_effect=AssertionError("No execution allowed")):
            self.assertEqual(validate_contract("evidence", record), [])

    def test_current_time_authority_is_not_claimed(self):
        # A historical record remains serializable; no permission to act follows.
        record = fixture("approval")
        for key in ["issued_at", "expires_at", "decision_at"]:
            record[key] = record[key].replace("2026", "2020")
        self.assertEqual(validate_contract("approval", record), [])

    def test_no_automatic_project_conformance_inference(self):
        record = fixture("evidence")
        record["scope"]["kind"] = "project"
        self.assertEqual(validate_contract("evidence", record), [])
        self.assertNotIn("conformant", record)
        # Completeness against Profile and evidence truth is a future gate.

    def test_cli_exit_codes_and_no_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "record.json"
            p.write_text(json.dumps(fixture("capability")))
            before = p.read_bytes()
            run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate-contracts.py"),
                                  "capability", str(p)], text=True, capture_output=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["claim"], "structural_and_local_coherence_only")
            self.assertEqual(p.read_bytes(), before)
            p.write_text('{"contract_version":"1.1.0"}')
            run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate-contracts.py"),
                                  "capability", str(p)], text=True, capture_output=True)
            self.assertEqual(run.returncode, 1, run.stderr)
            p.write_text('{malformed')
            run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate-contracts.py"),
                                  "capability", str(p)], text=True, capture_output=True)
            self.assertEqual(run.returncode, 2, run.stderr)


NEGATIVE = [
    ("capability", "unknown_control", put(["control_ids"], ["VCGF-IAM-" + "999"])),
    ("capability", "missing_condition", put(["dependencies", 0, "relation"], "requires_when")),
    ("capability", "empty_any_of", put(["dependencies", 0], {"relation": "any_of", "targets": [], "reason": "Alternatives"})),
    ("capability", "unknown_relation", put(["dependencies", 0, "relation"], "exec")),
    ("capability", "nondeclarative_operator", put(["applicability", "conditions"], [{"fact": "auth", "operator": "eval", "value": "code"}])),
    ("capability", "condition_missing_value", put(["applicability", "conditions"], [{"fact": "auth", "operator": "equals"}])),
    ("capability", "exists_with_value", put(["applicability", "conditions"], [{"fact": "auth", "operator": "exists", "value": True}])),
    ("capability", "plural_requires", put(["dependencies", 0, "targets"], ["audit", "email"])),
    ("preferences", "code_conventions_changed", put(["code_language_behavior"], "translate_identifiers")),
    ("preferences", "invalid_language", put(["interaction_language"], "made-up")),
    ("preferences", "invalid_timestamp", put(["updated_at"], "not-a-date")),
    ("preferences", "impossible_calendar_date", put(["updated_at"], "2026-02-30T12:00:00Z")),
    ("preferences", "timezone_required", put(["updated_at"], "2026-10-03T12:00:00")),
    ("preferences", "invalid_timezone_offset", put(["updated_at"], "2026-10-03T12:00:00+25:00")),
    ("context", "unknown_has_invented_value", put(["facts", 0, "state"], "unknown")),
    ("context", "known_null", put(["facts", 0, "value"], None)),
    ("context", "missing_provenance", delete(["facts", 0, "source"])),
    ("context", "invalid_hash", put(["facts", 0, "source", "content_sha256"], "wrong")),
    ("context", "reversed_expiry", put(["facts", 0, "expires_at"], "2020-01-01T00:00:00Z")),
    ("context", "duplicate_fact", lambda r: r["facts"].append(copy.deepcopy(r["facts"][0]))),
    ("context", "secret_handoff", put(["handoff", "secrets_included"], True)),
    ("route-result", "missing_selected_load", put(["loaded_control_ids"], [])),
    ("route-result", "unselected_loaded", put(["loaded_control_ids"], ["VCGF-GOV-002"])),
    ("route-result", "excluded_selected", put(["excluded"], [{"control_id": "VCGF-GOV-001", "reason": "Wrong exclusion"}])),
    ("route-result", "unexplained_selection", put(["reasons"], [])),
    ("route-result", "unavailable_zero", put(["budget", "cost_tokens"], 0)),
    ("route-result", "estimated_null", put(["budget", "measurement"], "estimated")),
    ("route-result", "uninspected_ready", put(["inspection", "completed"], False)),
    ("route-result", "proposed_profile_ready", put(["profile_selection"], "proposed")),
    ("route-result", "high_without_approval", put(["risk"], "HIGH")),
    ("route-result", "empty_blocked_reason", put(["decision"], "blocked")),
    ("route-result", "over_budget", lambda r: r["budget"].update(measurement="estimated", cost_tokens=3000)),
    ("approval", "reversed_validity", put(["expires_at"], "2020-01-01T00:00:00Z")),
    ("approval", "self_approval", put(["decision_by", "subject"], "fixture-agent")),
    ("approval", "unknown_environment", put(["environment"], "unknown")),
    ("approval", "missing_authority_evidence", delete(["decision_by", "authority_evidence"])),
    ("approval", "missing_scope_digest", delete(["action_sha256"])),
    ("approval", "decision_after_expiry", put(["decision_at"], "2027-01-01T00:00:00Z")),
    ("evidence", "empty_controls", put(["controls"], [])),
    ("evidence", "empty_required_set", put(["required_control_ids"], [])),
    ("evidence", "unknown_pass_control", put(["controls", 0, "control_id"], "VCGF-IAM-" + "999")),
    ("evidence", "passed_without_evidence", put(["controls", 0, "evidence_refs"], [])),
    ("evidence", "empty_exception", put(["exceptions"], [{}])),
    ("evidence", "invalid_date", put(["created_at"], "not-a-date")),
    ("evidence", "missing_artifact", put(["controls", 0, "evidence_refs"], ["missing"])),
    ("evidence", "declared_missing_control", put(["required_control_ids"], ["VCGF-GOV-001", "VCGF-GOV-002"])),
    ("evidence", "na_without_reason", lambda r: r["controls"][0].update(applicability="not_applicable", support="not_applicable", verification="not_run")),
    ("evidence", "unsupported_pass", put(["controls", 0, "support"], "unsupported")),
    ("evidence", "not_implemented_pass", put(["controls", 0, "implementation"], "not_implemented")),
    ("evidence", "contradictory_exit", put(["artifacts", 0, "test", "exit_code"], 1)),
    ("evidence", "future_artifact", put(["artifacts", 0, "created_at"], "2027-01-01T00:00:00Z")),
    ("evidence", "secret_flag", put(["privacy", "secrets_included"], True)),
    ("evidence", "duplicate_control", lambda r: r["controls"].append(dict(r["controls"][0], reason="duplicate"))),
    ("evidence", "unresolved_exception", put(["controls", 0, "exception_ref"], "absent")),
    ("evidence", "extra_conformance_claim", put(["conformant"], True)),
    ("adapter-capabilities", "behavioral_as_technical", lambda r: r["capabilities"][0].update(support="behavioral", mechanism="technical")),
    ("adapter-capabilities", "passed_without_test", put(["capabilities", 0, "verification"], "passed")),
    ("adapter-capabilities", "stable_untested", put(["maturity"], "stable")),
    ("adapter-capabilities", "native_as_external", put(["capabilities", 0, "support"], "native")),
]


def negative_test(name, mutation):
    def test(self):
        record = fixture(name)
        mutation(record)
        self.assertTrue(validate_contract(name, record), f"Expected rejection of {record}")
    return test


for name, label, mutation in NEGATIVE:
    setattr(ContractTests, "test_reject_" + name.replace("-", "_") + "_" + label,
            negative_test(name, mutation))

for name in sorted(NAMES):
    def positive(self, name=name):
        self.assertEqual(validate_contract(name, fixture(name)), [])
    setattr(ContractTests, "test_accept_" + name.replace("-", "_"), positive)
    setattr(ContractTests, "test_reject_version_" + name.replace("-", "_"),
            negative_test(name, put(["contract_version"], "1.0.0")))
    setattr(ContractTests, "test_reject_unknown_field_" + name.replace("-", "_"),
            negative_test(name, put(["unapproved_extension"], True)))


class CompatibilityTests(unittest.TestCase):
    def test_baseline_preserved_except_approved_documentation(self):
        snapshot = json.loads((ROOT / "tests/fixtures/v1.0/baseline-hashes.json").read_text())["files"]
        self.assertEqual(len(snapshot), 383)
        approval = json.loads((ROOT / "docs/project-history/v1.1.0/documentation-approval.json").read_text())
        allowed = approval["allowed_original_documentation_changes"]
        self.assertEqual(set(allowed), {"README.md", "README.ar.md", "CHANGELOG.md"})
        for name, digest in snapshot.items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), allowed.get(name, digest))

    def test_frozen_v1_schemas_identical(self):
        for p in (ROOT / "tests/fixtures/v1.0/schemas").glob("*.json"):
            self.assertEqual(p.read_bytes(), (ROOT / "schemas" / p.name).read_bytes())

    def test_95_legacy_records_still_accepted(self):
        records = json.loads((ROOT / "tests/fixtures/v1.0/records.json").read_text())["records"]
        count = 0
        for key, name in [("controls", "control"), ("profiles", "profile"), ("adapters", "adapter"), ("conformance", "conformance")]:
            schema = json.loads((ROOT / "schemas" / (name + ".schema.json")).read_text())
            validator = Draft202012Validator(schema)
            values = [records[key]] if key == "conformance" else records[key]
            for record in values:
                with self.subTest(schema=name, record=record.get("id", record.get("adapter_id"))):
                    self.assertEqual(list(validator.iter_errors(record)), [])
                count += 1
        self.assertEqual(count, 95)

    def test_legacy_permissiveness_not_silently_rewritten(self):
        schema = json.loads((ROOT / "schemas/conformance.schema.json").read_text())
        record = json.loads((ROOT / "tests/fixtures/v1.0/records.json").read_text())["records"]["conformance"]
        record["controls"] = []
        self.assertTrue(Draft202012Validator(schema).is_valid(record))


if __name__ == "__main__":
    unittest.main(verbosity=2)
