#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'manifest.json','SHA256SUMS.txt'}
entries=[]
# Sort by POSIX path parts so the manifest is byte-identical on case-insensitive file systems (Windows).
for p in sorted((q for q in ROOT.rglob('*') if q.is_file() and '__pycache__' not in q.parts),key=lambda q:q.relative_to(ROOT).parts):
    rel=p.relative_to(ROOT).as_posix()
    if rel in EXCLUDED:continue
    entries.append({'path':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'package':'VCGF Smart UI, Interaction, Screen & Journey Standards','package_version':'1.0.0','target_framework':'VCGF 1.3.0 development','status':'final-integration-candidate','hash_algorithm':'sha256','exclusions':sorted(EXCLUDED),'files':entries}
p=ROOT/'manifest.json';p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
sums=[e['sha256']+'  '+e['path'] for e in entries];sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  manifest.json')
(ROOT/'SHA256SUMS.txt').write_text('\n'.join(sums)+'\n',encoding='utf-8',newline='\n')
print('Wrote manifest for',len(entries),'files; checksum list includes manifest.json.')
