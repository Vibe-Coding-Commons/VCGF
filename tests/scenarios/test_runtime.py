# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from datetime import datetime, timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT
from runtime.registry import build_registry
from runtime.router import route
from runtime.context import context_facts, preferences_prompt, handoff
from runtime.loader import load, confined
from runtime.resolver import resolve, ResolutionError

NOW=datetime(2026,10,3,12,30,tzinfo=timezone.utc)


def node(name, deps=None, conditions=None):
    return {'capability_id':name,'dependencies':deps or [],'applicability':{'conditions':conditions or []}}


def dep(target, relation='requires', **kw):
    return {'relation':relation,'targets':[target], **kw}


class GraphTests(unittest.TestCase):
    def test_missing_reference(self):
        with self.assertRaises(ResolutionError):resolve([node('a',[dep('missing')])],['a'],{})
    def test_cycle(self):
        with self.assertRaisesRegex(ResolutionError,'cycle'):resolve([node('a',[dep('b')]),node('b',[dep('a')])],['a'],{})
    def test_shared_dependency(self):
        self.assertEqual(len(resolve([node('a',[dep('c')]),node('b',[dep('c')]),node('c')],['b','a'],{})),3)
    def test_unknown_not_false(self):
        with self.assertRaisesRegex(ResolutionError,'unknown'):
            resolve([node('a',[dep('b','requires_when',condition={'fact':'local','operator':'equals','value':True})]),node('b')],['a'],{})
    def test_boolean_not_number(self):
        x=resolve([node('a',[dep('b','requires_when',condition={'fact':'local','operator':'equals','value':True})]),node('b')],['a'],{'local':1})
        self.assertNotIn('b',x)
    def test_any_of_rollback(self):
        nodes=[node('a',[{'relation':'any_of','targets':['bad','good']}]),node('bad',[dep('a')]),node('good')]
        self.assertEqual(set(resolve(nodes,['a'],{})),{'a','good'})
    def test_all_alternatives_fail(self):
        with self.assertRaisesRegex(ResolutionError,'no satisfiable'):
            resolve([node('a',[dep('a','any_of')])],['a'],{})
    def test_alternative_backtracks_across_later_root(self):
        nodes=[node('a',[{'relation':'any_of','targets':['b','d']}]),node('b',[dep('c','conflicts_with')]),node('c'),node('d')]
        self.assertEqual(set(resolve(nodes,['a','c'],{})),{'a','c','d'})
    def test_conflict_symmetric(self):
        with self.assertRaisesRegex(ResolutionError,'conflict'):resolve([node('a',[dep('b','conflicts_with')]),node('b')],['b','a'],{})
    def test_optional_edges_do_not_force_load(self):
        self.assertEqual(set(resolve([node('a',[dep('b','recommends'),dep('c','provided_by')]),node('b'),node('c')],['a'],{})),{'a'})


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.project=Path(self.temp.name)
        (self.project/'config.json').write_text('{"auth":"local-password"}')
        self.context=json.loads((ROOT/'tests/fixtures/v1.1/context.json').read_text())['record']
        f=self.context['facts'][0];f['value']='local-password';f['source']['reference']='config.json';f['source']['content_sha256']=hashlib.sha256((self.project/'config.json').read_bytes()).hexdigest()
        self.task={'task_id':'synthetic','intent':'login','classification_confirmed':True,'profile':'baseline','profile_confirmed':True,'mode':'lean','budget':300000,'inspection':{'completed':True,'evidence_ref':'synthetic:test'}}
    def runroute(self):return route(self.task,self.context,self.project,NOW)
    def test_login_dependencies(self):
        x=self.runroute();self.assertEqual(x['route']['decision'],'ready_to_plan');self.assertIn('email',x['capabilities']);self.assertTrue(x['route']['approval_required'])
    def test_sso_has_no_local_recovery(self):
        self.context['facts'][0]['value']='sso';x=self.runroute();self.assertNotIn('email',x['capabilities'])
    def test_button_color_not_login(self):
        self.task['intent']='button-color';x=self.runroute();self.assertNotIn('identity',x['capabilities']);self.assertNotIn('email',x['capabilities'])
        paths={i['path'] for i in x['active_context']};self.assertIn('packs/requirements/section-15.md',paths);self.assertNotIn('packs/requirements/section-21.md',paths);self.assertNotIn('packs/requirements/section-27.md',paths)
    def test_agent_separate_from_product(self):
        self.task['intent']='button-color';x=self.runroute();self.assertIn('development-agent',x['capabilities']);self.assertNotIn('product-ai',x['capabilities'])
    def test_changed_source_blocks_dependent_task(self):
        (self.project/'config.json').write_text('changed');self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_changed_unrelated_fact_does_not_block_color(self):
        (self.project/'config.json').write_text('changed');self.task['intent']='button-color';self.assertEqual(self.runroute()['route']['decision'],'ready_to_plan')
    def test_expired_context(self):
        self.context['facts'][0]['expires_at']='2026-10-03T12:01:00Z';self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_budget_never_drops_controls(self):
        full=self.runroute();self.task['budget']=1;x=self.runroute();self.assertEqual(x['route']['selected_control_ids'],full['route']['selected_control_ids']);self.assertFalse(x['active_context']);self.assertEqual(x['route']['decision'],'blocked')
    def test_overlay_removal_blocks(self):
        self.task['overlay_remove_controls']=['VCGF-GOV-001'];self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_profile_recommendation_needs_confirmation(self):
        self.task['profile_confirmed']=False;self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_production_baseline_blocks(self):
        self.context['environment']='production';self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_uninspected_blocks(self):
        self.task['inspection']={'completed':False,'evidence_ref':None};self.assertEqual(self.runroute()['route']['decision'],'blocked')
    def test_determinism(self):self.assertEqual(self.runroute(),self.runroute())
    def test_modes_never_remove_minimum(self):
        lean=set(self.runroute()['route']['selected_control_ids']);self.task['mode']='deep';self.assertTrue(lean <= set(self.runroute()['route']['selected_control_ids']))
    def test_handoff_requires_revalidation(self):self.assertTrue(handoff(self.context,self.runroute()['route'])['revalidate_before_use'])
    def test_first_language_question(self):self.assertEqual(preferences_prompt(None)['choices'],['ar','en','auto'])
    def test_confirmed_language_not_reasked(self):self.assertIsNone(preferences_prompt(json.loads((ROOT/'tests/fixtures/v1.1/preferences.json').read_text())['record']))
    def test_all_12_original_intents(self):
        expected={'login':['VCGF-IAM-002','VCGF-IAM-005'],'reset':['VCGF-IAM-005','VCGF-TEST-006'],
                  'admin':['VCGF-IAM-006','VCGF-IAM-003'],'upload':['VCGF-FILE-001','VCGF-FILE-002'],
                  'payment':['VCGF-API-002','VCGF-API-004'],'migration':['VCGF-DB-001','VCGF-OPS-003'],
                  'pii':['VCGF-PRIV-002','VCGF-PRIV-004'],'api':['VCGF-API-001','VCGF-API-005'],
                  'dependency':['VCGF-DEP-001','VCGF-DEP-002'],'emergency':['VCGF-IR-001','VCGF-REL-003'],
                  'deletion':['VCGF-PRIV-004','VCGF-GOV-002'],'authorization':['VCGF-IAM-007','VCGF-TEST-001']}
        for name in ['login','reset','admin','upload','payment','migration','pii','api','dependency','emergency','deletion','authorization']:
            with self.subTest(name=name):
                self.task['intent']=name;self.task['profile']='high-assurance';result=self.runroute();self.assertEqual(result['route']['decision'],'ready_to_plan')
                self.assertTrue(set(expected[name])<=set(result['route']['selected_control_ids']))


class LoaderTests(unittest.TestCase):
    def test_traversal(self):
        with self.assertRaises(ValueError):confined(ROOT,'../secret')
    def test_absolute(self):
        with self.assertRaises(ValueError):confined(ROOT,'/etc/passwd')
    def test_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'link').symlink_to('/etc/passwd')
            with self.assertRaises(ValueError):confined(d,'link')
    def test_hash_mismatch(self):
        with self.assertRaises(ValueError):load(ROOT,[{'path':'runtime/bootstrap.md','sha256':'0'*64}],99999)
    def test_deduplicated(self):
        rec=build_registry()['bootstrap'];x=load(ROOT,[rec,rec],99999);self.assertEqual(len(x['items']),1)


if __name__=='__main__':unittest.main(verbosity=2)
