# relationship-authorization-governance-pack

Governance for relationship-based authorization schemas, tuples, derived relations, graph checks, list operations, consistency, inheritance, cycles, tenant isolation, mutation, and audit evidence.

## Package identity

- Pack ID: `pack:relationship-authorization`
- PyPI distribution: `relationship-authorization-governance-pack`
- Python import: `relationship_authorization_governance_pack`
- Reservation owner: `extension-pack:relationship-authorization-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add relationship-authorization-governance-pack
uv run ssot pack sync . relationship_authorization_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/
- https://openfga.dev/docs
