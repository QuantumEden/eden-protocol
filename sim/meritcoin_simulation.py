# sim/meritcoin_simulation.py
# MeritCoin Simulation – XP, Leveling, Decay, Lock Cycle

from src.leveling_system.leveling_system import (
    initialize_merit_profile,
    apply_xp as add_xp,  # ✅ Fixed alias
    apply_decay,
    lock_progress,
    unlock_progress,
    print_merit_status
)

print("\n=== MeritCoin Simulation: Full Lifecycle ===\n")

# Step 1: Initialization
profile = initialize_merit_profile()
print("Initial Profile:")
print_merit_status(profile)

# Step 2: Earn XP from behavior
print("Adding 120 XP from verified behavior")
add_xp(profile, 120)
print_merit_status(profile)

# Step 3: Apply decay from regression
print("Applying 40 XP decay for inactivity")
apply_decay(profile, 40)
print_merit_status(profile)

# Step 4: Lock progress due to falsified report
print("Locking MeritCoin due to protocol violation")
lock_progress(profile)
add_xp(profile, 100)  # Should be blocked
apply_decay(profile, 50)  # Should not affect
print_merit_status(profile)

# Step 5: Unlock after successful redemptive quest
print("Unlocking MeritCoin after verification")
unlock_progress(profile)
add_xp(profile, 80)
print_merit_status(profile)

print("\n=== Simulation Complete ===")
