# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

def main():
    errors=[]; v=(ROOT/'VERSION').read_text(encoding='utf-8').strip(); manifest=load_yaml(ROOT/'VCGF-MANIFEST.yaml')
    if not re.fullmatch(r'(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)',v): errors.append(f'Invalid stable semantic VERSION: {v}')
    if manifest.get('framework_version')!=v: errors.append('VCGF-MANIFEST framework_version mismatch')
    if manifest.get('release_status')!='stable': errors.append('framework release_status must be stable')
    for aid in ADAPTER_IDS:
        d=load_yaml(ROOT/'platforms'/aid/'adapter.yaml')
        if d.get('adapter_version')!='1.0.0': errors.append(f"{aid}: adapter_version must be 1.0.0 for initial release")
        if d.get('framework_compatibility')!='>=1.0.0 <2.0.0': errors.append(f"{aid}: framework_compatibility mismatch")
    if f'[{v}]' not in (ROOT/'CHANGELOG.md').read_text(encoding='utf-8'): errors.append(f'CHANGELOG lacks released version [{v}]')
    if str(load_yaml(ROOT/'CITATION.cff').get('version'))!=v: errors.append('CITATION version mismatch')
    if str(load_yaml(ROOT/'spec/control-catalog.yaml').get('framework_version'))!=v: errors.append('control-catalog framework_version mismatch')
    fail_if(errors); print('PASS validate-version')
if __name__=='__main__': main()
