# World Tree Simulation – Aggregates Trees of Life into Eden Status

from src.world_tree.world_tree_engine import generate_world_tree_report

print("\n=== Simulating World Tree Aggregation ===\n")

# Sample Trees of Life from diverse users
sample_user_trees = [
    {
        "discipline": {"score": 95},
        "empathy": {"score": 90},
        "resilience": {"score": 85},
        "craft": {"score": 80},
        "mindfulness": {"score": 90},
        "physical_care": {"score": 85},
        "expression": {"score": 92},
    },
    {
        "discipline": {"score": 70},
        "empathy": {"score": 65},
        "resilience": {"score": 75},
        "craft": {"score": 60},
        "mindfulness": {"score": 70},
        "physical_care": {"score": 68},
        "expression": {"score": 72},
    },
    {
        "discipline": {"score": 30},
        "empathy": {"score": 40},
        "resilience": {"score": 35},
        "craft": {"score": 25},
        "mindfulness": {"score": 38},
        "physical_care": {"score": 33},
        "expression": {"score": 30},
    }
]

# Run the engine
report = generate_world_tree_report(sample_user_trees)

# Output the symbolic state of Eden
print("=== World Tree Report ===")
for key, value in report.items():
    print(f"{key}: {value}")
