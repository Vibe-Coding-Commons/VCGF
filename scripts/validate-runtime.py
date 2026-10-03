# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from runtime.registry import build_registry
from runtime.resolver import resolve
registry=build_registry()
for c in registry['capabilities']:
    resolve(registry['capabilities'],[c['capability_id']],{'auth-model':'local-password','public-indexable':True})
print('PASS local capability schemas, canonical references and resolvable synthetic graph; no product/runtime integration claim')
