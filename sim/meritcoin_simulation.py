# sim/meritcoin_simulation.py
# MeritCoin Simulation – XP, Leveling, Decay, Lock Cycle

import sys, os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from leveling_system.leveling_system import (
    initialize_merit_profile,
    apply_xp as add_xp,
    apply_decay,
    lock_progress,
    unlock_progress,
    print_merit_status
)

def timestamp():
    return datetime.utcnow().isoformat() + "Z"

print("\n=== MeritCoin Simulation: Full Lifecycle ===\n")

# Step 1: Initialization
profile = initialize_merit_profile()
profile["log"] = []
profile["log"].append({"event": "initialize", "timestamp": timestamp()})
print("Initial Profile:")
print_merit_status(profile)

# Step 2: Earn XP from behavior
print("\nAdding 120 XP from verified behavior...")
add_xp(profile, 120)
profile["log"].append({"event": "xp_gain", "amount": 120, "timestamp": timestamp()})
print_merit_status(profile)

# Step 3: Apply decay from regression
print("\nApplying 40 XP decay for inactivity...")
apply_decay(profile, 40)
profile["log"].append({"event": "xp_decay", "amount": 40, "timestamp": timestamp()})
print_merit_status(profile)

# Step 4: Lock progress due to falsified report
print("\nLocking MeritCoin due to protocol violation...")
lock_progress(profile)
profile["log"].append({"event": "locked", "reason": "protocol_violation", "timestamp": timestamp()})
add_xp(profile, 100)  # Should be blocked
apply_decay(profile, 50)  # Should not affect
print_merit_status(profile)

# Step 5: Unlock after successful redemptive quest
print("\nUnlocking MeritCoin after verification...")
unlock_progress(profile)
profile["log"].append({"event": "unlocked", "reason": "verification_success", "timestamp": timestamp()})
add_xp(profile, 80)
profile["log"].append({"event": "xp_gain", "amount": 80, "timestamp": timestamp()})
print_merit_status(profile)

print("\n🧾 Full Merit Profile Log:")
for entry in profile["log"]:
    print(entry)

print("\n=== Simulation Complete ===")
