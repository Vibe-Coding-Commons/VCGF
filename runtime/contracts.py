# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Offline structural/local coherence checks. Acceptance is not authorization.

No conditions, commands, network references or artifact contents are executed.
Current-time evidence freshness, complete Profile coverage, graph resolution and
identity verification are intentionally outside this phase-1 boundary.
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "v1.1.0"
NAMES = frozenset({"capability", "context", "route-result", "approval", "evidence",
                   "preferences", "adapter-capabilities"})
FORMATS = FormatChecker()


@FORMATS.checks("date-time", raises=(ValueError, TypeError))
def _strict_timestamp(value):
    """Require timezone-aware calendar time without optional format dependencies.

    The contract uses an RFC3339 subset: no leap seconds, at most six fractional
    digits. A null value is handled by the surrounding schema's type constraint.
    """
    if not isinstance(value, str):
        return True
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}"
                        r"(?:\.\d{1,6})?(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)", value):
        return False
    return datetime.fromisoformat(value.upper().replace("Z", "+00:00")).tzinfo is not None


def _offline_only(uri):
    raise ValueError("Schema retrieval outside the local registry is forbidden")


def load_schemas():
    # Content-keyed cache: edits invalidate it even on coarse timestamp filesystems.
    sources = tuple((p.name, p.read_text(encoding="utf-8")) for p in sorted(SCHEMAS.glob("*.schema.json")))
    documents, registry = _checked_schemas(sources)
    return deepcopy(documents), registry


@lru_cache(maxsize=4)
def _checked_schemas(sources):
    documents = {}
    registry = Registry(retrieve=_offline_only)
    for name, content in sources:
        schema = json.loads(content)
        Draft202012Validator.check_schema(schema)
        documents[name.removesuffix(".schema.json")] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    return documents, registry


def _date(value):
    return datetime.fromisoformat(value.upper().replace("Z", "+00:00"))


def validate_contract(name: str, record: object) -> list[str]:
    if name not in NAMES:
        return ["Unknown contract name; use an explicit supported entry contract"]
    schemas, registry = load_schemas()
    validator = Draft202012Validator(schemas[name], registry=registry,
                                    format_checker=FORMATS)
    errors = sorted((f"{e.json_path}: {e.message}" for e in validator.iter_errors(record)))
    if errors:
        return errors
    # Schema acceptance above guarantees the shapes accessed below.
    catalog = yaml.safe_load((ROOT / "spec" / "control-catalog.yaml").read_text(encoding="utf-8"))
    known_controls = {row["id"] for row in catalog["controls"]}
    control_lists = {"control_ids", "required_control_ids", "selected_control_ids", "loaded_control_ids"}

    def walk(value, path="$"):
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "control_id" and item not in known_controls:
                    errors.append(f"{path}.{key}: unknown canonical control")
                if key in control_lists:
                    for cid in item:
                        if cid not in known_controls:
                            errors.append(f"{path}.{key}: unknown canonical control {cid}")
                walk(item, path + "." + key)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                walk(item, f"{path}[{i}]")
    # Do not interpret arbitrary context fact payloads as VCGF control metadata.
    if name == "context":
        walk({k: v for k, v in record.items() if k != "facts"})
    else:
        walk(record)

    def unique(rows, key, label):
        values = [r[key] for r in rows]
        if len(values) != len(set(values)):
            errors.append(label + ": duplicate logical identifier")

    def order(start, end, label, strict=False):
        left, right = _date(start), _date(end)
        if (left >= right) if strict else (left > right):
            errors.append(label + ": invalid timestamp ordering")

    if name == "capability":
        conditions = list(record["applicability"]["conditions"])
        conditions.extend(d["condition"] for d in record["dependencies"] if "condition" in d)
        for c in conditions:
            if c["operator"] == "exists" and "value" in c:
                errors.append("exists condition must not have a value")
            if c["operator"] != "exists" and "value" not in c:
                errors.append("comparison condition requires a value")
    elif name == "context":
        unique(record["facts"], "key", "facts")
        for fact in record["facts"]:
            order(fact["observed_at"], fact["expires_at"], "fact validity", strict=True)
    elif name == "route-result":
        selected, loaded = set(record["selected_control_ids"]), set(record["loaded_control_ids"])
        unique(record["excluded"], "control_id", "excluded")
        excluded = {x["control_id"] for x in record["excluded"]}
        if not loaded <= selected:
            errors.append("loaded controls must be selected")
        if excluded & selected:
            errors.append("a control cannot be selected and excluded")
        explained = {x["control_id"] for x in record["reasons"]}
        if explained != selected:
            errors.append("every selected control needs a reason; no unrelated reasons")
        b = record["budget"]
        if (b["measurement"] == "unavailable") != (b["cost_tokens"] is None):
            errors.append("unavailable cost must be null; observed/estimated require a number")
        if record["decision"] == "ready_to_plan":
            if loaded != selected:
                errors.append("ready_to_plan cannot omit selected controls from loaded set")
            if b["cost_tokens"] is not None and b["cost_tokens"] > b["limit_tokens"]:
                errors.append("over-budget route must be blocked until split/budget decision")
        if record["risk"] in {"HIGH", "CRITICAL"} and not record["approval_required"]:
            errors.append("HIGH/CRITICAL route cannot suppress required approval")
    elif name == "approval":
        order(record["issued_at"], record["expires_at"], "approval validity", strict=True)
        if "decision_at" in record:
            order(record["issued_at"], record["decision_at"], "decision after request")
            order(record["decision_at"], record["expires_at"], "decision before expiry", strict=True)
        if record["status"] == "approved":
            if record["requested_by"] == record["decision_by"]["subject"]:
                errors.append("requester cannot self-approve this contract")
            if record["environment"] == "unknown":
                errors.append("approved action requires a known environment")
    elif name == "evidence":
        unique(record["controls"], "control_id", "controls")
        unique(record["artifacts"], "artifact_id", "artifacts")
        unique(record["exceptions"], "exception_id", "exceptions")
        if set(record["required_control_ids"]) != {c["control_id"] for c in record["controls"]}:
            errors.append("control records must exactly cover the DECLARED required set")
        artifacts = {a["artifact_id"]: a for a in record["artifacts"]}
        exceptions = {e["exception_id"]: e for e in record["exceptions"]}
        order(record["created_at"], record["valid_until"], "evidence validity", strict=True)
        order(record["created_at"], record["reviewer"]["reviewed_at"], "review date")
        order(record["created_at"], record["privacy"]["retention_until"], "retention", strict=True)
        for artifact in artifacts.values():
            order(artifact["created_at"], record["created_at"], "artifact date")
            if artifact["kind"] == "test":
                test = artifact["test"]
                if (test["result"] == "passed") != (test["exit_code"] == 0):
                    errors.append("test result contradicts exit code")
        for control in record["controls"]:
            for aid in control["evidence_refs"]:
                if aid not in artifacts:
                    errors.append("control references missing evidence artifact")
                elif control["verification"] == "passed" and artifacts[aid].get("test", {}).get("result") == "failed":
                    errors.append("passed control cannot cite a failed test as passing evidence")
            if "exception_ref" in control:
                e = exceptions.get(control["exception_ref"])
                if e is None or e["control_id"] != control["control_id"]:
                    errors.append("exception link missing or for a different control")
                elif e["status"] != "approved":
                    errors.append("a control cannot rely on an unapproved exception")
        for e in exceptions.values():
            order(e["created_at"], e["expires_at"], "exception validity", strict=True)
            order(e["created_at"], e["review_at"], "exception review")
            order(e["review_at"], e["expires_at"], "exception review expiry")
    elif name == "adapter-capabilities":
        unique(record["capabilities"], "capability_id", "capabilities")
        mechanism_for = {"native": {"technical"}, "configurable": {"technical", "external"},
                         "behavioral": {"behavioral"}, "external": {"external"},
                         "unsupported": {"unsupported"}, "unverified": {"unverified"},
                         "partial": {"technical", "behavioral", "external"},
                         "not_applicable": {"unsupported"}}
        for cap in record["capabilities"]:
            if cap["mechanism"] not in mechanism_for[cap["support"]]:
                errors.append("support/mechanism mismatch")
            if cap["verified_at"] is not None:
                order(cap["verified_at"], record["assessed_at"], "adapter verification date")
    return sorted(set(errors))
