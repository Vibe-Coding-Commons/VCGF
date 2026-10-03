# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import copy,hashlib,json,sys,tempfile,unittest
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT
from runtime.approval import approval_gate,guarded_call
from runtime.evidence import evaluate
from runtime.evidence_pack import present
from runtime.scope_guard import check_scope,snapshot
NOW=datetime(2026,10,3,12,30,tzinfo=timezone.utc)


class GateTests(unittest.TestCase):
    def setUp(self):
        self.ap=json.loads((ROOT/'tests/fixtures/v1.1/approval.json').read_text())['record']
        self.expected={k:copy.deepcopy(self.ap[k]) for k in ['action','resources','environment','plan_sha256','action_sha256','policy_sha256']}
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        self.ev=json.loads((ROOT/'tests/fixtures/v1.1/evidence.json').read_text())['record']
        (self.root/'result.json').write_text('{"synthetic_test":true}')
        a=self.ev['artifacts'][0];a['reference']='result.json';a['sha256']=hashlib.sha256((self.root/'result.json').read_bytes()).hexdigest()
        self.ex={k:copy.deepcopy(self.ev[k]) for k in ['code_sha256','policy_sha256','environment','profile','scope','required_control_ids']}
    def approval(self,**kwargs):return approval_gate(self.ap,self.expected,now=NOW,**kwargs)
    def evidence(self,**kwargs):return evaluate(self.ev,self.root,self.ex,now=NOW,**kwargs)
    def test_missing_authenticator_blocks(self):self.assertFalse(self.approval()['allowed'])
    def test_trusted_fake_authenticator_only_for_fixture(self):self.assertTrue(self.approval(authenticate=lambda record:True)['allowed'])
    def test_wrong_identity_blocks(self):self.assertFalse(self.approval(authenticate=lambda record:False)['allowed'])
    def test_revocation(self):self.assertFalse(self.approval(authenticate=lambda r:True,revoked=[self.ap['approval_id']])['allowed'])
    def test_changed_scope_fields(self):
        for key in self.expected:
            with self.subTest(key=key):
                ex=copy.deepcopy(self.expected);ex[key]=['other'] if key=='resources' else 'other'
                self.assertFalse(approval_gate(self.ap,ex,lambda r:True,now=NOW)['allowed'])
    def test_expired_approval(self):
        self.ap['expires_at']='2026-10-03T12:20:00Z';self.assertFalse(self.approval(authenticate=lambda r:True)['allowed'])
    def test_denied_call_has_no_effect(self):
        calls=[]
        with self.assertRaises(PermissionError):guarded_call(self.ap,self.expected,lambda:calls.append('executed'),now=NOW)
        self.assertFalse(calls)
    def test_authenticator_exception_fails_closed(self):
        def bad(_):raise RuntimeError('offline')
        self.assertFalse(self.approval(authenticate=bad)['allowed'])
    def test_no_review_no_pass(self):self.assertEqual(self.evidence()['status'],'FAIL')
    def test_valid_synthetic_scoped_evidence(self):self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'PASS')
    def test_changed_artifact(self):
        (self.root/'result.json').write_text('tampered');self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'FAIL')
    def test_missing_artifact(self):
        (self.root/'result.json').unlink();self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'FAIL')
    def test_stale_evidence(self):
        self.ev['valid_until']='2026-10-03T12:20:00Z';self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'FAIL')
    def test_project_coverage_not_task_coverage(self):
        self.ev['scope']['kind']='project';self.ex['scope']['kind']='project';self.assertIn('incomplete required coverage',self.evidence(trusted_review=lambda r:True)['errors'])
    def test_code_changed(self):
        self.ex['code_sha256']='b'*64;self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'FAIL')
    def test_empty_legacy_not_upgraded(self):self.assertEqual(evaluate({},self.root,{},now=NOW)['status'],'FAIL')
    def test_artifact_traversal(self):
        self.ev['artifacts'][0]['reference']='../result.json';self.assertEqual(self.evidence(trusted_review=lambda r:True)['status'],'FAIL')
    def test_scope_guard_unapproved(self):self.assertFalse(check_scope({'a':'old'},{'a':'new'},[])['allowed'])
    def test_scope_guard_protected(self):self.assertFalse(check_scope({'a':'old'},{'a':'new'},['a'],['a'])['allowed'])
    def test_scope_guard_approved(self):self.assertTrue(check_scope({'a':'old'},{'a':'new'},['a'])['allowed'])
    def test_evidence_modes_preserve_failure_and_findings(self):
        decision={'status':'FAIL','errors':['test finding']}
        for mode in ['minimal','standard','audit']:
            result=present(self.ev,decision,mode);self.assertEqual(result['decision'],decision);self.assertEqual(result['controls'],self.ev['controls'])
    def test_snapshot_deletion(self):
        before=snapshot(self.root,['result.json']);(self.root/'result.json').unlink();after=snapshot(self.root,['result.json']);self.assertEqual(check_scope(before,after,['result.json'])['changed'],['result.json'])


if __name__=='__main__':unittest.main(verbosity=2)
