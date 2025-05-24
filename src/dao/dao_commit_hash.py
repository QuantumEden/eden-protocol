"""
DAO Proposal Hash Generator — Eden Protocol

Encodes proposal metadata (e.g., mod ID, soulform, XP, zkXP hash, type, timestamp)
into a cryptographic SHA-256 commitment used for DAO voting and audit integrity.
"""

import hashlib
import json
from datetime import datetime
from typing import Optional, Dict


def generate_proposal_commit(
    user_id: str,
    proposal_type: str,
    proposal_id: str,
    soulform_id: Optional[str] = None,
    zkxp_hash: Optional[str] = None,
    metadata: Optional[Dict] = None
) -> str:
    payload = {
        "user_id": user_id,
        "proposal_type": proposal_type,  # e.g., "MOD_PROPOSAL", "CORE_UPGRADE"
        "proposal_id": proposal_id,
        "soulform_id": soulform_id or "",
        "zkxp_hash": zkxp_hash or "",
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
        soulform_id="wu_xing_alpha",
        zkxp_hash="xp123abc456zkp",
        metadata={"xp": 50, "trait": "discipline", "mod_origin": "mod_registry"}
    )
    print("✅ Proposal Commit Hash:", hash_result)
