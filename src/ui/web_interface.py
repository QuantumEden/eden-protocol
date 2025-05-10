# /src/ui/web_interface.py

import streamlit as st
import json

# Load sample payload
with open("sim/sample_payload.json") as f:
    data = json.load(f)

# Title and header
st.set_page_config(page_title="Eden Protocol Viewer", layout="centered")
st.title("🌌 Eden Protocol Interface")

# Avatar Overview
st.header("🧬 Avatar Identity")
avatar = data["avatar"]
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"**MBTI Type:** {avatar['mbti']}")
    st.markdown(f"**Archetype:** {avatar['archetype']} ({avatar['element']})")
with col2:
    st.markdown(f"**Primary Aura:** {avatar['primary_aura']}")
    st.markdown(f"**Secondary Aura:** {avatar['secondary_aura']}")
st.markdown(f"**Glyphs:** {' | '.join(avatar['glyphs'])}")
st.markdown(f"**Eyes:** {avatar['eyes']}")

# Tree of Life Visualization
st.header("🌳 Tree of Life")
tree = data["tree_of_life"]
for trait, value in tree.items():
    if trait != "health_score":
        st.progress(value / 100, text=trait.title())
st.markdown(f"**Holistic Health Score:** {tree['health_score']:.2f}")

# MeritCoin Status
st.header("🎖️ Merit Progress")
merit = data["meritcoin"]
st.markdown(f"**Level:** {merit['level']}")
st.progress(merit["xp"] / merit["next_level"], text=f"XP: {merit['xp']} / {merit['next_level']}")
if merit["locked"]:
    st.error("⚠️ XP is currently locked due to misalignment.")
else:
    st.success("✅ XP growth is active.")

# Active Quest
st.header("🌀 Current Quest")
quest = data["edenquest"]
q = quest["quest"]
st.markdown(f"**Title:** {q['title']}")
st.markdown(f"**Theme:** {q['theme']}")
st.markdown(f"**Symbol:** {q['symbol']}")
st.markdown(f"**Target Trait:** {quest['target_branch']}")
st.markdown(f"**Objective:** {q['goal']}")

# DAO Proposal
st.header("📜 DAO Status")
dao = data["dao"]
st.markdown(f"**Proposal:** {dao['title']}")
col1, col2 = st.columns(2)
with col1:
    st.metric("Votes For", dao['votes_for'])
with col2:
    st.metric("Votes Against", dao['votes_against'])
st.info(f"Outcome: {dao['outcome'].capitalize()}")

# World Tree
st.header("🌍 World Tree Vitality")
world = data["world_tree"]
st.metric("Eden Vitality Index", f"{world['eden_vitality_index']}%")
st.markdown(f"**Status:** {world['status']}")
st.markdown(f"**Active Users:** {world['user_count']}")
