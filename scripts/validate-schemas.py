# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import jsonschema, yaml
from vcgf_lib import *

def main():
    errors=[]
    schemas={}
    for p in sorted((ROOT/'schemas').glob('*.json')):
        try:
            s=load_json(p); jsonschema.Draft202012Validator.check_schema(s); schemas[p.name]=s
        except Exception as e: errors.append(f"{rel(p)}: {e}")
    if 'adapter.schema.json' in schemas:
        v=jsonschema.Draft202012Validator(schemas['adapter.schema.json'])
        for aid in ADAPTER_IDS:
            p=ROOT/'platforms'/aid/'adapter.yaml'; d=load_yaml(p)
            for e in v.iter_errors(d): errors.append(f"{rel(p)}: {e.message}")
    if 'profile.schema.json' in schemas:
        v=jsonschema.Draft202012Validator(schemas['profile.schema.json'])
        for p in (ROOT/'profiles').glob('*/profile.yaml'):
            for e in v.iter_errors(load_yaml(p)): errors.append(f"{rel(p)}: {e.message}")
    cff=load_yaml(ROOT/'CITATION.cff')
    for key in ['cff-version','message','title','authors','version','date-released','license','repository-code']:
        if key not in cff: errors.append(f"CITATION.cff: missing {key}")
    fail_if(errors); print(f"PASS validate-schemas: {len(schemas)} JSON Schemas")
if __name__=='__main__': main()
