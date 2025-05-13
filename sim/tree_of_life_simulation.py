import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from tree_of_life.tree_of_life_engine import (
    initialize_tree_of_life,
    compute_health_score,
    apply_decay,
    grow_branch,
    apply_disclosure_adjustments
)

print("\n=== Tree of Life Simulation ===\n")

# Step 1: Initialize Tree
tree = initialize_tree_of_life()
print("Initial Tree:")
print(json.dumps(tree, indent=2))

# Step 2: Apply symbolic decay
decay_map = {
    "mindfulness": 10,
    "discipline": 5
}
tree = apply_decay(tree, decay_map)
print("\nAfter Decay:")
print(json.dumps(tree, indent=2))

# Step 3: Symbolic growth
tree = grow_branch(tree, "discipline", amount=15)
tree = grow_branch(tree, "expression", amount=10)
print("\nAfter Growth:")
print(json.dumps(tree, indent=2))

# Step 4: Disclosure event for trauma healing
disclosure_event = {
    "diagnosis": ["PTSD", "TBI"],
    "trauma_tags": ["combat", "insomnia"],
    "service_connected": True
}
tree = apply_disclosure_adjustments(tree, disclosure_event)
print("\nAfter Disclosure Adjustment:")
print(json.dumps(tree, indent=2))

# Step 5: Compute holistic health
health_score = compute_health_score(tree)
print(f"\nFinal Health Score: {health_score}")
