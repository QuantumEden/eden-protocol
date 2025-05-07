# Tree of Life Simulation Script
# Simulates user behavioral growth and decay across symbolic branches

from src.tree_of_life.tree_of_life_engine import (
    initialize_tree_of_life,
    grow_branch,
    decay_tree,
    print_tree_summary
)
import time

print("\n=== Running Tree of Life Simulation ===\n")

# Step 1: Initialize user tree
user_tree = initialize_tree_of_life()
print("Initial State:")
print_tree_summary(user_tree)

# Step 2: Simulate growth from positive user behavior
print("Simulating user discipline and craft development...")
grow_branch(user_tree, "discipline", 10)
grow_branch(user_tree, "craft", 7)
print_tree_summary(user_tree)

# Step 3: Simulate time passing (simulate 3 days of neglect)
print("Simulating decay over 3 days...")
for _ in range(3):
    time.sleep(0.1)  # symbolic pause (not functional delay)
    decay_tree(user_tree)
print_tree_summary(user_tree)

# Step 4: Simulate balance and recovery
grow_branch(user_tree, "mindfulness", 8)
grow_branch(user_tree, "empathy", 5)
print("User engages in mindful and empathic behavior...")
print_tree_summary(user_tree)

print("\n=== Simulation Complete ===")
