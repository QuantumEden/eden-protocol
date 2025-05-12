import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Sample profile for visual terminal output
profile = {
    "mbti": "ENFP",
    "iq": 128,
    "eq": 135,
    "moral": "care",
    "sacred_path": "Zen Buddhism",
    "group_opt_in": True
}

user_id = "terminal_user"
secret_key = "test_key_visual"

payload = generate_eden_payload(user_id, profile, secret_key)

# === ASCII Viewer ===
print("\n🔍 EDEN PAYLOAD VISUALIZER\n")

print("🎭 AVATAR")
print(f"  Archetype: {payload['avatar']['archetype']}")
print(f"  Element:   {payload['avatar']['element']}")
print(f"  Glyph:     {payload['avatar']['glyph']}")
print(f"  Aura:      {payload['avatar']['aura_color']}")

print("\n🌳 TREE OF LIFE")
for trait, value in payload['tree_of_life'].items():
    print(f"  {trait.capitalize().replace('_', ' '):20}: {value}")

print("\n🪙 MERITCOIN")
print(f"  Level:     {payload['meritcoin']['level']}")
print(f"  XP:        {payload['meritcoin']['xp']} / {payload['meritcoin']['xp_threshold']}")
print(f"  Locked:    {'Yes' if payload['meritcoin']['locked'] else 'No'}")

print("\n📜 QUEST")
print(f"  Title:     {payload['edenquest']['title']}")
print(f"  Theme:     {payload['edenquest']['theme']}")
print(f"  Metaphor:  {payload['edenquest']['metaphor']}")
print(f"  Growth:    {payload['edenquest']['growth_target']}")

print("\n🗳 DAO")
print(f"  Proposal:  {payload['dao']['last_proposal']}")
print(f"  Status:    {payload['dao']['status']}")
print(f"  Vote Weight: {payload['dao'].get('vote_weight', 'N/A')}")

print("\n🌐 WORLD TREE")
print(f"  State:     {payload['world_tree']['symbolic_state']}")
print(f"  Health:    {(payload['world_tree']['eden_health'] * 100):.1f}%")
print(f"  Active Users: {payload['world_tree']['active_dao_users']}")

print("\n🕊 GROUP STATE")
group = payload['group_state']
print(f"  Ritual:    {group.get('ritual_instance', 'None')}")
print(f"  Status:    {group.get('status', 'Unavailable')}")
print(f"  Synergy:   {group.get('synergy_score', 0) * 100:.1f}%")

print("\n✅ PAYLOAD RENDER COMPLETE\n")
