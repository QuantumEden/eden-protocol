# tests/load_balancer_route_test.py – Eidolon AI Load Test
# Simulates concurrent routing requests to test therapeutic agent stability

import sys, os
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Patch path to import Eidolon router
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ai.eidolon.agent_router import route_to_agent

# === Prompt Pool ===
PROMPT_POOL = [
    "I don’t know why I feel like this.",
    "My trauma still defines me.",
    "Why does life feel so meaningless?",
    "Sometimes I want to disappear.",
    "I’m having nightmares about the war.",
    "Do I need medication?",
    "Why do I push everyone away?",
    "I feel like I'm not real.",
    "Everything I do feels hollow.",
    "Tell me how to stop overthinking.",
    "I miss who I used to be.",
    "Can you diagnose me?",
    "What if my pain never goes away?"
]

# === Mock Personas ===
PERSONAS = [
    {"mbti": "INFJ"}, {"mbti": "ESTP"}, {"mbti": "INTJ"}, {"mbti": "ENFP"}
]

# === Test Function ===
def simulate_route(index: int):
    message = random.choice(PROMPT_POOL)
    persona = random.choice(PERSONAS)
    context = "Symbolic user session context for therapeutic evaluation."
    tone = random.choice(["calm", "gentle", "neutral", "direct", "reassuring"])

    try:
        response = route_to_agent(
            user_id=f"load_user_{index}",
            message=message,
            context=context,
            tone=tone,
            persona=persona
        )
        print(f"✅ User {index} routed to {response['agent']} → {response['response'][:60]}...")
    except Exception as e:
        print(f"❌ Error routing user {index}: {str(e)}")

# === Load Balancer Simulation ===
if __name__ == "__main__":
    print("\n🚦 Running Eidolon Load Balancer Route Test...\n")
    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(simulate_route, range(25))

    print(f"\n⏱️ Routing simulation completed in {time.time() - start:.2f} seconds.\n")
