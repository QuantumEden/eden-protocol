# Leveling System – XP, Merit, and Lock States

def initialize_merit_profile():
    return {
        "level": 1,
        "xp": 0,
        "xp_threshold": 100,
        "locked": False
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
