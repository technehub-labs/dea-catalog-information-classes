#!/usr/bin/env python3
"""Gate 7: record documentation standard (CR-IC-CAT-03).

Asserts the standard in docs/RECORD-STANDARD.md for every record under
entities/v1-alpha/: the semantic rules R-1..R-5 the schema cannot express,
and the per-record README contract.

With no records, the gate asserts the standard's own presence: the
standard document must exist, so the standard cannot be silently dropped
before population.

Run: python3 scripts/check_record_documentation.py
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
STANDARD_PATH = REPO / "docs" / "RECORD-STANDARD.md"
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_record(path: Path, findings: list[str]) -> None:
    rel = path.relative_to(REPO)
    doc = yaml.safe_load(_read(path)) or {}
    rid = doc.get("id") or "<missing id>"

    meta = doc.get("metadata") or {}
    if not str(meta.get("established_by", "")).strip():
        findings.append(f"{rel}: R-1: metadata.established_by is missing or empty")

    gov = doc.get("governance") or {}
    evidence = str(gov.get("source_and_evidence", "")).strip()
    if not evidence:
        findings.append(f"{rel}: R-2: governance.source_and_evidence is missing or empty")

    handling = doc.get("handling_requirements") or []
    if not handling:
        findings.append(f"{rel}: R-3: handling_requirements is empty; a class must mandate at least one control")

    regime = doc.get("regulatory_regime") or []
    if "none" in regime and len(regime) > 1:
        findings.append(f"{rel}: R-4: 'none' appears alongside other regimes in regulatory_regime")

    retention = str(doc.get("retention", "")).strip()
    if not retention:
        findings.append(f"{rel}: R-5: retention is missing or empty")

    subtree = path.parent
    readme = subtree / "README.md"
    if not readme.exists():
        findings.append(f"{rel}: README.md is missing from the record subtree (README-per-folder rule)")
    else:
        text = _read(readme)
        for section in ("## Classification", "## Handling requirements", "## Retention", "## Provenance"):
            if section not in text:
                findings.append(f"{rel}: README.md is missing required section {section!r}")
        if doc.get("name") and str(doc.get("name")) not in text:
            findings.append(f"{rel}: README.md does not name the record ({rid})")


def main() -> int:
    if not STANDARD_PATH.exists():
        print("FAIL: docs/RECORD-STANDARD.md is missing; the documentation standard cannot be dropped")
        print("Findings: 1")
        return 1

    records = sorted(glob.glob(str(REPO / RECORD_GLOB), recursive=True))
    print(f"Record count: {len(records)}")

    findings: list[str] = []
    for f in records:
        check_record(Path(f), findings)

    if findings:
        print("Documentation findings:")
        for f in findings:
            print(f"  - FAIL: {f}")
    else:
        if records:
            print(f"  OK: {len(records)} record(s) satisfy the documentation standard")
        else:
            print("  OK: no records yet; standard present and enforced on arrival")
    print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
