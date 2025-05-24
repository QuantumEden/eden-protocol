"""
Dialogue Mapper – Eden Protocol Symbolic Experience Engine

Maps NPC archetypes to branching dialogue sequences.
Supports emotional resonance, quest progression, and soulform reflection.
"""

from typing import Dict, List

def get_dialogue_branch(npc_name: str, emotion_state: str) -> List[Dict[str, str]]:
    """
    Returns a symbolic dialogue path based on the NPC identity and user mood.
    """
    if npc_name == "The Mirror":
        if emotion_state == "shame":
            return [
                {"npc": "You look away, but I am still here."},
                {"npc": "What have you buried to survive this long?"},
                {"user": "I buried my belief that I deserved love."},
                {"npc": "Then unbury it. Name it. Let it breathe."}
            ]
        else:
            return [
                {"npc": "You still do not see your whole self, do you?"},
                {"npc": "That blindness will cost you unless you confront it."}
            ]

    if npc_name == "Aurelia":
        return [
            {"npc": "You carry pain as if it were your birthright."},
            {"npc": "What would happen if you laid it down for one day?"},
            {"user": "I don’t know who I’d be without it."},
            {"npc": "Then today is your chance to find out."}
        ]

    if npc_name == "The Shadowling":
        return [
            {"npc": "I whisper what you're too afraid to say aloud."},
            {"npc": "Do you even recognize who you're becoming?"},
            {"user": "I'm starting to."},
            {"npc": "Then let’s see how far you're willing to go."}
        ]

    return [{"npc": "..."}, {"npc": "This presence has no script... yet."}]

# Example
if __name__ == "__main__":
    branch = get_dialogue_branch("The Mirror", "shame")
    for line in branch:
        for speaker, text in line.items():
            print(f"{speaker.upper()}: {text}")
