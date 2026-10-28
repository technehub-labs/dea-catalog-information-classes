# FOUNDATIONS: Information Class catalogue

**Status:** Established by `CR-IC-CAT-01` on 2026-02-11.
**Programme:** DEA catalog rollout (L4 data foundation).
**Scope of this document:** the catalogue **method**. No records are admitted here.

---

## 1. Cardinal scope

The Information Class catalogue records **classifications of information by sensitivity and regulatory regime**. A record names what class of information is being described, the sensitivity band it occupies, and the regulatory regimes that govern it. It does not record individual data entities or assets; those live elsewhere in the L4 data-foundation building block.

The boundary test is classification:

> Is the record a class that other records (data entities, information assets, business objects) can be mapped to via `dea:maps-to`?
>
> **Yes** -> this is an information class. Record it here.
> **No** -> it is a data entity, an information asset, or a business object. Record it in the corresponding catalogue.

This single test resolves most boundary disputes. PII is an information class; a customer record is not. PCI is an information class; a card number field in a table is not. Both are true statements about the enterprise's information; only the first is a class record.

## 2. What is deliberately excluded

| Excluded | Reason | Where it lives |
|---|---|---|
| Individual data entities, tables, schemas | Those are data concerns, not classes | `dea-catalog-information-assets` |
| Applied know-how, documents, knowledge artifacts | Knowledge assets, not information classes | Knowledge-asset catalogues |
| The `dea:maps-to` crosswalk itself | The crosswalk is a relationship between a mapped entity and the class; it is recorded on the mapped entity's side, not here | The mapped entity's catalogue |
| Control definitions | A class names mandatory controls via `handling_requirements`, but the control mechanism itself is a Control record | `dea-catalog-controls` |
| Retention schedules as standalone records | Retention is a field on the class record, not a separate class | This catalogue, `retention` field |

## 3. Classification axes

A record is classified on two axes. The axes are the admission test: a record that cannot be placed on all of them is not yet understood well enough to admit.

| Axis | Question | Vocabulary |
|---|---|---|
| **Sensitivity** | What level of protection does the class require? | public, internal, confidential, restricted |
| **Regulatory regime** | Which regulatory regimes govern the class? | PII, PHI, PCI, none |

The vocabularies are ratified artifacts under `classifications/` (`CR-IC-CAT-02`), one YAML file per axis, and are kept in lockstep with the schema enums by the taxonomy gate (`scripts/check_taxonomy.py`).

**Mutual exclusivity.** A record occupies exactly one cell on the sensitivity axis. Two records that would occupy the same two-tuple are either duplicates or genuinely distinct records that the axes fail to distinguish; the second case is a finding against the axes, not against the axes, and must be raised as a CR against the taxonomy. The regulatory-regime axis is multi-valued: one class may be governed by more than one regime (for example, a class covering both PII and PHI).

## 4. Admission criteria

The documentation standard for admitted records is `docs/RECORD-STANDARD.md` (`CR-IC-CAT-03`); the semantic rules R-1..R-5 there refine the criteria below, and Gate 7 enforces them.

1. It is a classification of information, not a data entity, per the section 1 boundary test.
2. Its `sensitivity` value is exactly one of the four bands in the schema enum.
3. Its `regulatory_regime` list carries at least one value from the schema enum; `none` appears only alone.
4. It carries a `version` and a `lifecycle_status` drawn from the metamodel lifecycle vocabulary (CR-3R).
5. Its `handling_requirements` are stated as controls the class mandates, not controls that merely happen to exist.
6. It carries a `governance` block naming a `functional_owner`, a `steward`, and an `approval_status`.

## 5. Allocation

The entity allocation is recorded in the OpenDEAM root model, not here. The local pointer (`metamodel-pointer.yaml`) mirrors the root-model allocation and is validated in CI against the pinned root-model ref (`v0.2.1`) via the reusable allocation validator. The allocation facts this catalogue relies on:

| Field | Value |
|---|---|
| Entity id | `dea:entity-information-class` |
| Canonical metamodel id | `dea:InformationClass` |
| Class alias | `IC` |
| Layer | L4 |
| Building block | L4-data-foundation |
| OpenDEAM version | v0.2.1 |
| Relationship to other entities | `dea:maps-to` (Entity to InformationClass, temporal, provenance required) |

A finding from the pointer gate means the allocation drifted. Fix the allocation in `dea-architecture-framework`, not the local pointer.

## 6. Cross-catalogue reference policy

References between catalogues are by canonical identifier, never by URL or repository name. The `dea:maps-to` relationship (OpenDEAM v0.2.1, section on traceability) is the sole means by which an entity in another catalogue declares that it falls under a class recorded here. The crosswalk itself is recorded on the mapped entity's side; this catalogue neither hosts nor validates crosswalks for entities it does not own.

## 7. Decision-points register

| # | Decision | Status |
|---|---|---|
| D-1 | The catalogue follows the methodology-first rule: no records are admitted before the population CR | Adopted (this CR) |
| D-2 | Sensitivity vocabulary fixed at public, internal, confidential, restricted; widening is a CR against the taxonomy | Adopted (this CR) |
| D-3 | Regulatory-regime vocabulary fixed at PII, PHI, PCI, none; widening is a CR against the taxonomy | Adopted (this CR) |
| D-4 | `none` is a legal value only as the sole entry in `regulatory_regime` | Adopted (this CR) |
| D-5 | `handling_requirements` are mandatory controls, not descriptive prose | Adopted (this methods CR) |
| D-6 | The crosswalk to the class lives on the mapped entity's side | Adopted (this CR) |
| D-7 | Population is deferred to a dedicated population CR | Adopted (this CR) |
| D-8 | Taxonomy refinement (per-sector classes, per-jurisdiction regimes) is out of scope until the taxonomy CR | Superseded by `CR-IC-CAT-02` (landed; refinement still requires a CR) |

## 8. Roadmap

| Phase | Change request | Scope |
|---|---|---|
| Foundation | `CR-IC-CAT-01` | Pointer gates, schema projection, FOUNDATIONS, five CI gates |
| Taxonomy (landed) | `CR-IC-CAT-02` | Ratify per-sector class refinements, jurisdiction-specific regime values |
| Record documentation standard (landed) | `CR-IC-CAT-03` | Define the evidence standard for admitted records |
| Population | `CR-IC-CAT-04` | Admit the initial class records |
| Cross-catalogue integration | `CR-IC-CAT-05` | Wire `dea:maps-to` crosswalk validation into the gate suite |
