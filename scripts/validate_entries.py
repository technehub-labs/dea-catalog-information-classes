#!/usr/bin/env python3
"""validate_entries.py: validate entities/**/*.yaml against the Information
Class JSON Schema (schemas/information-class.schema.json).

Run: python3 scripts/validate_entries.py [--strict]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import jsonschema
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "information-class.schema.json"
ENTITIES_GLOB = "entities/**/*.yaml"


def load_records() -> list[tuple[Path, dict]]:
    records = []
    for path in sorted(REPO_ROOT.glob(ENTITIES_GLOB)):
        with open(path) as f:
            data = yaml.safe_load(f)
        if isinstance(data, dict):
            records.append((path, data))
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    with open(SCHEMA_PATH) as f:
        schema = json.load(f)

    records = load_records()
    if not records:
        print(f"no records found under {ENTITIES_GLOB}")
        return 1

    failures = 0
    for path, record in records:
        errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(record), key=lambda e: e.path)
        if errors:
            failures += 1
            for error in errors:
                field = ".".join(str(p) for p in error.path) or "<root>"
                print(f"FAIL {path.relative_to(REPO_ROOT)}: {field}: {error.message}")
        else:
            print(f"OK   {path.relative_to(REPO_ROOT)}")

    print(f"\n{len(records) - failures}/{len(records)} records valid")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
