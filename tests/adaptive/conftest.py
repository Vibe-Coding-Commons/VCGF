# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import copy
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
NOW = datetime(2026, 10, 21, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def case(tmp_path):
    fp = json.loads((ROOT / 'examples/adaptive/fingerprint-laravel.json').read_text())
    ux = json.loads((ROOT / 'examples/adaptive/ux-crm.json').read_text())
    source = b'Synthetic product brief for contract integration tests. Not a deployed Laravel/React/Vue project.\n'
    (tmp_path / 'brief.md').write_bytes(source)
    digest = hashlib.sha256(source).hexdigest()
    for record in [fp, ux]:
        record['project_id'] = 'synthetic-contract-project'
        record['captured_at'] = NOW.isoformat()
    fp['sources'] = [{'path': 'brief.md', 'sha256': digest, 'kind': 'local_file'}]
    ux['source_refs'] = [{'ref': 'brief.md', 'sha256': digest, 'kind': 'product_document', 'confidence': 'reported'}]
    return copy.deepcopy(fp), copy.deepcopy(ux), tmp_path
