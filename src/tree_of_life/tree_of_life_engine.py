# Tree of Life Engine – Growth, Decay, Realignment Logic

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
    values = list(tree.values())
    return sum(values) // len(values)

def apply_decay(tree, decay_map):
    for trait, penalty in decay_map.items():
        if trait in tree:
            tree[trait] = max(tree[trait] - penalty, 0)
    return tree

def grow_branch(tree, branch, amount=5):
    """
    Symbolically increases the strength of a single trait branch.
    """
    if branch in tree:
        tree[branch] = min(tree[branch] + amount, 100)
    return tree

def apply_disclosure_adjustments(tree, disclosure_block):
    """
    Modulates Tree of Life based on voluntary disclosure of trauma or medical history.
    """
    diagnosis = disclosure_block.get("diagnosis", [])
    tags = disclosure_block.get("trauma_tags", [])
    service_connected = disclosure_block.get("service_connected", False)

    if "PTSD" in diagnosis:
        tree["resilience"] = max(tree["resilience"] - 10, 0)
        tree["emotional_regulation"] = max(tree["emotional_regulation"] - 5, 0)

    if "TBI" in diagnosis:
        tree["mindfulness"] = max(tree["mindfulness"] - 5, 0)

    if "insomnia" in tags:
        tree["physical_care"] = max(tree["physical_care"] - 5, 0)

    if "sexual_assault" in tags:
        tree["expression"] = max(tree["expression"] - 5, 0)

    if service_connected:
        tree["discipline"] = min(tree["discipline"] + 10, 100)
        tree["resilience"] = min(tree["resilience"] + 10, 100)

    return tree
