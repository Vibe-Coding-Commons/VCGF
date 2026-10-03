# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Gate for integration into a trusted host. JSON cannot authenticate its author."""
from datetime import datetime, timezone
from .contracts import validate_contract
from .context import instant


def approval_gate(record, expected, authenticate=None, revoked=(), now=None):
    errors=validate_contract('approval',record)
    if errors:return {'allowed':False,'errors':errors}
    now=now or datetime.now(timezone.utc)
    if record['status']!='approved':errors.append('not approved')
    if record['approval_id'] in revoked:errors.append('revoked')
    if not instant(record['issued_at'])<=now<instant(record['expires_at']):errors.append('approval expired/not yet valid')
    if record.get('decision_at') and instant(record['decision_at'])>now:errors.append('decision is in future')
    for field in ['action','resources','environment','plan_sha256','action_sha256','policy_sha256']:
        if field not in expected or record[field]!=expected[field]:errors.append('scope changed: '+field)
    if authenticate is None:errors.append('trusted identity adapter unavailable')
    else:
        try:
            if authenticate(record) is not True:errors.append('authority not authenticated')
        except Exception:
            errors.append('identity adapter failed closed')
    return {'allowed':not errors,'errors':errors,'scope':'host-gate only; not blanket execution permission'}


def guarded_call(record, expected, operation, authenticate=None, revoked=(), now=None):
    """Host must own operation, expected scope, authenticator and revocation store."""
    decision=approval_gate(record,expected,authenticate,revoked,now)
    if not decision['allowed']:raise PermissionError('; '.join(decision['errors']))
    return operation()
