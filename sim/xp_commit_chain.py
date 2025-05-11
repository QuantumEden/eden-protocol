# /sim/xp_commit_chain.py

import hashlib
import json
from datetime import datetime

# 🔐 Simulated XP Events (normally confirmed via avatar + quest engine)
xp_log = [
    {"user_id": "user_001", "event": "Completed Daily Quest", "xp": 50, "timestamp": "2025-05-10T08:12:00"},
    {"user_id": "user_001", "event": "Tree Realignment", "xp": 100, "timestamp": "2025-05-11T09:30:00"},
    {"user_id": "user_002", "event": "Voted on DAO Proposal", "xp": 30, "timestamp": "2025-05-11T10:00:00"},
]

# 📦 XP Commit Chain
def generate_commit_chain(log):
    chain = []
    prev_hash = "0" * 64  # Genesis hash

    for entry in log:
        # Canonicalize entry
        entry_string = json.dumps(entry, sort_keys=True)
        combined = entry_string + prev_hash
        current_hash = hashlib.sha256(combined.encode()).hexdigest()

        block = {
            "entry": entry,
            "prev_hash": prev_hash,
            "commit_hash": current_hash
        }

        chain.append(block)
        prev_hash = current_hash

    return chain

# 🧪 Simulate Chain
commit_chain = generate_commit_chain(xp_log)

# 🖨️ Print Result
for i, block in enumerate(commit_chain):
    print(f"\n🔗 Block {i + 1}")
    print("🧠 Event:", block['entry']['event'])
    print("📅 Timestamp:", block['entry']['timestamp'])
    print("📊 XP Gained:", block['entry']['xp'])
    print("🔓 Previous Hash:", block['prev_hash'][:16], "...")
    print("🔐 Commit Hash :", block['commit_hash'][:16], "...")
