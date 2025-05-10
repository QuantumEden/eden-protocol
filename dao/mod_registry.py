# /dao/mod_registry.py

"""
DAO Mod Registry — Ledger of Approved Symbolic Modules

Tracks mod_id, creator, approval status, registration metadata,
and now cryptographic chain signatures for future blockchain anchoring.
"""

import datetime
import json
import hashlib

# Simulated registry (would be a blockchain anchor in production)
approved_mods = {
    "tai_chi_001": {
        "creator": "user0x8da3...",
        "approved_on": "2025-05-01",
        "trait": "discipline",
        "xp_value": 50,
        "glyph": "🜂",
        "chain_signature": ""
    }
}


def is_mod_approved(mod_id: str) -> bool:
    return mod_id in approved_mods


def get_approved_mod_ids():
    return list(approved_mods.keys())


def register_mod(mod_id: str, creator: str, trait: str, xp_value: int, glyph: str, manifest: dict):
    manifest_serialized = json.dumps(manifest, sort_keys=True)
    chain_signature = hashlib.sha256(manifest_serialized.encode()).hexdigest()

    approved_mods[mod_id] = {
        "creator": creator,
        "approved_on": datetime.date.today().isoformat(),
        "trait": trait,
        "xp_value": xp_value,
        "glyph": glyph,
        "chain_signature": chain_signature
    }
    return True


def get_mod_signature(mod_id: str):
    return approved_mods.get(mod_id, {}).get("chain_signature", None)


# Example
if __name__ == "__main__":
    print("Approved mods:", get_approved_mod_ids())
    print("Tai Chi mod approved?", is_mod_approved("tai_chi_001"))
    print("Mod hash:", get_mod_signature("tai_chi_001"))
