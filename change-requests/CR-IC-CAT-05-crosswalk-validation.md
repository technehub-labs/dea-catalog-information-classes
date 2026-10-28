# CR-IC-CAT-05: Cross-Catalogue Crosswalk Validation

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-05 |
| **Title** | Wire dea:maps-to crosswalk validation into the gate suite |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-04` (population) |

## 1. Executive summary

This CR lands the final roadmap item: the cross-catalogue `dea:maps-to` crosswalk contract. Per FOUNDATIONS D-6, the crosswalk is recorded on the mapped entity's side; this catalogue validates the class side. It adds the inverse-reference field to the schema, an intake queue for crosswalks proposed by other catalogues, and Gate 8 to enforce both.

## 2. Scope

### In scope

1. `schemas/entity.schema.json`: optional `relationships.mapped_from[]` (canonical ids of external entities mapping to the class). `additionalProperties: false` is retained.
2. `reconciliation/crosswalk-inbox.yaml`: the intake queue. Entries cite the proposing CR and target a canonical record here.
3. `scripts/check_crosswalk.py` (Gate 8): every `mapped_from` entry must be a canonical entity id (never a URL or repository name); an entry resolving to this catalogue's own records is a finding (mapped_from catalogues external entities only); every inbox entry must carry a `cr` and a resolvable `target`.
4. The Gate 8 step in `validate-catalogue.yml`; README, CONTRIBUTING, FOUNDATIONS, CHANGELOG updates.

### Out of scope

1. Hosting crosswalks for entities this catalogue does not own (D-6 stands).
2. Resolving references against live remote catalogues; resolution is against this catalogue's canonical records (the mapped side's own gate validates its half).
3. Any new records or vocabulary changes.

## 3. The two-sided contract

The metamodel defines `dea:maps-to` (source `dea:Entity`, target `dea:InformationClass`, inverse `dea:mapped-from`, category traceability). The two sides validate complementary halves:

- **Mapped side (other catalogues):** the entity record carries `maps_to: dea:information-class-<slug>`; its gate validates the id form and its own admission.
- **Class side (this catalogue):** the class record may catalogue the inverse via `relationships.mapped_from`; Gate 8 validates that entries are canonical external ids. The inbox queues crosswalk proposals from other catalogues until their landing CR promotes them.

Neither side resolves remote repositories at gate time; both validate identifier form and local resolution. This keeps the gate fast, offline, and deterministic in CI.
