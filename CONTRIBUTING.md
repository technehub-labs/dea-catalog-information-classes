# Contributing to `dea-catalog-information-classes`

Minimal. The cardinal rules govern the only contribution shape that
matters for this repository.

## Authorship

Every authorship-bearing field in this repository must carry
`Emmanuel A. Otchere` (or, for org-level CFF entries, `TechNeHub Labs`).
The string `Coder`, `Agent`, `Hermes`, `Claude`, `GPT`, `Cline`, `OpenAI`,
`MiniMax`, `MiniMax-M3`, or any other agent/tool name is forbidden in
any authorship-bearing field of any published artifact.

This rule is enforced by gate [32] (`scripts/check_authorship.py`,
blocking). It is data-driven from
`reconciliation/authorship-fields.yaml`. The full rule statement lives
in `docs/governance/cardinal-rules.md`.

If your contribution introduces a new authorship-bearing field, extend
the registry in the same PR; the gate will block the change otherwise.

## Entity records

Each record is a YAML file under `entities/v1-alpha/` and must:

- carry a canonical `id` matching `^dea:information-class-[a-z0-9-]+$`,
- declare `type: InformationClass`,
- satisfy the envelope in `reconciliation/entity-system-registry.yaml`
  (ES-001..ES-005),
- validate against `schemas/information-class.schema.json`,
- carry `provenance.change_history` referencing the landing CR
  (`cr`, `date`, `change`).

`metamodel-pointer.yaml` is auto-generated from the OpenDEAM root model —
do not edit it manually; allocation changes go through
[dea-architecture-framework](https://github.com/technehub-labs/dea-architecture-framework).

## How to land work

1. Open a `feature/...`, `fix/...`, or `refactor/...` branch.
2. Develop, test, commit.
3. Open a PR; CI runs the conformance gates (allocation, entity system,
   authorship, entry schema). Address any failures before requesting
   review.
4. Squash-merge on approval; the branch is auto-deleted.

## Cardinal-rules reference

- [docs/governance/cardinal-rules.md](docs/governance/cardinal-rules.md)
- `reconciliation/authorship-fields.yaml`
- `reconciliation/entity-system-registry.yaml`
- `scripts/check_authorship.py` (gate [32])
