# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Deterministic bounded backtracking for typed capability dependencies."""


class ResolutionError(ValueError):
    pass


def condition(rule, facts):
    key=rule['fact']
    if key not in facts or facts[key] is None:return None
    if rule['operator']=='exists':return True
    equal=type(facts[key]) is type(rule['value']) and facts[key]==rule['value']
    return equal if rule['operator']=='equals' else not equal


def resolve(capabilities,requested,facts,max_states=10000):
    nodes={c['capability_id']:c for c in capabilities}
    if len(nodes)!=len(capabilities):raise ResolutionError('duplicate capability')
    for node in nodes.values():
        for d in node['dependencies']:
            if any(t not in nodes for t in d['targets']):raise ResolutionError('missing dependency: '+node['capability_id'])
    states=0
    def search(pending,selected):
        nonlocal states
        states+=1
        if states>max_states:raise ResolutionError('dependency search budget exhausted; block and inspect')
        if not pending:return selected
        choices,stack=pending[0];rest=pending[1:];errors=[]
        for cid in choices:
            try:
                if cid in stack:raise ResolutionError('dependency cycle: '+' -> '.join(stack+[cid]))
                if cid in selected:return search(rest,selected)
                if cid not in nodes:raise ResolutionError('unknown capability: '+cid)
                node=nodes[cid]
                for rule in node['applicability']['conditions']:
                    value=condition(rule,facts)
                    if value is not True:raise ResolutionError(('unknown applicability: ' if value is None else 'not applicable: ')+cid+'/'+rule['fact'])
                for old in [cid]+list(selected):
                    for d in nodes[old]['dependencies']:
                        if d['relation']=='conflicts_with' and ((old==cid and any(t in selected or t==cid for t in d['targets'])) or (old!=cid and cid in d['targets'])):raise ResolutionError('capability conflict: '+cid+'/'+old)
                trial={**selected,cid:{'reason':'requested' if not stack else 'dependency of '+stack[-1]}}
                next_items=[]
                for d in node['dependencies']:
                    rel=d['relation']
                    if rel in ['recommends','provided_by','conflicts_with']:continue
                    if rel=='requires_when':
                        value=condition(d['condition'],facts)
                        if value is None:raise ResolutionError('unknown conditional dependency: '+cid+'/'+d['condition']['fact'])
                        if not value:continue
                    if rel=='any_of':next_items.append((d['targets'],stack+[cid]))
                    else:next_items.extend(([t],stack+[cid]) for t in d['targets'])
                return search(next_items+rest,trial)
            except ResolutionError as exc:
                errors.append(str(exc))
        label='no satisfiable alternative: ' if len(choices)>1 else ''
        # A single self-referential any_of is still a failed alternative.
        if any(d['relation']=='any_of' for c in choices if c in nodes for d in nodes[c]['dependencies']):label='no satisfiable alternative: '
        raise ResolutionError(label+'; '.join(errors))
    selected=search([([cid],[]) for cid in sorted(set(requested))],{})
    return {cid:selected[cid] for cid in sorted(selected)}
