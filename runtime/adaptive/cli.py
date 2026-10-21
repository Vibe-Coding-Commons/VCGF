# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Versioned opt-in commands integrated into scripts/vcgf.py."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import InputError, read_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='VCGF adaptive planning; read-only, no execution authorization')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ['advise-engineering', 'advise-ux']:
        p = sub.add_parser(name)
        p.add_argument('input', type=Path)
    p = sub.add_parser('design-plan')
    p.add_argument('fingerprint', type=Path)
    p.add_argument('discovery', type=Path)
    p.add_argument('--project-root', type=Path, required=True)
    p.add_argument('--task', type=Path)
    p.add_argument('--context', type=Path)
    p.add_argument('--budget-bytes', type=int, default=131_072)
    p.add_argument('--quiet', action='store_true', help='Omit loaded text, never blockers or decisions')
    p = sub.add_parser('release-readiness')
    p.add_argument('evidence', type=Path)
    p.add_argument('--artifact-root', type=Path, required=True)
    p.add_argument('--candidate', required=True, help='Expected candidate commit, not a branch name')
    args = parser.parse_args(argv)
    try:
        if args.command == 'advise-engineering':
            from .engineering import advise
            result = advise(read_json(args.input))
        elif args.command == 'advise-ux':
            from .ux import explain
            result = explain(read_json(args.input))
        elif args.command == 'design-plan':
            from .coordinator import plan
            result = plan(read_json(args.fingerprint), read_json(args.discovery), args.project_root,
                          task=read_json(args.task) if args.task else None,
                          context=read_json(args.context) if args.context else None,
                          budget_bytes=args.budget_bytes)
            if args.quiet:
                result.pop('loaded_context', None)
        else:
            from .release import assess
            result = assess(read_json(args.evidence), args.artifact_root, args.candidate)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 1 if result.get('state') == 'blocked' or result.get('status') == 'BLOCKED' else 0
    except (InputError, OSError, KeyError, TypeError, ValueError, ImportError) as exc:
        # Details are intentionally bounded and do not expose arbitrary input values.
        print(json.dumps({'status': 'input_error', 'error_type': type(exc).__name__,
                          'message': str(exc)[:300]}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
