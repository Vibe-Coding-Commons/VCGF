#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from datetime import datetime, timezone
try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:
    print('Missing validation dependency:',exc,file=sys.stderr);raise SystemExit(2)
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def add(name,cond,detail=''):
    CHECKS.append({'name':name,'status':'pass' if cond else 'fail','details':detail})
def load(rel):return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def sha(path):
    p=ROOT/path if isinstance(path,str) else path
    return hashlib.sha256(p.read_bytes()).hexdigest()
def run_context(rel):
    out=subprocess.check_output([sys.executable,str(ROOT/'scripts/select_smart_ui.py'),str(ROOT/rel)],text=True,encoding='utf-8')
    return json.loads(out)
def frontmatter(text):
    m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
    return yaml.safe_load(m.group(1)) if m else None

def validate_schema(instance_rel,schema_rel,name):
    try:
        errors=list(Draft202012Validator(load(schema_rel)).iter_errors(load(instance_rel)))
        add(name,not errors,'valid' if not errors else '; '.join(e.message for e in errors[:4]))
    except Exception as e:add(name,False,str(e))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify-manifest',action='store_true');ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    cat=load('catalog.json');icat=load('interaction-catalog.json');scat=load('screen-composition-catalog.json');jcat=load('journey-catalog.json')
    comps=cat['components'];ints=icat['patterns'];scrs=scat['compositions'];jrns=jcat['journeys']
    add('Package catalog counts',len(comps)==36 and len(ints)==24 and len(scrs)==20 and len(jrns)==18,f'{len(comps)}/{len(ints)}/{len(scrs)}/{len(jrns)}')
    add('Screen composition split',sum(x['kind']=='primary' for x in scrs)==18 and sum(x['kind']=='modifier' for x in scrs)==2,'18 primary + 2 modifiers expected')
    ids=[x['id'] for x in comps+ints+scrs+jrns];add('Unique standard IDs',len(ids)==len(set(ids)),f'{len(ids)} IDs')
    add('Package metadata final candidate',all(d.get('package_version')=='1.0.0' and d.get('status')=='final-integration-candidate' for d in [cat,icat,scat,jcat]),'catalog package metadata')
    # rules counts
    cr=load('catalog/selection-rules.json');ir=load('catalog/interaction-rules.json');sr=load('catalog/screen-composition-rules.json');jr=load('catalog/journey-rules.json')
    add('Component rule coverage',len(cr['component_rules'])==36 and {x['standard_id'] for x in cr['component_rules']}=={x['id'] for x in comps},'36/36')
    add('Interaction rule coverage',len(ir['interaction_rules'])==24 and {x['standard_id'] for x in ir['interaction_rules']}=={x['id'] for x in ints},'24/24')
    add('Composition rule coverage',len(sr['composition_rules'])==20 and {x['standard_id'] for x in sr['composition_rules']}=={x['id'] for x in scrs},'20/20')
    add('Journey rule coverage',len(jr['journey_rules'])==18 and {x['standard_id'] for x in jr['journey_rules']}=={x['id'] for x in jrns},'18/18')
    add('External bindings exactly two',{x['standard_id'] for x in cr['external_rules']}=={'CALENDAR-GOVERNANCE-ADDENDUM','UI-COMP-SEARCHABLE-SELECT'},'Calendar + Searchable Select')
    # source integrity and bound extension
    add('Calendar source snapshot digest',sha('source-snapshots/CALENDAR-GOVERNANCE-ADDENDUM.source.txt')=='c8e2f84da5e1a0d33e772a5222d7d9b93ba3c58ea012b560c24233327c02c43c')
    add('Searchable source snapshot digest',sha('source-snapshots/ENTERPRISE-SEARCHABLE-SELECT.source.txt')=='032c4caf1632bd9d24f1032b4810252bb67daf434d5678d0d4ee3c32f0e46c94')
    cal=(ROOT/'external-standards/CALENDAR-GOVERNANCE-ADDENDUM.md').read_text(encoding='utf-8')
    for tok in ['اختيار السنة مباشرة','اختيار الشهر مباشرة','viewDate','selectedDate','birthDate','CAL-NAV-AC14']:
        add('Calendar direct navigation: '+tok,tok in cal)
    sel=(ROOT/'external-standards/ENTERPRISE-SEARCHABLE-SELECT-COMBOBOX.md').read_text(encoding='utf-8')
    for tok in ['embedded, auto-focused search input','أول صف داخل القائمة','التركيز تلقائيًا','لا تفرض مكوّنًا معقدًا على كل اختيار']:
        add('Searchable Select contract: '+tok,tok in sel)
    # docs coverage, ids, req/ac, status
    specs=[('component',comps,'standards','VCGF-UI-COMP-'),('interaction',ints,'interactions','VCGF-UI-INT-'),('screen',scrs,'screen-compositions','VCGF-UI-SCR-'),('journey',jrns,'journeys','VCGF-UI-JRN-')]
    req_total=ac_total=0
    for kind,arr,folder,prefix in specs:
        errs=[]
        for x in arr:
            p=ROOT/x['path']
            if not p.is_file():errs.append('missing '+x['path']);continue
            text=p.read_text(encoding='utf-8');fm=frontmatter(text)
            if not fm or fm.get('id')!=x['id']:errs.append(x['id']+' frontmatter id')
            if not fm or fm.get('status')!='final-integration-candidate':errs.append(x['id']+' status')
            if not fm or fm.get('application_tests')!='not_run':errs.append(x['id']+' runtime state')
            rids=sorted(set(re.findall(rf'{re.escape(x["id"])}-R\d{{2}}',text)))
            aids=sorted(set(re.findall(rf'{re.escape(x["id"])}-AC\d{{2}}',text)))
            if len(rids)!=12:errs.append(x['id']+f' req={len(rids)}')
            if len(aids)!=12:errs.append(x['id']+f' ac={len(aids)}')
            req_total+=len(rids);ac_total+=len(aids)
        add(kind.title()+' document contracts',not errs,'OK' if not errs else '; '.join(errs[:12]))
    add('Total requirements',req_total==1176,str(req_total))
    add('Total acceptance scenarios',ac_total==1176,str(ac_total))
    comp_settings=sum(len(x.get('settings',[])) for x in comps);int_settings=sum(len(x.get('settings',[])) for x in ints);scr_settings=sum(len(x.get('policies',[])) for x in scrs);jrn_settings=sum(len(x.get('policies',[])) for x in jrns)
    add('Reference settings/policies',comp_settings==288 and int_settings==144 and scr_settings==120 and jrn_settings==108,f'{comp_settings}+{int_settings}+{scr_settings}+{jrn_settings}={comp_settings+int_settings+scr_settings+jrn_settings}')
    # traceability journey and matrix acceptance
    jt=load('tests/journey-traceability.json');add('Journey traceability count',len(jt)==216,f'{len(jt)}')
    matrix=(ROOT/'tests/ACCEPTANCE-MATRIX.md').read_text(encoding='utf-8');add('Acceptance matrix total',matrix.count('`not_run` |')==1176,f"{matrix.count('`not_run` |')} rows")
    # schema validation map
    mappings=[
      ('catalog.json','schemas/catalog.schema.json','Component catalog schema'),
      ('interaction-catalog.json','schemas/interaction-catalog.schema.json','Interaction catalog schema'),
      ('screen-composition-catalog.json','schemas/screen-composition-catalog.schema.json','Screen catalog schema'),
      ('journey-catalog.json','schemas/journey-catalog.schema.json','Journey catalog schema'),
      ('catalog/component-contracts.json','schemas/component-contract.schema.json','Component contracts schema'),
      ('catalog/interaction-contracts.json','schemas/interaction-contract.schema.json','Interaction contracts schema'),
      ('catalog/screen-composition-contracts.json','schemas/screen-composition-contract.schema.json','Screen contracts schema'),
      ('catalog/journey-contracts.json','schemas/journey-contract.schema.json','Journey contracts schema'),
      ('catalog/compatibility-matrix.json','schemas/compatibility-matrix.schema.json','Component compatibility schema'),
      ('catalog/interaction-compatibility-matrix.json','schemas/interaction-compatibility-matrix.schema.json','Interaction compatibility schema'),
      ('catalog/screen-composition-compatibility-matrix.json','schemas/screen-composition-compatibility-matrix.schema.json','Screen compatibility schema'),
      ('catalog/journey-compatibility-matrix.json','schemas/journey-compatibility-matrix.schema.json','Journey compatibility schema'),
      ('config/central-settings.example.json','schemas/central-settings.schema.json','Central settings schema'),
      ('config/interaction-policy.example.json','schemas/interaction-policy.schema.json','Interaction policy schema'),
      ('config/screen-orchestration-policy.example.json','schemas/screen-orchestration-policy.schema.json','Screen orchestration schema'),
      ('templates/screen-context.example.json','schemas/screen-context.schema.json','Screen context template schema'),
      ('templates/project-assessment.example.json','schemas/project-assessment.schema.json','Project assessment schema'),
      ('templates/evidence-record.example.json','schemas/evidence-record.schema.json','Evidence record schema')]
    for a,b,n in mappings:validate_schema(a,b,n)
    # all contexts and generated plans
    cv=Draft202012Validator(load('schemas/screen-context.schema.json'));pv=Draft202012Validator(load('schemas/component-selection-plan.schema.json'))
    ctx_errors=[];plan_errors=[];plans={}
    for p in sorted((ROOT/'examples').glob('*.json')):
        if p.name.endswith('.plan.json'):continue
        d=json.loads(p.read_text(encoding='utf-8'));e=list(cv.iter_errors(d))
        if e:ctx_errors.append(p.name+': '+e[0].message)
        plan=run_context('examples/'+p.name);plans[p.stem]=plan
        pe=list(pv.iter_errors(plan))
        if pe:plan_errors.append(p.name+': '+pe[0].message)
        pp=p.with_name(p.stem+'.plan.json');pp.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    add('All example contexts validate',not ctx_errors,'OK' if not ctx_errors else '; '.join(ctx_errors[:6]))
    add('All generated plans validate',not plan_errors,'OK' if not plan_errors else '; '.join(plan_errors[:6]))
    # selection assertions
    no=plans['no-ui-service'];add('No-UI selects zero',not(no['selected_components'] or no['selected_interactions'] or no['selected_screen_compositions'] or no['selected_journeys'] or no['external_standards']))
    birth=plans['simple-birthdate-screen'];add('Birthdate selective component',[x['standard_id'] for x in birth['selected_components']]==['VCGF-UI-COMP-003']);add('Birthdate journey',[x['standard_id'] for x in birth['selected_journeys']]==['VCGF-UI-JRN-002']);add('Birthdate bound standards',{x['standard_id'] for x in birth['external_standards']}=={'CALENDAR-GOVERNANCE-ADDENDUM','UI-COMP-SEARCHABLE-SELECT'})
    ent=plans['enterprise-operations-screen'];add('Enterprise remains selective',len(ent['selected_components'])==11 and len(ent['selected_interactions'])==11 and len(ent['selected_screen_compositions'])==2 and [x['standard_id'] for x in ent['selected_journeys']]==['VCGF-UI-JRN-006'],f"{len(ent['selected_components'])}/{len(ent['selected_interactions'])}/{len(ent['selected_screen_compositions'])}/{len(ent['selected_journeys'])}")
    bulk=plans['bulk-job-screen'];add('Bulk + long-running journey selection',{x['standard_id'] for x in bulk['selected_journeys']}=={'VCGF-UI-JRN-007','VCGF-UI-JRN-017'});add('Bulk journey compatibility review',any(r['left']=='VCGF-UI-JRN-007' and r['right']=='VCGF-UI-JRN-017' for r in bulk['journey_reviews']))
    appr=plans['approval-workspace-screen'];add('Approval dual branch journeys',{x['standard_id'] for x in appr['selected_journeys']}=={'VCGF-UI-JRN-004','VCGF-UI-JRN-005'});add('Approval branch review emitted',any(r['relation_type']=='alternative-branch' for r in appr['journey_reviews']))
    scope=plans['scope-switch-journey'];add('Scope switch journey only expected', [x['standard_id'] for x in scope['selected_journeys']]==['VCGF-UI-JRN-015'])
    doc=plans['document-sign-archive-journey'];add('Document lifecycle journey', [x['standard_id'] for x in doc['selected_journeys']]==['VCGF-UI-JRN-009'])
    public=plans['public-self-service-journey'];add('Public self-service journey', [x['standard_id'] for x in public['selected_journeys']]==['VCGF-UI-JRN-011'])
    # independent layer guards via temp contexts
    base={'schema_version':'1.0.0','project_id':'guard','screen_id':'guard','screen_purpose':'guard','has_ui':True,'signals':[],'interaction_signals':[],'composition_signals':[],'journey_signals':[],'languages':['en'],'directions':['ltr'],'devices':['desktop'],'tenant_scoped':False,'sensitive_data':False,'existing_capabilities':[],'notes':None,'risk_level':'low','data_volume':'small','offline_required':False,'user_roles':['operator'],'task_frequency':'regular','information_density':'adaptive','viewport_priority':'desktop-first','primary_input':'keyboard','entry_channel':'internal-navigation','completion_expectation':'unknown','context_continuity':'task-scoped'}
    def inline(mod):
        d=copy.deepcopy(base);mod(d)
        with tempfile.NamedTemporaryFile('w',suffix='.json',encoding='utf-8',delete=False) as f:json.dump(d,f);name=f.name
        try:return json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/select_smart_ui.py'),name],text=True,encoding='utf-8'))
        finally:Path(name).unlink(missing_ok=True)
    p=inline(lambda d:d['signals'].append('tabular_operational_data'));add('Component-only guard',len(p['selected_components'])==1 and not p['selected_interactions'] and not p['selected_screen_compositions'] and not p['selected_journeys'])
    p=inline(lambda d:d['interaction_signals'].append('error_state'));add('Interaction-only guard',len(p['selected_interactions'])==1 and not p['selected_components'] and not p['selected_screen_compositions'] and not p['selected_journeys'])
    p=inline(lambda d:d['composition_signals'].append('dashboard_overview'));add('Composition-only guard',len(p['selected_screen_compositions'])==1 and not p['selected_components'] and not p['selected_interactions'] and not p['selected_journeys'])
    p=inline(lambda d:d['journey_signals'].append('deep_link_authorize_return'));add('Journey-only guard',len(p['selected_journeys'])==1 and not p['selected_components'] and not p['selected_interactions'] and not p['selected_screen_compositions'])
    # catalog HTML coverage
    html=(ROOT/'CATALOG.html').read_text(encoding='utf-8');missing=[i for i in ids if i not in html];add('Interactive catalog covers all 98 core standards',not missing,'OK' if not missing else ','.join(missing[:8]));add('Interactive catalog includes bound standards','CALENDAR-GOVERNANCE-ADDENDUM' in html and 'UI-COMP-SEARCHABLE-SELECT' in html)
    # Markdown code fences + local links
    link_errors=[];fence_errors=[];link_count=0
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        if len(re.findall(r'^```',text,re.M))%2:fence_errors.append(str(p.relative_to(ROOT)))
        stripped=re.sub(r'^```.*?^```[^\n]*$','',text,flags=re.M|re.S)
        for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)',stripped):
            dest=dest.strip().split(' "',1)[0]
            if urlsplit(dest).scheme or dest.startswith('//'):continue
            link_count+=1;url,_,anchor=dest.partition('#');target=(p.parent/unquote(url)).resolve() if url else p.resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():link_errors.append(f'{p.relative_to(ROOT)} -> {dest}');continue
            if anchor and anchor.startswith(('VCGF-UI-COMP-','VCGF-UI-INT-','VCGF-UI-SCR-','VCGF-UI-JRN-')) and f'id="{anchor}"' not in target.read_text(encoding='utf-8'):link_errors.append(f'{p.relative_to(ROOT)} missing anchor {dest}')
    add('Markdown code fences balanced',not fence_errors,'OK' if not fence_errors else ','.join(fence_errors[:8]));add('Local links and anchors resolve',not link_errors,f'{link_count} checked' if not link_errors else '; '.join(link_errors[:8]))
    # negative schema tests
    neg=0;negfail=[]
    def reject(name,instance_rel,schema_rel,mut):
        nonlocal neg
        neg+=1;d=copy.deepcopy(load(instance_rel));mut(d);errs=list(Draft202012Validator(load(schema_rel)).iter_errors(d));
        if not errs:negfail.append(name)
    reject('context missing journey_signals','templates/screen-context.example.json','schemas/screen-context.schema.json',lambda d:d.pop('journey_signals'))
    reject('context invalid entry_channel','templates/screen-context.example.json','schemas/screen-context.schema.json',lambda d:d.__setitem__('entry_channel','unsafe'))
    reject('context wrong version','templates/screen-context.example.json','schemas/screen-context.schema.json',lambda d:d.__setitem__('schema_version','0.5.0'))
    reject('journey catalog missing journey','journey-catalog.json','schemas/journey-catalog.schema.json',lambda d:d['journeys'].pop())
    reject('journey catalog bad priority','journey-catalog.json','schemas/journey-catalog.schema.json',lambda d:d['journeys'][0].__setitem__('priority','P9'))
    reject('journey contract bad kind','catalog/journey-contracts.json','schemas/journey-contract.schema.json',lambda d:d['contracts'][0].__setitem__('kind','component'))
    reject('component catalog missing item','catalog.json','schemas/catalog.schema.json',lambda d:d['components'].pop())
    reject('interaction catalog missing item','interaction-catalog.json','schemas/interaction-catalog.schema.json',lambda d:d['patterns'].pop())
    reject('screen catalog missing item','screen-composition-catalog.json','schemas/screen-composition-catalog.schema.json',lambda d:d['compositions'].pop())
    reject('central settings activation','config/central-settings.example.json','schemas/central-settings.schema.json',lambda d:d['enabledComponents'].append('VCGF-UI-COMP-001'))
    reject('interaction activation','config/interaction-policy.example.json','schemas/interaction-policy.schema.json',lambda d:d['enabledInteractions'].append('VCGF-UI-INT-001'))
    reject('screen global activation','config/screen-orchestration-policy.example.json','schemas/screen-orchestration-policy.schema.json',lambda d:d['enabledCompositions'].append('VCGF-UI-SCR-001'))
    add('Negative schema tests',not negfail,f'{neg}/{neg} rejected' if not negfail else 'accepted invalid: '+','.join(negfail))
    # Manifest
    if args.verify_manifest:
        issues=[];mp=ROOT/'manifest.json';sp=ROOT/'SHA256SUMS.txt'
        if not mp.is_file() or not sp.is_file():issues.append('missing manifest/checksums')
        else:
            man=load('manifest.json');entries=man['files'];allowed={'manifest.json','SHA256SUMS.txt'}
            actual={str(p.relative_to(ROOT)).replace('\\','/') for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts};recorded={e['path'] for e in entries}
            if recorded!=actual-allowed:issues.append('file set mismatch')
            for e in entries:
                p=ROOT/e['path']
                if not p.is_file() or p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:issues.append('content '+e['path'])
            sums={}
            for line in sp.read_text(encoding='utf-8').splitlines():
                dig,rel=line.split('  ',1);sums[rel]=dig
            if set(sums)!=recorded|{'manifest.json'}:issues.append('checksum set mismatch')
            for rel,dig in sums.items():
                if not (ROOT/rel).is_file() or sha(rel)!=dig:issues.append('checksum '+rel)
        add('Manifest and SHA-256 integrity',not issues,'OK' if not issues else '; '.join(issues[:8]))
    passed=sum(x['status']=='pass' for x in CHECKS);failed=len(CHECKS)-passed
    summary={'component_standards':36,'interaction_patterns':24,'screen_compositions':20,'journey_patterns':18,'bound_standards':2,'reference_settings_and_policies':660,'requirements':1176,'acceptance_scenarios':1176,'calendar_navigation_acceptance':14,'checks':len(CHECKS),'passed':passed,'failed':failed,'negative_schema_tests':neg,'local_links_checked':link_count,'runtime_application_tests':'not_run','manifest_verified_in_this_run':args.verify_manifest}
    ok=failed==0
    if args.write_report:
        (ROOT/'reports').mkdir(exist_ok=True)
        report={'package_version':'1.0.0','status':'pass' if ok else 'fail','scope':'specification-package-schema-selection-traceability-and-integrity','generated_at':datetime.now(timezone.utc).isoformat(),'summary':summary,'checks':CHECKS,'claim_boundary':'Runtime application conformance is not established by these checks.'}
        (ROOT/'reports/DOCUMENTATION-VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        lines=['# فحص VCGF Smart UI v1.0.0','',f'**{"PASS" if ok else "FAIL"}**','',f'- Components: 36','- Interactions: 24','- Screen Compositions: 20','- Journeys: 18','- Requirements / Acceptance: 1176 / 1176',f'- Checks: {passed}/{len(CHECKS)}',f'- Local links: {link_count}',f'- Negative schema tests: {neg}/{neg if not negfail else neg-len(negfail)} rejected','', '> الفحص يثبت سلامة الحزمة والمخططات والاختيار والتتبع فقط. Runtime tests للتطبيقات تبقى `not_run`.','', '| الفحص | الحالة | التفاصيل |','|---|---|---|']
        for c in CHECKS:lines.append('| '+c['name'].replace('|','/')+' | '+c['status']+' | '+c['details'].replace('|','/').replace('\n',' ')+' |')
        (ROOT/'reports/DOCUMENTATION-VALIDATION.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    for c in CHECKS:print(f"[{c['status'].upper()}] {c['name']}: {c['details']}")
    print(json.dumps(summary,ensure_ascii=False))
    return 0 if ok else 1
if __name__=='__main__':raise SystemExit(main())
