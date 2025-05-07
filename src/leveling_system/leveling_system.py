# MeritCoin Leveling System
# Manages XP, decay, thresholds, and status tied to behavioral integrity

from typing import Dict

# Step 1: Define XP thresholds per level (simplified linear scale for now)
XP_PER_LEVEL = 100
MAX_LEVEL = 60

# Step 2: Initialize player progression

def initialize_merit_profile() -> Dict[str, int]:
    return {
        "level": 1,
        "xp": 0,
        "decay_locked": False
    }

# Step 3: Gain XP and check for level up

def add_xp(profile: Dict[str, int], amount: int) -> None:
    if profile["decay_locked"]:
        return

    profile["xp"] += amount

    while profile["xp"] >= XP_PER_LEVEL and profile["level"] < MAX_LEVEL:
        profile["xp"] -= XP_PER_LEVEL
        profile["level"] += 1

# Step 4: Apply XP decay (e.g., inactivity, false behavior, community regression)

def apply_decay(profile: Dict[str, int], decay_amount: int) -> None:
    if profile["decay_locked"]:
        return

    profile["xp"] = max(0, profile["xp"] - decay_amount)

# Step 5: Lock XP when behavior contradicts protocol (dishonesty, relapse, etc.)

def lock_progress(profile: Dict[str, int]) -> None:
    profile["decay_locked"] = True

# Step 6: Unlock XP after redemptive behavior or quest completion

def unlock_progress(profile: Dict[str, int]) -> None:
    profile["decay_locked"] = False

# Step 7: Print current status

def print_merit_status(profile: Dict[str, int]) -> None:
    print("\n=== MeritCoin Profile ===")
    print(f"Level: {profile['level']}")
    print(f"XP: {profile['xp']} / {XP_PER_LEVEL}")
    print(f"Decay Locked: {profile['decay_locked']}")
    print("==========================\n")

# Local test (simulated)
if __name__ == "__main__":
    user = initialize_merit_profile()
    add_xp(user, 120)
    print_merit_status(user)
    apply_decay(user, 30)
    print_merit_status(user)
    lock_progress(user)
    add_xp(user, 100)
    print_merit_status(user)
    unlock_progress(user)
    add_xp(user, 100)
    print_merit_status(user)
