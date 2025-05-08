# World Tree Engine
# Aggregates individual Trees of Life into a collective Eden Vitality Index

from typing import List, Dict

# Step 1: Normalize individual user tree scores into health metrics
def compute_tree_health(tree: Dict[str, Dict[str, int]]) -> float:
    scores = [data['score'] for data in tree.values()]
    return sum(scores) / len(scores)

# Step 2: Aggregate all user trees to form a global vitality index
def compute_global_health(all_trees: List[Dict[str, Dict[str, int]]]) -> float:
    if not all_trees:
        return 0.0

    total = 0
    for tree in all_trees:
        total += compute_tree_health(tree)

    return round(total / len(all_trees), 2)

# Step 3: Classify Eden status by symbolic thresholds
def classify_eden_status(global_health: float) -> str:
    if global_health >= 90:
        return "Radiant (Eden Flourishes)"
    elif global_health >= 70:
        return "Stable (Eden is Sustained)"
    elif global_health >= 50:
        return "Wilting (Eden Weakens)"
    elif global_health >= 30:
        return "Fading (Eden in Peril)"
    else:
        return "Dying (Eden in Collapse)"

# Step 4: Render symbolic state object
def generate_world_tree_report(all_trees: List[Dict[str, Dict[str, int]]]) -> Dict[str, any]:
    health = compute_global_health(all_trees)
    status = classify_eden_status(health)

    return {
        "eden_vitality_index": health,
        "status": status,
        "user_count": len(all_trees)
    }

# Optional local test
if __name__ == "__main__":
    sample_trees = [
        {
            "discipline": {"score": 80},
            "empathy": {"score": 70},
            "resilience": {"score": 75},
            "craft": {"score": 65},
            "mindfulness": {"score": 90},
            "physical_care": {"score": 85},
            "expression": {"score": 78},
        },
        {
            "discipline": {"score": 60},
            "empathy": {"score": 50},
            "resilience": {"score": 45},
            "craft": {"score": 55},
            "mindfulness": {"score": 60},
            "physical_care": {"score": 40},
            "expression": {"score": 50},
        }
    ]

    report = generate_world_tree_report(sample_trees)
    print("\n=== World Tree Report ===")
    for k, v in report.items():
        print(f"{k}: {v}")
