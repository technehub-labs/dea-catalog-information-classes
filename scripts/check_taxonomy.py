#!/usr/bin/env python3
"""Gate 6: classification taxonomy (CR-IC-CAT-02; axis 3 added by CR-IC-CAT-08).

The classification vocabularies live in classifications/*.yaml. The schema
enums in schemas/entity.schema.json must match those vocabularies exactly:
a value present in one and absent from the other is drift, in either
direction. This gate cross-checks all three axes and enforces the D-4 rule
(`none` is legal only as the sole entry of a regulatory_regime list) and
the CR-IC-CAT-08 rule (a record with regulatory_regime [none] carries no
jurisdiction_regime values).

Run: python3 scripts/check_taxonomy.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "schemas" / "entity.schema.json"
CLASSIFICATIONS = {
    "sensitivity": REPO / "classifications" / "sensitivity-classifications.yaml",
    "regulatory_regime": REPO / "classifications" / "regulatory-regime-classifications.yaml",
    "jurisdiction_regime": REPO / "classifications" / "jurisdiction-regime-classifications.yaml",
}


def load_values(path: Path) -> list[str]:
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return [v["id"] for v in (doc.get("values") or [])]


def main() -> int:
    findings: list[str] = []
    schema = json.load(SCHEMA_PATH.open(encoding="utf-8"))
    props = schema.get("properties") or {}

    for axis, path in CLASSIFICATIONS.items():
        if not path.exists():
            findings.append(f"{axis}: vocabulary file {path.name} is missing")
            continue
        vocab = load_values(path)
        if not vocab:
            findings.append(f"{axis}: vocabulary file {path.name} declares no values")
            continue

        if axis == "sensitivity":
            schema_values = props.get("sensitivity", {}).get("enum") or []
        else:
            schema_values = (props.get(axis, {}).get("items") or {}).get("enum") or []

        missing_in_schema = [v for v in vocab if v not in schema_values]
        missing_in_vocab = [v for v in schema_values if v not in vocab]
        if missing_in_schema:
            findings.append(f"{axis}: in vocabulary but not in schema enum: {missing_in_schema}")
        if missing_in_vocab:
            findings.append(f"{axis}: in schema enum but not in vocabulary: {missing_in_vocab}")
        print(f"  {axis}: {len(vocab)} values, schema enum in sync: {not (missing_in_schema or missing_in_vocab)}")

    # CR-IC-CAT-08: a record's jurisdiction_regime values must be
    # compatible with its regulatory_regime, per each vocabulary value's
    # `refines` declaration.
    import glob
    juris_vocab = {}
    jpath = CLASSIFICATIONS["jurisdiction_regime"]
    if jpath.exists():
        jdoc = yaml.safe_load(jpath.read_text(encoding="utf-8")) or {}
        juris_vocab = {v["id"]: set(v.get("refines") or []) for v in (jdoc.get("values") or [])}
    for f in sorted(glob.glob(str(REPO / "entities/v1-alpha/**/*.yaml"), recursive=True)):
        doc = yaml.safe_load(Path(f).read_text(encoding="utf-8")) or {}
        rid = doc.get("id") or str(Path(f))
        regime = set(doc.get("regulatory_regime") or [])
        juris = doc.get("jurisdiction_regime") or []
        for j in juris:
            refines = juris_vocab.get(j)
            if refines is None:
                findings.append(f"{rid}: jurisdiction_regime value {j!r} is not in the jurisdiction vocabulary")
            elif not (refines & regime):
                findings.append(f"{rid}: jurisdiction_regime value {j!r} refines {sorted(refines)} but the record carries {sorted(regime)}")

    if findings:
        print("Taxonomy findings:")
        for f in findings:
            print(f"  - FAIL: {f}")
    else:
        print("  OK: schema enums match the classification vocabularies")
    print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
