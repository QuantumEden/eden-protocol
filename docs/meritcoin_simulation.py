# meritcoin_simulation.py

"""
MeritCoin Simulation Logic

This file simulates the behavior of a non-tradable, reputation-based MeritCoin system
intended for integration with the Eden Protocol blockchain.

Each user has a merit score that:
- Increases through verified contributions
- Decays over time unless re-earned
- Is stored and auditable

This simulation does not require a blockchain. It proves the internal logic.
"""

import time
from datetime import datetime, timedelta

# ------------------------------
# User Class Definition
# ------------------------------

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.merit = 0.0
        self.history = []  # List of (timestamp, action, merit_change)
        self.last_updated = datetime.utcnow()

    def contribute(self, action_description: str, value: float):
        self.merit += value
        timestamp = datetime.utcnow()
        self.history.append((timestamp, action_description, f"+{value}"))
        self.last_updated = timestamp

    def decay(self, decay_rate_per_day: float = 0.5):
        now = datetime.utcnow()
        days_passed = (now - self.last_updated).days
        decay_amount = decay_rate_per_day * days_passed
        if decay_amount > 0:
            self.merit = max(0.0, self.merit - decay_amount)
            self.history.append((now, "decay", f"-{decay_amount}"))
            self.last_updated = now

    def audit_log(self):
        print(f"Merit history for User {self.user_id}:")
        for entry in self.history:
            print(f"{entry[0].isoformat()} | {entry[1]} | {entry[2]}")
        print(f"Current merit: {self.merit}\n")


# ------------------------------
# Simulation Logic
# ------------------------------

def simulate_meritcoin():
    alice = User("alice42")
    bob = User("bob77")

    # Simulated contributions
    alice.contribute("Submitted cybersecurity patch", 10)
    bob.contribute("Verified veteran identity and community hours", 8)

    # Wait to simulate time passing (normally you'd mock or patch datetime)
    print("Simulating 3 days later...")
    alice.last_updated -= timedelta(days=3)
    bob.last_updated -= timedelta(days=3)

    # Apply decay
    alice.decay()
    bob.decay()

    # Audit logs
    alice.audit_log()
    bob.audit_log()


if __name__ == "__main__":
    simulate_meritcoin()
