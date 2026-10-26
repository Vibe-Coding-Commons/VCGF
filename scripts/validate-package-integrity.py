# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

"""Repository-level integrity validator for frozen packages (finding V13-006).

Every frozen package ships a SHA256SUMS.txt and a manifest.json. This validator
re-hashes the bytes actually present in the tree and fails the release gate when
the tree, the manifest and the checksum list disagree in any way, so a tampered,
added or dropped instruction file cannot ship under the frozen package's name.
All problems are collected before failing; nothing is truncated.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from vcgf_lib import ROOT, fail_if

PACKAGES=[('packs/ux/smart-ui','SHA256SUMS.txt','manifest.json')]
SUM_LINE=re.compile(r'^([0-9a-f]{64})  (.+)$')
HEX64=re.compile(r'^[0-9a-f]{64}$')


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1<<20), b''): h.update(chunk)
    return h.hexdigest()


def path_problem(p):
    """Reason a listed path is unsafe, or None when it is a plain relative POSIX path inside the package."""
    if not isinstance(p,str) or not p: return 'empty or non-string path'
    if any(ord(c)<32 for c in p): return 'control character in path'
    if '\\' in p: return 'backslash in path'
    if p.startswith('/') or re.match(r'^[A-Za-z]:',p): return 'absolute path'
    parts=p.split('/')
    if '..' in parts: return "'..' segment in path"
    if any(part in ('','.') for part in parts): return 'malformed path segment'
    return None


def actual_files(pkg: Path, exclusions):
    out=set()
    for p in pkg.rglob('*'):
        if not p.is_file(): continue
        r=p.relative_to(pkg)
        if '__pycache__' in r.parts: continue
        rp=r.as_posix()
        if rp not in exclusions: out.add(rp)
    return out


def parse_sums(text, label, errors):
    sums={}
    lines=text.split('\n')
    if lines and lines[-1]=='': lines.pop()
    for n,line in enumerate(lines,1):
        m=SUM_LINE.match(line)
        if not m: errors.append(f'{label}:{n}: malformed checksum line (expected "<sha256>  <relative path>")'); continue
        digest,rp=m.groups()
        why=path_problem(rp)
        if why: errors.append(f'{label}:{n}: {why}: {rp!r}'); continue
        if rp in sums: errors.append(f'{label}:{n}: duplicate entry for {rp}'); continue
        sums[rp]=digest
    return sums


def parse_manifest(path: Path, label, errors):
    """Return (exclusions, {path: (bytes, sha256)}) or None when the manifest is unusable."""
    try: data=json.loads(path.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{label}: invalid JSON: {e}'); return None
    if not isinstance(data,dict): errors.append(f'{label}: top-level JSON must be an object'); return None
    if data.get('hash_algorithm')!='sha256': errors.append(f"{label}: hash_algorithm must be 'sha256', got {data.get('hash_algorithm')!r}")
    excl=data.get('exclusions')
    if not isinstance(excl,list) or not all(isinstance(x,str) for x in excl): errors.append(f'{label}: exclusions must be a list of relative paths'); excl=[]
    files=data.get('files')
    if not isinstance(files,list): errors.append(f'{label}: files must be a list of {{path, bytes, sha256}} objects'); files=[]
    entries={}
    for i,e in enumerate(files):
        where=f'{label}: files[{i}]'
        if not isinstance(e,dict): errors.append(f'{where}: entry must be an object'); continue
        rp,size,digest=e.get('path'),e.get('bytes'),e.get('sha256')
        why=path_problem(rp)
        if why: errors.append(f'{where}: {why}: {rp!r}'); continue
        if not isinstance(size,int) or isinstance(size,bool) or size<0: errors.append(f'{where} ({rp}): bytes must be a non-negative integer'); size=None
        if not isinstance(digest,str) or not HEX64.match(digest): errors.append(f'{where} ({rp}): sha256 must be 64 lowercase hex characters'); digest=None
        if rp in entries: errors.append(f'{where}: duplicate entry for {rp}'); continue
        entries[rp]=(size,digest)
    return set(excl),entries


def check_package(root: Path, pkg_rel, sums_name, manifest_name, errors):
    """Append every problem found in one package to errors; return the number of distinct paths verified."""
    pkg=root/pkg_rel
    if not pkg.is_dir(): errors.append(f'{pkg_rel}: package directory missing'); return 0
    sums_label,manifest_label=f'{pkg_rel}/{sums_name}',f'{pkg_rel}/{manifest_name}'
    sums_path,manifest_path=pkg/sums_name,pkg/manifest_name
    if not sums_path.is_file(): errors.append(f'{sums_label}: missing'); return 0
    if not manifest_path.is_file(): errors.append(f'{manifest_label}: missing'); return 0
    digests={}
    def digest_of(rp):
        if rp not in digests: digests[rp]=sha256(pkg/rp)
        return digests[rp]

    sums_raw=sums_path.read_bytes()
    if b'\r' in sums_raw: errors.append(f'{sums_label}: checksum file must use LF line endings (CR found)')
    sums=parse_sums(sums_raw.decode('utf-8','replace'),sums_label,errors)
    for rp,digest in sums.items():
        if not (pkg/rp).is_file(): errors.append(f'{sums_label}: listed file missing: {rp}'); continue
        actual=digest_of(rp)
        if actual!=digest: errors.append(f'{pkg_rel}/{rp}: sha256 mismatch against {sums_name} (expected {digest}, actual {actual})')

    parsed=parse_manifest(manifest_path,manifest_label,errors)
    if parsed is None: return len(sums)
    exclusions,entries=parsed
    for required in (sums_name,manifest_name):
        if required not in exclusions: errors.append(f'{manifest_label}: exclusions must include {required}')
    for rp,(size,digest) in entries.items():
        f=pkg/rp
        if not f.is_file(): errors.append(f'{manifest_label}: listed file missing: {rp}'); continue
        actual_size=f.stat().st_size
        if size is not None and actual_size!=size: errors.append(f'{pkg_rel}/{rp}: size mismatch against {manifest_name} (expected {size} bytes, actual {actual_size})')
        actual=digest_of(rp)
        if digest is not None and actual!=digest: errors.append(f'{pkg_rel}/{rp}: sha256 mismatch against {manifest_name} (expected {digest}, actual {actual})')

    for rp in sorted(actual_files(pkg,exclusions)-set(entries)): errors.append(f'{pkg_rel}/{rp}: present in package but not listed in {manifest_name}')
    expected_sums=set(entries)|{manifest_name}
    for rp in sorted(set(sums)-expected_sums): errors.append(f'{sums_label}: lists {rp} which is not in {manifest_name}')
    for rp in sorted(expected_sums-set(sums)): errors.append(f'{sums_label}: missing entry for {rp}')
    for rp in sorted(set(sums)&set(entries)):
        if entries[rp][1] is not None and sums[rp]!=entries[rp][1]: errors.append(f'{pkg_rel}/{rp}: {sums_name} digest disagrees with {manifest_name}')
    return len(set(sums)|set(entries))


def main(argv=None):
    ap=argparse.ArgumentParser(description='Verify frozen package checksum lists and manifests against the bytes present in the tree.')
    ap.add_argument('--root',type=Path,default=ROOT,help='repository root to validate (default: this checkout)')
    args=ap.parse_args(argv)
    root=args.root.resolve()
    errors=[]; results=[]
    for pkg_rel,sums_name,manifest_name in PACKAGES:
        results.append((pkg_rel,check_package(root,pkg_rel,sums_name,manifest_name,errors)))
    fail_if(errors)
    for pkg_rel,n in results: print(f'PASS validate-package-integrity: {n} files verified in {pkg_rel}')

if __name__=='__main__': main()
