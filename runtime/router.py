# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Explicit inspected task classification; no false claims of general NLP understanding."""
from .context import digest, context_facts
from .contracts import ROOT, validate_contract
from .loader import load
from .resolver import resolve, ResolutionError
from .registry import build_registry


def route(task, context, project_root, now=None, root=ROOT):
    registry = build_registry(root)
    policy = registry['policy']
    if set(task) - {'task_id','intent','classification_confirmed','profile','profile_confirmed','mode','budget','inspection','overlay_add_controls','overlay_remove_controls','risk_signals'}:
        raise ValueError('unknown task field')
    for required in ['task_id','intent','classification_confirmed','profile','profile_confirmed','mode','budget','inspection']:
        if required not in task:
            raise ValueError('missing task field: ' + required)
    if task['mode'] not in ['lean','standard','deep'] or task['profile'] not in registry['profiles']:
        raise ValueError('invalid mode/profile')
    if not isinstance(task['task_id'],str) or not task['task_id']:
        raise ValueError('missing task identifier')
    if type(task['classification_confirmed']) is not bool or type(task['profile_confirmed']) is not bool:
        raise ValueError('confirmation must be boolean')
    intent = policy['intents'].get(task['intent'])
    if intent is None:
        raise ValueError('unrecognized task intent: explicit reviewed classification required')
    facts, invalid = context_facts(context, project_root, now)
    blockers=[]
    inspection=task['inspection']
    if not isinstance(inspection,dict) or set(inspection)!={'completed','evidence_ref'} or type(inspection['completed']) is not bool:
        raise ValueError('invalid inspection')
    if not inspection['completed'] or not inspection['evidence_ref']:
        blockers.append('targeted inspection required')
    if not task['classification_confirmed']:
        blockers.append('task classification must be confirmed after inspection')
    if not task['profile_confirmed']:
        blockers.append('profile selection requires confirmation')
    requested=list(intent['capabilities'])
    if context['development_agent']['uses_tools'] or context['development_agent']['uses_external_content']:
        requested.append('development-agent')
    if context['product_ai']['uses_agent'] or context['product_ai']['uses_llm']:
        requested.append('product-ai')
    try:
        selected=resolve(registry['capabilities'],requested,facts)
    except ResolutionError as exc:
        selected={};blockers.append(str(exc))
    nodes={c['capability_id']:c for c in registry['capabilities']}
    if 'identity' in selected and facts.get('auth-model') not in ['local-password','sso','passkey','passwordless']:
        blockers.append('unsupported or unknown authentication model; inspect before recovery selection')
    reasons={}
    for cap in selected:
        for cid in nodes[cap]['control_ids']:
            reasons.setdefault(cid,{'control_id':cid,'capability_id':cap,'source':'canonical capability registry','reason':selected[cap]['reason']})
    for cid in policy['minimum_controls']:
        reasons.setdefault(cid,{'control_id':cid,'capability_id':'runtime-core','source':'routing-policy.yaml','reason':'minimum task governance'})
    if task.get('overlay_remove_controls'):
        blockers.append('overlay cannot remove canonical or capability requirements')
    for cid in task.get('overlay_add_controls',[]):
        if cid not in registry['controls']:
            raise ValueError('unknown overlay control')
        reasons[cid]={'control_id':cid,'capability_id':'overlay','source':'explicit task overlay','reason':'additive requirement'}
    risk=intent['risk']
    signals=task.get('risk_signals',[])
    if not isinstance(signals,list) or any(s not in ['destructive','production-secrets','security-disablement','high-impact-payment','sensitive-data','privileged','irreversible','unknown-impact'] for s in signals):
        raise ValueError('invalid risk signals')
    if set(signals)&{'destructive','production-secrets','security-disablement','high-impact-payment','irreversible'}:
        risk='CRITICAL'
    elif signals and risk!='CRITICAL':risk='HIGH'
    if context['environment']=='production' or facts.get('sensitive-data') is True:
        risk='HIGH' if risk != 'CRITICAL' else risk
    recommended='high-assurance' if risk=='CRITICAL' else ('production' if context['environment']=='production' else 'baseline')
    ranks={'baseline':0,'production':1,'high-assurance':2}
    if ranks[task['profile']]<ranks[recommended]:
        blockers.append('confirmed profile below risk recommendation: '+recommended)
    if risk in ['HIGH','CRITICAL']:
        for cid in ['VCGF-GOV-002','VCGF-GOV-004','VCGF-TEST-002','VCGF-SEC-006']:
            reasons.setdefault(cid,{'control_id':cid,'capability_id':'risk-governance','source':'canonical risk model','reason':'high or critical change governance'})
    if risk=='CRITICAL':
        reasons.setdefault('VCGF-REL-003',{'control_id':'VCGF-REL-003','capability_id':'risk-governance','source':'canonical risk model','reason':'critical change rollback and recovery'})
    if task['mode']=='deep':
        for cid in policy['deep_review_controls']:
            reasons.setdefault(cid,{'control_id':cid,'capability_id':'deep-review','source':'routing-policy.yaml','reason':'additional deep review'})
    elif task['mode']=='standard':
        for cid in policy['standard_review_controls']:
            reasons.setdefault(cid,{'control_id':cid,'capability_id':'standard-review','source':'routing-policy.yaml','reason':'additional standard review'})
    records=[registry['bootstrap']]+[registry['controls'][cid] for cid in sorted(reasons)]
    for mapping in registry['pack_map'].values():
        for cap in sorted(selected):
            records.extend(registry['resources'][path] for path in mapping.get(cap,[]))
    loaded=load(root,records,task['budget'])
    if loaded['blocked']:
        blockers.append('budget exceeded: split task or explicitly raise budget; never drop required controls')
    result={'contract_version':'1.1.0','task_id':task['task_id'],'input_sha256':digest(task),
            'policy_sha256':registry['policy_sha256'],'context_sha256':digest(context),'environment':context['environment'],
            'risk':risk,'profile':task['profile'],'profile_selection':'user_confirmed' if task['profile_confirmed'] else 'proposed',
            'mode':task['mode'],'decision':'blocked' if blockers else 'ready_to_plan','selected_control_ids':sorted(reasons),
            'loaded_control_ids':[] if blockers else sorted(reasons),'excluded':[], 'reasons':[reasons[k] for k in sorted(reasons)],
            'blockers':blockers,'budget':{'limit_tokens':task['budget'],'cost_tokens':loaded['cost_tokens'],
                                       'measurement':loaded['measurement'],'method':loaded['method'],'overflow_policy':'split_raise_or_block'},
            'inspection':inspection,'approval_required':risk in ['HIGH','CRITICAL']}
    errors=validate_contract('route-result',result)
    if errors:
        raise ValueError('; '.join(errors))
    return {'route':result,'active_context':loaded['items'] if not blockers else [],'capabilities':list(selected),
            'invalid_facts':invalid,'recommended_profile':recommended,'handoff_required':True}
