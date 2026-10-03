# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import hashlib
from datetime import datetime,timezone
import yaml
from .contracts import ROOT, validate_contract
from .context import instant
from .loader import confined


def evaluate(record, artifact_root, expected, trusted_review=None, now=None):
    """Result claims inspected evidence, not that this function executed tests."""
    errors=validate_contract('evidence',record)
    if errors:return {'status':'FAIL','errors':errors,'exceptions':[]}
    now=now or datetime.now(timezone.utc)
    for field in ['code_sha256','policy_sha256','environment','profile','scope']:
        if field not in expected or record[field]!=expected[field]:errors.append('changed evidence binding: '+field)
    if not instant(record['created_at'])<=now<instant(record['valid_until']):errors.append('stale/future evidence')
    if instant(record['reviewer']['reviewed_at'])>now:errors.append('review in future')
    if instant(record['privacy']['retention_until'])<=now:errors.append('retention expired')
    if record['scope']['kind'] in ['project','release']:
        path=ROOT/'profiles'/record['profile']/'profile.yaml'
        if not path.is_file():errors.append('unknown profile');required=set()
        else:required=set(yaml.safe_load(path.read_text())['required_controls'])
    else:
        required=set(expected.get('required_control_ids',[]))
        if not required:errors.append('trusted task coverage set missing')
    required.update(expected.get('overlay_required_control_ids',[]))
    if not required <= set(record['required_control_ids']):errors.append('incomplete required coverage')
    if trusted_review is None:errors.append('trusted reviewer adapter unavailable')
    else:
        try:
            if trusted_review(record) is not True:errors.append('review authority rejected')
        except Exception:errors.append('review adapter failed closed')
    for artifact in record['artifacts']:
        try:
            path=confined(artifact_root,artifact['reference'])
            if hashlib.sha256(path.read_bytes()).hexdigest()!=artifact['sha256']:errors.append('artifact changed: '+artifact['artifact_id'])
        except (OSError,ValueError):errors.append('artifact missing/unsafe: '+artifact['artifact_id'])
    active_exceptions={}
    for item in record['exceptions']:
        if item['status']!='approved' or not instant(item['created_at'])<=now<instant(item['expires_at']) or now>=instant(item['review_at']):
            errors.append('exception expired/revoked/review due: '+item['exception_id'])
        else:active_exceptions[item['exception_id']]=item
    for c in record['controls']:
        if c['applicability']=='not_applicable':
            continue # reason is mandatory in schema; trusted review must assess it
        if c['verification']!='passed' or c['implementation']!='implemented' or c['support'] in ['unsupported','unverified']:
            if c.get('exception_ref') not in active_exceptions:errors.append('unverified/failed control: '+c['control_id'])
    if record['outstanding_findings']:errors.append('unresolved findings require explicit disposition')
    return {'status':'FAIL' if errors else ('CONDITIONAL' if active_exceptions else 'PASS'),
            'scope':record['scope'],'errors':errors,'exceptions':sorted(active_exceptions),
            'claim':'local evidence integrity and trusted review; no tests executed by evaluator'}
