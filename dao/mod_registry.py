"""
DAO Mod Registry — Ledger of Approved Symbolic Modules

Tracks mod_id, creator, approval status, registration metadata,
and now includes zkXP commit hashes, soulform requirements,
and cryptographic chain signatures for blockchain anchoring.
"""

import datetime
import json
import hashlib
from typing import Optional, Dict

# Simulated registry (would be blockchain-anchored in production)
approved_mods: Dict[str, Dict] = {
    "tai_chi_001": {
        "creator": "user0x8da3...",
        "approved_on": "2025-05-01",
        "trait": "discipline",
        "xp_value": 50,
        "glyph": "🜂",
        "soulform_required": "wu_xing_alpha",
        "zkxp_hash": "zkxp001",
        "chain_signature": ""
    }
}


def is_mod_approved(mod_id: str) -> bool:
    return mod_id in approved_mods


def get_approved_mod_ids() -> list:
    return list(approved_mods.keys())


def register_mod(
    mod_id: str,
    creator: str,
    trait: str,
    xp_value: int,
    glyph: str,
    soulform_required: Optional[str],
    zkxp_hash: Optional[str],
    manifest: dict
) -> bool:
    manifest_serialized = json.dumps(manifest, sort_keys=True)
    chain_signature = hashlib.sha256(manifest_serialized.encode()).hexdigest()

    approved_mods[mod_id] = {
        "creator": creator,
        "approved_on": datetime.date.today().isoformat(),
        "trait": trait,
        "xp_value": xp_value,
        "glyph": glyph,
        "soulform_required": soulform_required or "none",
        "zkxp_hash": zkxp_hash or "none",
        "chain_signature": chain_signature
    }
    return True


def get_mod_signature(mod_id: str) -> Optional[str]:
    return approved_mods.get(mod_id, {}).get("chain_signature")


def get_mod_metadata(mod_id: str) -> Optional[Dict]:
    return approved_mods.get(mod_id)


# Example
if __name__ == "__main__":
    print("✅ Approved mods:", get_approved_mod_ids())
    print("✅ Tai Chi mod approved?", is_mod_approved("tai_chi_001"))
    print("🔐 Mod hash:", get_mod_signature("tai_chi_001"))
