#!/usr/bin/env python3
"""Gate 10: machine-readable control references (CR-IC-CAT-09).

Each mandated_controls[] entry on a class record pairs the class-side
obligation with the canonical Control id it references in
dea-catalog-controls (entity dea:entity-control, alias CTL).

Two-stage enforcement:

- Stage 1 (now): id form. Every entry's control id must match the
  canonical CTL form ^dea:control-[a-z0-9-]+$, and every entry must
  carry a non-empty obligation-phrased requirement. The controls
  catalogue is an unpopulated scaffold, so resolution is deferred.
- Stage 2 (when CTL records land): resolution. The gate consults
  reconciliation/control-reference-registry.yaml, which maps each
  referenced control id to the CTL catalogue's canonical index. An id
  absent from the registry activates resolution as a finding.

Run: python3 scripts/check_control_references.py
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"
REGISTRY_PATH = REPO / "reconciliation" / "control-reference-registry.yaml"

CONTROL_ID_RE = re.compile(r"^dea:control-[a-z0-9-]+$")


def main() -> int:
    findings: list[str] = []
    referenced: set[str] = set()

    for f in sorted(glob.glob(str(REPO / RECORD_GLOB), recursive=True)):
        doc = yaml.safe_load(Path(f).read_text(encoding="utf-8")) or {}
        rid = doc.get("id") or str(Path(f))
        for i, entry in enumerate(doc.get("mandated_controls") or []):
            cid = entry.get("control") or ""
            req = str(entry.get("requirement") or "").strip()
            if not CONTROL_ID_RE.match(cid):
                findings.append(f"{rid}: mandated_controls[{i}] control {cid!r} does not match the canonical CTL id form")
                continue
            referenced.add(cid)
            if not req:
                findings.append(f"{rid}: mandated_controls[{i}] ({cid}) has no requirement text")

    registry = {}
    stage2 = False
    if REGISTRY_PATH.exists():
        rdoc = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or {}
        registry = {e["id"]: e for e in (rdoc.get("entries") or []) if isinstance(e, dict) and "id" in e}
        stage2 = bool(rdoc.get("resolution_active"))

    print(f"Referenced control ids: {len(referenced)} (unique)")
    print(f"Resolution stage: {'2 (active)' if stage2 else '1 (id-form only; CTL catalogue unpopulated)'}")

    if stage2:
        for cid in sorted(referenced):
            if cid not in registry:
                findings.append(f"control {cid!r} does not resolve against the control-reference registry")

    if findings:
        print("Control-reference findings:")
        for f in findings:
            print(f"  - FAIL: {f}")
    else:
        print("  OK: control references well-formed")
    print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
