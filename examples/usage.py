"""Find a specification and its downstream path in the installed manifest."""

from relationship_authorization_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:relationship-schema-and-tuple-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-relationship-schema-and-tuple-contract.yaml"
