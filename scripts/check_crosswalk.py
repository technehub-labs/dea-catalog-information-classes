#!/usr/bin/env python3
"""Gate 8: cross-catalogue crosswalk integrity (CR-IC-CAT-05).

The dea:maps-to relationship (Entity -> InformationClass, category
traceability, inverse dea:mapped-from) is recorded on the mapped entity's
side (FOUNDATIONS D-6). This catalogue's side of the contract:

- A record's mapped_from[] entries (inverse references, cataloguing which
  entities map to this class) must name canonical entity ids, not URLs or
  repository names.
- Every incoming reference recorded here must resolve to this catalogue's
  own canonical records: an entry naming a class that is not in this
  catalogue is an unresolved reference.
- The crosswalk registry (reconciliation/crosswalk-inbox.yaml) is the
  intake queue for crosswalks proposed by other catalogues; entries there
  must cite a CR and target a canonical record.

Run: python3 scripts/check_crosswalk.py
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"
INBOX_PATH = REPO / "reconciliation" / "crosswalk-inbox.yaml"

ID_PREFIX = "dea:"


def load_records() -> dict[str, dict]:
    records = {}
    for f in sorted(glob.glob(str(REPO / RECORD_GLOB), recursive=True)):
        doc = yaml.safe_load(Path(f).read_text(encoding="utf-8")) or {}
        rid = doc.get("id")
        if rid:
            records[rid] = doc
    return records


def main() -> int:
    findings: list[str] = []
    records = load_records()
    canonical_ids = set(records.keys())
    print(f"Canonical records: {len(canonical_ids)}")

    for rid, doc in sorted(records.items()):
        rel = doc.get("relationships") or {}
        maps_to = rel.get("mapped_from") or []
        if not isinstance(maps_to, list):
            findings.append(f"{rid}: relationships.mapped_from must be a list")
            continue
        for ref in maps_to:
            if not isinstance(ref, str) or not ref.startswith(ID_PREFIX):
                findings.append(f"{rid}: mapped_from entry {ref!r} is not a canonical entity id (must start 'dea:')")
            elif ref in canonical_ids:
                findings.append(f"{rid}: mapped_from entry {ref!r} resolves to this catalogue's own record; mapped_from catalogues external entities")

    if INBOX_PATH.exists():
        inbox = yaml.safe_load(INBOX_PATH.read_text(encoding="utf-8")) or {}
        entries = inbox.get("entries") or []
        for e in entries:
            target = e.get("target") or ""
            cr = e.get("cr") or ""
            if not target.startswith(ID_PREFIX):
                findings.append(f"crosswalk-inbox: entry {e.get('source', '?')!r} target {target!r} is not a canonical id")
            elif target not in canonical_ids:
                findings.append(f"crosswalk-inbox: entry {e.get('source', '?')!r} targets unknown record {target!r}")
            if not cr:
                findings.append(f"crosswalk-inbox: entry {e.get('source', '?')!r} has no cr reference")
        print(f"Inbox entries: {len(entries)}")
    else:
        print("Inbox entries: 0 (no inbox file)")

    if findings:
        print("Crosswalk findings:")
        for f in findings:
            print(f"  - FAIL: {f}")
    else:
        print("  OK: crosswalk contract intact")
    print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
