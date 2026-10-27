# Cardinal Rules (CR-BP-118)

Pinned governance rules that the conformance gate cannot silently relax.

## R1. Authorship-field cardinal rule

Every authorship-bearing field in every artifact of every `technehub-labs/*`
repository must carry the value `Emmanuel A. Otchere` (or, for org-level
CITATION.cff entries, `TechNeHub Labs`). The string `Coder`, `Agent`,
`Hermes`, `Claude`, `GPT`, `Cline`, `OpenAI`, `MiniMax`, `MiniMax-M3`, or
any other agent/tool name is forbidden in any authorship-bearing field of
any published artifact.

**Authorship-bearing fields** (the registry at
`reconciliation/authorship-fields.yaml` is the canonical list):

- `**Owner**` in CR doc headers (`change-requests/CR-*.md`)
- `**Author**` in CR doc headers

The agent's role in producing the work is recorded in
`change-requests/CR-IC-NNN.md` per the CR governance chain. It is not a
named role in the published artifact.

## R2. Named-role file cardinal rule

Any file or field whose purpose is to name a person playing a named role
(commissioning authority, decision-maker, accountable owner, signatory,
copyright holder, etc.) — including `NOTICE`, `LICENSE`, copyright
headers, `AUTHORS`, named-role fields in schemas, named-role fields in
contribution templates — must carry `Emmanuel A. Otchere` (or, for the
org, `TechNeHub Labs`).

The role of a tool or AI agent in producing the work is recorded in the
CR chain; it is not a named role in the published artifact.

## How the rules are enforced

`scripts/check_authorship.py` (gate [32] in the rollup, blocking) enforces
R1 mechanically. The gate is data-driven from
`reconciliation/authorship-fields.yaml`; adding a new authorship-bearing
field to the registry is itself a CR-level change, not a gate-level
relaxation. Three sub-rules:

- **AUT-001 (blocking)**: every authorship-bearing field's value must
  pass the denylist substring check.
- **AUT-002 (blocking)**: every authorship-bearing field, if its parent
  block is present, must itself be present.
- **AUT-003 (blocking under `--strict`)**: every authorship-bearing
  field's value must be in the allowlist.

## Entity-system conformance

`scripts/check_entity_system.py` (CR-BP-123) enforces the General Entity
System on `entities/**/*.yaml`, data-driven from
`reconciliation/entity-system-registry.yaml`. `scripts/validate_entries.py`
additionally validates every record against
`schemas/information-class.schema.json`.
