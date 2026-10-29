# CR-IC-CAT-09: Machine-Readable Control References

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-09 |
| **Title** | Reference Control records from class handling requirements |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-02-11 |
| **Depends on** | `CR-IC-CAT-07` (lattice enrichment) |

## 1. Executive summary

This CR makes the class-to-control relationship machine-readable. Every record's `handling_requirements` prose now has a parallel `mandated_controls[]` array: each entry pairs the class-side obligation with the canonical Control id it references in `dea-catalog-controls` (entity `dea:entity-control`, alias CTL). The controls catalogue is currently an unpopulated scaffold, so the gate enforces id form now and activates cross-catalogue resolution when CTL records land.

## 2. Design

Each entry is `{control, requirement}`:

- `control`: the canonical CTL id form `dea:control-<slug>`. Id-form validated at gate time; never a URL or a repository name.
- `requirement`: the obligation the class places on the referenced control, phrased as a mandate. This preserves R-3's human semantics while giving tooling a resolvable join key.

The two-stage gate (`scripts/check_control_references.py`, Gate 10):

- **Stage 1 (active):** every `control` matches `^dea:control-[a-z0-9-]+$`; every entry carries a non-empty `requirement`.
- **Stage 2 (dormant):** `reconciliation/control-reference-registry.yaml` carries `resolution_active: false` while the CTL catalogue is unpopulated. Flipping it to true (a follow-up CR when CTL records land) requires every referenced id to appear in the registry with a resolvable CTL record; an unresolvable reference becomes a finding.

## 3. Records enriched

All eight records. 20 unique control ids referenced across the catalogue, including shared controls (`dea:control-encryption-at-rest-and-transit` referenced by six classes, `dea:control-need-to-know-access` by two, `dea:control-disclosure-logging` by two); the sharing is intentional and is the join surface downstream consumers query.

## 4. Out of scope

1. Landing the CTL records themselves: the controls catalogue's own population, governed by its lifecycle (currently `proposed`).
2. Flipping `resolution_active`: a follow-up CR coordinated with the controls catalogue's population CR.
3. Any change to `handling_requirements` semantics; the prose remains the normative obligation statement, `mandated_controls` is the machine-readable projection.
