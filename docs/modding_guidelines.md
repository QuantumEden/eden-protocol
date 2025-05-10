# 🧘 Modding Guidelines for the Eden Protocol

Welcome, Mod Architects. This document outlines the principles, structure, and expectations for contributing symbolic content to the Eden Protocol.

---

## 🌀 What is a Mod?
A "mod" in Eden is a symbolic module — a self-contained quest, ritual, or behavioral challenge designed to:
- Advance a user’s **Tree of Life** trait
- Award a specific amount of XP (max 100 per instance)
- Be verified through a **truth gate** (e.g., biometric data, journaling, ritual completion)

---

## 🧱 Required Structure
All mods must include:

- `mod_manifest.json` using the provided [schema](../../schemas/mod_manifest.schema.json)
- An identifiable **glyph** (e.g. 🜂 for Fire, 🜄 for Water)
- A `target_trait`: one of:
  - `discipline`, `empathy`, `resilience`, `mindfulness`, `vitality`, `expression`
- A symbolic description or script for the user to follow
- Optional: audio, video, overlays, or sensor data to enhance the experience

---

## 🛡️ Modding Rules
- ❌ Do **not** gamify trauma or trivialize suffering
- ✅ Align with Eden’s core symbolic values: **healing, truth, individuation**
- ❌ No direct monetary incentives, performance tracking, or competitive pressure
- ✅ Use metaphors, narrative, and intention to guide inner transformation
- ✅ Be mindful of accessibility and cultural origins

---

## 🔐 Truth Gates (Verification Types)
Choose one truth gate per mod:

- `biometric`: must pass via smart device (e.g., movement, HRV, sleep tracker)
- `journal`: user must submit symbolic written reflection
- `ritual`: completion of a self-guided, timed, or spatial ritual
- `voice`: user recites affirmation, prayer, or guided myth
- `self-report`: user clicks complete with honor-based trust (lowest XP tier)

---

## 🗳️ DAO Submission
To submit a mod:
1. Fork the Eden Protocol GitHub repo
2. Add your mod folder to `/community_mods/{your_mod_id}/`
3. Include `mod_manifest.json` and all relevant assets
4. Submit a pull request with the title: `[MOD PROPOSAL] {your_mod_id}`
5. DAO members will vote based on:
   - Symbolic value
   - Balance
   - Trait harmony
   - XP consistency

---

## 🌱 What Happens After Approval?
- Your mod becomes part of Eden’s ecosystem
- Trait gains affect real players
- XP is granted upon verified completion
- World Tree reflects your contribution
- Your mod ID and name are forever etched into `/dao/mod_registry.py`

---

> “We shape Eden not as engineers, but as gardeners of the soul.”
