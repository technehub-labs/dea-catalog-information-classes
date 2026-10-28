# CR-IC-CAT-02: Information Class Classification Taxonomy

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-02 |
| **Title** | Ratify the Information Class classification taxonomy |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-01` (catalogue foundation) |
| **Blocks** | `CR-IC-CAT-03` (record documentation standard), `CR-IC-CAT-04` (population) |

## 1. Executive summary

This CR ratifies the classification taxonomy that `CR-IC-CAT-01` deferred. The two axes and their vocabularies move from schema-embedded enums to first-class vocabulary files under `classifications/`, cross-checked against the schema by a new taxonomy gate. The vocabularies themselves are unchanged from the values fixed by `CR-IC-CAT-01`; this CR makes them governed artifacts with definitions, versions, and drift protection.

## 2. Scope

### In scope

1. `classifications/sensitivity-classifications.yaml` (axis 1, four values).
2. `classifications/regulatory-regime-classifications.yaml` (axis 2, four values).
3. `scripts/check_taxonomy.py` (Gate 6): the schema enums must match the vocabulary files exactly, in both directions.
4. The taxonomy step added to `validate-catalogue.yml` and to the local validation lists in `README.md`, `CONTRIBUTING.md`.

### Out of scope

1. Widening either vocabulary (a future taxonomy CR; the D-2 and D-3 decisions stand).
2. Per-sector or per-jurisdiction refinements (D-8).
3. Record population (still `CR-IC-CAT-04`).

## 3. Taxonomy shape

The shape mirrors the metric catalogue's classification model (`CR-MET-002` binding): one YAML file per axis, each declaring a `version` and a `values` list of `{id, definition}` entries. The schema enums remain the normative validation surface for records; the vocabulary files are the human-facing registry and the gate keeps the two in lockstep.

| Axis | Cardinality | Values | Source |
|---|---|---|---|
| sensitivity | 1 | public, internal, confidential, restricted | `classifications/sensitivity-classifications.yaml` |
| regulatory_regime | 1..* | PII, PHI, PCI, none | `classifications/regulatory-regime-classifications.yaml` |

The D-4 rule is restated in the `none` definition: it is legal only as the sole entry of a record's `regulatory_regime` list. Enforcement of D-4 at record level lands with the record validator in the population CR; this gate enforces vocabulary/schema coherence only.

## 4. Gate

`scripts/check_taxonomy.py` runs after the schema-projection gate and asserts, for each axis, that the vocabulary file and the schema enum contain exactly the same value set. A value added to one without the other is a finding. This is the same lockstep rule the schema-projection gate applies between this catalogue and the metamodel, applied one level down: the vocabulary files and the schema must not diverge.
