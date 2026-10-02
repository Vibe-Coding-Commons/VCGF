# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from __future__ import annotations
from pathlib import Path
import re, json, yaml

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_MAPPING = {"NATIVE","CONFIGURABLE","PROMPT-ENFORCED","EXTERNAL","PARTIAL","UNSUPPORTED","NOT-APPLICABLE","UNVERIFIED"}
DOMAINS = {"governance","ai-governance","architecture","security","identity-access","data-protection","privacy","database","api","secrets","dependencies","file-handling","logging-auditing","testing","release","operations","incident-response"}
PROFILE_IDS = {"baseline","production","high-assurance"}
ADAPTER_IDS = {"generic","lovable","claude","bolt","v0","replit","cursor"}

class ValidationError(RuntimeError):
    pass

def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)

def control_files():
    return sorted(p for p in (ROOT/"controls").rglob("*.md") if p.name != "README.md")

def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValidationError(f"missing YAML front matter: {path.relative_to(ROOT)}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValidationError(f"unterminated YAML front matter: {path.relative_to(ROOT)}")
    data = yaml.safe_load(text[4:end]) or {}
    body = text[end+5:]
    return data, body

def control_index():
    result = {}
    for p in control_files():
        meta,_=parse_frontmatter(p)
        cid=meta.get("id")
        if cid in result:
            raise ValidationError(f"duplicate control ID {cid}: {p} and {result[cid]}")
        result[cid]=p
    return result

def fail_if(errors):
    errors=[str(e) for e in errors if e]
    if errors:
        raise ValidationError("\n".join(errors))

def rel(path: Path):
    return path.relative_to(ROOT).as_posix()

def text_files():
    allowed={".md",".yaml",".yml",".json",".py",".cff",".mdc",".txt"}
    names={".gitignore",".gitattributes",".editorconfig","VERSION","LICENSE"}
    for p in ROOT.rglob("*"):
        if p.is_file() and (p.suffix.lower() in allowed or p.name in names):
            yield p
