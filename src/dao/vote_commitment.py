"""
DAO Vote Commitment Engine — Now with Mod Proposal Support

Supports soulbound XP-weighted voting on all proposal types:
- Core system upgrades
- Shadow protocol changes
- Mod integration requests
- Ritual-enforced governance
- zkXP commit tracking
"""

import hashlib

# Proposal type enums
CORE_UPGRADE = 0
SHADOW_PROTOCOL = 1
MOD_PROPOSAL = 2
RITUAL_DECREE = 3
XP_GOVERNANCE = 4


def generate_vote_commitment(
    user_id: str,
    proposal_id: str,
    vote_choice: str,
    proposal_type: int,
    soulform_id: str = "",
    zkxp_hash: str = ""
) -> str:
    payload = f"{user_id}:{proposal_id}:{vote_choice}:{proposal_type}:{soulform_id}:{zkxp_hash}"
    return hashlib.sha256(payload.encode()).hexdigest()


def validate_vote_commitment(
    user_id: str,
    proposal_id: str,
    vote_choice: str,
    proposal_type: int,
    commitment_hash: str,
    soulform_id: str = "",
    zkxp_hash: str = ""
) -> bool:
    expected = generate_vote_commitment(
        user_id,
        proposal_id,
        vote_choice,
        proposal_type,
        soulform_id,
        zkxp_hash
    )
    return expected == commitment_hash


# Example
if __name__ == "__main__":
    h = generate_vote_commitment(
        "user123",
        "mod:tai_chi_001",
        "yes",
        MOD_PROPOSAL,
        soulform_id="wu_xing_alpha",
        zkxp_hash="a1b2c3d4"
    )
    assert validate_vote_commitment(
        "user123",
        "mod:tai_chi_001",
        "yes",
        MOD_PROPOSAL,
        h,
        soulform_id="wu_xing_alpha",
        zkxp_hash="a1b2c3d4"
    )
    print("✅ Mod vote commitment with soulform and zkXP hash verified.")
