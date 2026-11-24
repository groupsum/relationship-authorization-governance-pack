"""Inspect the installed pack identity."""

from relationship_authorization_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:relationship-authorization"
print(metadata["origin"]["id"])
