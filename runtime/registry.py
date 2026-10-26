# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import hashlib
import yaml
from pathlib import Path
from .contracts import ROOT, validate_contract
from .context import digest
from .loader import confined


_CACHE = {}


def _signature(root):
    # Every file the registry derives from: a changed size or mtime rebuilds; hashes inside the registry stay authoritative.
    paths = [root/'spec/control-catalog.yaml', root/'runtime/bootstrap.md', root/'runtime/routing-policy.yaml', root/'runtime/pack-map.yaml',
             root/'spec/applicability-matrix.yaml', root/'spec/control-cards/common-clauses.md']
    paths += sorted((root/'capabilities').glob('*.yaml')) + sorted((root/'profiles').glob('*/profile.yaml'))
    paths += sorted((root/'controls').rglob('*.md')) + sorted((root/'spec/control-cards').glob('*.md'))
    pack_map = yaml.safe_load((root/'runtime/pack-map.yaml').read_text(encoding='utf-8'))
    for mapping in pack_map.values():
        for files in mapping.values():
            paths += [confined(root, p) for p in files]
    out = []
    for p in paths:
        try:
            st = Path(p).stat(); out.append((str(p), st.st_mtime_ns, st.st_size))
        except FileNotFoundError:
            out.append((str(p), None, None))
    return tuple(out)


def build_registry(root=ROOT):
    """Canonical registry; cached per process while no source file changed. Callers treat the result as read-only."""
    root = Path(root)
    signature = _signature(root)
    cached = _CACHE.get(str(root))
    if cached and cached[0] == signature:
        return cached[1]
    registry = _build(root)
    _CACHE[str(root)] = (signature, registry)
    return registry


def _build(root):
    catalog = yaml.safe_load((root/'spec/control-catalog.yaml').read_text(encoding='utf-8'))
    controls = {c['id']: {**c, 'sha256': hashlib.sha256((root/c['path']).read_bytes()).hexdigest()} for c in catalog['controls']}
    capabilities = []
    for path in sorted((root/'capabilities').glob('*.yaml')):
        record = yaml.safe_load(path.read_text(encoding='utf-8'))
        errors = validate_contract('capability', record)
        if errors:
            raise ValueError(path.name + ': ' + '; '.join(errors))
        capabilities.append(record)
    profiles = {p.parent.name: yaml.safe_load(p.read_text(encoding='utf-8'))['required_controls'] for p in sorted((root/'profiles').glob('*/profile.yaml'))}
    bootstrap = {'path': 'runtime/bootstrap.md', 'sha256': hashlib.sha256((root/'runtime/bootstrap.md').read_bytes()).hexdigest()}
    cards = {}
    for cid in controls:
        card = root/'spec/control-cards'/f'{cid}.md'
        if not card.is_file():
            raise ValueError(f'control card missing for {cid}; run scripts/generate-control-cards.py')
        cards[cid] = {'path': f'spec/control-cards/{cid}.md', 'sha256': hashlib.sha256(card.read_bytes()).hexdigest()}
    common = {'path': 'spec/control-cards/common-clauses.md', 'sha256': hashlib.sha256((root/'spec/control-cards/common-clauses.md').read_bytes()).hexdigest()}
    policy = yaml.safe_load((root/'runtime/routing-policy.yaml').read_text(encoding='utf-8'))
    pack_map = yaml.safe_load((root/'runtime/pack-map.yaml').read_text(encoding='utf-8'))
    applicability = yaml.safe_load((root/'spec/applicability-matrix.yaml').read_text(encoding='utf-8'))
    resources = {}
    for mapping in pack_map.values():
        for paths in mapping.values():
            for path in paths:
                resources[path] = {'path': path, 'sha256': hashlib.sha256(confined(root,path).read_bytes()).hexdigest()}
    result = {'$comment': 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0', 'version': '1.1.0', 'controls': controls, 'capabilities': capabilities,
              'profiles': profiles, 'bootstrap': bootstrap, 'cards': cards, 'common_clauses': common, 'policy': policy,
              'pack_map': pack_map, 'resources': resources, 'applicability': applicability['controls']}
    result['policy_sha256'] = digest(result)
    return result
