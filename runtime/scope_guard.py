# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Exact file scope enforcement for a host-owned approved change manifest."""
import hashlib
from .loader import confined


def snapshot(root, paths):
    result={}
    for path in sorted(set(paths)):
        f=confined(root,path)
        result[path]=hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None
    return result


def check_scope(before,after,approved_paths,protected=(),max_changed_files=None):
    changed={p for p in set(before)|set(after) if before.get(p)!=after.get(p)}
    errors=[]
    if changed-set(approved_paths):errors.append('change outside approved manifest')
    if changed & set(protected):errors.append('protected file changed')
    if max_changed_files is not None and len(changed)>max_changed_files:errors.append('change size exceeds approved file count')
    return {'allowed':not errors,'changed':sorted(changed),'errors':errors,
            'limitation':'caller must inventory all relevant paths; does not infer semantic architecture drift'}
