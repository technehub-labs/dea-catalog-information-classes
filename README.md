# Information Class

> A classification of information by sensitivity and regulatory regime (PII, PHI, PCI).

**Layer:** L4 · **Entity:** `IC` · **Metamodel:** [OpenDEAM v0.2.1](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=IC)

## Status

Content population in progress. The catalog carries seed
Information Class records under `entities/v1-alpha/` and the full
conformance gate suite (allocation, entity system, authorship,
entry schema) in CI.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-information-class` |
| Class Alias | `IC` |
| Layer | `L4` |
| Building Block | `L4-data-foundation` |
| Metamodel Version | v0.2.1 |

## Catalog Structure

```
dea-catalog-information-classes/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── entities/
│   └── v1-alpha/            ← Information Class records
├── schemas/
│   └── information-class.schema.json
├── reconciliation/          ← gate registries (entity system, authorship)
├── scripts/                 ← conformance gates
├── change-requests/         ← CR records
├── docs/governance/         ← cardinal rules
└── .github/workflows/       ← allocation, entity-system, authorship, entry validation
```

## Seed Classes

| Class | Sensitivity | Regulatory regime |
|-------|-------------|-------------------|
| Public | public | none |
| Internal | internal | none |
| Confidential | confidential | none |
| PII | restricted | PII |
| PHI | restricted | PHI |
| PCI | restricted | PCI |

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
