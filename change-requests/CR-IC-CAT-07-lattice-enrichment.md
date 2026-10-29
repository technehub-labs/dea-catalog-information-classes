# CR-IC-CAT-07: Sensitivity-Lattice Enrichment

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-07 |
| **Title** | Admit restricted-but-unregulated classes; exercise the confidential/restricted boundary |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-04` (population), `CR-IC-CAT-06` (generated index) |

## 1. Executive summary

The initial population covered all four sensitivity bands but left the restricted band populated only by regulated classes (PII, PHI, PCI). This CR admits two restricted classes whose protection obligation derives from legal authority outside the three named regimes, exercising the confidential/restricted boundary with unregulated classes and completing the lattice: every band now carries at least one unregulated class, and the restricted band carries both regulated and unregulated members.

## 2. Records admitted

| Record | Sensitivity | Regulatory regime | Authority |
|---|---|---|---|
| `dea:information-class-trade-secret` | restricted | none | Trade-secret statutes (e.g. DTSA, EU Trade Secrets Directive) |
| `dea:information-class-material-nonpublic-information` | restricted | none | Securities statutes (insider-trading, Regulation FD) |

Both records satisfy the record standard (R-1..R-5): canonical ids, schema-valid fields, authority-named `source_and_evidence`, obligation-phrased `handling_requirements`, D-4-compliant `none`-only regime lists, rule-named `retention`, and per-record READMEs mirrored from their fields.

## 3. The boundary question this answers

`CR-IC-CAT-01` fixed the four-band vocabulary but the population only demonstrated restriction via regulatory regime. The trade-secret record demonstrates restriction via economic value plus secrecy efforts; the MNPI record demonstrates restriction via securities-law exposure. Neither widens the taxonomy: the sensitivity and regulatory-regime vocabularies are unchanged; the records occupy existing cells (`restricted`, `none`) that were previously empty.

## 4. Out of scope

1. Additional unregulated restricted classes (e.g. critical-infrastructure details): follow-up CRs in the same shape.
2. Per-jurisdiction regime refinement: `CR-IC-CAT-08`.
3. Machine-readable control references: `CR-IC-CAT-09`.
