# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import json,sys,unittest
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from runtime.contracts import ROOT,validate_contract


class AdapterTests(unittest.TestCase):
    def test_all_eight_candidates_match_template(self):
        template=(ROOT/'templates/adapters/runtime-rules.template.md').read_text()
        for aid in ['generic','claude','cursor','lovable','bolt','v0','replit','chatgpt']:
            with self.subTest(adapter=aid):self.assertEqual((ROOT/'platforms'/aid/'rules/runtime.generated.md').read_text(),template)
    def test_capability_sidecars_do_not_inherit_legacy_verified(self):
        for path in (ROOT/'platforms').glob('*/runtime-capabilities.yaml'):
            record=yaml.safe_load(path.read_text());self.assertEqual(validate_contract('adapter-capabilities',record),[])
            self.assertTrue(all(c['verification']=='not_tested' for c in record['capabilities']))
    def test_chatgpt_old_schema_and_control_coverage(self):
        schema=json.loads((ROOT/'schemas/adapter.schema.json').read_text());record=yaml.safe_load((ROOT/'platforms/chatgpt/adapter.yaml').read_text())
        self.assertEqual(list(Draft202012Validator(schema).iter_errors(record)),[])
        mappings=yaml.safe_load((ROOT/'platforms/chatgpt/control-mapping.yaml').read_text())['mappings']
        canonical=yaml.safe_load((ROOT/'spec/control-catalog.yaml').read_text())['controls']
        self.assertEqual({m['control_id'] for m in mappings},{m['id'] for m in canonical});self.assertTrue(all(m['status']=='UNVERIFIED' for m in mappings))
    def test_generated_entry_is_compact(self):
        text=(ROOT/'templates/adapters/runtime-rules.template.md').read_text();self.assertLess(len(text.encode()),1800)
    def test_repository_skill_frontmatter_and_size(self):
        text=(ROOT/'platforms/chatgpt/skills/vcgf/SKILL.md').read_text();parts=text.split('---',2)
        self.assertEqual(parts[0],'');meta=yaml.safe_load(parts[1]);self.assertEqual(set(meta),{'name','description'});self.assertEqual(meta['name'],'vcgf');self.assertLess(len(text.splitlines()),500)


if __name__=='__main__':unittest.main(verbosity=2)
