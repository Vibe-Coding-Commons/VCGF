#!/usr/bin/env python3
"""VCGF Smart UI v1.0.0 reference selector.
Four independent selective layers: composition, components, interactions, journeys.
Relationships are review-only and never auto-activate another layer.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))

def action_for(standard_id, existing):
    item=next((x for x in existing if x.get('standard_id')==standard_id),None)
    if not item: return 'build_new'
    fitness=item.get('fitness'); evidence=item.get('evidence_ref')
    if fitness=='fit' and evidence:return 'reuse'
    if fitness=='partial' and evidence:return 'extend'
    if fitness=='unfit' and evidence:return 'replace'
    return 'verify_first'

def reviews(active,matrix):
    out=[]
    for r in matrix.get('relations',[]):
        if r['left'] in active and r['right'] in active:
            out.append({'left':r['left'],'right':r['right'],'relation_type':r['type'],'severity':r['severity'],'rule':r['rule']})
    return out

def resolve_orchestration(ctx,primary,mods):
    if not primary and not mods:return None
    mids=[x['standard_id'] for x in mods]; devices=set(ctx.get('devices',[])); freq=ctx.get('task_frequency','unknown'); info=ctx.get('information_density','adaptive')
    if info=='high' and freq=='high-frequency' and devices.intersection({'desktop','large-screen'}):density='compact'
    elif info=='low' or 'VCGF-UI-SCR-019' in mids or (devices and devices <= {'mobile','tablet'}):density='comfortable'
    else:density='adaptive'
    pid=primary['standard_id'] if primary else None
    mobile='list-detail' if pid=='VCGF-UI-SCR-015' else ('stacked-panels' if pid in {'VCGF-UI-SCR-008','VCGF-UI-SCR-009','VCGF-UI-SCR-016'} else 'task-preserving-reflow')
    large='comparison-expansion' if pid in {'VCGF-UI-SCR-011','VCGF-UI-SCR-015','VCGF-UI-SCR-016'} else ('controlled-regions' if 'VCGF-UI-SCR-020' in mids else 'context-expansion')
    responsive='mobile-primary-task' if 'VCGF-UI-SCR-019' in mids else ('large-screen-context' if 'VCGF-UI-SCR-020' in mids else 'task-preserving-adaptive')
    return {'primary_composition_id':pid,'modifier_ids':mids,'density_policy':density,'responsive_strategy':responsive,'mobile_transform':mobile,'large_screen_transform':large,'primary_action_limit':1,'progressive_disclosure':True,'role_adaptation':'priority-only','preserve_task_context':True}

def experience_orchestration(ctx,selected_journeys):
    if not selected_journeys:return None
    return {
      'entry_channel':ctx.get('entry_channel','unknown'),
      'completion_expectation':ctx.get('completion_expectation','unknown'),
      'context_continuity':ctx.get('context_continuity','unknown'),
      'selected_journey_ids':[x['standard_id'] for x in selected_journeys],
      'return_to_origin':'validate-then-return',
      'deep_link_policy':'authorize-and-prerequisite-check',
      'scope_change_policy':'invalidate-incompatible-context',
      'runtime_evidence_required':True,
      'cross_layer_auto_activation':False
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('context');ap.add_argument('--output');args=ap.parse_args()
    ctx=json.loads(Path(args.context).read_text(encoding='utf-8'))
    comp_cat=load('catalog.json');int_cat=load('interaction-catalog.json');scr_cat=load('screen-composition-catalog.json');jrn_cat=load('journey-catalog.json')
    cr=load('catalog/selection-rules.json');ir=load('catalog/interaction-rules.json');sr=load('catalog/screen-composition-rules.json');jr=load('catalog/journey-rules.json')
    cm=load('catalog/compatibility-matrix.json');im=load('catalog/interaction-compatibility-matrix.json');sm=load('catalog/screen-composition-compatibility-matrix.json');jm=load('catalog/journey-compatibility-matrix.json')
    counts=(len(comp_cat['components']),len(int_cat['patterns']),len(scr_cat['compositions']),len(jrn_cat['journeys']))
    existing=ctx.get('existing_capabilities',[])
    if not ctx.get('has_ui',True):
        plan={'schema_version':'1.0.0','project_id':ctx['project_id'],'screen_id':ctx['screen_id'],'selection_status':'no_ui','catalog_component_count':counts[0],'interaction_pattern_count':counts[1],'screen_composition_count':counts[2],'journey_pattern_count':counts[3],'selected_components':[],'selected_interactions':[],'selected_screen_compositions':[],'selected_journeys':[],'external_standards':[],'compatibility_reviews':[],'interaction_reviews':[],'composition_reviews':[],'journey_reviews':[],'standards_to_load':[],'not_selected_component_count':counts[0],'not_selected_interaction_count':counts[1],'not_selected_screen_composition_count':counts[2],'not_selected_journey_count':counts[3],'composition_status':'no_ui','journey_status':'no_ui','orchestration':None,'experience_orchestration':None,'warnings':[]}
    else:
        signals=set(ctx.get('signals',[]));isig=set(ctx.get('interaction_signals',[]));ssig=set(ctx.get('composition_signals',[]));jsig=set(ctx.get('journey_signals',[]))
        cby={x['id']:x for x in comp_cat['components']};iby={x['id']:x for x in int_cat['patterns']};sby={x['id']:x for x in scr_cat['compositions']};jby={x['id']:x for x in jrn_cat['journeys']}
        comps=[];ints=[];screens=[];journeys=[];external=[];load_paths=[];warnings=[]
        for r in cr['component_rules']:
            m=sorted(signals.intersection(r['triggers']))
            if not m:continue
            x=cby[r['standard_id']]; comps.append({'standard_id':r['standard_id'],'decision':r['default_decision'],'matched_signals':m,'implementation_action':action_for(r['standard_id'],existing),'standard_path':x['path'],'review_relationships':x.get('dependencies',[]),'reason':'Explicit component capability signals matched; relationships are review-only.'});load_paths.append(x['path'])
        for r in ir['interaction_rules']:
            m=sorted(isig.intersection(r['triggers']))
            if not m:continue
            x=iby[r['standard_id']];ints.append({'standard_id':r['standard_id'],'decision':r['default_decision'],'matched_signals':m,'implementation_action':action_for(r['standard_id'],existing),'standard_path':x['path'],'review_components':x.get('review_components',[]),'reason':'Explicit interaction-state/risk signals matched; no cross-layer auto-activation.'});load_paths.append(x['path'])
        # one primary composition, explicit modifiers
        pm=[];mm=[]
        for r in sr['composition_rules']:
            m=sorted(ssig.intersection(r['triggers']))
            if not m:continue
            (pm if r['kind']=='primary' else mm).append((r,m))
        creviews=[];primary=None;mods=[]
        if pm:
            pm.sort(key=lambda z:(-len(z[1]),z[0]['rank']));r,m=pm[0];x=sby[r['standard_id']]
            primary={'standard_id':r['standard_id'],'kind':'primary','decision':r['default_decision'],'matched_signals':m,'implementation_action':action_for(r['standard_id'],existing),'standard_path':x['path'],'review_components':x.get('review_components',[]),'review_interactions':x.get('review_interactions',[]),'reason':'Highest explicit composition evidence; other layers remain independent.'};screens.append(primary);load_paths.append(x['path'])
            for r2,m2 in pm[1:]:
                if len(m2)==len(m):creviews.append({'left':r['standard_id'],'right':r2['standard_id'],'relation_type':'alternative','severity':'review','rule':'Ambiguous primary composition matched equal explicit evidence; selected by declared rank and requires intent review.'})
        for r,m in sorted(mm,key=lambda z:z[0]['rank']):
            x=sby[r['standard_id']];it={'standard_id':r['standard_id'],'kind':'modifier','decision':r['default_decision'],'matched_signals':m,'implementation_action':action_for(r['standard_id'],existing),'standard_path':x['path'],'review_components':x.get('review_components',[]),'review_interactions':x.get('review_interactions',[]),'reason':'Explicit adaptive modifier signal matched.'};screens.append(it);mods.append(it);load_paths.append(x['path'])
        # journeys can coexist when explicitly signaled
        for r in jr['journey_rules']:
            m=sorted(jsig.intersection(r['triggers']))
            if not m:continue
            x=jby[r['standard_id']];journeys.append({'standard_id':r['standard_id'],'decision':r['default_decision'],'matched_signals':m,'implementation_action':action_for(r['standard_id'],existing),'standard_path':x['path'],'review_compositions':x.get('review_compositions',[]),'review_components':x.get('review_components',[]),'review_interactions':x.get('review_interactions',[]),'reason':'Explicit cross-screen journey signals matched; journey is independent of screen/component/interaction activation.'});load_paths.append(x['path'])
        for r in cr.get('external_rules',[]):
            m=sorted(signals.intersection(r['triggers'])); excluded=set(r.get('exclude_signals',[])).intersection(signals)
            if m and not excluded:
                external.append({'standard_id':r['standard_id'],'decision':r['default_decision'],'matched_signals':m,'standard_path':r['path'],'reason':'Explicit bound-standard signal matched.'});load_paths.append(r['path'])
        cset={x['standard_id'] for x in comps};iset={x['standard_id'] for x in ints};sset={x['standard_id'] for x in screens};jset={x['standard_id'] for x in journeys}
        creviews+=reviews(sset,sm)
        comp_reviews=reviews(cset,cm);int_reviews=reviews(iset,im);jreviews=reviews(jset,jm)
        if jsig and not journeys:warnings.append('Journey signals were supplied but no journey rule matched; review journey vocabulary/context.')
        if not ssig and screens:warnings.append('Unexpected composition selection without composition signals.')
        anysel=bool(comps or ints or screens or journeys or external)
        cstatus='selected' if primary and not any(x['severity']=='review' for x in creviews) else ('needs_review' if screens else 'not_selected')
        jstatus='selected' if journeys and not any(x['severity']=='review' for x in jreviews) else ('needs_review' if journeys or jsig else 'not_selected')
        plan={'schema_version':'1.0.0','project_id':ctx['project_id'],'screen_id':ctx['screen_id'],'selection_status':'selected' if anysel else 'needs_review','catalog_component_count':counts[0],'interaction_pattern_count':counts[1],'screen_composition_count':counts[2],'journey_pattern_count':counts[3],'selected_components':comps,'selected_interactions':ints,'selected_screen_compositions':screens,'selected_journeys':journeys,'external_standards':external,'compatibility_reviews':comp_reviews,'interaction_reviews':int_reviews,'composition_reviews':creviews,'journey_reviews':jreviews,'standards_to_load':list(dict.fromkeys(load_paths)) if anysel else [],'not_selected_component_count':counts[0]-len(comps),'not_selected_interaction_count':counts[1]-len(ints),'not_selected_screen_composition_count':counts[2]-len(screens),'not_selected_journey_count':counts[3]-len(journeys),'composition_status':cstatus,'journey_status':jstatus,'orchestration':resolve_orchestration(ctx,primary,mods),'experience_orchestration':experience_orchestration(ctx,journeys),'warnings':warnings}
    out=json.dumps(plan,ensure_ascii=False,indent=2)+'\n'
    if args.output:Path(args.output).write_text(out,encoding='utf-8')
    else:print(out,end='')
    return 0
if __name__=='__main__':raise SystemExit(main())
