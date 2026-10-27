#!/usr/bin/env python3
"""Gate 3: the catalogue schema is a faithful projection of the metamodel schema.

The schema at schemas/entity.schema.json is a projection of the metamodel
InformationClass entity schema with the catalogue-instance layer added. This
gate asserts the projection has not drifted from the metamodel on the
normative fields.

The rule this gate exists to enforce: never widen a normative enum here to
accept a value the metamodel does not define. If a record fails because it
carries a value the metamodel does not have, the record is wrong, not the
schema. A catalogue that diverges from the metamodel is a second source of
truth.

The population CR extends this gate to validate actual records against the
schema. Until records exist, this gate validates the schema itself.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "entity.schema.json"

EXPECTED_TYPE_CONST = "InformationClass"
EXPECTED_LIFECYCLE_ENUM = ["proposed", "planned", "active", "deprecated", "retired"]
EXPECTED_REQUIRED = ["id", "type", "name", "version", "lifecycle_status"]
EXPECTED_ID_PATTERN = "^dea:information-class-[a-z0-9-]+$"
EXPECTED_SENSITIVITY_ENUM = ["public", "internal", "confidential", "restricted"]
EXPECTED_REGULATORY_ENUM = ["PII", "PHI", "PCI", "none"]


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"FAIL: {SCHEMA_PATH.name} is missing")
        print("Findings: 1")
        return 1

    schema = json.load(SCHEMA_PATH.open(encoding="utf-8"))
    props = schema.get("properties") or {}
    findings: list[str] = []

    if schema.get("title") != f"{EXPECTED_TYPE_CONST} (catalogue instance schema)":
        findings.append(f"title is {schema.get('title')!r}")

    if schema.get("type") != "object":
        findings.append(f"type is {schema.get('type')!r}, expected 'object'")
    if schema.get("additionalProperties") is not False:
        findings.append("additionalProperties is not false")

    required = schema.get("required") or []
    if required != EXPECTED_REQUIRED:
        findings.append(f"required is {required!r}, expected {EXPECTED_REQUIRED!r}")

    if props.get("type", {}).get("const") != EXPECTED_TYPE_CONST:
        findings.append(f"type const is {props.get('type', {}).get('const')!r}, expected {EXPECTED_TYPE_CONST!r}")

    if props.get("lifecycle_status", {}).get("enum") != EXPECTED_LIFECYCLE_ENUM:
        findings.append(f"lifecycle_status enum is {props.get('lifecycle_status', {}).get('enum')!r}")

    if props.get("id", {}).get("pattern") != EXPECTED_ID_PATTERN:
        findings.append(f"id pattern is {props.get('id', {}).get('pattern')!r}")

    if props.get("sensitivity", {}).get("enum") != EXPECTED_SENSITIVITY_ENUM:
        findings.append(f"sensitivity enum is {props.get('sensitivity', {}).get('enum')!r}")

    if (props.get("regulatory_regime", {}).get("items") or {}).get("enum") != EXPECTED_REGULATORY_ENUM:
        findings.append(
            f"regulatory_regime items enum is {(props.get('regulatory_regime', {}).get('items') or {}).get('enum')!r}"
        )

    for prop in ("handling_requirements", "retention", "governance", "external_references", "tags", "metadata"):
        if prop not in props:
            findings.append(f"catalogue-instance property {prop!r} is missing")

    if findings:
        print("Schema-projection findings:")
        for f in findings:
            print(f"  - FAIL: {f}")
    else:
        print("  OK: schema projection matches the metamodel on all normative fields")
    print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
