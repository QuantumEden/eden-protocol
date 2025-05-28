"""
Avatar Identity Engine Simulation – Eden Protocol

Simulates the generation of avatars based on psychometric profiles
using the identity engine to validate symbolic consistency.
"""

import sys
import os
import json

# 🧠 Patch module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from avatar_identity_engine.identity_engine import generate_avatar

# 🧬 Sample user psychometric profiles
sample_profiles = [
    {
        "mbti": "ISTP",
        "iq": 132,
        "eq": 95,
        "moral": "loyalty"
    },
    {
        "mbti": "ENFP",
        "iq": 110,
        "eq": 125,
        "moral": "care"
    },
    {
        "mbti": "INTJ",
        "iq": 142,
        "eq": 108,
        "moral": "fairness"
    },
    {
        "mbti": "ISFJ",
        "iq": 100,
        "eq": 115,
        "moral": "authority"
    },
    {
        "mbti": "ENTP",
        "iq": 120,
        "eq": 100,
        "moral": "liberty"
    }
]

# 🔁 Run simulation
print("\n🎭 Avatar Identity Engine Simulation\n" + "—" * 50)
for i, profile in enumerate(sample_profiles):
    print(f"\n🧾 Profile {i+1} — {profile['mbti']}")
    avatar = generate_avatar(profile)
    print(json.dumps(avatar, indent=2))
