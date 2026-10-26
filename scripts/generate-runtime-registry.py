# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from runtime.registry import build_registry
from runtime.contracts import ROOT
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
data=json.dumps(build_registry(),ensure_ascii=False,indent=2,sort_keys=True)+'\n'
target=ROOT/'spec/runtime-registry.json'
if args.check:
    ok=target.exists() and target.read_text(encoding='utf-8').replace('\r\n','\n')==data
    print('PASS registry matches sources' if ok else 'FAIL stale/missing registry');sys.exit(0 if ok else 1)
target.write_text(data,encoding='utf-8',newline='\n');print(target)
