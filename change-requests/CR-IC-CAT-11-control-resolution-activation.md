# CR-IC-CAT-11: Control-Reference Resolution Activation

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-11 |
| **Title** | Activate stage-2 control resolution against the populated controls catalogue |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | Org-wide catalog advancement (Wave 1) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-02 |
| **Depends on** | CR-IC-CAT-09 (the two-stage contract), CR-CTL-CAT-02 (the population that resolves every reference) |
| **Trigger** | CR-IC-CAT-09 deferred cross-catalogue resolution ("stage 2, when CTL records land"). The controls catalogue populated 20 canonical records under CR-CTL-CAT-02 (dea-catalog-controls PR #2), one per referenced id. Stage 2 can activate. |

## 1. Executive summary

`reconciliation/control-reference-registry.yaml` flips `resolution_active: true` and carries all 20 referenced control ids, each citing CR-CTL-CAT-02. Gate 10 now resolves every `mandated_controls` reference against the registry; an id absent from the registry is a finding.

## 2. Scope

In scope: the registry file, this CR, CHANGELOG, `CATALOG.yaml` regeneration (no entity-count change; the open-CR counter moves 10 to 11 under the known defect, CR-IC-CAT-10 section 5).

Out of scope: record content (the citations were already correct); controls-catalogue changes; the regenerator modernization.

## 3. Acceptance criteria

1. `check_control_references.py` prints `Resolution stage: 2 (active)` and `Findings: 0`.
2. All ten gates pass in CI.

## 4. NOT-list

1. No class-record changes.
2. No new controls referenced.
