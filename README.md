# Information Class

> A classification of information by sensitivity and regulatory regime (PII, PHI, PCI).

**Layer:** L4 : **Building block:** L4-data-foundation : **Entity:** `dea:InformationClass` (class alias `IC`) : **Metamodel:** [OpenDEAM v0.2.1](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=IC)

## Status

**Planned.** Established by `CR-IC-CAT-01` (Information Class catalogue foundation) on 2026-02-11.

This repository currently contains the **catalogue method** and **no records**. Content population is gated on the taxonomy CR. Nothing in this repository asserts that a class exists; it establishes the criteria by which a class would be admitted, and the evidence a record must carry when it is.

| Item | State |
|---|---|
| Repository | planned, no records |
| Metamodel pointer | pinned to OpenDEAM v0.2.1 |
| Schema projection | landed (mirrors the metamodel entity schema) |
| Taxonomy | landed (`CR-IC-CAT-02`): vocabulary files under `classifications/`, gate-enforced against the schema enums |
| Record documentation standard | deferred to `CR-IC-CAT-03` |
| Population | deferred to `CR-IC-CAT-04` |
| Cross-catalogue integration | deferred to `CR-IC-CAT-05` |

## What this catalogue is

The catalogue of **classes**, not of data. An Information Class record names a band of information sensitivity and the regulatory regimes that govern it. The data entities, information assets, and business objects that fall under a class are catalogued separately; the crosswalk is recorded on their side via `dea:maps-to`.

## What this catalogue is not

| Not this | Why | Where it lives |
|---|---|---|
| A data-entity catalogue | A data entity is a unit of stored information; a class is the sensitivity band it occupies | Information-asset and business-object catalogues |
| A controls catalogue | A class names mandatory controls via `handling_requirements`; the control mechanism itself is a Control record | `dea-catalog-controls` |
| A retention schedule | Retention is a field on the class record, not a separate record | This catalogue, `retention` field |
| A crosswalk registry | The `dea:maps-to` crosswalk is recorded on the mapped entity's side | The mapped entity's catalogue |

## Entity definition

| Field | Value |
|---|---|
| Entity ID | `dea:InformationClass` |
| OpenDEAM entity id | `dea:entity-information-class` |
| Class alias | `IC` |
| Layer | L4 |
| Building block | L4-data-foundation |
| Metamodel version | v0.2.1 |
| Status | normative |
| Lifecycle | planned |

## Key tenets

1. **A class is a classification, not a datum.** If a record describes a specific stored item, it belongs in a data or asset catalogue, not here. The test: can other records be mapped to it via `dea:maps-to`? If no, it is not a class.
2. **The axes are the admission test.** A record that cannot be placed on both the sensitivity axis and the regulatory-regime axis is not yet understood well enough to admit.
3. **The vocabulary is closed.** The sensitivity and regulatory-regime enums are fixed by this CR; widening either is a CR against the taxonomy, not a schema edit.
4. **Controls named by a class are mandatory.** `handling_requirements` states controls the class mandates, not controls that happen to exist where the class is found.
5. **The crosswalk lives on the mapped side.** This catalogue neither hosts nor validates `dea:maps-to` crosswalks for entities it does not own.

## Catalogue structure

```
dea-catalog-information-classes/
├── metamodel-pointer.yaml           ← entity allocation (do not edit manually)
├── docs/
│   └── FOUNDATIONS.md               ← catalogue method
├── schemas/
│   └── entity.schema.json           ← projection of the metamodel entity schema
├── scripts/
│   ├── check_parse.py               ← Gate 1: YAML/JSON parsing
│   ├── check_pointer.py             ← Gate 2: pointer consistency
│   ├── check_schema_projection.py   ← Gate 3: schema projection
│   ├── check_writing_rules.py       ← Gate 4: D-004/D-005 writing rules
│   └── check_record_posture.py      ← Gate 5: records-directory posture
├── classifications/                 ← classification vocabularies (CR-IC-CAT-02)
│   ├── sensitivity-classifications.yaml
│   └── regulatory-regime-classifications.yaml
├── entities/
│   └── v1-alpha/                    ← records go here (population gated)
└── .github/workflows/
    ├── validate-allocation.yml      ← OpenDEAM allocation validator (root model)
    └── validate-catalogue.yml       ← the five catalogue gates
```

## Local validation

Run the gates before opening a pull request. They are the same scripts CI runs.

```
python3 scripts/check_parse.py
python3 scripts/check_pointer.py
python3 scripts/check_schema_projection.py
python3 scripts/check_writing_rules.py
python3 scripts/check_record_posture.py
python3 scripts/check_taxonomy.py
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md).
