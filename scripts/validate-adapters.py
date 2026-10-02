# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import jsonschema
from vcgf_lib import *

def main():
    schema=load_json(ROOT/"schemas/adapter.schema.json"); validator=jsonschema.Draft202012Validator(schema)
    controls=set(control_index()); errors=[]
    required_files=["README.md","ADAPTER.md","adapter.yaml","control-mapping.yaml","CONTROL-MAPPING.md","CAPABILITIES.md","LIMITATIONS.md","INSTALLATION.md","CHANGELOG.md","verification/sources.yaml","verification/verification-report.md"]
    required_dirs=["rules","prompts","mappings","templates","examples","tests","verification"]
    for aid in sorted(ADAPTER_IDS):
        ad=ROOT/"platforms"/aid
        for f in required_files:
            if not (ad/f).is_file(): errors.append(f"platforms/{aid}: missing {f}")
        for d in required_dirs:
            if not (ad/d).is_dir(): errors.append(f"platforms/{aid}: missing dir {d}")
        if errors and not (ad/"adapter.yaml").exists(): continue
        m=load_yaml(ad/"adapter.yaml")
        for e in validator.iter_errors(m): errors.append(f"platforms/{aid}/adapter.yaml: {e.message}")
        if m.get('adapter_id')!=aid: errors.append(f"platforms/{aid}: adapter_id mismatch")
        src=load_yaml(ad/"verification/sources.yaml") or {}; claims={c.get('id') for c in src.get('claims',[])}
        if m.get('status')=='stable' and m.get('verification_status')!='verified': errors.append(f"platforms/{aid}: stable adapter must be verified")
        if m.get('status')=='stable' and not claims: errors.append(f"platforms/{aid}: stable adapter needs source claims")
        mp=load_yaml(ad/"control-mapping.yaml") or {}; rows=mp.get('mappings',[]); ids=[r.get('control_id') for r in rows]
        if len(ids)!=len(set(ids)): errors.append(f"platforms/{aid}: duplicate mapping control IDs")
        missing=controls-set(ids); extra=set(ids)-controls
        if missing: errors.append(f"platforms/{aid}: missing mappings {sorted(missing)}")
        if extra: errors.append(f"platforms/{aid}: unknown mappings {sorted(extra)}")
        for r in rows:
            if r.get('status') not in ALLOWED_MAPPING: errors.append(f"platforms/{aid}: invalid mapping status {r.get('status')} for {r.get('control_id')}")
            claim=r.get('source_claim')
            if claim and claim not in claims: errors.append(f"platforms/{aid}: mapping {r.get('control_id')} references unknown source claim {claim}")
    # Template must be structurally complete but is not a supported adapter.
    t=ROOT/"platforms/_adapter-template"
    for f in required_files:
        if not (t/f).is_file(): errors.append(f"platforms/_adapter-template: missing {f}")
    fail_if(errors); print(f"PASS validate-adapters: {len(ADAPTER_IDS)} supported adapters")
if __name__=="__main__": main()
