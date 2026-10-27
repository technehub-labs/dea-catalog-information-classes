# Contributing to the Information Class catalogue

## Before you propose a record

Population is gated. No record may be admitted before `CR-IC-CAT-02` ratifies
the classification taxonomy and `CR-IC-CAT-03` defines the documentation
standard. A pull request that adds a record before both land will fail the
record-posture gate.

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
```
