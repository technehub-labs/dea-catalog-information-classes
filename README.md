# Information Class

> A classification of information by sensitivity and regulatory regime (PII, PHI, PCI).

**Layer:** L4 : **Building block:** L4-data-foundation : **Entity:** `dea:InformationClass` (class alias `IC`) : **Metamodel:** [OpenDEAM v0.2.1](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=IC)

## Status

**Populated.** Foundation `CR-IC-CAT-01` (2026-02-11); taxonomy `CR-IC-CAT-02`; record documentation standard `CR-IC-CAT-03`; initial population `CR-IC-CAT-04`.

The catalogue carries its first six Information Class records under `entities/v1-alpha/`, each admitted against the ratified taxonomy and the record documentation standard. Further admissions require a CR; cross-catalogue crosswalk validation is `CR-IC-CAT-05`.

| Item | State |
|---|---|
| Repository | populated: eight records; the sensitivity lattice is complete (all bands carry unregulated classes; restricted carries regulated and unregulated members) |
| Metamodel pointer | pinned to OpenDEAM v0.2.1 |
| Schema projection | landed (mirrors the metamodel entity schema) |
| Taxonomy | three axes (`CR-IC-CAT-02` + `CR-IC-CAT-08`): sensitivity, regulatory regime, jurisdiction regime; vocabulary files under `classifications/`, gate-enforced against the schema enums |
| Record documentation standard | landed (`CR-IC-CAT-03`): `docs/RECORD-STANDARD.md`, enforced by Gate 7 |
| Population | landed (`CR-IC-CAT-04`): six records admitted under the standard |
| Cross-catalogue integration | landed (`CR-IC-CAT-05`): `relationships.mapped_from` + crosswalk inbox, enforced by Gate 8 |
| Generated index | landed (`CR-IC-CAT-06`): `CATALOG.yaml`, regenerator + strict gate in CI |
| Control references | landed (`CR-IC-CAT-09`): `mandated_controls[]` per record, id-form gate; CTL resolution deferred |

## Admitted records

| Record | Sensitivity | Regulatory regime | Jurisdiction anchors |
|---|---|---|---|
| [`dea:information-class-public`](./entities/v1-alpha/dea:information-class-public/) | public | none | (none) |
| [`dea:information-class-internal`](./entities/v1-alpha/dea:information-class-internal/) | internal | none | (none) |
| [`dea:information-class-confidential`](./entities/v1-alpha/dea:information-class-confidential/) | confidential | none | (none) |
| [`dea:information-class-pii`](./entities/v1-alpha/dea:information-class-pii/) | restricted | PII | eu-gdpr, uk-gdpr, us-ccpa-cpra |
| [`dea:information-class-phi`](./entities/v1-alpha/dea:information-class-phi/) | restricted | PHI | us-hipaa |
| [`dea:information-class-pci`](./entities/v1-alpha/dea:information-class-pci/) | restricted | PCI | pci-dss |
| [`dea:information-class-trade-secret`](./entities/v1-alpha/dea:information-class-trade-secret/) | restricted | none | us-dtsa, eu-trade-secrets-directive |
| [`dea:information-class-material-nonpublic-information`](./entities/v1-alpha/dea:information-class-material-nonpublic-information/) | restricted | none | us-securities-insider-trading |

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
├── CATALOG.yaml                     ← machine-generated index (CR-IC-CAT-06; do not hand-edit)
├── docs/
│   ├── FOUNDATIONS.md               ← catalogue method
│   └── RECORD-STANDARD.md           ← record documentation standard (CR-IC-CAT-03)
├── schemas/
│   └── entity.schema.json           ← projection of the metamodel entity schema
├── scripts/
│   ├── check_parse.py               ← Gate 1: YAML/JSON parsing
│   ├── check_pointer.py             ← Gate 2: pointer consistency
│   ├── check_schema_projection.py   ← Gate 3: schema projection
│   ├── check_writing_rules.py       ← Gate 4: D-004/D-005 writing rules
│   ├── check_record_posture.py      ← Gate 5: records-directory posture
│   ├── check_taxonomy.py            ← Gate 6: classification taxonomy
│   ├── check_record_documentation.py ← Gate 7: record documentation standard
│   ├── check_crosswalk.py           ← Gate 8: cross-catalogue crosswalk
│   └── check_control_references.py  ← Gate 10: machine-readable control references
├── classifications/                 ← classification vocabularies (CR-IC-CAT-02)
│   ├── sensitivity-classifications.yaml
│   └── regulatory-regime-classifications.yaml
├── entities/
│   └── v1-alpha/                    ← records go here (population gated)
└── .github/workflows/
    ├── validate-allocation.yml      ← OpenDEAM allocation validator (root model)
    └── validate-catalogue.yml       ← the ten catalogue gates
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
python3 scripts/check_record_documentation.py
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md).
