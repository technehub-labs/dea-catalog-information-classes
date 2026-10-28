# RECORD STANDARD: Information Class record documentation

**Status:** Established by `CR-IC-CAT-03` on 2026-02-11.
**Scope of this document:** the documentation standard every admitted Information Class record must satisfy. Population (`CR-IC-CAT-04`) enforces this standard through Gate 7 (`scripts/check_record_documentation.py`).

---

## 1. Record file

One canonical YAML file per record, at `entities/v1-alpha/<entity-id>/<entity-id>.yaml` (colons normalized to hyphens in the path, per the org-wide path-derivation contract). The record's `id` matches the metamodel InformationClass namespace: `dea:information-class-<slug>`.

### 1.1 Canonical shape (illustrative)

```yaml
id: dea:information-class-<slug>
type: InformationClass
name: <class name, 1..200 chars>
description: <what the class covers, <= 2000 chars>
version: 0.1.0
lifecycle_status: planned
sensitivity: <public | internal | confidential | restricted>
regulatory_regime: [<PII | PHI | PCI | none>, ...]
handling_requirements:
  - <mandatory control implied by the class>
retention: <retention rule or schedule>
governance:
  functional_owner: <owner>
  steward: <steward>
  approval_status: <proposed | under_review | approved>
  source_and_evidence: <the authority that makes the class real>
metadata:
  established_by: <CR reference that admitted the record>
```

### 1.2 Field rules beyond the schema

The schema (`schemas/entity.schema.json`) is the validation surface; this standard adds semantic rules the schema cannot express:

| Rule | Requirement |
|---|---|
| R-1 | `metadata.established_by` must be present and name the admission CR (`CR-IC-CAT-04` or successor) |
| R-2 | `governance.source_and_evidence` must be non-empty and name an authority: a statute or regulation, a published standard, a contractual mandate, or an internal policy with an owner. Descriptive prose is not evidence |
| R-3 | `handling_requirements` must be non-empty; each entry states a control the class mandates, phrased as an obligation, not an observation |
| R-4 | D-4: `none` appears in `regulatory_regime` only as the sole entry |
| R-5 | `retention` must be present and name a rule or schedule, not a duration alone |

## 2. Record README

Each record subtree carries a `README.md` next to the canonical YAML, per the README-per-folder rule in the org-wide entity-storage layout. Required sections:

```markdown
# <class name>

<the record's `description`, verbatim>

## Classification
- **Sensitivity:** <sensitivity>
- **Regulatory regime:** <regime list>

## Handling requirements
<the record's `handling_requirements`, as a list>

## Retention
<the record's `retention`>

## Provenance
- **Established by:** <metadata.established_by>
- **Owner / steward:** <functional_owner> / <steward>
- **Evidence:** <governance.source_and_evidence>
```

The README mirrors the record; it does not extend it. Facts that belong in the record go in the record, and the README is regenerated.

## 3. Admission posture

A record lands in `candidate` form (in its subtree, not yet canonical) with `lifecycle_status: planned` and `governance.approval_status: proposed`. The admission CR moves it to canonical: `lifecycle_status: active`, `approval_status: approved`. Gate 7 enforces the documentation standard on every record file under `entities/v1-alpha/`, regardless of posture; the record-posture gate (Gate 5) enforces the population-gates contract.

## 4. Gate

`scripts/check_record_documentation.py` (Gate 7) walks every `entities/v1-alpha/**/*.yaml` record and asserts R-1 through R-5 and the README contract. With no records it asserts the standard's own presence: the gate fails if this document or the required gate list drifts, so the standard cannot be silently dropped before population.
