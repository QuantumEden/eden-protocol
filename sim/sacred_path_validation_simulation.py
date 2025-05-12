import json
from src.paths.sacred_path_engine import apply_sacred_path_effects

# Sample sacred profiles
test_profiles = [
    {"mbti": "INTJ", "sacred_path": "Alchemy"},
    {"mbti": "ISFJ", "sacred_path": "Judaism"},
    {"mbti": "ENFP", "sacred_path": "Zen Buddhism"},
    {"mbti": "INFJ", "sacred_path": "Christianity"},
    {"mbti": "ENTP", "sacred_path": "Undeclared"}
]

print("\n=== Sacred Path Application Simulation ===\n")

for profile in test_profiles:
    result = apply_sacred_path_effects(profile.copy())
    print(f"-- {profile['sacred_path']} --")
    print(json.dumps(result, indent=2))
    print()
