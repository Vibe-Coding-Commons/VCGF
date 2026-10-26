#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Agent-hook guard: block a tool call that would modify canonical governance files or run a destructive command.

Reads a tool-call description as JSON on stdin (the shape used by Claude Code PreToolUse hooks: {"tool_name", "tool_input"})
or takes paths as arguments, and exits 2 (block) when a protected path from platforms/enforcement-matrix.yaml would be written
or deleted, or when a shell command matches a destructive pattern, unless the environment variable
VCGF_ALLOW_GOVERNANCE_CHANGE names a task identifier (an explicit, auditable allowance). Exit 0 lets the call proceed.
It prints a JSON decision either way. Prompt text never enforces; this script does, where the platform runs it.
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DESTRUCTIVE = re.compile(r'(\brm\s+-rf?\b|\bgit\s+push\s+.*--force|\bgit\s+reset\s+--hard|\bgit\s+clean\s+-[a-z]*f|\bdrop\s+(table|database)\b|\btruncate\s+table\b|\bmkfs\b|\bdel\s+/[sq]\b|Remove-Item\s+.*-Recurse)', re.I)
WRITE_TOOLS = {'Edit', 'Write', 'MultiEdit', 'NotebookEdit', 'edit_file', 'write_file', 'create_file', 'delete_file'}
SHELL_TOOLS = {'Bash', 'PowerShell', 'shell', 'run_command'}


def protected_paths():
    import yaml
    doc = yaml.safe_load((ROOT / 'platforms' / 'enforcement-matrix.yaml').read_text(encoding='utf-8'))
    return [p.replace('\\', '/') for p in doc['protected_paths']]


def is_protected(path, prefixes):
    rel = str(path).replace('\\', '/')
    try:
        rel = str(Path(rel).resolve().relative_to(ROOT)).replace('\\', '/')
    except (ValueError, OSError):
        pass
    return any(rel == p.rstrip('/') or rel.startswith(p) for p in prefixes)


def decide(call, prefixes, allowance):
    tool = call.get('tool_name') or ''
    inp = call.get('tool_input') or {}
    paths = [v for k, v in inp.items() if isinstance(v, str) and k in ('file_path', 'path', 'target_file', 'notebook_path')]
    if tool in WRITE_TOOLS:
        hits = [p for p in paths if is_protected(p, prefixes)]
        if hits and not allowance:
            return {'decision': 'block', 'reason': f'canonical governance file(s) {hits} may not be changed without an explicit allowance (VCGF_ALLOW_GOVERNANCE_CHANGE=<task id>); VCGF-GOV-006, VCGF-AI-007'}
        if hits:
            return {'decision': 'allow', 'reason': f'governance change allowed for task {allowance}; record it in the task evidence'}
    if tool in SHELL_TOOLS:
        command = inp.get('command') or ''
        if DESTRUCTIVE.search(command) and not allowance:
            return {'decision': 'block', 'reason': 'destructive command requires scoped approval at the trusted boundary (VCGF-GOV-002, VCGF-REL-003)'}
    return {'decision': 'allow', 'reason': 'no protected path or destructive pattern'}


def main():
    allowance = os.environ.get('VCGF_ALLOW_GOVERNANCE_CHANGE', '').strip()
    prefixes = protected_paths()
    if len(sys.argv) > 1:
        call = {'tool_name': 'Write', 'tool_input': {'file_path': sys.argv[1]}}
    else:
        raw = sys.stdin.read()
        try:
            call = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            print(json.dumps({'decision': 'block', 'reason': 'unreadable tool call; failing closed'})); return 2
    decision = decide(call, prefixes, allowance)
    print(json.dumps(decision, ensure_ascii=False))
    return 2 if decision['decision'] == 'block' else 0


if __name__ == '__main__':
    sys.exit(main())
