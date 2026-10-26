# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from pathlib import Path
import re, jsonschema
from vcgf_lib import *

def main():
    # Current contract (v1.4.0 superset) for every control; the frozen v1.0 contract must still accept every v1.0 control.
    schema=load_json(ROOT/"schemas/v1.4.0/control.schema.json")
    validator=jsonschema.Draft202012Validator(schema)
    frozen=jsonschema.Draft202012Validator(load_json(ROOT/"schemas/control.schema.json"))
    errors=[]; seen=set(); required_sections=["Requirement","Purpose","Risk Addressed","Rationale","Applicability","Implementation-Neutral Guidance","Verification Method","Required Evidence","Exceptions","Dependencies","Related Controls","References","Platform Considerations","Change History"]
    for p in control_files():
        try: meta,body=parse_frontmatter(p)
        except Exception as e: errors.append(e); continue
        cid=meta.get("id")
        if cid in seen: errors.append(f"duplicate ID: {cid}")
        seen.add(cid)
        for e in validator.iter_errors(meta): errors.append(f"{rel(p)}: schema: {e.message}")
        if meta.get("framework_version_introduced")=="1.0.0":
            for e in frozen.iter_errors(meta): errors.append(f"{rel(p)}: frozen v1.0 schema: {e.message}")
        if meta.get("domain") != p.parent.name: errors.append(f"{rel(p)}: domain does not match folder")
        if not p.name.startswith(str(cid).lower()+"-"): errors.append(f"{rel(p)}: filename must start with lower-case control ID")
        if f"# {cid} -" not in body: errors.append(f"{rel(p)}: visible title does not match control ID")
        for section in required_sections:
            if f"## {section}" not in body: errors.append(f"{rel(p)}: missing section {section}")
        if ("VCGF-" + "SEC-SECRET-") in body or ("VCGF-" + "SEC-SECRET-") in str(meta): errors.append(f"{rel(p)}: legacy secrets ID remains")
    v10=sum(1 for p in control_files() if parse_frontmatter(p)[0].get("framework_version_introduced")=="1.0.0")
    if v10 != 84: errors.append(f"expected the 84 immutable v1.0.0 controls; found {v10}")
    if len(seen) < 84: errors.append(f"expected at least 84 controls; found {len(seen)}")
    fail_if(errors)
    print(f"PASS validate-controls: {len(seen)} controls")
if __name__=="__main__": main()
