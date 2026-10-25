# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Validate spec/acceptance/*.yaml: every control has specific, verifiable acceptance tests (see spec/acceptance/README.md)."""
import re
from vcgf_lib import *

TYPES={'automated','manual','review'}
EVIDENCE={'test-result','code-review','configuration-record','security-scan','migration-review','manual-verification','screenshot','log-sample','threat-model','inventory','approval-record','release-checksum'}
AUTOMATION={'none','script','validator','hook','ci'}
NEGATIVE_DOMAINS={'security','identity-access','data-protection','database','api','file-handling','secrets','privacy'}
GENERIC=re.compile(r'^(inspect implementation and configuration|at least one reproducible artifact|apply when the project or change contains|review the change)',re.I)
TEST_ID=re.compile(r'^(VCGF-[A-Z]+-\d{3})-AT(\d{2})$')
UI_ID=re.compile(r'^(VCGF-UI-(COMP|INT|SCR|JRN)-\d{3}|CALENDAR-GOVERNANCE-ADDENDUM|UI-COMP-SEARCHABLE-SELECT)$')


def smart_ui_ids():
    import json
    pack=ROOT/'packs/ux/smart-ui'; ids={'CALENDAR-GOVERNANCE-ADDENDUM','UI-COMP-SEARCHABLE-SELECT'}
    for f,key in [('catalog.json','components'),('interaction-catalog.json','patterns'),('screen-composition-catalog.json','compositions'),('journey-catalog.json','journeys')]:
        ids|={x['id'] for x in json.loads((pack/f).read_text(encoding='utf-8'))[key]}
    return ids


def main():
    import sys
    partial='--partial' in sys.argv  # authoring aid: validate the present files only; completeness is enforced by default
    errors=[]
    catalog={c['id']:c for c in load_yaml(ROOT/'spec/control-catalog.yaml')['controls']}
    sections={f"S{p['section']}" for p in load_yaml(ROOT/'packs/index.yaml')['packs']}
    ui_ids=smart_ui_ids()
    seen_controls={}; seen_ids={}; criteria={}
    files=sorted((ROOT/'spec/acceptance').glob('*.yaml'))
    if not files: fail_if(['spec/acceptance/*.yaml: no acceptance files'])
    for f in files:
        rp=rel(f); d=load_yaml(f) or {}
        if d.get('acceptance_version')!='1.0.0': errors.append(f'{rp}: acceptance_version must be 1.0.0')
        domain=d.get('domain')
        if domain!=f.stem: errors.append(f'{rp}: domain {domain!r} must equal file name {f.stem!r}')
        if domain not in DOMAINS: errors.append(f'{rp}: unknown domain {domain!r}')
        controls=d.get('controls') or {}
        if not isinstance(controls,dict): errors.append(f'{rp}: controls must be a mapping'); continue
        for cid,entry in controls.items():
            if cid not in catalog: errors.append(f'{rp}: unknown control {cid}'); continue
            if catalog[cid]['domain']!=domain: errors.append(f'{rp}: {cid} belongs to domain {catalog[cid]["domain"]}, not {domain}')
            if cid in seen_controls: errors.append(f'{rp}: {cid} already defined in {seen_controls[cid]}')
            seen_controls[cid]=rp
            for src in (entry or {}).get('requirement_sources') or []:
                if not (src in sections or (UI_ID.match(str(src)) and src in ui_ids)): errors.append(f'{rp}: {cid}: unknown requirement source {src!r}')
            tests=(entry or {}).get('tests') or []
            if len(tests)<2: errors.append(f'{rp}: {cid}: at least two acceptance tests are required (found {len(tests)})')
            if not any(t.get('type') in {'automated','review'} for t in tests): errors.append(f'{rp}: {cid}: at least one automated or review test is required')
            if domain in NEGATIVE_DOMAINS and not any(t.get('negative_path') is True for t in tests): errors.append(f'{rp}: {cid}: at least one negative_path test is required for {domain} controls')
            if domain=='user-experience' and not any(UI_ID.match(str(s)) for s in (entry or {}).get('requirement_sources') or []): errors.append(f'{rp}: {cid}: user-experience controls must reference at least one Smart UI standard')
            for t in tests:
                tid=str(t.get('id')); m=TEST_ID.match(tid)
                if not m or m.group(1)!=cid: errors.append(f'{rp}: {cid}: test id {tid!r} must look like {cid}-AT01'); continue
                if tid in seen_ids: errors.append(f'{rp}: duplicate test id {tid}')
                seen_ids[tid]=rp
                if t.get('type') not in TYPES: errors.append(f'{rp}: {tid}: type must be one of {sorted(TYPES)}')
                crit=' '.join(str(t.get('criterion') or '').split())
                if len(crit)<60: errors.append(f'{rp}: {tid}: criterion too short or missing (min 60 characters)')
                if GENERIC.match(crit): errors.append(f'{rp}: {tid}: criterion is generic template text')
                key=crit.lower()
                if key in criteria and criteria[key][0]!=cid: errors.append(f'{rp}: {tid}: criterion duplicates {criteria[key][1]}')
                criteria.setdefault(key,(cid,tid))
                if not str(t.get('method') or '').strip(): errors.append(f'{rp}: {tid}: method is required')
                if not isinstance(t.get('negative_path'),bool): errors.append(f'{rp}: {tid}: negative_path must be true or false')
                ev=t.get('evidence') or []
                if not ev or any(e not in EVIDENCE for e in ev): errors.append(f'{rp}: {tid}: evidence must be a non-empty subset of {sorted(EVIDENCE)}')
                auto=t.get('automation') or {}
                kind=auto.get('kind')
                if kind not in AUTOMATION: errors.append(f'{rp}: {tid}: automation.kind must be one of {sorted(AUTOMATION)}')
                elif kind!='none' and not str(auto.get('reference') or '').strip(): errors.append(f'{rp}: {tid}: automation.reference required when kind is {kind}')
                if t.get('type')=='automated' and kind=='none': errors.append(f'{rp}: {tid}: automated tests need an automation kind other than none')
    missing=sorted(set(catalog)-set(seen_controls))
    if missing and not partial: errors.append(f'controls without acceptance tests: {missing}')
    fail_if(errors); print(f'PASS validate-acceptance: {len(seen_controls)} controls, {len(seen_ids)} acceptance tests')
if __name__=='__main__': main()
