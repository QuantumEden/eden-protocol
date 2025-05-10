# /src/dao/vote_commitment.py

"""
DAO Vote Commitment Engine for Eden Protocol

This module simulates a secure XP-weighted voting commitment
system for symbolic proposals, using hashed identity and XP integrity.
"""

import hashlib

def generate_vote_commitment(user_hash: str, proposal_id: str, vote: str, xp_score: int) -> str:
    """
    Create a deterministic commitment string (simulated ZK-style hash).
    Inputs:
      - user_hash: anonymized ID from identity_hash.py
      - proposal_id: DAO proposal identifier
      - vote: "yes" or "no"
      - xp_score: user's verified XP (used as weight)
    Output:
      - hashed commitment string
    """
    vote_data = f"{user_hash}|{proposal_id}|{vote.lower()}|{xp_score}"
    return hashlib.sha256(vote_data.encode("utf-8")).hexdigest()

# Simulated test
if __name__ == "__main__":
    user_hash = "4dcfe834...mocked"
    proposal_id = "DAO_PROPOSAL_001"
    vote = "yes"
    xp = 820

    commit = generate_vote_commitment(user_hash, proposal_id, vote, xp)
    print("\n[DAO VOTE COMMITMENT HASH]")
    print(f"Commitment: {commit}")
