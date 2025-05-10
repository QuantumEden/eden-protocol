# /narrative/oracle_prompt_bank.py

# This file maps psychological models to symbolic therapeutic prompts.
# These will be used by the EdenQuest engine to render mythic quests
# appropriate for a user’s archetype, Tree of Life state, and narrative alignment.

oracle_prompt_bank = {
    "CBT": {
        "resilience": "Name the voice that always tells you to give up. Then prove it wrong.",
        "discipline": "Write down your daily failures without judgment. Choose one to fix today.",
        "mindfulness": "Observe your thoughts as clouds—not truths. Let them pass." 
    },
    "DBT": {
        "empathy": "You must speak with someone who hurt you, but you can only ask questions.",
        "expression": "You feel too much. Find the middle path: draw what silence feels like.",
        "physical_care": "Treat your body as if it belonged to someone you loved."
    },
    "Freudian": {
        "resilience": "Return to the place in memory you abandoned. There is something buried there.",
        "craft": "Build something without purpose. Then ask yourself why you built it.",
        "discipline": "You rebel against your superego. What would your inner judge say about this quest?"
    },
    "Jungian": {
        "expression": "Paint your shadow. Then explain what it wants.",
        "mindfulness": "Meditate on the archetype that frightens you most. You are becoming it.",
        "resilience": "Your ego clings to comfort. Descend into the underworld and retrieve your truth."
    },
    "Logotherapy": {
        "resilience": "What would you suffer for, if it gave someone else hope?",
        "discipline": "There is no meaning without struggle. Walk the long road without distraction.",
        "empathy": "Your pain is a signal. Find someone who needs what you’ve survived."
    }
}

# Optional accessor

def get_prompt(model, trait):
    return oracle_prompt_bank.get(model, {}).get(trait, "No prompt found.")

# Example usage (for testing)
if __name__ == "__main__":
    model = "Jungian"
    trait = "resilience"
    print(get_prompt(model, trait))
