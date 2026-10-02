# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import jsonschema
from vcgf_lib import *

def main():
    schema=load_json(ROOT/"schemas/profile.schema.json"); validator=jsonschema.Draft202012Validator(schema)
    controls=control_index(); errors=[]; memberships={cid:set() for cid in controls}
    for pp in sorted((ROOT/"profiles").glob("*/profile.yaml")):
        d=load_yaml(pp)
        for e in validator.iter_errors(d): errors.append(f"{rel(pp)}: {e.message}")
        if d.get("profile_id") != pp.parent.name: errors.append(f"{rel(pp)}: profile_id mismatch")
        req=d.get("required_controls",[])
        if len(req)!=len(set(req)): errors.append(f"{rel(pp)}: duplicate required controls")
        for cid in req:
            if cid not in controls: errors.append(f"{rel(pp)}: unknown control {cid}")
            else: memberships[cid].add(d['profile_id'])
        for cid in d.get("optional_controls",[]):
            if cid not in controls: errors.append(f"{rel(pp)}: unknown optional control {cid}")
        overlap=set(req)&set(d.get("optional_controls",[]))
        if overlap: errors.append(f"{rel(pp)}: required/optional overlap {sorted(overlap)}")
    for cid,p in controls.items():
        meta,_=parse_frontmatter(p)
        if set(meta.get('profiles',[])) != memberships[cid]: errors.append(f"{rel(p)}: front-matter profiles {meta.get('profiles',[])} != canonical profile membership {sorted(memberships[cid])}")
    fail_if(errors); print("PASS validate-profiles")
if __name__=="__main__": main()
