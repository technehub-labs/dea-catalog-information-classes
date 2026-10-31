# CR-IC-CAT-13: Pointer-Based Repository URL in the Index

| Field | Value |
|---|---|
| **CR** | CR-IC-CAT-13 |
| **Title** | Resolve CATALOG.yaml's repository field from the pointer, not the live remote |
| **Status** | Implemented in this PR |
| **Layer** | Catalogue (L4 Data Foundation) |
| **Programme** | DEA catalog rollout (L4 data foundation) |
| **Repository** | `technehub-labs/dea-catalog-information-classes` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-31 |
| **Depends on** | `CR-IC-CAT-06` (generated index), PR #17 (post-merge index alignment) |

## 1. Executive summary

The vendored regenerator resolves the index's `repository` field from the checkout's live `remote.origin.url`. That value varies across environments (with or without the `.git` suffix, credential-bearing authenticated forms, mirrors), while the freshness gate compares the regenerated index byte-for-byte against the committed one. Twice in this engagement (PRs #11 and #17) that variance failed CI spuriously. This CR makes the field environment-independent: the pointer's new top-level `repository` key is the canonical source, with the live remote as a backward-compatible fallback.

## 2. Change to the vendored regenerator

`scripts/regenerate_catalog.py` gains `resolve_repository_url(catalog_root, pointer)`:

1. If the pointer carries a top-level `repository` key, use it (credential-stripped, same sanitization as before).
2. Otherwise fall back to `remote.origin.url` (legacy behavior, unchanged).

The fallback preserves compatibility for catalogues that have not yet added the pointer key. The vendored copy here is patched in place; the same patch is flagged for upstreaming to `dea-metaframework` so every catalogue benefits (section 5).

## 3. Pointer change

`metamodel-pointer.yaml` gains a top-level `repository` key carrying the canonical `.git`-form URL. This is an additive pointer change (PR + patch bump per the pointer header) and follows the `id`/`name`/`abbreviation` precedent of CR-IC-CAT-06 and PR #13. The CI remote-canonicalization workaround (added in PR #11) is removed: it is now redundant, and its removal is itself a test that the pointer path works.

## 4. Verification

The failure mode was reproduced and then killed: a fresh clone whose origin was set to a credential-bearing, non-`.git` URL (the exact PR #11 failure shape) regenerates the identical committed index (`--check` current, exit 0) because the pointer value takes precedence over the wrong remote. The committed index was regenerated against the pointer value; strict validation passes (8 entities).

## 5. Upstream note

The identical patch applies to `dea-metaframework`'s `tools/regenerate_catalog.py` (the vendored source, v2.6.0): the `resolve_repository_url` precedence change is behavior-preserving for catalogues without the pointer key and removes an environment-dependent output for those that adopt it. Recommended as a metaframework CR; this catalogue will re-vendor when it lands.
