# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Token accounting for loaded context: bytes are measured, tokens are estimated unless a tokenizer is opted in.

Three quantities are kept apart everywhere a budget is reported:
- bytes: UTF-8 size of the text actually served (measured);
- estimated tokens: a documented heuristic (ASCII characters / 4.0 + non-ASCII characters / 1.6), measurement 'estimated';
- observed tokens: only when the operator sets VCGF_TOKENIZER (for example 'tiktoken:cl100k_base') and that tokenizer is
  importable; measurement 'observed' then names the tokenizer, which is a reference, not necessarily the target model.
No value here is a measurement of the target model's tokenizer unless the operator configured that tokenizer explicitly.
"""
import math
import os
from functools import lru_cache

ASCII_CHARS_PER_TOKEN = 4.0
NON_ASCII_CHARS_PER_TOKEN = 1.6
ESTIMATE_METHOD = 'estimated: ASCII characters / 4.0 + non-ASCII characters / 1.6; not a tokenizer measurement'


def estimate(text):
    ascii_count = sum(1 for ch in text if ord(ch) < 128)
    return int(math.ceil(ascii_count / ASCII_CHARS_PER_TOKEN + (len(text) - ascii_count) / NON_ASCII_CHARS_PER_TOKEN))


@lru_cache(maxsize=1)
def _tokenizer(spec):
    name, _, encoding = spec.partition(':')
    if name == 'tiktoken':
        import tiktoken  # optional dependency; only when the operator opted in
        enc = tiktoken.get_encoding(encoding or 'cl100k_base')
        return f'tiktoken:{enc.name}', enc.encode
    raise ValueError(f'unsupported tokenizer specification: {spec!r}')


def configured_tokenizer():
    spec = os.environ.get('VCGF_TOKENIZER', '').strip()
    if not spec:
        return None
    try:
        return _tokenizer(spec)
    except Exception:  # missing package or unknown encoding: fall back to the estimate and say so
        return None


def count(text):
    """Return {'tokens', 'bytes', 'measurement', 'method'} for one text."""
    data = text.encode('utf-8')
    tokenizer = configured_tokenizer()
    if tokenizer:
        name, encode = tokenizer
        return {'tokens': len(encode(text)), 'bytes': len(data), 'measurement': 'observed',
                'method': f'observed with reference tokenizer {name} (VCGF_TOKENIZER); not necessarily the target model'}
    return {'tokens': estimate(text), 'bytes': len(data), 'measurement': 'estimated', 'method': ESTIMATE_METHOD}
