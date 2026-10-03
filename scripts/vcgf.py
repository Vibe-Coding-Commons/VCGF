# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Read-only reference CLI. No shell command or deployment execution."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from runtime.contracts import validate_contract,NAMES
from runtime.registry import build_registry
from runtime.router import route
from runtime.context import handoff
from runtime.evidence import evaluate
from runtime.evidence_pack import present


def read(path):
    value=json.loads(Path(path).read_text())
    return value['record'] if isinstance(value,dict) and set(value)<= {'$comment','synthetic','record'} and 'record' in value else value


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    r=sub.add_parser('route');r.add_argument('task');r.add_argument('context');r.add_argument('--project-root',required=True);r.add_argument('--dry-run',action='store_true');r.add_argument('--quiet',action='store_true');r.add_argument('--presentation',choices=['beginner','expert'],default='expert')
    v=sub.add_parser('validate');v.add_argument('contract',choices=sorted(NAMES));v.add_argument('file')
    sub.add_parser('controls')
    e=sub.add_parser('explain');e.add_argument('control_id');e.add_argument('--route-file')
    h=sub.add_parser('handoff');h.add_argument('context');h.add_argument('route_file')
    for name in ['evidence','release-check']:
        e=sub.add_parser(name);e.add_argument('record');e.add_argument('expected');e.add_argument('--artifact-root',required=True)
        e.add_argument('--mode',choices=['minimal','standard','audit'],default='standard')
    args=p.parse_args();code=0
    try:
        if args.cmd=='route':
            result=route(read(args.task),read(args.context),args.project_root);code=1 if result['route']['blockers'] else 0
            if args.quiet:result.pop('active_context')
            if args.presentation=='beginner':result['help']='Resolve blockers, inspect selected controls, plan; ready_to_plan does not authorize execution.'
        elif args.cmd=='validate':
            errors=validate_contract(args.contract,read(args.file));result={'accepted':not errors,'errors':errors,'claim':'structural/local coherence only'};code=bool(errors)
        elif args.cmd=='controls':result=build_registry()['controls']
        elif args.cmd=='explain':
            registry=build_registry();result={'control':registry['controls'][args.control_id]}
            if args.route_file:result['reasons']=[x for x in read(args.route_file)['reasons'] if x['control_id']==args.control_id]
        elif args.cmd=='handoff':result=handoff(read(args.context),read(args.route_file))
        else:
            record=read(args.record);result=evaluate(record,args.artifact_root,read(args.expected));code=1 if result['status']!='PASS' else 0
            if not validate_contract('evidence',record):result=present(record,result,args.mode)
            # CLI has no trusted review identity provider; it must remain fail-closed.
        print(json.dumps(result,ensure_ascii=False,indent=2));return int(code)
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({'status':'input_error','message':str(exc)},ensure_ascii=False));return 2


if __name__=='__main__':sys.exit(main())
