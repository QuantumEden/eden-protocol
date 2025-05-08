# Governance Simulation – DAO Proposal and Voting Test

from src.dao.governance_engine import (
    create_proposal,
    cast_vote,
    close_proposal
)

print("\n=== Governance Simulation: DAO Voting Test ===\n")

# Step 1: Create a proposal
proposal = create_proposal(
    title="Launch World Tree Visualization",
    description="Enable public symbolic dashboard for collective health tracking.",
    proposer_id="user001"
)

# Step 2: Simulate votes
print("Casting votes with weighted XP levels...\n")
cast_vote(proposal, "user001", "for", 12)
cast_vote(proposal, "user042", "against", 7)
cast_vote(proposal, "user777", "for", 15)
cast_vote(proposal, "user999", "for", 9)

# Step 3: Close and resolve the proposal
final_result = close_proposal(proposal)

# Step 4: Display outcome
print("=== Final Proposal Outcome ===")
for k, v in final_result.items():
    print(f"{k}: {v}")
