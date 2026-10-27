# CR-IC-CAT-01: Information Class Catalogue Foundation

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-01 |
| **Title** | Information Class catalogue foundation (methodology-first bring-up) |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |

## 1. Executive summary

This CR establishes the Information Class catalogue as a **method**, not as content. It lands the pointer gates, the schema projection, the classification axes, the admission criteria, the cross-catalogue reference policy, and five CI gates. It admits **no records**.

It follows the methodology-first rule established for the business-capability catalogue and restated for the Information System Service catalogue (`CR-IS-CAT-03A`): the first increment of a catalogue establishes admission criteria, the evidence process, and the framework-overlay rules. Records come later, gated on the taxonomy CR.

## 2. Scope

### In scope

1. `schemas/entity.schema.json`, a projection of the metamodel InformationClass entity schema with the catalogue-instance layer added.
2. `docs/FOUNDATIONS.md`: cardinal scope, exclusions, two classification axes, six admission criteria, the cross-catalogue reference policy, and an eight-entry decision-points register.
3. `README.md`: catalogue boundary table, entity definition, five key tenets, catalogue structure, change-control matrix.
4. Five CI gates (`scripts/check_*.py`) wired into `.github/workflows/validate-catalogue.yml`.
5. `.gitignore`, landed before any Python exists in the repository.

### Out of scope

1. Record population (deferred to `CR-IC-CAT-04`).
2. Taxonomy refinement beyond the two axes (deferred to `CR-IC-CAT-02`).
3. Cross-catalogue crosswalk validation (deferred to `CR-IC-CAT-05`).

## 3. Methodology-first rationale

The Information Class entity is normative in the metamodel but lifecycle-planned in the root model. A catalogue that admits records before its taxonomy is ratified accumulates content it cannot govern: sensitivity bands drift, regime values multiply, and the first population CR inherits a cleanup instead of a clean admission. This CR therefore lands the method first and gates population on the taxonomy CR, following the pattern ratified for the ISS catalogue.

## 4. Classification axes

Two axes, both closed vocabularies fixed by this CR:

| Axis | Vocabulary |
|---|---|
| Sensitivity | public, internal, confidential, restricted |
| Regulatory regime | PII, PHI, PCI, none |

Widening either vocabulary is a CR against the taxonomy (`CR-IC-CAT-02`), not a schema edit.

## 5. Allocation reconciliation

The repository's `metamodel-pointer.yaml` is the OpenDEAM v0.2.1 fan-out artifact and is never hand-edited. The pointer pins `dea:entity-information-class` (alias `IC`) to L4 / `L4-data-foundation`. The pre-existing `validate-allocation.yml` workflow continues to validate the pointer against the pinned root-model ref; this CR adds the pointer-consistency gate (`scripts/check_pointer.py`) that asserts the same facts locally, so a pointer drift fails CI twice for the same reason: once against the root model, once on the declared fields.

## 6. Gates

| Gate | Script | Enforces |
|---|---|---|
| 1 | `check_parse.py` | Every tracked YAML and JSON file parses |
| 2 | `check_pointer.py` | Pointer present, internally consistent, identity fields match the allocation |
| 3 | `check_schema_projection.py` | Schema projection matches the metamodel on normative fields |
| 4 | `check_writing_rules.py` | D-004 and D-005 writing rules |
| 5 | `check_record_posture.py` | No records before the population CR; canonical ids when they land |

## 7. Roadmap

| Phase | CR | Scope |
|---|---|---|
| Foundation (this CR) | `CR-IC-CAT-01` | Method, schema projection, gates |
| Taxonomy | `CR-IC-CAT-02` | Per-sector class refinements, jurisdiction regimes |
| Record documentation standard | `CR-IC-CAT-03` | Evidence standard for admitted records |
| Population | `CR-IC-CAT-04` | Initial class records |
| Cross-catalogue integration | `CR-IC-CAT-05` | `dea:maps-to` crosswalk validation |
