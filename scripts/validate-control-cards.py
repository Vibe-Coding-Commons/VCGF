# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons
"""Semantic fidelity of the derived control cards against the canonical control Markdown.

Independent of the generator (it does not call it): for every catalog control the card plus the cited common clauses must
contain, verbatim, the Requirement, the Implementation-Neutral Guidance, the References and every applicability,
verification, evidence, exception, dependency, related-control and platform section; every normative sentence (MUST,
MUST NOT, SHOULD, SHALL) of the control appears in the loaded text; every control identifier the control names appears in
the loaded text; the header states the catalog level, domain and profiles and names the full text. Only Purpose,
Risk Addressed, Rationale and Change History may be absent, and the README must list them as the informative sections.
"""
import re

from vcgf_lib import *

CARDS = ROOT / 'spec' / 'control-cards'
KEPT = ['Requirement', 'Implementation-Neutral Guidance', 'References', 'Applicability', 'Verification Method', 'Required Evidence',
        'Exceptions', 'Dependencies', 'Related Controls', 'Platform Considerations']
INFORMATIVE = ['Purpose', 'Risk Addressed', 'Rationale', 'Change History']
CANONICAL = ['Requirement', 'Purpose', 'Risk Addressed', 'Rationale', 'Applicability', 'Implementation-Neutral Guidance', 'Verification Method', 'Required Evidence', 'Exceptions', 'Dependencies', 'Related Controls', 'References', 'Platform Considerations', 'Change History']
SHORT = {'Applicability': 'Applicability', 'Verification Method': 'Verification', 'Required Evidence': 'Evidence', 'Exceptions': 'Exceptions',
         'Dependencies': 'Dependencies', 'Related Controls': 'Related', 'Platform Considerations': 'Platform'}
CONTROL_ID = re.compile(r'VCGF-[A-Z]+-\d{3}')
NORMATIVE = re.compile(r'[^.!?\n]*\b(MUST NOT|MUST|SHALL NOT|SHALL|SHOULD NOT|SHOULD)\b[^.!?\n]*')


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


def norm(text):
    return ' '.join(text.split())


def main():
    errors = []
    catalog = load_yaml(ROOT / 'spec/control-catalog.yaml')['controls']
    common_text = (CARDS / 'common-clauses.md').read_text(encoding='utf-8') if (CARDS / 'common-clauses.md').is_file() else ''
    common = {}
    for part in re.split(r'\n## ', '\n' + common_text)[1:]:
        head, _, content = part.partition('\n')
        m = re.match(r'(.+?) \[([A-Z])\]$', head.strip())
        if m:
            common[(m.group(1), m.group(2))] = content.strip()
    readme = (CARDS / 'README.md').read_text(encoding='utf-8') if (CARDS / 'README.md').is_file() else ''
    for name in INFORMATIVE:
        if name not in readme:
            errors.append(f'spec/control-cards/README.md: informative section {name!r} not declared as left in the full text')
    for c in catalog:
        cid = c['id']; card_path = CARDS / f'{cid}.md'
        if not card_path.is_file():
            errors.append(f'{cid}: card missing'); continue
        control = (ROOT / c['path']).read_text(encoding='utf-8'); card = card_path.read_text(encoding='utf-8')
        secs = sections(control)
        cited = dict(re.findall(r'(\w+)\[([A-Z])\]', card.split('Common clauses (spec/control-cards/common-clauses.md):')[1]) if 'Common clauses (spec/control-cards/common-clauses.md):' in card else [])
        loaded = norm(card)
        for short, letter in cited.items():
            name = next((k for k, v in SHORT.items() if v == short), None)
            text = common.get((name, letter)) if name else None
            if text is None:
                errors.append(f'{cid}: cites unknown common clause {short}[{letter}]'); continue
            loaded += ' ' + norm(text)
        lines = card.splitlines()
        if len(lines) < 3 or not lines[1].startswith(f'# {cid} '):
            errors.append(f'{cid}: card header does not start with the control identifier'); continue
        header = lines[2]
        for expected in [c['requirement_level'], c['domain'], c['path'], 'profiles: ' + ', '.join(sorted(c['profiles']))]:
            if expected not in header:
                errors.append(f'{cid}: header lacks {expected!r}')
        for name in KEPT:
            text = secs.get(name)
            if text is None:
                continue
            body = norm(re.sub(r'^# .*\n+', '', text) if name == 'Implementation-Neutral Guidance' else text)
            if body and body not in loaded:
                errors.append(f'{cid}: section {name!r} is not carried verbatim by the card or its cited common clauses')
        for name in secs:
            if name not in KEPT and name not in INFORMATIVE:
                errors.append(f'{cid}: unexpected section {name!r} in the control; the card policy does not cover it')
        kept_text = ' '.join(secs.get(n, '') for n in KEPT)
        for sentence in NORMATIVE.finditer(kept_text):
            if norm(sentence.group(0)) not in loaded:
                errors.append(f'{cid}: normative sentence missing from loaded text: {norm(sentence.group(0))[:80]!r}')
        for ref in sorted(set(CONTROL_ID.findall(kept_text)) - {cid}):
            if ref not in loaded:
                errors.append(f'{cid}: referenced control {ref} is not present in the loaded text')
        if card.count('<!--') != 1 or not card.startswith('<!-- SPDX-FileCopyrightText'):
            errors.append(f'{cid}: card must start with exactly one attribution comment')
    fail_if(errors)
    print(f'PASS validate-control-cards: {len(catalog)} cards semantically complete against their controls')


if __name__ == '__main__':
    main()
