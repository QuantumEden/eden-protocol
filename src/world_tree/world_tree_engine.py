# src/world_tree/world_tree_engine.py – Global Eden Vitality Report Engine
# Aggregates individual Trees of Life into a collective Eden Vitality Index

from typing import List, Dict, Any

# Step 1: Normalize individual user tree scores into health metrics
def compute_tree_health(tree: Dict[str, Dict[str, int]]) -> float:
    scores = [branch["score"] for branch in tree.values()]
    return sum(scores) / len(scores) if scores else 0.0

# Step 2: Aggregate all user trees to form a global vitality index
def compute_global_health(all_trees: List[Dict[str, Dict[str, int]]]) -> float:
    if not all_trees:
        return 0.0

    total_health = sum(compute_tree_health(tree) for tree in all_trees)
    return round(total_health / len(all_trees), 2)

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
def generate_world_tree_report(all_trees: List[Dict[str, Dict[str, int]]]) -> Dict[str, Any]:
    vitality = compute_global_health(all_trees)
    status = classify_eden_status(vitality)

    return {
        "eden_vitality_index": vitality,
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
            "expression": {"score": 78}
        },
        {
            "discipline": {"score": 60},
            "empathy": {"score": 50},
            "resilience": {"score": 45},
            "craft": {"score": 55},
            "mindfulness": {"score": 60},
            "physical_care": {"score": 40},
            "expression": {"score": 50}
        }
    ]

    report = generate_world_tree_report(sample_trees)
    print("\n=== 🌍 World Tree Vitality Report ===")
    for key, value in report.items():
        print(f"{key}: {value}")
