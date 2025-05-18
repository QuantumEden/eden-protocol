# src/leveling_system/leveling_system.py
# Leveling System – XP, Merit, and Lock States

def initialize_merit_profile():
    return {
        "level": 1,
        "xp": 0,
        "xp_threshold": 100,
        "locked": False,
        "meritcoin_score": 0.0,
        "soulform_xp_multiplier": 1.0  # Default neutral multiplier
    }

# ✅ NEW FUNCTION: XP bonus for truthful disclosure
def calculate_disclosure_xp(disclosure_block):
    """
    Calculates XP reward for voluntary trauma/medical disclosure.
    Prevents abuse by scaling rewards based on rarity and depth.
    """
    xp = 25  # Base reward for any disclosure

    diagnosis = disclosure_block.get("diagnosis", [])
    tags = disclosure_block.get("trauma_tags", [])
    service_connected = disclosure_block.get("service_connected", False)

    # Weighted multipliers
    if "PTSD" in diagnosis:
        xp += 50
    if "TBI" in diagnosis:
        xp += 30
    if "depression" in diagnosis:
        xp += 25

    if "combat" in tags:
        xp += 20
    if "sexual_assault" in tags:
        xp += 40
    if "insomnia" in tags:
        xp += 15

    if service_connected:
        xp += 30

    # Cap max XP from single upload
    return min(xp, 150)

# ✅ APPLY XP WITH SCALING
def apply_xp(profile, base_xp):
    """
    Applies XP to profile and handles leveling, merit boost, and soulform multipliers.
    """
    if profile.get("locked"):
        return profile  # Progress blocked

    multiplier = profile.get("soulform_xp_multiplier", 1.0)
    earned_xp = int(base_xp * multiplier)
    profile["xp"] += earned_xp

    while profile["xp"] >= profile["xp_threshold"]:
        profile["xp"] -= profile["xp_threshold"]
        profile["level"] += 1
        profile["xp_threshold"] = int(profile["xp_threshold"] * 1.25)  # Scaling curve

    # Optional: boost meritcoin score
    if "meritcoin_score" in profile:
        profile["meritcoin_score"] += earned_xp * 0.05  # Conversion rate: XP to Merit

    return profile

# ✅ DECAY LOGIC
def apply_decay(profile, amount):
    """
    Symbolic XP decay due to regression, dishonesty, or inaction.
    Will not drop below zero XP.
    """
    if profile.get("locked"):
        return profile

    profile["xp"] = max(0, profile["xp"] - amount)
    return profile

# ✅ LOCK MECHANISM
def lock_progress(profile):
    profile["locked"] = True

# ✅ UNLOCK MECHANISM
def unlock_progress(profile):
    profile["locked"] = False

# ✅ OUTPUT UTILITY
def print_merit_status(profile):
    print(f"Level: {profile['level']}")
    print(f"XP: {profile['xp']} / {profile['xp_threshold']}")
    print(f"Locked: {profile['locked']}")
    print(f"MeritCoin Score: {round(profile['meritcoin_score'], 2)}")
    print(f"Soulform Multiplier: x{profile.get('soulform_xp_multiplier', 1.0)}")
