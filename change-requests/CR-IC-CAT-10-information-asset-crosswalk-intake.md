# CR-IC-CAT-10: Information Asset Crosswalk Intake

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-10 |
| **Title** | Promote the first mapped-from crosswalks (information-assets catalogue) |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | Information Asset catalog bring-up (unblocks capabilities U-2) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-29 |
| **Depends on** | CR-IC-CAT-05 (crosswalk contract), CR-IA-CAT-04 (proposing CR, landed as dea-catalog-information-assets PR #4) |
| **Trigger** | The information-assets catalogue admitted its first seven canonical records, each asserting a `dea:maps-to` crosswalk into a canonical class here. Per CR-IC-CAT-05 section 3, promotion onto `relationships.mapped_from` happens in a landing change on this side. These are the first bound objects for this catalogue's classes. |

## 1. Executive summary

This CR promotes seven crosswalks proposed by `CR-IA-CAT-04` (dea-catalog-information-assets): the class records `dea:information-class-confidential` and `dea:information-class-internal` gain `relationships.mapped_from` inverse references, and their READMEs gain a Mapped-from section. The crosswalk inbox stays empty (all seven entries are promoted by this CR, none queued).

## 2. Scope

### In scope

1. `entities/v1-alpha/dea:information-class-confidential/`: `mapped_from` with 1 entry; README Mapped-from section.
2. `entities/v1-alpha/dea:information-class-internal/`: `mapped_from` with 6 entries; README Mapped-from section.
3. `CATALOG.yaml` regeneration (no count changes; `open_change_requests` moves 9 to 10 under the current counter, see section 5).
4. CHANGELOG entry and this CR's register row.

### Out of scope

1. Any change to the class taxonomy, sensitivity or regime vocabularies, or handling requirements.
2. Any change to the mapped side (the assertions live on the information-asset records; their catalogue's Gate 7 validates them against its vendored snapshot of our canonical ids).
3. Regenerator modernization (section 5 names it; it is a separate CR).

## 3. The two-sided contract, exercised

Mapped side (dea-catalog-information-assets, `CR-IA-CAT-04`): each record carries a `maps-to` relationship instance targeting the canonical id here, with `mapping`, `rationale`, and `provenance`; their Gate 7 validates targets against a vendored registry snapshot fetched from this catalogue's CATALOG.yaml (2026-10-29).

Class side (this CR): the inverse references catalogued on the class records; Gate 8 validates they are canonical external ids and never resolve to this catalogue's own records. Neither side resolves remote repositories at gate time.

## 4. Acceptance criteria

1. Gate 8 passes: every `mapped_from` entry is an external canonical id; inbox entries (none) trivially valid.
2. All ten gates pass in CI.
3. `CATALOG.yaml` regenerates without entity-count changes (8 canonical).

## 5. Known defect named (not fixed here)

The vendored `regenerate_catalog.py` counts a CR as open unless its status line reads exactly `Merged` (the pre-CR-ECF-011 heuristic). With all nine prior CRs implemented, the committed counter reads 9; after this CR it reads 10. The org-consistent fix (terminal-status closed set, landed in dea-metaframework v2.6.0 tools) requires this catalogue's CR status vocabulary and pointer shape to move together; that modernization is a standalone CR and is recorded here so the inflated count is not mistaken for nine (now ten) open requests.

## 6. NOT-list

1. No new class records; no taxonomy changes.
2. No local hosting of crosswalks for entities this catalogue does not own (D-6 stands).
3. No remote resolution introduced into any gate.
