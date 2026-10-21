# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Bounded offline input, immutable fingerprints and local contract validation."""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import stat
from copy import deepcopy
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry
from referencing.exceptions import Unresolvable

MAX_BYTES = 1_048_576
MAX_DEPTH = 32
MAX_NODES = 20_000
FORMATS = FormatChecker()


class InputError(ValueError):
    """Invalid, stale or unsafe planning input; never an execution instruction."""


def parse_time(value: str) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(
        r'\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)', value
    ):
        raise InputError('A timezone-aware RFC3339 timestamp is required')
    try:
        return datetime.fromisoformat(value.upper().replace('Z', '+00:00'))
    except ValueError as exc:
        raise InputError('Invalid calendar timestamp') from exc


@FORMATS.checks('date-time', raises=(ValueError, TypeError))
def _timestamp(value: Any) -> bool:
    return True if not isinstance(value, str) else parse_time(value).tzinfo is not None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def bound_object(value: Any) -> None:
    """Reject cyclic/oversized or non-JSON data before recursive libraries see it."""
    pending_nodes = [(value, 0)]
    count = 0
    while pending_nodes:
        item, depth = pending_nodes.pop()
        count += 1
        if depth > MAX_DEPTH or count > MAX_NODES:
            raise InputError('Input complexity limit exceeded')
        if type(item) is dict:
            if any(type(k) is not str for k in item):
                raise InputError('JSON object keys must be strings')
            pending_nodes.extend((x, depth + 1) for x in item.values())
        elif type(item) is list:
            pending_nodes.extend((x, depth + 1) for x in item)
        elif type(item) is float and not math.isfinite(item):
            raise InputError('Non-finite numbers are forbidden')
        elif type(item) not in (str, int, float, bool, type(None)):
            raise InputError('Only JSON-compatible values are accepted')
        if type(item) is str and len(item.encode('utf-8')) > MAX_BYTES:
            raise InputError('String size limit exceeded')


def _unique_object(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError('Duplicate JSON object key')
        result[key] = value
    return result


def json_bytes(data: bytes) -> Any:
    if len(data) > MAX_BYTES:
        raise InputError('JSON byte limit exceeded')
    try:
        value = json.loads(data.decode('utf-8'), object_pairs_hook=_unique_object,
                           parse_constant=lambda _: (_ for _ in ()).throw(InputError('Non-finite JSON number')))
        bound_object(value)
        return value
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise InputError('Invalid UTF-8 JSON or excessive nesting') from exc


def read_json(path: Path) -> Any:
    path = Path(path)
    if path.is_symlink():
        raise InputError('Input symlinks are forbidden')
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0)
    try:
        with os.fdopen(os.open(path, flags), 'rb') as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                raise InputError('A regular JSON file is required')
            return json_bytes(handle.read(MAX_BYTES + 1))
    except OSError as exc:
        raise InputError('Input file is unavailable or unsafe') from exc


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(payload: Any) -> str:
    bound_object(payload)
    return sha_bytes(json.dumps(payload, sort_keys=True, ensure_ascii=False,
                               separators=(',', ':'), allow_nan=False).encode('utf-8'))


def _offline(uri: str) -> Any:
    raise InputError('Remote schema retrieval is forbidden')


@lru_cache(maxsize=16)
def _validator(content: bytes) -> Draft202012Validator:
    schema = json_bytes(content)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FORMATS, registry=Registry(retrieve=_offline))


def validate(schema_path: Path, data: Any) -> None:
    bound_object(data)
    content = schema_path.read_bytes()
    try:
        errors = _validator(content).iter_errors(data)
        first = next(errors, None)
    except Unresolvable as exc:
        raise InputError('Schema references must resolve locally; remote retrieval is forbidden') from exc
    if first is not None:
        # Do not echo secrets or large attacker-supplied values in CLI errors.
        raise InputError(f'Contract violation at {first.json_path}: {first.validator}')


@lru_cache(maxsize=8)
def _catalog(content: bytes) -> dict:
    if len(content) > MAX_BYTES:
        raise InputError('Catalog byte limit exceeded')
    data = yaml.safe_load(content)
    bound_object(data)
    if not isinstance(data, dict):
        raise InputError('A mapping catalog is required')
    return data


def load_catalog(path: Path) -> dict:
    """Content-keyed cache invalidates on edit; callers cannot mutate shared data."""
    return deepcopy(_catalog(path.read_bytes()))


def checked_relative(reference: str) -> tuple[str, ...]:
    if not isinstance(reference, str) or not reference or '\x00' in reference or '\\' in reference or ':' in reference:
        raise InputError('Unsafe source reference')
    path = PurePosixPath(reference)
    if path.is_absolute() or PureWindowsPath(reference).drive or any(p in {'', '.', '..'} for p in reference.split('/')):
        raise InputError('Source must be a normalized project-relative path')
    for part in path.parts:
        lower = part.lower()
        if lower.startswith('.env') or lower in {'.git', '.ssh', '.aws', 'credentials'} or lower.endswith(('.pem', '.key', '.p12', '.pfx')):
            raise InputError('Sensitive source paths are not permitted')
    return path.parts


def read_source(root: Path, reference: str) -> bytes:
    """Read only an explicit regular source; reject symlinks beneath a trusted root.

    POSIX uses dir_fd/O_NOFOLLOW for every path component. On other systems the
    host must lock the project snapshot against concurrent replacement.
    """
    parts = checked_relative(reference)
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise InputError('Project root must be a real directory')
    if os.open in os.supports_dir_fd and hasattr(os, 'O_NOFOLLOW'):
        current = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            for part in parts[:-1]:
                nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=current)
                os.close(current)
                current = nxt
            fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=current)
            with os.fdopen(fd, 'rb') as handle:
                if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                    raise InputError('Source is not a regular file')
                data = handle.read(MAX_BYTES + 1)
        except OSError as exc:
            raise InputError('Source unavailable or symlink rejected') from exc
        finally:
            os.close(current)
    else:
        path = root
        for part in parts:
            path = path / part
            if path.is_symlink():
                raise InputError('Source symlinks are forbidden')
        if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
            raise InputError('Source escapes the project or is not a regular file')
        with path.open('rb') as handle:
            data = handle.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise InputError('Source byte limit exceeded')
    return data
