# /blockchain/edenchain_payload.py

import json
import os
from secure_enclave.zk_token_vault import vault
from dao.expansion_engine import proposals
from world_tree.ledger import compute_eden_vitality, user_snapshots

# Output all simulated payloads for blockchain anchoring
def export_edenchain_payloads():
    os.makedirs("data/edenchain/", exist_ok=True)

    # Export ZK token commitments
    with open("data/edenchain/zk_commitments.json", "w") as f:
        json.dump(vault, f, indent=2)

    # Export DAO proposals + votes
    with open("data/edenchain/dao_proposals.json", "w") as f:
        json.dump(proposals, f, indent=2)

    # Export symbolic world state
    world_state = {
        "user_count": len(user_snapshots),
        "eden_vitality_index": compute_eden_vitality()
    }
    with open("data/edenchain/world_tree_summary.json", "w") as f:
        json.dump(world_state, f, indent=2)

    print("✅ EdenChain payloads exported for ledger simulation.")

if __name__ == "__main__":
    export_edenchain_payloads()
