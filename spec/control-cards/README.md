<!--
VCGF — Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Founder & Maintainer: Eng. Hamada Sami
Email: i@hamada.io
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Control cards (derived)

Every file here except this README is **generated** by `scripts/generate-control-cards.py` from the canonical control Markdown under `controls/`. The control Markdown is the only normative source; a card is the compact form the Task Router loads into an agent's context in `lean` and `standard` mode (`deep` mode loads the full control text). `scripts/generate-control-cards.py --check` fails the release gate when a card is stale.

A card keeps, verbatim: the control identity (ID, title, requirement level, domain, profiles, path of the full text), the **Requirement**, the **Implementation-Neutral Guidance**, the **References**, and every control-specific section (Applicability, Verification Method, Required Evidence, Dependencies, Related Controls). Sections whose text is shared verbatim by five or more controls (the Exceptions and Platform Considerations clauses and the template variants of the other sections) are emitted once in `common-clauses.md` and cited from the card by variant letter, so nothing normative is dropped from the loaded context. Purpose, Risk Addressed, Rationale and Change History (the informative sections) remain in the full control text. `scripts/validate-control-cards.py` independently checks, for every control, that the card plus its cited common clauses carry every kept section, every normative sentence and every referenced control identifier verbatim.

The loader strips HTML comments (the attribution header of every file) from the text it serves while hashing the file bytes as stored, so the attribution stays in the repository and costs no context. Cards do not change Control IDs, requirement levels or texts; editing a card is useless because the generator overwrites it.
