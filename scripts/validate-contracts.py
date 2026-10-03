# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Founder & Maintainer: Eng. Hamada Sami
"""Read one contract instance; never execute its commands or fetch references."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from runtime.contracts import NAMES, validate_contract


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", choices=sorted(NAMES))
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.file.read_text(encoding="utf-8"))
        errors = validate_contract(args.contract, record)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "input_error", "message": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({"contract": args.contract, "accepted": not errors,
                      "claim": "structural_and_local_coherence_only",
                      "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
