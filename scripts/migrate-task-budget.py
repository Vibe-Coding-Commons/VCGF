# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Migrate a pre-1.4 task record whose budget was effectively compared in bytes to an explicit budget unit.

Since 1.4.0 the Router compares `budget` (declared as limit_tokens) with estimated tokens of the served text. Before, it
compared raw UTF-8 bytes, so a budget tuned as bytes allowed roughly four times less context than its number suggests.
This tool never guesses silently: it writes the chosen unit into the task so the behaviour is explicit.

  --keep-bytes   set budget_unit: bytes      (exactly the pre-1.4 comparison; no number changes)
  --to-tokens    set budget_unit: tokens and divide the budget by the documented ASCII ratio (4.0), rounding down
  --declare      set budget_unit: tokens and keep the number (the budget was meant as tokens all along)

Reads JSON (the bare task or {"record": task}); writes to --output or stdout. Never modifies the input in place.
"""
import argparse
import json
import sys
from pathlib import Path

ASCII_CHARS_PER_TOKEN = 4.0  # runtime/tokens.py


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('task')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--keep-bytes', action='store_true'); mode.add_argument('--to-tokens', action='store_true'); mode.add_argument('--declare', action='store_true')
    parser.add_argument('--output')
    args = parser.parse_args()
    document = json.loads(Path(args.task).read_text(encoding='utf-8'))
    wrapped = isinstance(document, dict) and 'record' in document and 'budget' not in document
    task = document['record'] if wrapped else document
    if not isinstance(task, dict) or type(task.get('budget')) is not int or task['budget'] <= 0:
        print(json.dumps({'status': 'input_error', 'message': 'task must carry a positive integer budget'})); return 2
    if 'budget_unit' in task:
        print(json.dumps({'status': 'input_error', 'message': f"task already declares budget_unit {task['budget_unit']!r}; nothing to migrate"})); return 2
    before = task['budget']
    if args.keep_bytes:
        task['budget_unit'] = 'bytes'; note = 'legacy byte comparison kept; the number is unchanged'
    elif args.to_tokens:
        task['budget_unit'] = 'tokens'; task['budget'] = max(1, int(before / ASCII_CHARS_PER_TOKEN))
        note = f'budget {before} bytes converted to {task["budget"]} estimated tokens at {ASCII_CHARS_PER_TOKEN} ASCII characters per token (non-ASCII text estimates higher; review the value)'
    else:
        task['budget_unit'] = 'tokens'; note = 'budget declared as tokens; the number is unchanged'
    out = json.dumps(document, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        Path(args.output).write_text(out, encoding='utf-8', newline='\n')
    else:
        sys.stdout.write(out)
    print(json.dumps({'status': 'migrated', 'budget_before': before, 'budget_after': task['budget'], 'budget_unit': task['budget_unit'], 'note': note}, ensure_ascii=False), file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
