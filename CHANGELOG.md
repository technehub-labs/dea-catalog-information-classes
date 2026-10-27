# Changelog

All notable changes to this repository are documented here.

## [0.1.0] — 2026-02-11

### Added (CR-IC-01)

- `schemas/information-class.schema.json` — JSON Schema (draft 2020-12)
  for the InformationClass entity envelope.
- `entities/v1-alpha/` — six seed Information Class records: public,
  internal, confidential, PII, PHI, PCI.
- Entity-system conformance gate (`scripts/check_entity_system.py`,
  `reconciliation/entity-system-registry.yaml`), ported from
  `dea-catalog-concepts`.
- Authorship cardinal-rule gate (`scripts/check_authorship.py`,
  `reconciliation/authorship-fields.yaml`).
- Entry-schema validation (`scripts/validate_entries.py`).
- CI workflows: `validate-entity-system.yml`, `validate-authorship.yml`,
  `validate-entries.yml`.
- `CONTRIBUTING.md`, `docs/governance/cardinal-rules.md`,
  `change-requests/CR-IC-01-catalog-buildout.md`.

### Changed (CR-IC-01)

- README refreshed: entity metadata aligned with OpenDEAM v0.2.1
  (`dea:entity-information-class`, alias `IC`, L4 · L4-data-foundation);
  catalog structure updated to the populated layout.
