# /sim/final_demo_simulation.py

import json
from src.ui.renderer import render
from narrative.voice_module import speak
from narrative.oracle_prompt_bank import get_prompt

# Load sample payload
with open("sim/sample_payload.json") as f:
    payload = json.load(f)

# Render symbolic CLI output
render(payload)

# Fetch prompt for active quest
model = payload["edenquest"]["quest"].get("model", "Jungian")
trait = payload["edenquest"].get("target_branch", "resilience")
prompt = get_prompt(model, trait)

# Narrate prompt (simulate or voice)
print("\n🧠 THERAPEUTIC PROMPT:")
speak(prompt, voice_id="creator", simulate=True)  # simulate=False if ElevenLabs is enabled
