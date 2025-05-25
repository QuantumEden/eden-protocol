"""
Agent Shift Simulation – Eden Protocol Testing Suite

Simulates sequential interactions to verify Eidolon’s ability to dynamically
route user inputs to appropriate therapeutic agents based on symbolic tone and need.
"""

from src.ai.eidolon.core_orchestrator import process_user_input

def simulate_agent_shift():
    user_id = "test_shift_002"
    conversation = [
        "I can’t stop thinking about how I disappointed my parents.",
        "Sometimes I wonder if any of this has meaning.",
        "My thoughts spiral when I’m alone for too long.",
        "I’ve been journaling more, but it still feels pointless.",
        "I need help structuring my next steps forward."
    ]

    print(f"\n🧠 Agent Shift Test for {user_id}\n")
    for idx, msg in enumerate(conversation):
        response = process_user_input(
            user_id=user_id,
            message=msg,
            metadata={"test_index": idx}
        )
        print(f"User: {msg}")
        print(f"Eidolon: {response}\n")

if __name__ == "__main__":
    simulate_agent_shift()
