# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

SEMVER=re.compile(r'(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)')
COMPAT=re.compile(r'^>=(\d+\.\d+\.\d+) <(\d+\.\d+\.\d+)$')
RELEASE_STATUSES={'stable','release-candidate','development'}  # development: unreleased work on a develop branch; release workflows refuse it
CANDIDATE_STATUSES={'experimental','candidate'}
LEGACY_VERSION_CLAIM=re.compile(r'VERSION remains \d+\.\d+\.\d+')

def read(rp): return (ROOT/rp).read_text(encoding='utf-8')
def vtuple(s): return tuple(int(x) for x in s.split('.'))

def check_adapters(v,manifest,errors):
    supported=[str(a) for a in manifest.get('supported_adapters') or []]; candidates=[str(a) for a in manifest.get('candidate_adapters') or []]
    sv=manifest.get('adapter_versions') or {}; cv=manifest.get('candidate_adapter_versions') or {}
    both=sorted(set(supported)&set(candidates))
    if both: errors.append(f'adapters listed as both supported and candidate: {both}')
    for aid in supported:
        if aid not in sv: errors.append(f'{aid}: supported adapter missing from manifest adapter_versions')
    for aid in candidates:
        if aid not in cv: errors.append(f'{aid}: candidate adapter missing from manifest candidate_adapter_versions')
    seen=set()
    for d in sorted((ROOT/'platforms').iterdir()):
        if not d.is_dir() or d.name.startswith('_') or not (d/'adapter.yaml').is_file(): continue
        a=load_yaml(d/'adapter.yaml') or {}; aid=str(a.get('adapter_id')); seen.add(aid); av=str(a.get('adapter_version')); st=a.get('status')
        if aid!=d.name: errors.append(f'platforms/{d.name}: adapter_id {aid!r} does not match its directory name')
        if aid in supported:
            if av!=str(sv.get(aid)): errors.append(f'{aid}: adapter_version {av} != manifest adapter_versions {sv.get(aid)}')
            if st!='stable': errors.append(f'{aid}: supported adapter status must be stable, got {st!r}')
        elif aid in candidates:
            if av!=str(cv.get(aid)): errors.append(f'{aid}: adapter_version {av} != manifest candidate_adapter_versions {cv.get(aid)}')
            if st not in CANDIDATE_STATUSES: errors.append(f'{aid}: candidate adapter status must be one of {sorted(CANDIDATE_STATUSES)}, got {st!r}')
        else: errors.append(f'platforms/{d.name}: adapter {aid!r} is neither in supported_adapters nor candidate_adapters')
        m=COMPAT.match(str(a.get('framework_compatibility','')))
        if not m: errors.append(f"{aid}: framework_compatibility must look like '>=X.Y.Z <X.Y.Z', got {a.get('framework_compatibility')!r}")
        elif not (vtuple(m.group(1))<=vtuple(v)<vtuple(m.group(2))): errors.append(f'{aid}: framework_compatibility {a.get("framework_compatibility")} excludes VERSION {v}')
    for aid in supported+candidates:
        if aid not in seen: errors.append(f'{aid}: listed in manifest but platforms/{aid}/adapter.yaml is missing')
    return supported

def check_contract_schemas(manifest,errors):
    declared=manifest.get('contract_schema_versions')
    if not isinstance(declared,dict): errors.append('VCGF-MANIFEST contract_schema_versions block missing'); return
    expected={}
    for d in sorted((ROOT/'schemas').glob('v*')):
        if not d.is_dir() or not SEMVER.fullmatch(d.name[1:]): continue
        for p in sorted(d.glob('*.schema.json')):
            name=p.name[:-len('.schema.json')]
            if name=='common': continue
            if name in expected: errors.append(f'contract schema {name} exists under more than one schema version directory')
            expected[name]=d.name[1:]
    for name,ver in expected.items():
        if name not in declared: errors.append(f'contract_schema_versions missing {name} (schemas/v{ver})')
        elif str(declared[name])!=ver: errors.append(f'contract_schema_versions {name}: {declared[name]} != directory version {ver}')
    for name in declared:
        if name not in expected: errors.append(f'contract_schema_versions lists unknown schema {name}')

def main():
    errors=[]; v=read('VERSION').strip(); manifest=load_yaml(ROOT/'VCGF-MANIFEST.yaml') or {}
    if not SEMVER.fullmatch(v): fail_if([f'Invalid stable semantic VERSION: {v}'])
    if str(manifest.get('framework_version'))!=v: errors.append(f"VCGF-MANIFEST framework_version {manifest.get('framework_version')} != VERSION {v}")
    if manifest.get('release_status') not in RELEASE_STATUSES: errors.append(f"framework release_status must be one of {sorted(RELEASE_STATUSES)}, got {manifest.get('release_status')!r}")
    supported=check_adapters(v,manifest,errors)
    first=next((l for l in read('CHANGELOG.md').splitlines() if l.startswith('## [')),None)
    if first is None or not first.startswith(f'## [{v}]'): errors.append(f'CHANGELOG first release heading must be ## [{v}] ..., got {first!r}')
    if str(load_yaml(ROOT/'CITATION.cff').get('version'))!=v: errors.append('CITATION version mismatch')
    if str(load_yaml(ROOT/'spec/control-catalog.yaml').get('framework_version'))!=v: errors.append('control-catalog framework_version mismatch (regenerate spec/control-catalog.yaml)')
    for rp in ('README.md','README.ar.md'):
        if f'badge/version-{v}-' not in read(rp): errors.append(f'{rp}: version badge does not advertise {v}')
    if LEGACY_VERSION_CLAIM.search(read('runtime/bootstrap.md')): errors.append('runtime/bootstrap.md asserts a fixed VERSION; only the VERSION file is authoritative')
    for aid in supported:
        gp=ROOT/'docs/platform-guides'/f'{aid}.md'
        if not gp.is_file(): errors.append(f'missing platform guide docs/platform-guides/{aid}.md')
        else:
            gt=gp.read_text(encoding='utf-8')
            if f'**Framework:** VCGF {v}' not in gt: errors.append(f'docs/platform-guides/{aid}.md: metadata line must state **Framework:** VCGF {v}')
            stale=sorted({m for m in re.findall(r'VCGF (\d+\.\d+\.\d+)',gt) if m!=v})
            if stale: errors.append(f'docs/platform-guides/{aid}.md: mentions framework version(s) {stale} other than VERSION {v}')
    major,minor=v.split('.')[:2]; notes=ROOT/'docs/quality'/f'v{major}.{minor}'/f'release-notes-v{v}.md'
    if not notes.is_file(): errors.append(f'missing release notes {rel(notes)}')
    check_contract_schemas(manifest,errors)
    fail_if(errors); print('PASS validate-version')
if __name__=='__main__': main()
