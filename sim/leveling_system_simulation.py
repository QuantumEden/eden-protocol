# sim/leveling_system_simulation.py
# MeritCoin Leveling Simulation
# Tests XP gain, decay, and lock mechanisms from leveling_system module

from src.leveling_system.leveling_system import (
    initialize_merit_profile,
    apply_xp as add_xp,  # ✅ Fixed import alias
    apply_decay,
    lock_progress,
    unlock_progress,
    print_merit_status
)

print("\n=== Running MeritCoin Leveling Simulation ===\n")

# Step 1: Initialize profile
profile = initialize_merit_profile()
print("Initial State:")
print_merit_status(profile)

# Step 2: Gain XP and level up
print("Gaining 250 XP...")
add_xp(profile, 250)
print_merit_status(profile)

# Step 3: Apply decay
print("Applying 50 XP decay...")
apply_decay(profile, 50)
print_merit_status(profile)

# Step 4: Lock progress (due to dishonesty or relapse)
print("Locking progress...")
lock_progress(profile)
add_xp(profile, 100)  # Should have no effect
apply_decay(profile, 30)  # Should have no effect
print_merit_status(profile)

# Step 5: Unlock and resume
print("Unlocking progress...")
unlock_progress(profile)
add_xp(profile, 75)
print_merit_status(profile)

print("\n=== Simulation Complete ===")
