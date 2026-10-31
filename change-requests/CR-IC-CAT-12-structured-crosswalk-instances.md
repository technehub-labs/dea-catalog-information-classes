# CR-IC-CAT-12: Structured Crosswalk Instances

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-12 |
| **Title** | Upgrade mapped_from from bare ids to structured relationship instances |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | `CR-IC-CAT-10` (information-asset crosswalk intake) |

## 1. Executive summary

`CR-IC-CAT-10` promoted the seven `dea:maps-to` assertions from `dea-catalog-information-assets` onto this catalogue's class records as bare inverse ids. The mapped side, however, carries full relationship instances: id, relationship instance id, classification rationale, and provenance. The class side mirrored only the ids, discarding the acceptance evidence. This CR upgrades `relationships.mapped_from` entries from bare strings to structured instances mirroring the asserting side, so the class record carries *why* each asset maps to it, not merely *that* it does.

## 2. Cross-org sweep (motivation evidence)

A sweep of every populated catalogue in the org for records asserting mappings into this catalogue (business-objects: 75 records; business-capabilities: 41; information-assets: 7; others empty) found exactly one source: `dea-catalog-information-assets`. All seven assertions target `dea:information-class-internal` (six) and `dea:information-class-confidential` (one). No other catalogue currently maps into this one; the structured form is validated against the full known population, not a sample.

## 3. Entry shape

Each `mapped_from` entry is now an object:

| Field | Source | Rule |
|---|---|---|
| `id` | the asserting record's canonical id | must start `dea:`; must not resolve to this catalogue's own records |
| `relationship` | the relationship instance id on the mapped side | must match `^dea:relationship-` |
| `rationale` | verbatim from the mapped side's assertion | non-empty |
| `provenance.asserted_at` / `asserted_by` / `verification_status` | verbatim | all present; status in {verified, unverified} |

The rationale and provenance are copied verbatim from the asserting records (pulled fresh from `dea-catalog-information-assets` at `CR-IA-CAT-04`), not paraphrased; the class side mirrors, never interprets. Gate 8 enforces the full structure; the legacy bare-id form remains parseable but non-conformant to the new schema and flagged for upgrade, so no silent mixing.

## 4. Records enriched

| Record | Entries | Notes |
|---|---|---|
| `dea:information-class-internal` | 6 structured instances | viewer and governance assets; all `kind: related` |
| `dea:information-class-confidential` | 1 structured instance | the capability-catalog integrity report: need-to-know consumption |

Both records' READMEs now carry the classification rationale per mapped asset, not just the id list.

## 5. Out of scope

1. The mapped side's data (assertions live in `dea-catalog-information-assets`; their gates validate them).
2. A `classification` mapping kind: the mapped side notes their `kind: related` is pending a metamodel classification mapping kind (`CR-IA-CAT-02` §2); when the metamodel ratifies one, both sides upgrade in coordinated CRs.
3. New mapped assets: each new asserting catalogue population follows the `CR-IC-CAT-10` intake pattern.
