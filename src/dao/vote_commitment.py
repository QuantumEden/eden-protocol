# /src/dao/vote_commitment.py

"""
DAO Vote Commitment Engine — Now with Mod Proposal Support

Supports soulbound XP-weighted voting on all proposal types:
- Core system upgrades
- Shadow protocol changes
- Mod integration requests
"""

import hashlib

# Proposal type enums
CORE_UPGRADE = 0
SHADOW_PROTOCOL = 1
MOD_PROPOSAL = 2  # New: symbolic ritual, quest, or trait extension via mod


def generate_vote_commitment(user_id: str, proposal_id: str, vote_choice: str, proposal_type: int) -> str:
    payload = f"{user_id}:{proposal_id}:{vote_choice}:{proposal_type}"
    return hashlib.sha256(payload.encode()).hexdigest()


def validate_vote_commitment(user_id: str, proposal_id: str, vote_choice: str, proposal_type: int, commitment_hash: str) -> bool:
    expected = generate_vote_commitment(user_id, proposal_id, vote_choice, proposal_type)
    return expected == commitment_hash


# Example
if __name__ == "__main__":
    h = generate_vote_commitment("user123", "mod:tai_chi_001", "yes", MOD_PROPOSAL)
    assert validate_vote_commitment("user123", "mod:tai_chi_001", "yes", MOD_PROPOSAL, h)
    print("Mod vote commitment verified.")
