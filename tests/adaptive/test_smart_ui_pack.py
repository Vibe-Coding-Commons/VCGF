# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / 'packs/ux/smart-ui'


def test_smart_ui_pack_shape():
    assert PACK.is_dir()
    assert len(list((PACK / 'standards').glob('VCGF-UI-COMP-*.md'))) == 36
    assert len(list((PACK / 'interactions').glob('VCGF-UI-INT-*.md'))) == 24
    assert len(list((PACK / 'screen-compositions').glob('VCGF-UI-SCR-*.md'))) == 20
    assert len(list((PACK / 'journeys').glob('VCGF-UI-JRN-*.md'))) == 18
    assert (PACK / 'external-standards/CALENDAR-GOVERNANCE-ADDENDUM.md').is_file()
    assert (PACK / 'external-standards/ENTERPRISE-SEARCHABLE-SELECT-COMBOBOX.md').is_file()


def test_smart_ui_selector_no_ui_is_selective(tmp_path):
    context = {
        'project_id': 'vcgf-test',
        'screen_id': 'no-ui',
        'has_ui': False,
    }
    src = tmp_path / 'context.json'
    out = tmp_path / 'plan.json'
    src.write_text(json.dumps(context), encoding='utf-8')
    subprocess.run([
        sys.executable,
        str(PACK / 'scripts/select_smart_ui.py'),
        str(src), '--output', str(out)
    ], check=True, cwd=ROOT)
    plan = json.loads(out.read_text(encoding='utf-8'))
    assert plan['selection_status'] == 'no_ui'
    assert plan['selected_components'] == []
    assert plan['selected_interactions'] == []
    assert plan['selected_screen_compositions'] == []
    assert plan['selected_journeys'] == []


def test_runtime_pack_map_references_smart_ui():
    text = (ROOT / 'runtime/pack-map.yaml').read_text(encoding='utf-8')
    assert 'packs/ux/smart-ui/README.md' in text
    assert 'packs/ux/smart-ui/governance/MASTER-POLICY.md' in text
