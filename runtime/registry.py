# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import hashlib
import yaml
from .contracts import ROOT, validate_contract
from .context import digest
from .loader import confined


def build_registry(root=ROOT):
    catalog = yaml.safe_load((root/'spec/control-catalog.yaml').read_text())
    controls = {c['id']: {**c, 'sha256': hashlib.sha256((root/c['path']).read_bytes()).hexdigest()} for c in catalog['controls']}
    capabilities = []
    for path in sorted((root/'capabilities').glob('*.yaml')):
        record = yaml.safe_load(path.read_text())
        errors = validate_contract('capability', record)
        if errors:
            raise ValueError(path.name + ': ' + '; '.join(errors))
        capabilities.append(record)
    profiles = {p.parent.name: yaml.safe_load(p.read_text())['required_controls'] for p in sorted((root/'profiles').glob('*/profile.yaml'))}
    bootstrap = {'path': 'runtime/bootstrap.md', 'sha256': hashlib.sha256((root/'runtime/bootstrap.md').read_bytes()).hexdigest()}
    policy = yaml.safe_load((root/'runtime/routing-policy.yaml').read_text())
    pack_map = yaml.safe_load((root/'runtime/pack-map.yaml').read_text())
    resources = {}
    for mapping in pack_map.values():
        for paths in mapping.values():
            for path in paths:
                resources[path] = {'path': path, 'sha256': hashlib.sha256(confined(root,path).read_bytes()).hexdigest()}
    result = {'$comment': 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0', 'version': '1.1.0', 'controls': controls, 'capabilities': capabilities,
              'profiles': profiles, 'bootstrap': bootstrap, 'policy': policy,
              'pack_map': pack_map, 'resources': resources}
    result['policy_sha256'] = digest(result)
    return result
