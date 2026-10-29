# Contributing to the Information Class catalogue

## Before you propose a record

Population is gated. The classification taxonomy was ratified by
`CR-IC-CAT-02` and the record documentation standard by `CR-IC-CAT-03`.
A pull request that adds a record before the population CR
(`CR-IC-CAT-04`) lands will fail the record-posture gate. A record must
satisfy `docs/RECORD-STANDARD.md` (R-1..R-5 and the per-record README
contract) to pass the documentation gate.

Read [`docs/FOUNDATIONS.md`](./docs/FOUNDATIONS.md) first. It carries the
cardinal scope, the classification axes, the admission criteria, and the
decision register that later change requests cite by number.

## The one test

> Is the record a class that other records can be mapped to via `dea:maps-to`?

If no, you are describing a data entity, an information asset, or a business
object. That record belongs in the corresponding catalogue, not here.

## Change control

| Artefact | Authority |
|---|---|
| `metamodel-pointer.yaml` | OpenDEAM root model. Never hand-edited; a finding from the pointer gate means the allocation drifted |
| `schemas/*.json` | This repository, by CR, mirroring the metamodel |
| Records | This repository, by CR, gated on the taxonomy CR |

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
python3 scripts/check_crosswalk.py
python3 scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json
python3 scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json
```
