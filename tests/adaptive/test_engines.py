# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import copy
from datetime import datetime, timezone

import pytest

from conftest import NOW
from runtime.adaptive.engineering import advise
from runtime.adaptive.ux import explain
from runtime.adaptive.schools import locale_direction


def selected(result, cid):
    return next(x['selected'] for x in result['choices'] if x['id']==cid)


def test_simple_laravel_stays_simple(case):
    fp,_,_=case;r=advise(fp,decided_at=NOW.isoformat())
    assert r['architecture']=='lean_layers'
    assert not selected(r,'repository')
    assert not selected(r,'strategy-and-factory')


def test_enterprise_label_does_not_force_ddd(case):
    fp,_,_=case;fp['project_kind']='enterprise_app'
    assert advise(fp)['architecture']=='lean_layers'


@pytest.mark.parametrize('key',['multiple_persistence_sources','multiple_service_providers','highly_reused_operations','complex_workflow','retriable_financial_operations'])
def test_unknown_not_false(case,key):
    fp,_,_=case;fp['architecture_facts'][key]=None
    assert advise(fp)['state']=='blocked'


def test_conflicting_risk_flags(case):
    fp,_,_=case;fp['risk_flags']=['none','payment']
    assert advise(fp)['state']=='blocked'


def test_duplicate_source_reference(case):
    fp,_,_=case;fp['sources']+=copy.deepcopy(fp['sources'])
    assert advise(fp)['state']=='blocked'


def test_multiple_persistence_selects_repository(case):
    fp,_,_=case;fp['architecture_facts']['multiple_persistence_sources']=True
    assert selected(advise(fp),'repository')


def test_provider_strategy_only_when_justified(case):
    fp,_,_=case;fp['architecture_facts']['multiple_service_providers']=True
    assert selected(advise(fp),'strategy-and-factory')


def test_selective_ddd_is_domain_based(case):
    fp,_,_=case;fp['architecture_facts']['independent_domains']=True
    fp['complexity']['bounded_contexts']=3;fp['complexity']['business_rules']=3
    assert advise(fp)['architecture']=='selective_ddd'


def test_preserve_existing_react(case):
    fp,_,_=case;fp['frontend']='react';fp['architecture_facts']['existing_component_library']='Existing Radix'
    r=advise(fp);assert selected(r,'shadcn-ui-radix')
    assert not selected(r,'shadcn-ui-base-ui')


def test_preserve_existing_vue(case):
    fp,_,_=case;fp['frontend']='vue';fp['architecture_facts']['existing_component_library']='PrimeVue'
    assert selected(advise(fp),'primevue')


@pytest.mark.parametrize('backend',['python','node','dotnet','java','none'])
def test_vendor_neutral_backend(case,backend):
    fp,_,_=case;fp['backend']=backend
    assert not any(c['id'].startswith('spatie/') for c in advise(fp)['choices'])


def test_fixed_clock_reproducibility(case):
    fp,_,_=case
    assert advise(fp,decided_at=NOW.isoformat())==advise(fp,decided_at=NOW.isoformat())


def test_default_clock_is_not_hardcoded(case):
    fp,_,_=case;before=datetime.now(timezone.utc);r=advise(fp);after=datetime.now(timezone.utc)
    assert before<=datetime.fromisoformat(r['decided_at'])<=after


@pytest.mark.parametrize('interaction',['form','approval','monitor','kiosk_action'])
def test_dense_workflows_keep_semantics(case,interaction):
    _,ux,_=case;ux['workflows'][0]['interaction']=interaction
    result=explain(ux)
    assert result['workflow_choices'][0]['pattern']!='high_density_task_workbench'


def test_dense_browse_gets_workbench(case):
    _,ux,_=case;ux['workflows'][0]['interaction']='browse'
    assert explain(ux)['workflow_choices'][0]['pattern']=='high_density_task_workbench'


def test_goals_and_tasks_override_category(case):
    _,ux,_=case;ux['product_type']='business_operations'
    ux['goal_priorities']=[{'goal_index':0,'outcome':'comprehension','weight':5}]
    ux['workflows'][0]['interaction']='read'
    assert explain(ux)['primary_school']=='editorial_brand'


def test_audience_contributes_to_ranking(case):
    _,ux,_=case;ux['audiences'][0]['proficiency']='novice'
    result=explain(ux)
    assert any('Novice actor' in c for r in result['ranking'] for c in r['contributions'])


def test_missing_goal_classification_blocks(case):
    _,ux,_=case;ux.pop('goal_priorities')
    assert explain(ux)['state']=='blocked'


def test_invalid_goal_reference_blocks(case):
    _,ux,_=case;ux['goal_priorities'][0]['goal_index']=255
    assert explain(ux)['state']=='blocked'


def test_unsupported_devices_are_not_proposed(case):
    _,ux,_=case;ux['workflows'][0]['devices']=['mobile']
    row=explain(ux)['workflow_choices'][0]
    assert row['desktop']==row['tablet']==row['wide']=='not_applicable'
    assert row['mobile']!='not_applicable'


def test_wide_context_and_required_information_preserved(case):
    _,ux,_=case;row=explain(ux)['workflow_choices'][0]
    assert row['wide'].endswith('_with_context_panel')
    assert row['important_data']==ux['workflows'][0]['important_data']


def test_existing_design_system_is_preserved(case):
    _,ux,_=case;assert explain(ux)['design_system_policy']=='preserve_existing'


@pytest.mark.parametrize('locale,direction',[('ar-SA','rtl'),('en-US','ltr'),('az-Arab','rtl'),('ar-Latn','ltr'),('en-Hebr','rtl'),('zz-Zzzz',None)])
def test_direction_respects_script(locale,direction):
    assert locale_direction(locale)==direction


def test_unknown_locale_is_blocker(case):
    _,ux,_=case;ux['localization']['languages'].append('zz-Zzzz')
    assert explain(ux)['state']=='blocked'


def test_quality_gates_not_automatically_passed(case):
    _,ux,_=case;r=explain(ux)
    assert all(x['status']=='not_run' for x in r['quality_gates'])
    assert r['font_strategy']['real_font_assets_included'] is False


def test_owner_confirmation_is_not_execution_approval(case):
    _,ux,_=case;ux['criticality']='high';ux['human_confirmation']='confirmed'
    assert explain(ux)['human_approval']['status']=='pending'


def test_input_not_mutated(case):
    fp,ux,_=case;saved=copy.deepcopy((fp,ux));advise(fp);explain(ux)
    assert (fp,ux)==saved


def test_kiosk_only_journey_keeps_an_actionable_touch_view(case):
    _,ux,_=case
    ux['workflows'][0]['devices']=['kiosk']
    ux['workflows'][0]['interaction']='kiosk_action'
    result=explain(ux)['workflow_choices'][0]
    assert result['kiosk']=='touch_guided_flow'
    assert result['desktop']==result['mobile']==result['tablet']=='not_applicable'
