# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
#
# Deterministic CycloneDX 1.5 SBOM for the Python requirements declared in the
# repository. Only exact 'name==version' pins become components; range or other
# specifiers are recorded as properties so that unpinned inputs stay visible.

from pathlib import Path
import argparse, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENT_FILES = ['requirements-dev.txt', 'requirements-quality.txt', 'examples/integrations/requirements.txt']
PIN_RX = re.compile(r'^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]*\])?\s*===?\s*(?P<version>[A-Za-z0-9][A-Za-z0-9._+!-]*)\s*(;.*)?$')
RANGE_RX = re.compile(r'^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]*\])?\s*(~=|!=|<=|>=|<|>)')

def purl_name(name):
    return re.sub(r'[-_.]+', '-', name).lower()

def parse_requirements(rel_path, errors):
    p = ROOT / rel_path
    if not p.is_file():
        errors.append(f'missing requirements file: {rel_path}'); return [], []
    components, notes = [], []
    for raw in p.read_text(encoding='utf-8').splitlines():
        line = raw.split('#', 1)[0].strip() if not raw.lstrip().startswith('#') else ''
        if not line:
            continue
        m = PIN_RX.match(line)
        if m:
            name, version = m.group('name'), m.group('version')
            components.append({'type': 'library', 'name': name, 'version': version, 'purl': f'pkg:pypi/{purl_name(name)}@{version}'})
            continue
        kind = 'vcgf:unpinned-requirement' if RANGE_RX.match(line) else 'vcgf:unparsed-requirement'
        notes.append({'name': kind, 'value': f'{rel_path}: {line}'})
    return components, notes

def build_sbom(timestamp=None):
    errors, components, notes = [], [], []
    for rel_path in REQUIREMENT_FILES:
        c, n = parse_requirements(rel_path, errors)
        components.extend(c); notes.extend(n)
    if errors:
        raise SystemExit('FAIL generate-sbom\n' + '\n'.join(errors))
    unique = {(c['name'].lower(), c['version']): c for c in components}
    ordered = [unique[k] for k in sorted(unique)]
    metadata = {}
    if timestamp:
        metadata['timestamp'] = timestamp
    metadata['component'] = {'type': 'application', 'name': 'VCGF', 'version': (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
                             'licenses': [{'license': {'id': 'Apache-2.0'}}], 'copyright': '2026 Eng. Hamada Sami'}
    sbom = {'bomFormat': 'CycloneDX', 'specVersion': '1.5', 'version': 1, 'metadata': metadata, 'components': ordered}
    if notes:
        sbom['properties'] = sorted(notes, key=lambda n: (n['name'], n['value']))
    return sbom

def main():
    ap = argparse.ArgumentParser(description='Emit a deterministic CycloneDX 1.5 SBOM of the pinned Python requirements.')
    ap.add_argument('--output', help='destination path (default: stdout)')
    ap.add_argument('--timestamp', help='ISO-8601 timestamp to record in metadata (omitted by default for reproducibility)')
    a = ap.parse_args()
    text = json.dumps(build_sbom(a.timestamp), indent=2, ensure_ascii=False) + '\n'
    if a.output:
        out = Path(a.output); out.parent.mkdir(parents=True, exist_ok=True)
        with out.open('w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'PASS generate-sbom {a.output}')
    else:
        sys.stdout.write(text)

if __name__ == '__main__':
    main()
