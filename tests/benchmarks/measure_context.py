# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Local deterministic context benchmark; NOT LLM token usage or platform quality."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from runtime.router import route
from runtime.contracts import ROOT


def main():
    baseline=sum(p.stat().st_size for p in (ROOT/'controls').rglob('*.md') if p.name!='README.md')
    rows=[]
    for directory in sorted((ROOT/'examples/runtime').iterdir()):
        task=json.loads((directory/'task.json').read_text())['record'];context=json.loads((directory/'context.json').read_text())['record']
        # Fixed fixture clock: measures routing, not freshness on a user's live project.
        now=datetime.fromisoformat(context['facts'][0]['observed_at'])
        for repeat in range(3):
            start=time.perf_counter();result=route(task,context,directory,now);duration=time.perf_counter()-start
            text='\n'.join(item['text'] for item in result['active_context'])
            rows.append({'scenario':directory.name,'repeat':repeat+1,'decision':result['route']['decision'],
                         'selected_controls':result['route']['selected_control_ids'],'loaded_utf8_bytes':len(text.encode()),
                         'static_all_controls_utf8_bytes':baseline,'elapsed_seconds':duration,
                         'observed_model_tokens':None,'token_measurement':'Unverified: no model/tokenizer run',
                         'context_sha256':hashlib.sha256(text.encode()).hexdigest()})
    out={'$comment':'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0',
         'scope':'12 curated original intents x 3 local repetitions; no NLP/AR-EN or live adapter inference',
         'generated_at':datetime.now(timezone.utc).isoformat(),'results':rows,
         'remaining':'T13–T24 model behavior and AR/EN 24x2x3 platform/model experiment remain unverified; no paid calls authorized'}
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return int(any(x['decision']!='ready_to_plan' for x in rows))


if __name__=='__main__':sys.exit(main())
