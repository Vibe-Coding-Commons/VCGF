# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import copy
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import pytest

from conftest import ROOT, NOW
from runtime.adaptive.coordinator import CONTROL_IDS, PACKS, plan
from runtime.adaptive.cli import main
from runtime.adaptive.common import InputError


def test_both_engines_use_real_core_loader(case):
    fp,ux,root=case;r=plan(fp,ux,root,now=NOW)
    assert r['state']=='proposed'
    assert len(r['loaded_context'])==len(CONTROL_IDS)+len(PACKS)
    assert r['engineering']['project_id']==r['ux']['project_id']
    assert r['sources'][0]['verification']=='bytes_only'
    assert r['execution_authorized'] is False


def test_different_projects_are_blocked(case):
    fp,ux,root=case;ux['project_id']='different'
    assert plan(fp,ux,root,now=NOW)['state']=='blocked'


def test_changed_source_blocks(case):
    fp,ux,root=case;(root/'brief.md').write_text('tampered')
    assert plan(fp,ux,root,now=NOW)['state']=='blocked'


def test_conflicting_digests_block(case):
    fp,ux,root=case;ux['source_refs'][0]['sha256']='0'*64
    assert any('Conflicting' in x for x in plan(fp,ux,root,now=NOW)['blockers'])


@pytest.mark.parametrize('captured',['2020-01-01T00:00:00Z','2030-01-01T00:00:00Z'])
def test_stale_future_discovery(case,captured):
    fp,ux,root=case;fp['captured_at']=captured
    assert plan(fp,ux,root,now=NOW)['state']=='blocked'


def test_self_asserted_reviewer_is_not_trusted(case):
    fp,ux,root=case;ux['source_refs'][0]['kind']='trusted_reviewer'
    assert plan(fp,ux,root,now=NOW)['state']=='blocked'


def test_missing_digest_is_not_evidence(case):
    fp,ux,root=case;ux['source_refs'][0]['sha256']=None
    assert plan(fp,ux,root,now=NOW)['state']=='blocked'


@pytest.mark.parametrize('budget',[0,-1,True,1.5,32*1048576])
def test_invalid_budgets_rejected(case,budget):
    fp,ux,root=case
    with pytest.raises(InputError):plan(fp,ux,root,now=NOW,budget_bytes=budget)


def test_insufficient_budget_drops_no_requirements(case):
    fp,ux,root=case;r=plan(fp,ux,root,now=NOW,budget_bytes=100)
    assert r['state']=='blocked' and not r['loaded_context']
    assert set(r['selected_control_ids'])==set(CONTROL_IDS)


def test_partial_legacy_context_not_accepted(case):
    fp,ux,root=case
    assert plan(fp,ux,root,now=NOW,task={'intent':'design-review'})['state']=='blocked'


def test_wrong_task_classification_cannot_bypass(case):
    fp,ux,root=case
    r=plan(fp,ux,root,now=NOW,task={'intent':'button-color'},context={'project_id':fp['project_id']})
    assert r['state']=='blocked'


def test_wrong_legacy_project_blocks(case):
    fp,ux,root=case
    r=plan(fp,ux,root,now=NOW,task={'intent':'design-review'},context={'project_id':'other'})
    assert r['state']=='blocked'


def test_concurrent_plans_are_deterministic(case):
    fp,ux,root=case
    with ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(lambda _: plan(fp,ux,root,now=NOW),range(16)))
    assert len({json.dumps(x,sort_keys=True) for x in results})==1


def test_new_vcgf_cli_subprocess(case):
    fp,ux,root=case
    from datetime import datetime, timezone
    for row in [fp, ux]: row['captured_at'] = datetime.now(timezone.utc).isoformat()
    for name,record in [('fp.json',fp),('ux.json',ux)]:
        (root/name).write_text(json.dumps(record))
    result=subprocess.run([sys.executable,str(ROOT/'scripts/vcgf.py'),'design-plan',str(root/'fp.json'),str(root/'ux.json'),'--project-root',str(root),'--quiet'],capture_output=True,text=True)
    # The CLI uses current time; the example date belongs to the current review.
    assert result.returncode==0, result.stderr+result.stdout
    data=json.loads(result.stdout);assert data['state']=='proposed'
    assert 'loaded_context' not in data and 'blockers' in data


@pytest.mark.parametrize('command,key',[('advise-engineering','fp'),('advise-ux','ux')])
def test_cli_engine_commands(case,capsys,command,key):
    fp,ux,root=case;path=root/'input.json';path.write_text(json.dumps(fp if key=='fp' else ux))
    assert main([command,str(path)])==0
    assert json.loads(capsys.readouterr().out)['state']=='proposed'


def test_cli_invalid_input_structured_error(case,capsys):
    _,_,root=case;path=root/'input.json';path.write_text('{"a":1,"a":2}')
    assert main(['advise-engineering',str(path)])==2
    assert json.loads(capsys.readouterr().out)['status']=='input_error'
