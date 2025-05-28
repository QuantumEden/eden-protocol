# sim/leveling_system_simulation.py
# MeritCoin Leveling Simulation
# Tests XP gain, decay, and lock mechanisms from leveling_system module

import sys, os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from leveling_system.leveling_system import (
    initialize_merit_profile,
    apply_xp as add_xp,  # ✅ Fixed import alias
    apply_decay,
    lock_progress,
    unlock_progress,
    print_merit_status
)

def divider(title="Step"):
    print(f"\n--- {title} @ {datetime.utcnow().isoformat()}Z ---")

print("\n🌱=== Running MeritCoin Leveling Simulation ===\n")

# Step 1: Initialize profile
divider("Initialization")
profile = initialize_merit_profile()
print_merit_status(profile)

# Step 2: Gain XP and level up
divider("Gaining 250 XP")
add_xp(profile, 250)
print_merit_status(profile)

# Step 3: Apply decay
divider("Applying 50 XP decay")
apply_decay(profile, 50)
print_merit_status(profile)

# Step 4: Lock progress (simulate dishonesty or relapse)
divider("Locking progress")
lock_progress(profile)

# Safe XP and decay attempts while locked
try:
    add_xp(profile, 100)
    apply_decay(profile, 30)
except Exception as e:
    print(f"⚠️ Action while locked failed: {e}")

print_merit_status(profile)

# Step 5: Unlock and resume
divider("Unlocking progress")
unlock_progress(profile)
add_xp(profile, 75)
print_merit_status(profile)

print("\n✅ MeritCoin Simulation Complete")
