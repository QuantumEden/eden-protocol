# /src/ui/renderer.py

import json
import os

def render_avatar(avatar):
    print("\n🧬 AVATAR IDENTITY")
    print(f"MBTI Type       : {avatar['mbti']}")
    print(f"Archetype       : {avatar['archetype']} ({avatar['element']})")
    print(f"Primary Aura    : {avatar['primary_aura']}")
    print(f"Secondary Aura  : {avatar['secondary_aura']}")
    print(f"Glyphs          : {', '.join(avatar['glyphs'])}")
    print(f"Eyes            : {avatar['eyes']}")

def render_tree(tree):
    print("\n🌳 TREE OF LIFE")
    for trait, value in tree.items():
        if trait != "health_score":
            bar = "█" * (value // 10)
            print(f"{trait.title():<15}: {bar} {value}")
    print(f"\nHolistic Health Score: {tree['health_score']}")

def render_meritcoin(coin):
    print("\n🎖️ MERIT STATUS")
    print(f"Level           : {coin['level']}")
    print(f"XP              : {coin['xp']} / {coin['next_level']}")
    print(f"XP Locked?      : {'Yes' if coin['locked'] else 'No'}")

def render_quest(quest):
    print("\n🌀 ACTIVE QUEST")
    print(f"Title           : {quest['quest']['title']}")
    print(f"Theme           : {quest['quest']['theme']}")
    print(f"Symbol          : {quest['quest']['symbol']}")
    print(f"Target Trait    : {quest['target_branch']}")
    print(f"Objective       : {quest['quest']['goal']}")

def render_dao(dao):
    print("\n📜 DAO STATUS")
    print(f"Proposal        : {dao['title']}")
    print(f"Votes For       : {dao['votes_for']}")
    print(f"Votes Against   : {dao['votes_against']}")
    print(f"Outcome         : {dao['outcome']}")

def render_world_tree(world):
    print("\n🌍 WORLD TREE")
    print(f"Eden Vitality   : {world['eden_vitality_index']}%")
    print(f"Status          : {world['status']}")
    print(f"User Count      : {world['user_count']}")

def render(payload):
    os.system('cls' if os.name == 'nt' else 'clear')
    render_avatar(payload["avatar"])
    render_tree(payload["tree_of_life"])
    render_meritcoin(payload["meritcoin"])
    render_quest(payload["edenquest"])
    render_dao(payload["dao"])
    render_world_tree(payload["world_tree"])

if __name__ == "__main__":
    with open("sim/sample_payload.json") as f:
        data = json.load(f)
        render(data)
