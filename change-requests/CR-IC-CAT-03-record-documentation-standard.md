# CR-IC-CAT-03: Information Class Record Documentation Standard

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-03 |
| **Title** | Record documentation standard for admitted Information Class records |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-01` (foundation), `CR-IC-CAT-02` (taxonomy) |
| **Blocks** | `CR-IC-CAT-04` (population) |

## 1. Executive summary

This CR defines the documentation standard a record must satisfy before it can be admitted. It lands the standard (`docs/RECORD-STANDARD.md`), the gate that enforces it (`scripts/check_record_documentation.py`, Gate 7), and reconciles the record-posture gate's population-gates contract with the gates this catalogue actually runs. It admits **no records**; population is `CR-IC-CAT-04`, which can now land because its two prerequisites are complete.

## 2. Scope

### In scope

1. `docs/RECORD-STANDARD.md`: the canonical record shape, five semantic rules beyond the schema (R-1..R-5), the per-record README contract, and the admission posture.
2. `scripts/check_record_documentation.py` (Gate 7): enforces R-1..R-5 and the README contract on every record under `entities/v1-alpha/`; with no records it asserts the standard's own presence.
3. `scripts/check_record_posture.py`: the population-gates list reconciled with the actual gates (`check_schema_projection`, `check_taxonomy`, `check_record_documentation`).
4. The Gate 7 step added to `validate-catalogue.yml` and the local validation lists.
5. Doc updates: README, CONTRIBUTING, FOUNDATIONS roadmap, CHANGELOG.

### Out of scope

1. Record population (`CR-IC-CAT-04`).
2. Cross-catalogue crosswalk validation (`CR-IC-CAT-05`).
3. Any widening of the classification vocabularies.

## 3. The five semantic rules

The schema is the structural surface; these rules carry the semantics the schema cannot express, following the evidence-anchor pattern ratified for the metric catalogue (CR-MET-009: `established_by` + evidence entries) and the README-per-folder rule from the org-wide entity-storage layout:

| Rule | Requirement |
|---|---|
| R-1 | `metadata.established_by` names the admission CR |
| R-2 | `governance.source_and_evidence` names an authority, not prose |
| R-3 | `handling_requirements` is non-empty and phrased as obligations |
| R-4 | D-4: `none` appears in `regulatory_regime` only as the sole entry |
| R-5 | `retention` names a rule or schedule |

## 4. Why a record README

The org-wide entity-storage layout requires a README per entity subtree: the level, the record id, a prose summary from the record's own fields, and enumerated children. For a flat catalogue like this one, the README carries the record's classification, handling requirements, retention, and provenance, mirrored from the record. The README does not extend the record; facts belong in the record, and the README is regenerated.

## 5. Admission posture

Records land as `candidate` in their subtree with `lifecycle_status: planned` and `governance.approval_status: proposed`; the admission CR moves them to canonical (`lifecycle_status: active`, `approval_status: approved`). Gate 5 (posture) and Gate 7 (documentation) together enforce that no record lands before the population CR, and that every record that lands satisfies the standard.

## 6. Gate

`scripts/check_record_documentation.py` runs after the taxonomy gate. On a populated tree it enforces R-1..R-5 and the README contract per record. On an empty tree it fails if the standard document is missing, so the standard cannot be silently dropped between now and population.
