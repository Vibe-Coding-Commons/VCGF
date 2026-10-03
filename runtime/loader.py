# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Root-confined, hash-pinned context loading; no fetches or execution."""
import hashlib
from pathlib import Path


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


def load(root, records, budget):
    if type(budget) is not int or budget <= 0:
        raise ValueError('budget must be a positive integer')
    seen, items = set(), []
    for record in records:
        name = record['path']
        if name in seen:
            continue
        seen.add(name)
        data = confined(root, name).read_bytes()
        if hashlib.sha256(data).hexdigest() != record['sha256']:
            raise ValueError('stale registry hash: ' + name)
        items.append({'path': name, 'sha256': record['sha256'], 'text': data.decode('utf-8')})
    # UTF-8 bytes are a conservative estimate, not observed model tokens.
    estimated = sum(len(x['text'].encode('utf-8')) for x in items)
    return {'items': items if estimated <= budget else [], 'cost_tokens': estimated,
            'measurement': 'estimated', 'method': 'UTF-8 byte upper estimate; not a tokenizer measurement',
            'blocked': estimated > budget}
