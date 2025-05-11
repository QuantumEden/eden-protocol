# Tree of Life Engine – Avatar Trait Mapping & Health Calculation

def initialize_tree_of_life():
    return {
        "discipline": 50,
        "resilience": 50,
        "mindfulness": 50,
        "expression": 50,
        "physical_care": 50,
        "emotional_regulation": 50
    }

def compute_health_score(tree):
    scores = list(tree.values())
    return sum(scores) // len(scores)

# ✅ NEW FUNCTION: Applies symbolic trait adjustments based on disclosures
def apply_disclosure_adjustments(tree, disclosure_block):
    """
    Modulates Tree of Life based on voluntary disclosure of trauma or medical history.
    """
    diagnosis = disclosure_block.get("diagnosis", [])
    tags = disclosure_block.get("trauma_tags", [])
    service_connected = disclosure_block.get("service_connected", False)

    # Example logic: boost or weaken based on traits
    if "PTSD" in diagnosis:
        tree["resilience"] = max(tree["resilience"] - 10, 0)
        tree["emotional_regulation"] = max(tree["emotional_regulation"] - 5, 0)

    if "TBI" in diagnosis:
        tree["mindfulness"] = max(tree["mindfulness"] - 5, 0)

    if "insomnia" in tags:
        tree["physical_care"] = max(tree["physical_care"] - 5, 0)

    if "sexual_assault" in tags:
        tree["expression"] = max(tree["expression"] - 5, 0)

    # Symbolic healing bonus for service-connected users
    if service_connected:
        tree["discipline"] = min(tree["discipline"] + 10, 100)
        tree["resilience"] = min(tree["resilience"] + 10, 100)

    return tree

# 🔁 Optionally, you may add more tag mappings over time
