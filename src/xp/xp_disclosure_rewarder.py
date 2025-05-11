# 🎖️ XP Disclosure Rewarder – Symbolic XP for Trauma Transparency

def calculate_disclosure_xp(disclosure: dict) -> int:
    """
    Calculates XP based on disclosure payload contents.
    XP rewards are symbolic, not diagnostic, and tuned to incentivize transparency.
    """
    xp = 25  # Base bonus for any submission

    # Diagnosis weights
    diagnosis = disclosure.get("diagnosis", [])
    if "PTSD" in diagnosis:
        xp += 50
    if "TBI" in diagnosis:
        xp += 30
    if "depression" in diagnosis:
        xp += 25
    if "anxiety" in diagnosis:
        xp += 20

    # Trauma tags
    tags = disclosure.get("trauma_tags", [])
    weighted_tags = {
        "combat": 20,
        "sexual_assault": 40,
        "moral_injury": 25,
        "insomnia": 15,
        "childhood_abuse": 35,
        "substance_dependency": 30,
        "betrayal": 15,
        "homelessness": 20
    }

    for tag in tags:
        xp += weighted_tags.get(tag, 0)

    # Service-connected multiplier
    if disclosure.get("service_connected", False):
        xp += 30

    # Cap XP per submission
    return min(xp, 150)
