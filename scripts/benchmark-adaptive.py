# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Reproducible local microbenchmark; not a production concurrency benchmark."""
import argparse
import hashlib
import json
import os
import platform
import statistics
import sys
import tempfile
import time
import tracemalloc
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from runtime.adaptive.coordinator import plan
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);p.add_argument('--iterations',type=int,default=100);a=p.parse_args()
if not 10<=a.iterations<=1000: p.error('iterations must be 10..1000')
now=datetime.now(timezone.utc)
fp=json.loads((ROOT/'examples/adaptive/fingerprint-laravel.json').read_text(encoding='utf-8'))
ux=json.loads((ROOT/'examples/adaptive/ux-crm.json').read_text(encoding='utf-8'))
with tempfile.TemporaryDirectory() as root:
    source=b'Synthetic bounded benchmark product brief. Not a live application.\n'
    Path(root,'brief.md').write_bytes(source);h=hashlib.sha256(source).hexdigest()
    for record in [fp,ux]:record.update(project_id='synthetic-benchmark',captured_at=now.isoformat())
    fp['sources']=[{'path':'brief.md','sha256':h,'kind':'local_file'}]
    ux['source_refs']=[{'ref':'brief.md','sha256':h,'kind':'product_document','confidence':'reported'}]
    def execute(_=None):return plan(fp,ux,Path(root),now=now)
    t=time.perf_counter();cold=execute();cold_ms=(time.perf_counter()-t)*1000
    samples=[]
    for _ in range(a.iterations):
        t=time.perf_counter();result=execute();samples.append((time.perf_counter()-t)*1000)
        assert result['state']=='proposed' and not result['execution_authorized']
    tracemalloc.start();execute();current,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    t=time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(execute,range(32)))
    elapsed=time.perf_counter()-t
    report={'observed_at':now.isoformat(),'scope':'single-process synthetic microbenchmark',
      'python':platform.python_version(),'platform':platform.platform(),'logical_cpu_count':os.cpu_count(),
      'iterations':a.iterations,'cold_ms':round(cold_ms,3),'warm_p50_ms':round(statistics.median(samples),3),
      'warm_p95_ms':round(sorted(samples)[int(.95*len(samples))-1],3),'warm_max_ms':round(max(samples),3),
      'traced_peak_bytes_one_warm_call':peak,'threaded_requests':32,'workers':4,
      'threaded_elapsed_seconds':round(elapsed,3),'threaded_blocked':sum(r['state']=='blocked' for r in results),
      'deterministic_thread_results':len({json.dumps(r,sort_keys=True) for r in results})==1,
      'no_production_slo_claim':True,'fixture_bytes':len(source),'raw_warm_ms':samples}
Path(a.output).write_text(json.dumps(report,indent=2),encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k!='raw_warm_ms'},indent=2))
