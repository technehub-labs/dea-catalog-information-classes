# CR-IC-01: Initial Information Class Catalog Build-Out

## Summary

Populates this scaffold repository with its first content and conformance
layer, per the General Entity System (CR-BP-123) and the Authorship
Cardinal Rule (CR-BP-118):

- `schemas/information-class.schema.json` — JSON Schema (draft 2020-12) for
  the InformationClass entity envelope: identity, sensitivity
  (public/internal/confidential/restricted), regulatory regime
  (PII/PHI/PCI/none), handling requirements, lifecycle, and provenance.
- `entities/v1-alpha/` — six seed records: public, internal,
  confidential, PII, PHI, PCI.
- `reconciliation/entity-system-registry.yaml` — this repo's slice of the
  entity-system registry, declaring the InformationClass profile.
- `reconciliation/authorship-fields.yaml` — this repo's slice of the
  authorship-field registry.
- `scripts/check_entity_system.py`, `scripts/check_authorship.py`,
  `scripts/validate_entries.py` — conformance and schema gates, ported
  from `dea-catalog-concepts` (registry-driven, unmodified gate logic).
- CI workflows: `validate-entity-system.yml`, `validate-authorship.yml`,
  `validate-entries.yml` (alongside the existing `validate-allocation.yml`).
- `CONTRIBUTING.md`, `CHANGELOG.md`, `docs/governance/cardinal-rules.md`,
  README refresh aligning entity metadata with OpenDEAM v0.2.1.

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Date:** 2026-02-11
