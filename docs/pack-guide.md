# Relationship Authorization Governance pack guide

Governance for relationship-based authorization schemas, tuples, derived relations, graph checks, list operations, consistency, inheritance, cycles, tenant isolation, mutation, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `relationship-authorization-governance-pack` is an installable SSOT governance pack for Relationship Authorization. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for relationship authorization, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`relationship-authorization-governance-pack`](https://pypi.org/project/relationship-authorization-governance-pack/)
- GitHub package repository: [`groupsum/relationship-authorization-governance-pack`](https://github.com/groupsum/relationship-authorization-governance-pack)
- Import package: `relationship_authorization_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 5 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:relationship-authorization`
- PyPI package: `relationship-authorization-governance-pack`
- Import package: `relationship_authorization_governance_pack`
- GitHub repository: [groupsum/relationship-authorization-governance-pack](https://github.com/groupsum/relationship-authorization-governance-pack)
- Reservation owner: `extension-pack:relationship-authorization-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Relationship Authorization

## Authority Sources

- [Zanzibar: Google's Consistent, Global Authorization System](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/)
- [OpenFGA Documentation](https://openfga.dev/docs)

## Included ADRs

- [`adr:relationships-own-graph-based-resource-authorization`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/adr/ADR-1000-relationships-own-graph-based-resource-authorization.yaml) - Relationships Own Graph Based Resource Authorization
- [`adr:relationship-consistency-model-is-explicit`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/adr/ADR-1001-relationship-consistency-model-is-explicit.yaml) - Relationship Consistency Model Is Explicit
- [`adr:tenant-boundaries-are-enforced-in-the-relationship-model`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/adr/ADR-1002-tenant-boundaries-are-enforced-in-the-relationship-model.yaml) - Tenant Boundaries Are Enforced In The Relationship Model

## Included SPECs

- [`spc:relationship-schema-and-tuple-contract`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/specs/SPEC-2000-relationship-schema-and-tuple-contract.yaml) - Relationship Schema And Tuple Contract
- [`spc:derived-relation-and-permission-contract`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/specs/SPEC-2001-derived-relation-and-permission-contract.yaml) - Derived Relation And Permission Contract
- [`spc:relationship-check-and-list-contract`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/specs/SPEC-2002-relationship-check-and-list-contract.yaml) - Relationship Check And List Contract
- [`spc:consistency-inheritance-and-cycle-contract`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/specs/SPEC-2003-consistency-inheritance-and-cycle-contract.yaml) - Consistency Inheritance And Cycle Contract
- [`spc:tenant-isolation-mutation-and-audit-contract`](https://github.com/groupsum/relationship-authorization-governance-pack/blob/master/src/relationship_authorization_governance_pack/templates/specs/SPEC-2004-tenant-isolation-mutation-and-audit-contract.yaml) - Tenant Isolation Mutation And Audit Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect relationship_authorization_governance_pack
uvx --from ssot-registry ssot pack preflight . relationship_authorization_governance_pack --all
uvx --from ssot-registry ssot pack sync . relationship_authorization_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from relationship_authorization_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-relationship-schema-and-tuple-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/relationship-authorization-governance-pack](https://github.com/groupsum/relationship-authorization-governance-pack)
- PyPI package: [relationship-authorization-governance-pack](https://pypi.org/project/relationship-authorization-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the relationship authorization governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
