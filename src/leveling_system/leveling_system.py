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

# ✅ NEW FUNCTION: Apply XP and handle leveling logic
def apply_xp(profile, base_xp):
    """
    Applies XP to profile and handles leveling, merit boost, and soulform multipliers.
    """
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
