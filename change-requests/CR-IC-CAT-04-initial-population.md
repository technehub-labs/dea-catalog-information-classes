# CR-IC-CAT-04: Initial Information Class Population

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-04 |
| **Title** | Admit the initial Information Class records |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-01` (foundation), `CR-IC-CAT-02` (taxonomy), `CR-IC-CAT-03` (record documentation standard) |

## 1. Executive summary

This CR admits the catalogue's first six Information Class records, completing the foundation-to-population arc: the classification taxonomy is ratified (`CR-IC-CAT-02`), the record documentation standard is landed (`CR-IC-CAT-03`), and the records below satisfy both. Each record lands as a canonical per-record subtree (`entities/v1-alpha/<entity-id>/`) with its README, per the org-wide entity-storage layout and the record standard.

## 2. Records admitted

| Record | Sensitivity | Regulatory regime | Evidence anchor |
|---|---|---|---|
| `dea:information-class-public` | public | none | Enterprise information-security policy, public-disclosure chapter |
| `dea:information-class-internal` | internal | none | Enterprise information-security policy, classification scheme |
| `dea:information-class-confidential` | confidential | none | Enterprise information-security policy, classification scheme |
| `dea:information-class-pii` | restricted | PII | Privacy statutes (e.g. GDPR, CCPA); internal privacy policy |
| `dea:information-class-phi` | restricted | PHI | Health-privacy regimes (e.g. HIPAA); internal health-information policy |
| `dea:information-class-pci` | restricted | PCI | PCI DSS; card-brand operating regulations |

The set covers all four sensitivity bands and all three named regulatory regimes. The three `none`-regime records occupy the three non-regulated bands; no record mixes `none` with a named regime (D-4).

## 3. Conformance state

Each record: carries a canonical `dea:information-class-*` id; validates against `schemas/entity.schema.json`; satisfies R-1..R-5 (`metadata.established_by` = this CR; `governance.source_and_evidence` names an authority; non-empty `handling_requirements` phrased as obligations; D-4 regime exclusivity; `retention` names a rule or schedule); and carries the per-record README mirrored from its fields. Gate 5 (posture) has switched to populated mode: it now asserts canonical ids per record and the presence of the population gates. All seven gates are green on this tree.

## 4. Out of scope

1. Additional classes (per-sector or per-jurisdiction refinements): a future CR against the taxonomy.
2. Cross-catalogue `dea:maps-to` crosswalk validation: `CR-IC-CAT-05`.
3. Widening the classification vocabularies.
