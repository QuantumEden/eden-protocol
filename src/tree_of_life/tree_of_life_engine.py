# Tree of Life Engine
# Tracks user behavior, growth, and decay across symbolic skill branches

from typing import Dict, Any
import datetime

# Step 1: Define symbolic branches and default tree state
def initialize_tree_of_life() -> Dict[str, Dict[str, Any]]:
    branches = [
        "discipline", "empathy", "resilience",
        "craft", "mindfulness", "physical_care", "expression"
    ]
    
    return {
        branch: {
            "score": 50,  # starts balanced
            "last_updated": datetime.datetime.now().isoformat()
        }
        for branch in branches
    }

# Step 2: Grow a specific branch (e.g., user completes quest or logs positive habit)
def grow_branch(tree: Dict[str, Dict[str, Any]], branch: str, amount: int = 5) -> None:
    if branch in tree:
        tree[branch]["score"] = min(100, tree[branch]["score"] + amount)
        tree[branch]["last_updated"] = datetime.datetime.now().isoformat()

# Step 3: Decay neglected branches (called during daily update)
def decay_tree(tree: Dict[str, Dict[str, Any]], decay_rate: int = 1) -> None:
    now = datetime.datetime.now()
    for branch, data in tree.items():
        last = datetime.datetime.fromisoformat(data["last_updated"])
        days_passed = (now - last).days
        if days_passed > 0:
            decay_amount = decay_rate * days_passed
            tree[branch]["score"] = max(0, tree[branch]["score"] - decay_amount)
            tree[branch]["last_updated"] = now.isoformat()

# Step 4: Get average score or health of the whole tree
def tree_health(tree: Dict[str, Dict[str, Any]]) -> float:
    scores = [data["score"] for data in tree.values()]
    return sum(scores) / len(scores)

# Optional Step 5: Print tree summary for reporting or visualization
def print_tree_summary(tree: Dict[str, Dict[str, Any]]) -> None:
    print("\n=== Tree of Life Summary ===")
    for branch, data in tree.items():
        print(f"{branch.capitalize()}: {data['score']}%")
    print(f"Overall Health: {tree_health(tree):.2f}%\n")

# Local test routine (can be triggered from simulation)
if __name__ == "__main__":
    tree = initialize_tree_of_life()
    grow_branch(tree, "discipline", 10)
    decay_tree(tree)
    print_tree_summary(tree)
