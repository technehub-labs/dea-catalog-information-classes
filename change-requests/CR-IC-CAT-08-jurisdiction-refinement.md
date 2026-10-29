# CR-IC-CAT-08: Per-Jurisdiction Regime Refinement

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-08 |
| **Title** | Jurisdiction-regime axis: refine regulatory regimes with anchoring statutes |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-02` (taxonomy), `CR-IC-CAT-07` (lattice enrichment) |
| **Supersedes** | FOUNDATIONS D-8 (refinement-out-of-scope decision; this CR is the refinement it deferred) |

## 1. Executive summary

This CR adds the jurisdiction-regime axis: an optional, closed third classification that refines a record's regulatory-regime values with the jurisdiction-specific statute or rule that anchors them. It resolves the D-8 deferral without widening any existing vocabulary: the regulatory-regime enum is untouched, and the new axis is a separate, gate-checked vocabulary.

## 2. Design: refine, never widen

The axis carries eight values at landing (eu-gdpr, uk-gdpr, us-ccpa-cpra, us-hipaa, pci-dss, us-dtsa, eu-trade-secrets-directive, us-securities-insider-trading). Each value declares which regime(s) it `refines`:

- Values refining a named regime (PII, PHI, PCI) may appear only on records carrying that regime.
- Values refining `none` anchor statutory authority for unregulated-but-protected classes (the CR-IC-CAT-07 lattice) and may appear only on `[none]` records.

Gate 6 enforces compatibility per record from the vocabulary's `refines` declarations; the schema enum and the vocabulary file remain in lockstep like the other two axes. Adding a jurisdiction value is a taxonomy CR; editing a value's `refines` set is a taxonomy CR.

## 3. Records enriched

| Record | regulatory_regime | jurisdiction_regime |
|---|---|---|
| `dea:information-class-pii` | PII | eu-gdpr, uk-gdpr, us-ccpa-cpra |
| `dea:information-class-phi` | PHI | us-hipaa |
| `dea:information-class-pci` | PCI | pci-dss |
| `dea:information-class-trade-secret` | none | us-dtsa, eu-trade-secrets-directive |
| `dea:information-class-material-nonpublic-information` | none | us-securities-insider-trading |

The three `[none]` band records (public, internal, confidential) carry no jurisdiction values: their protection derives from enterprise policy alone, with no anchoring statute.

## 4. Out of scope

1. Exhaustive jurisdiction coverage (e.g. all US state privacy statutes, APPI, LGPD): follow-up taxonomy CRs in the same shape.
2. Machine-readable control references: `CR-IC-CAT-09`.
3. Retention periods per jurisdiction: retention remains a stated rule per record; jurisdiction-specific retention matrices are a future CR if the population demands them.
