# /src/dao/dao_commit_hash.py

"""
DAO Proposal Hash Generator — Eden Protocol

Encodes proposal metadata (e.g., mod ID, proposal type, user, timestamp)
into a cryptographic SHA-256 commitment used for DAO voting integrity.
"""

import hashlib
import json
from datetime import datetime


def generate_proposal_commit(user_id: str, proposal_type: str, proposal_id: str, metadata: dict = None) -> str:
    payload = {
        "user_id": user_id,
        "proposal_type": proposal_type,  # e.g., "MOD_PROPOSAL", "CORE_UPGRADE"
        "proposal_id": proposal_id,
        "metadata": metadata or {},
        "timestamp": datetime.utcnow().isoformat()
    }
    encoded = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(encoded.encode()).hexdigest()


# Example use case
if __name__ == "__main__":
    hash_result = generate_proposal_commit(
        user_id="elder42",
        proposal_type="MOD_PROPOSAL",
        proposal_id="tai_chi_001",
        metadata={"xp": 50, "trait": "discipline"}
    )
    print("Proposal Commit Hash:", hash_result)
