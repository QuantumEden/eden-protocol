# /src/tree_of_life/tree_of_life_engine.py

"""
Tree of Life Engine — Symbolic Trait System

Supports core trait growth, decay, and now mod-based behavioral inputs.
"""

class TreeOfLife:
    def __init__(self):
        self.traits = {
            "discipline": 50,
            "empathy": 50,
            "resilience": 50,
            "mindfulness": 50,
            "vitality": 50,
            "expression": 50
        }

    def apply_core_effect(self, trait: str, delta: int):
        if trait not in self.traits:
            raise ValueError("Invalid trait")
        self.traits[trait] += delta
        self.traits[trait] = max(0, min(100, self.traits[trait]))
        return self.traits[trait]

    def apply_mod_effect(self, trait: str, delta: int, mod_id: str, user_id: str):
        from src.xp.xp_integrity import validate_xp_from_mod

        if trait not in self.traits:
            raise ValueError("Invalid trait")

        # Validate symbolic XP change via mod approval
        if validate_xp_from_mod(user_id, mod_id, abs(delta)):
            self.traits[trait] += delta
            self.traits[trait] = max(0, min(100, self.traits[trait]))
            return self.traits[trait]

    def get_trait(self, trait: str):
        return self.traits.get(trait, None)


# Example use case
if __name__ == "__main__":
    tree = TreeOfLife()
    print("Original discipline:", tree.get_trait("discipline"))
    tree.apply_core_effect("discipline", 5)
    print("After core effect:", tree.get_trait("discipline"))
    tree.apply_mod_effect("discipline", 10, "tai_chi_001", "user123")
    print("After mod effect:", tree.get_trait("discipline"))
