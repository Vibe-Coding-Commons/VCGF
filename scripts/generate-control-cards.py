# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Generate derived control cards (spec/control-cards/) from the canonical control Markdown.

A card keeps everything an agent needs to apply a control during a task: identity, requirement level, profiles, the
Requirement, the Implementation-Neutral Guidance and every control-specific section (Applicability, Verification
Method, Required Evidence, Dependencies, Related Controls). Sections whose text is shared verbatim by several controls
(Exceptions, Platform Considerations and the template variants of Applicability/Verification/Evidence/Dependencies/
Related Controls) are emitted once in spec/control-cards/common-clauses.md and referenced from the card by variant
letter, so nothing normative is lost; References stay in the card. Purpose, Risk Addressed, Rationale and Change
History stay in the full control text, which the card names. Cards are derived: the control Markdown remains the single normative source,
`--check` verifies the cards are current, and the Router loads cards in lean/standard mode and full controls in deep mode.
"""
import re
import sys

from vcgf_lib import *

CARDS = ROOT / 'spec' / 'control-cards'
COMMON = CARDS / 'common-clauses.md'
SHARED_CANDIDATES = ['Applicability', 'Verification Method', 'Required Evidence', 'Exceptions', 'Dependencies', 'Related Controls', 'Platform Considerations']
CARD_ONLY = ['Requirement', 'Implementation-Neutral Guidance', 'References']
DROPPED = ['Purpose', 'Risk Addressed', 'Rationale', 'Change History']
CANONICAL = ['Requirement', 'Purpose', 'Risk Addressed', 'Rationale', 'Applicability', 'Implementation-Neutral Guidance', 'Verification Method', 'Required Evidence', 'Exceptions', 'Dependencies', 'Related Controls', 'References', 'Platform Considerations', 'Change History']
SHORT = {'Applicability': 'Applicability', 'Verification Method': 'Verification', 'Required Evidence': 'Evidence', 'Exceptions': 'Exceptions',
         'Dependencies': 'Dependencies', 'Related Controls': 'Related', 'Platform Considerations': 'Platform'}
MIN_SHARED = 5  # a section text shared by at least this many controls is a common clause
SPDX = 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami | SPDX-License-Identifier: Apache-2.0'


def sections(text):
    end = text.find('\n---\n', 4)
    body = text[end + 5:] if end >= 0 else text
    out = {}; current = None
    for part in re.split(r'\n## ', '\n' + body)[1:]:
        name, _, content = part.partition('\n')
        name = name.strip()
        if name in CANONICAL:
            out[name] = content.strip(); current = name
        elif current is not None:  # a sub-heading inside a canonical section (for example '## CSP' under the guidance) stays with it
            out[current] = (out[current] + '\n\n## ' + name + '\n' + content.strip()).strip()
        else:
            out[name] = content.strip()
    return out


def normalise(text):
    return ' '.join(text.split())


def build(root=ROOT):
    catalog = load_yaml(root / 'spec/control-catalog.yaml')['controls']
    parsed = {}
    for c in catalog:
        parsed[c['id']] = (c, sections((root / c['path']).read_text(encoding='utf-8')))
    variants = {}  # section -> [text, ...] in first-seen order of controls sorted by id
    counts = {}
    for cid in sorted(parsed):
        _, secs = parsed[cid]
        for name in SHARED_CANDIDATES:
            text = secs.get(name)
            if text is None:
                continue
            counts[(name, normalise(text))] = counts.get((name, normalise(text)), 0) + 1
    for cid in sorted(parsed):
        _, secs = parsed[cid]
        for name in SHARED_CANDIDATES:
            text = secs.get(name)
            if text is not None and counts[(name, normalise(text))] >= MIN_SHARED:
                variants.setdefault(name, [])
                if normalise(text) not in [normalise(v) for v in variants[name]]:
                    variants[name].append(text)
    letter = {(name, normalise(v)): chr(65 + i) for name, vs in variants.items() for i, v in enumerate(vs)}
    files = {}
    lines = [f'<!-- {SPDX} | DERIVED by scripts/generate-control-cards.py from controls/; do not edit -->',
             '# Common control clauses',
             'Shared verbatim by five or more controls. A control card cites the variant letter that applies to it; the full control text is normative.', '']
    for name in SHARED_CANDIDATES:
        for i, v in enumerate(variants.get(name, [])):
            lines.append(f'## {name} [{chr(65 + i)}]')
            lines.append(v)
            lines.append('')
    files[COMMON] = '\n'.join(lines).rstrip('\n') + '\n'
    for cid in sorted(parsed):
        c, secs = parsed[cid]
        out = [f'<!-- {SPDX} | DERIVED control card; normative text: {c["path"]} -->',
               f'# {cid} — {c["title"]}',
               f'{c["requirement_level"]} · {c["domain"]} · profiles: {", ".join(sorted(c["profiles"]))} · full text: {c["path"]}', '']
        out.append('## Requirement'); out.append(secs.get('Requirement', '').strip()); out.append('')
        guidance = secs.get('Implementation-Neutral Guidance', '').strip()
        guidance = re.sub(r'^# .*\n+', '', guidance).strip()
        if guidance:
            out.append('## Guidance'); out.append(guidance); out.append('')
        references = secs.get('References', '').strip()
        if references:
            out.append('## References'); out.append(references); out.append('')
        common_refs = []
        for name in SHARED_CANDIDATES:
            text = secs.get(name)
            if text is None:
                continue
            key = (name, normalise(text))
            if key in letter:
                common_refs.append(f'{SHORT[name]}[{letter[key]}]')
            else:
                out.append(f'## {name}'); out.append(text.strip()); out.append('')
        if common_refs:
            out.append('Common clauses (spec/control-cards/common-clauses.md): ' + ' '.join(common_refs))
            out.append('')
        files[CARDS / f'{cid}.md'] = '\n'.join(out).rstrip('\n') + '\n'
    return files, variants


def main():
    check = '--check' in sys.argv
    files, variants = build()
    expected = set(files)
    stale = sorted(p for p in CARDS.glob('*.md') if p.name != 'README.md' and p not in expected)
    differences = []
    for path, content in files.items():
        current = path.read_text(encoding='utf-8') if path.is_file() else None
        if current is not None and current.replace('\r\n', '\n') == content:
            continue
        differences.append(rel(path))
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    if check:
        errors = [f'{d}: control card is stale; run scripts/generate-control-cards.py' for d in differences]
        errors += [f'{rel(p)}: card has no control in the catalog' for p in stale]
        fail_if(errors)
        print(f'PASS generate-control-cards: {len(files) - 1} cards and common clauses up to date')
        return
    for p in stale:
        p.unlink()
    shared = sum(len(v) for v in variants.values())
    print(f'generated {len(files) - 1} control cards and common clauses ({shared} shared clause variants); changed {len(differences)}, removed {len(stale)}')


if __name__ == '__main__':
    main()
