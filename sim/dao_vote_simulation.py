# /sim/dao_vote_simulation.py

import hashlib
import json
from datetime import datetime

# 🔐 Simulated User Ledger (normally pulled from verified payload)
users = {
    "user_001": {"xp": 1200, "soulbound_id": "arch-strat-001"},
    "user_002": {"xp": 300, "soulbound_id": "guard-heal-002"},
    "user_003": {"xp": 700, "soulbound_id": "build-sage-003"},
}

# 📜 DAO Proposal (symbolic narrative)
proposal = {
    "title": "🌿 Construct Trauma Sanctuary in VR Zone Delta",
    "description": "Create a sacred space accessible to users with Tree Decay Score > 80 for guided Shadow Work rituals.",
    "proposer": "user_001",
    "timestamp": datetime.now().isoformat(),
    "threshold_xp": 500,
}

# 🗳️ XP-Weighted Voting Ledger
votes = {
    "user_001": "yes",
    "user_002": "no",
    "user_003": "yes",
}

# 🧠 Voting Engine
def compute_vote_weight(xp):
    return xp / 100  # XP:100 ratio

def tally_votes(users, votes):
    yes_weight = 0
    no_weight = 0

    for uid, decision in votes.items():
        if uid in users:
            weight = compute_vote_weight(users[uid]["xp"])
            if decision == "yes":
                yes_weight += weight
            elif decision == "no":
                no_weight += weight

    return yes_weight, no_weight

def is_passed(yes_weight, no_weight):
    return yes_weight > no_weight

# 🔐 ZK-style commit hash (simulated)
def hash_proposal(proposal):
    proposal_str = json.dumps(proposal, sort_keys=True).encode()
    return hashlib.sha256(proposal_str).hexdigest()

# 🧪 Run Simulation
yes, no = tally_votes(users, votes)
result = is_passed(yes, no)

print("🗳️ DAO Proposal:", proposal["title"])
print("🔐 Proposal Hash:", hash_proposal(proposal))
print("✅ Yes Weight:", yes)
print("❌ No Weight:", no)
print("📣 Result:", "PASSED ✅" if result else "REJECTED ❌")
