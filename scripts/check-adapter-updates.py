# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Compare trusted captured source hashes. No implicit network or support upgrade."""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('previous');p.add_argument('current');args=p.parse_args()
try:
    previous=json.loads(Path(args.previous).read_text());current=json.loads(Path(args.current).read_text())
    changed=[];unavailable=[]
    for source in previous['sources']:
        old=source.get('sha256');new=next((x for x in current['sources'] if x['url']==source['url']),None)
        if not old or not new or new.get('status')!='retrieved' or not new.get('sha256'):unavailable.append(source['url'])
        elif old!=new['sha256']:changed.append(source['url'])
    print(json.dumps({'changed':changed,'unverified':unavailable,'action':'rerun canary for changed or unavailable sources','support_upgraded':False},ensure_ascii=False))
    sys.exit(1 if changed or unavailable else 0)
except (OSError,ValueError,KeyError):
    print('{"status":"input_error"}');sys.exit(2)
