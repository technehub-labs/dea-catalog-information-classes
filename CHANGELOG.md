# Changelog

All notable changes to the Information Class catalogue are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Allocation is recorded in the OpenDEAM root model; see `metamodel-pointer.yaml`.

## [Unreleased]

### Added

- `CR-IC-CAT-09`: machine-readable control references. `mandated_controls[]` on every record pairs the class-side obligation with the canonical Control id (`dea:control-<slug>`) it references in `dea-catalog-controls`. Gate 10 validates id form (stage 1) with cross-catalogue resolution deferred via `reconciliation/control-reference-registry.yaml` until the CTL catalogue populates (stage 2). All eight records enriched; 20 unique control references.

### Added

- `CR-IC-CAT-08`: jurisdiction-regime axis. Eight-value closed vocabulary (`classifications/jurisdiction-regime-classifications.yaml`) refining regulatory regimes with anchoring statutes; each value declares which regimes it refines, and Gate 6 enforces per-record compatibility. Five records enriched; the regulatory-regime enum is untouched.

### Added

- `CR-IC-CAT-07`: sensitivity-lattice enrichment. Two restricted-but-unregulated classes admitted: Trade Secret and Material Non-Public Information (MNPI). The confidential/restricted boundary is now exercised by unregulated classes; every sensitivity band carries at least one unregulated member. Catalogue count: 8.

### Added

- `CR-IC-CAT-06`: generated `CATALOG.yaml` index per the catalog repository standard. Vendored regenerator + index gate from `dea-metaframework` v2.6.0; record subtrees renamed to the id-verbatim layout; pointer gained its additive `id` field; `contributions/` intake directory added; CI Step 9 enforces index freshness and strict validation.

### Added

- `CR-IC-CAT-05`: cross-catalogue crosswalk validation. Optional `relationships.mapped_from[]` added to the schema (inverse of `dea:maps-to`), `reconciliation/crosswalk-inbox.yaml` intake queue for crosswalks proposed by other catalogues, and Gate 8 (`scripts/check_crosswalk.py`) validating id form, external-only resolution, and inbox entries.

### Added

- `CR-IC-CAT-04`: initial population. Six Information Class records admitted under the record standard: public, internal, confidential, PII, PHI, PCI. Each carries a canonical id, schema-valid fields, R-1..R-5 conformance, and a per-record README.

### Added

- `CR-IC-CAT-03`: record documentation standard. `docs/RECORD-STANDARD.md` defines the canonical record shape, the semantic rules R-1..R-5 beyond the schema, the per-record README contract, and the admission posture. Gate 7 (`scripts/check_record_documentation.py`) enforces the standard on every record and asserts the standard's own presence on an empty tree. The record-posture gate's population-gates list is reconciled with the actual gates.

### Added

- `CR-IC-CAT-02`: classification taxonomy. The two axes moved to first-class vocabulary files under `classifications/` (sensitivity, regulatory regime), cross-checked against the schema enums by a new taxonomy gate (`scripts/check_taxonomy.py`, Gate 6). Vocabularies unchanged from `CR-IC-CAT-01`.

## [0.1.0] - 2026-02-11

### Added

- `CR-IC-CAT-01`: catalogue foundation (methodology-first bring-up). Metamodel pointer remains pinned to OpenDEAM v0.2.1 by the root model.
- Schema projection of the metamodel InformationClass entity schema with the catalogue-instance layer (classification axes, governance).
- `docs/FOUNDATIONS.md`: cardinal scope, two classification axes, six admission criteria, cross-catalogue reference policy, eight-decision register.
- Five CI gates: parse, pointer, schema projection, writing rules, record posture.

### Not in this release

- No records admitted. Population is `CR-IC-CAT-04`, gated on the taxonomy CR (`CR-IC-CAT-02`) and the record documentation standard (`CR-IC-CAT-03`).
