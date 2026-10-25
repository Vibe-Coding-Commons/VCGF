# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Root-confined, hash-pinned context loading; no fetches or execution."""
import hashlib
import re
from pathlib import Path

from .tokens import count

COMMENT = re.compile(r'<!--.*?-->[ \t]*\r?\n?', re.S)


def served_text(name, data):
    """Text handed to the agent: Markdown HTML comments (attribution headers) are stripped; the file hash is on raw bytes."""
    text = data.decode('utf-8')
    if name.endswith('.md'):
        text = COMMENT.sub('', text).lstrip('\n')
    return text


def confined(root, relative):
    root = Path(root).resolve()
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('path must be relative without traversal')
    path = root / rel
    if any(p.is_symlink() for p in [path, *path.parents] if p != root and p.is_relative_to(root)):
        raise ValueError('symlink not permitted')
    if not path.resolve().is_relative_to(root):
        raise ValueError('path outside trusted root')
    return path


def load(root, records, budget, already_loaded=()):
    """Load hash-pinned records within a token budget.

    already_loaded: iterable of {'path','sha256'} the caller already holds. A record whose path and hash match an entry is
    not re-sent (delta loading) but still counted in reused_tokens; if the file on disk no longer matches the hash the
    registry pins, loading fails closed as for any stale hash, and a caller holding an older hash simply receives the
    current text again (hash-based invalidation).
    """
    if type(budget) is not int or budget <= 0:
        raise ValueError('budget must be a positive integer')
    held = set()
    for entry in already_loaded:
        if not isinstance(entry, dict) or not isinstance(entry.get('path'), str) or not isinstance(entry.get('sha256'), str):
            raise ValueError('already_loaded entries must be {path, sha256}')
        held.add((entry['path'], entry['sha256']))
    seen, items, reused = {}, [], []
    for record in records:
        name = record['path']
        if name in seen:
            if seen[name] != record['sha256']:
                raise ValueError('conflicting hashes for duplicate path: ' + name)
            continue
        seen[name] = record['sha256']
        data = confined(root, name).read_bytes()
        if hashlib.sha256(data).hexdigest() != record['sha256']:
            raise ValueError('stale registry hash: ' + name)
        text = served_text(name, data)
        measured = count(text)
        item = {'path': name, 'sha256': record['sha256'], 'text': text, 'bytes': measured['bytes'], 'tokens': measured['tokens']}
        (reused if (name, record['sha256']) in held else items).append(item)
    cost = sum(x['tokens'] for x in items)
    measurement = count('')['measurement']
    return {'items': items if cost <= budget else [], 'cost_tokens': cost, 'cost_bytes': sum(x['bytes'] for x in items),
            'reused_tokens': sum(x['tokens'] for x in reused), 'reused': [{'path': x['path'], 'sha256': x['sha256']} for x in reused],
            'measurement': measurement, 'method': count('')['method'], 'blocked': cost > budget}
