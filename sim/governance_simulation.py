# sim/governance_simulation.py
# Eden Protocol – Governance Simulation: DAO Proposal and Voting Test

import sys, os
import json
from datetime import datetime

# === Patch import path ===
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dao.governance_engine import (
    create_proposal,
    cast_vote,
    close_proposal
)

print("\n🌿 Governance Simulation: DAO Voting Ritual\n")

# === Step 1: Create Proposal ===
proposal = create_proposal(
    title="🌳 Launch World Tree Visualization",
    description="Enable symbolic dashboard for collective archetypal growth and health.",
    proposer_id="user001",
    timestamp=datetime.utcnow().isoformat() + "Z"
)

print("📜 Proposal Created:")
print(json.dumps(proposal, indent=2))
print("\n—" * 40)

# === Step 2: Cast XP-Weighted Votes ===
print("🗳️ Casting votes with symbolic XP weights...\n")

voters = {
    "user001": {"vote": "for", "xp": 12},
    "user042": {"vote": "against", "xp": 7},
    "user777": {"vote": "for", "xp": 15},
    "user999": {"vote": "for", "xp": 9}
}

for uid, v in voters.items():
    try:
        cast_vote(proposal, uid, v["vote"], v["xp"])
        print(f"✅ {uid} voted '{v['vote']}' with XP {v['xp']}")
    except Exception as e:
        print(f"❌ Vote failed for {uid}: {str(e)}")

print("\n—" * 40)

# === Step 3: Resolve Proposal Outcome ===
final_result = close_proposal(proposal)

# === Step 4: Print Final Results ===
print("📣 Final Proposal Outcome:")
print(json.dumps(final_result, indent=2))
