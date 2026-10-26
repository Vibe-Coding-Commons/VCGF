# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
import json
import os
from pathlib import Path

import pytest

from runtime.adaptive.common import (InputError, MAX_BYTES, bound_object, canonical_sha,
    checked_relative, json_bytes, load_catalog, parse_time, read_json, read_source, validate)
from conftest import ROOT


@pytest.mark.parametrize('body', [b'{"a":1,"a":2}', b'{"a":NaN}', b'Infinity', b'1e999', b'{', b'\xff', b'['*2000+b']'*2000])
def test_bad_json(body):
    with pytest.raises(InputError):
        json_bytes(body)


def test_oversized_json():
    with pytest.raises(InputError):
        json_bytes(b' '*(MAX_BYTES+1))


def test_unicode_hash_order_is_stable():
    assert canonical_sha({'b': 2, 'a': '\u0627'}) == canonical_sha({'a': '\u0627', 'b': 2})


@pytest.mark.parametrize('data', [{1: 'x'}, {'value': object()}, {'float': float('nan')}, ['x']*20001])
def test_non_json_and_excessive_nodes(data):
    with pytest.raises(InputError):
        bound_object(data)


def test_cyclic_data_rejected():
    data=[];data.append(data)
    with pytest.raises(InputError):
        bound_object(data)


@pytest.mark.parametrize('value', ['2026-10-21', '2026-10-21T12:00:00', '2026-02-30T12:00:00Z', '2026-10-21T12:00:00+99:00'])
def test_invalid_timestamp(value):
    with pytest.raises(InputError):
        parse_time(value)


@pytest.mark.parametrize('value', ['2026-10-21T12:00:00Z','2026-10-21T15:00:00+03:00'])
def test_aware_timestamp(value):
    assert parse_time(value).utcoffset().total_seconds() in (0,10800)


@pytest.mark.parametrize('path', ['', '../outside', '/etc/passwd', 'a/../b', 'C:/data', 'C:\\data', 'a//b', './a', 'a/./b', '.env', 'cfg/.env.production', '.git/config', '.ssh/id_rsa', 'private.pem', 'https://host/file', 'a\x00b'])
def test_unsafe_source_names(path):
    with pytest.raises(InputError):
        checked_relative(path)


def test_read_only_explicit_source(tmp_path):
    (tmp_path/'docs').mkdir();(tmp_path/'docs/brief.md').write_text('verified')
    assert read_source(tmp_path,'docs/brief.md') == b'verified'


def _symlink(link, target, **kw):
    try:
        link.symlink_to(target, **kw)
    except (OSError, NotImplementedError) as exc:  # Windows without the symlink privilege
        pytest.skip(f'symlinks unavailable here: {exc}')


def test_source_symlinks_rejected(tmp_path):
    (tmp_path/'real').write_text('x');_symlink(tmp_path/'link',tmp_path/'real')
    with pytest.raises(InputError):
        read_source(tmp_path,'link')


def test_directory_symlink_rejected(tmp_path):
    (tmp_path/'real').mkdir();(tmp_path/'real/a.md').write_text('x');_symlink(tmp_path/'alias',tmp_path/'real',target_is_directory=True)
    with pytest.raises(InputError):
        read_source(tmp_path,'alias/a.md')


def test_missing_source_fails_closed(tmp_path):
    with pytest.raises(InputError):
        read_source(tmp_path,'absent.md')


def test_source_size_limit(tmp_path):
    (tmp_path/'large.md').write_bytes(b'x'*(MAX_BYTES+1))
    with pytest.raises(InputError):
        read_source(tmp_path,'large.md')


def test_fifo_is_not_read_or_blocked(tmp_path):
    if not hasattr(os,'mkfifo'):
        pytest.skip('POSIX FIFO test is platform-specific')
    os.mkfifo(tmp_path/'pipe')
    with pytest.raises(InputError):
        read_source(tmp_path,'pipe')


def test_json_symlink_and_directory(tmp_path):
    (tmp_path/'a.json').write_text('{}');_symlink(tmp_path/'link',tmp_path/'a.json')
    for path in [tmp_path/'link',tmp_path]:
        with pytest.raises(InputError):
            read_json(path)


def test_catalog_cache_invalidates_and_does_not_leak_mutation(tmp_path):
    path=tmp_path/'catalog.yaml';path.write_text('name: first\n')
    first=load_catalog(path);first['name']='changed'
    assert load_catalog(path)['name']=='first'
    path.write_text('name: second\n')
    assert load_catalog(path)['name']=='second'


def test_invalid_catalog_shape(tmp_path):
    path=tmp_path/'catalog.yaml';path.write_text('- not-a-map\n')
    with pytest.raises(InputError):
        load_catalog(path)


def test_schema_extra_property_is_rejected(case):
    fp,_,_=case;fp['execute_shell']='rm -rf /'
    with pytest.raises(InputError):
        validate(ROOT/'schemas/v1.2.0/project-fingerprint.schema.json',fp)


def test_schema_remote_resolution_forbidden(tmp_path):
    path=tmp_path/'schema.json';path.write_text(json.dumps({'$schema':'https://json-schema.org/draft/2020-12/schema','$ref':'https://example.invalid/remote.json'}))
    with pytest.raises(InputError, match='remote retrieval is forbidden'):
        validate(path,{})

@pytest.mark.parametrize('stamp', ['2026-10-21T00:00:00+00:60', '2026-10-21T00:00:00+24:00'])
def test_invalid_timezone_offsets(stamp):
    with pytest.raises(InputError): parse_time(stamp)
