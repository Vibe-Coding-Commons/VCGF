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
or deleted, or when a shell command matches a destructive pattern, unless VCGF_GOVERNANCE_APPROVAL points to an
approval record (schemas/v1.1.0/approval.schema.json) that is approved, unexpired, has action `governance-change`, names
the touched paths in `resources`, and was decided by a subject other than the requester. A bare environment flag never
unlocks anything: an agent that can set variables must not be able to grant itself governance changes. The record is
tamper-evident, not tamper-proof: without a host-held authenticator (runtime/approval.py approval_gate with an identity
adapter) this hook is a process control, and platforms/enforcement-matrix.yaml rates it accordingly. Exit 0 lets the
call proceed; the JSON decision is printed either way. Prompt text never enforces; this script does, where the platform runs it.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
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


def load_approval(path, now=None):
    """Return (record, errors): structural approval checks; identity is NOT authenticated here (no host adapter)."""
    from runtime.contracts import validate_contract
    from runtime.context import instant
    try:
        record = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return None, [f'approval record unreadable: {exc}']
    if isinstance(record, dict) and 'record' in record and 'approval_id' not in record:
        record = record['record']
    errors = validate_contract('approval', record)
    if errors:
        return None, errors
    now = now or datetime.now(timezone.utc)
    if record['status'] != 'approved':
        errors.append('approval not approved')
    if not instant(record['issued_at']) <= now < instant(record['expires_at']):
        errors.append('approval expired/not yet valid')
    if record['action'] != 'governance-change':
        errors.append('approval action is not governance-change')
    return record, errors


def covers(record, hits):
    resources = [r.replace('\\', '/').rstrip('/') for r in record.get('resources') or []]
    missing = []
    for h in hits:
        rel = str(h).replace('\\', '/')
        try:
            rel = str(Path(rel).resolve().relative_to(ROOT)).replace('\\', '/')
        except (ValueError, OSError):
            pass
        if not any(rel == r or rel.startswith(r + '/') for r in resources):
            missing.append(rel)
    return missing


def decide(call, prefixes, approval_path, now=None):
    tool = call.get('tool_name') or ''
    inp = call.get('tool_input') or {}
    paths = [v for k, v in inp.items() if isinstance(v, str) and k in ('file_path', 'path', 'target_file', 'notebook_path')]
    hits = [p for p in paths if is_protected(p, prefixes)] if tool in WRITE_TOOLS else []
    destructive = tool in SHELL_TOOLS and bool(DESTRUCTIVE.search(inp.get('command') or ''))
    if not hits and not destructive:
        return {'decision': 'allow', 'reason': 'no protected path or destructive pattern'}
    if not approval_path:
        what = f'canonical governance file(s) {hits}' if hits else 'destructive command'
        return {'decision': 'block', 'reason': f'{what} requires an approval record (VCGF_GOVERNANCE_APPROVAL=<path>) with action governance-change naming the resources; environment flags alone never unlock; VCGF-GOV-002, VCGF-GOV-006, VCGF-AI-007'}
    record, errors = load_approval(approval_path, now)
    if errors:
        return {'decision': 'block', 'reason': 'approval record rejected: ' + '; '.join(errors)}
    missing = covers(record, hits) if hits else ([] if 'shell:destructive' in (record.get('resources') or []) else ['shell:destructive'])
    if missing:
        return {'decision': 'block', 'reason': f'approval {record["approval_id"]} does not cover {missing}'}
    return {'decision': 'allow', 'reason': f'approval {record["approval_id"]} by {record["decision_by"]["subject"]} covers the change; structural check only (no host identity adapter); record it in the task evidence'}


def main():
    approval_path = os.environ.get('VCGF_GOVERNANCE_APPROVAL', '').strip()
    prefixes = protected_paths()
    if len(sys.argv) > 1:
        call = {'tool_name': 'Write', 'tool_input': {'file_path': sys.argv[1]}}
    else:
        raw = sys.stdin.read()
        try:
            call = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            print(json.dumps({'decision': 'block', 'reason': 'unreadable tool call; failing closed'})); return 2
    decision = decide(call, prefixes, approval_path)
    print(json.dumps(decision, ensure_ascii=False))
    return 2 if decision['decision'] == 'block' else 0


if __name__ == '__main__':
    sys.exit(main())
