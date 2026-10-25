# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from __future__ import annotations
from pathlib import Path
import re, json, yaml, subprocess

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {'.git', '__pycache__', '.pytest_cache', '.mypy_cache', '.venv', '.tox', '.coverage'}
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

def _excluded(p: Path):
    return any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts)

def tracked_files():
    """Deterministic repository enumeration: the files git tracks (``git ls-files -z``, no shell),
    so untracked local files cannot change validator or manifest results. Falls back to a filesystem
    walk with the same excluded directories when ROOT is not itself a git work tree (release archive)."""
    try:
        probe=subprocess.run(["git","rev-parse","--is-inside-work-tree","--show-toplevel"],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
        lines=probe.stdout.splitlines()
        if probe.returncode==0 and len(lines)>=2 and lines[0].strip()=="true" and Path(lines[1].strip()).resolve()==ROOT:
            listing=subprocess.run(["git","ls-files","-z"],cwd=ROOT,capture_output=True,check=True).stdout.decode("utf-8")
            files=[p for p in (ROOT/name for name in listing.split("\0") if name) if p.is_file() and not _excluded(p)]
            if files:
                return sorted(files,key=rel)
    except (OSError,subprocess.SubprocessError,UnicodeDecodeError):
        pass
    return sorted((p for p in ROOT.rglob("*") if p.is_file() and not _excluded(p)),key=rel)

def all_files():
    """Every repository file (tracked set, or the fallback walk) without the text-file filter."""
    return tracked_files()

def text_files():
    allowed={".md",".yaml",".yml",".json",".py",".cff",".mdc",".txt"}
    names={".gitignore",".gitattributes",".editorconfig","VERSION","LICENSE"}
    for p in all_files():
        if p.suffix.lower() in allowed or p.name in names:
            yield p

def write_generated(target: Path, text: str, name: str, check: bool=False) -> int:
    """Write generated text as UTF-8 with LF line endings, or with ``check`` compare it to the
    existing file (CRLF-normalised) without writing. Returns the process exit code."""
    if not check:
        target.write_text(text,encoding="utf-8",newline="\n"); return 0
    current=target.read_text(encoding="utf-8").replace("\r\n","\n") if target.is_file() else ""
    if current==text:
        print(f"PASS {name}: up to date"); return 0
    old,new=current.splitlines(),text.splitlines()
    line=next((i for i,(a,b) in enumerate(zip(old,new),1) if a!=b),min(len(old),len(new))+1)
    print(f"FAIL {name}: stale"); print(f"  first difference at line {line}; run without --check to regenerate")
    return 1
