# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Read-only reference CLI. No shell command or deployment execution."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')


def references(items):
    # Default CLI output: hash-pinned references the agent reads itself (the files are in the repository); --full inlines the text.
    return [{k:item[k] for k in ('path','sha256','bytes','tokens','served') if k in item} for item in items]


def read(path):
    value=json.loads(Path(path).read_text(encoding='utf-8'))
    return value['record'] if isinstance(value,dict) and set(value)<= {'$comment','synthetic','record'} and 'record' in value else value


def main():
    if len(sys.argv) > 1 and sys.argv[1] in {
        'advise-engineering', 'advise-ux', 'design-plan', 'release-readiness'
    }:
        from runtime.adaptive.cli import main as adaptive_main
        return adaptive_main(sys.argv[1:])
    from runtime.contracts import validate_contract,NAMES
    from runtime.registry import build_registry
    from runtime.router import route
    from runtime.context import handoff
    from runtime.evidence import evaluate
    from runtime.evidence_pack import present
    from runtime.ui_select import select_ui
    from runtime.acceptance import acceptance_tests,acceptance_summary
    from runtime.compliance import applicable_controls,evaluate_compliance

    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    r=sub.add_parser('route');r.add_argument('task');r.add_argument('context');r.add_argument('--project-root',required=True);r.add_argument('--dry-run',action='store_true');r.add_argument('--quiet',action='store_true');r.add_argument('--full',action='store_true',help='print loaded text inline (default: hash-pinned references only)');r.add_argument('--presentation',choices=['beginner','expert'],default='expert');r.add_argument('--as-of',help='evaluate fact validity at this RFC 3339 instant instead of now (examples, fixtures, reproducible runs)')
    v=sub.add_parser('validate');v.add_argument('contract',choices=sorted(NAMES));v.add_argument('file')
    sub.add_parser('controls')
    e=sub.add_parser('explain');e.add_argument('control_id');e.add_argument('--route-file')
    h=sub.add_parser('handoff');h.add_argument('context');h.add_argument('route_file')
    u=sub.add_parser('ui-select',help='governed Smart UI selection bound to a route');u.add_argument('route_file');u.add_argument('screen_context');u.add_argument('--budget',type=int);u.add_argument('--quiet',action='store_true');u.add_argument('--full',action='store_true',help='print loaded standards inline (default: references only)')
    a=sub.add_parser('acceptance',help='acceptance tests defined for a control, or a summary with: all');a.add_argument('control_id')
    c=sub.add_parser('compliance',help='verify recorded acceptance results and their evidence against the applicable controls');c.add_argument('results');c.add_argument('--artifact-root',required=True);c.add_argument('--route');c.add_argument('--profile',choices=['baseline','production','high-assurance']);c.add_argument('--expect-code-sha256');c.add_argument('--as-of')
    for name in ['evidence','release-check']:
        e=sub.add_parser(name);e.add_argument('record');e.add_argument('expected');e.add_argument('--artifact-root',required=True)
        e.add_argument('--mode',choices=['minimal','standard','audit'],default='standard')
    args=p.parse_args();code=0
    try:
        if args.cmd=='route':
            now=None
            if args.as_of:
                from runtime.context import instant
                now=instant(args.as_of)
            result=route(read(args.task),read(args.context),args.project_root,now);code=1 if result['route']['blockers'] else 0
            result['dry_run']=bool(args.dry_run);result['evaluated_at']=args.as_of or 'now'
            if args.dry_run:result['dry_run_note']='read-only routing; no file, deployment or approval effect (the CLI never has one; --dry-run records the intent)'
            if args.quiet:result.pop('active_context');result.pop('reused_context',None)
            elif not args.full:result['active_context']=references(result['active_context'])
            if args.presentation=='beginner':result['help']='Resolve blockers, inspect selected controls, plan; ready_to_plan does not authorize execution.'
        elif args.cmd=='validate':
            errors=validate_contract(args.contract,read(args.file));result={'accepted':not errors,'errors':errors,'claim':'structural/local coherence only'};code=bool(errors)
        elif args.cmd=='controls':result=build_registry()['controls']
        elif args.cmd=='explain':
            registry=build_registry();result={'control':registry['controls'][args.control_id]}
            if args.route_file:result['reasons']=[x for x in read(args.route_file)['reasons'] if x['control_id']==args.control_id]
        elif args.cmd=='handoff':result=handoff(read(args.context),read(args.route_file))
        elif args.cmd=='ui-select':
            result=select_ui(read(args.route_file),read(args.screen_context),args.budget);code=1 if result['selection']['blockers'] else 0
            if args.quiet:result.pop('active_context');result.pop('selection_plan')
            elif not args.full:result['active_context']=references(result['active_context'])
        elif args.cmd=='compliance':
            controls,profile=applicable_controls(read(args.route) if args.route else None,args.profile)
            expected={'profile':profile}
            if args.expect_code_sha256:expected['code_sha256']=args.expect_code_sha256
            now=None
            if args.as_of:
                from runtime.context import instant
                now=instant(args.as_of)
            result=evaluate_compliance(read(args.results),args.artifact_root,controls,expected,now);code=0 if result['status']=='COMPLIANT' else 1
        elif args.cmd=='acceptance':
            if args.control_id=='all':result=acceptance_summary();code=0
            else:result=acceptance_tests(args.control_id);code=0 if result['tests'] else 1
        else:
            record=read(args.record);result=evaluate(record,args.artifact_root,read(args.expected));code=1 if result['status']!='PASS' else 0
            if not validate_contract('evidence',record):result=present(record,result,args.mode)
            # CLI has no trusted review identity provider; it must remain fail-closed.
        print(json.dumps(result,ensure_ascii=False,indent=2));return int(code)
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({'status':'input_error','message':str(exc)},ensure_ascii=False));return 2


if __name__=='__main__':sys.exit(main())
