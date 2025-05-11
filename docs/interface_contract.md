# 🧩 Eden Protocol – Interface Contract

> This document defines the data input and output structure between the Eden Protocol backend and all user-facing interfaces (mobile, desktop, web, XR/VR clients, and DAO platforms).

---

## 🔽 INPUT STRUCTURE
All inputs are passed to the `generate_eden_payload()` function via the `user_profile` dictionary.

### 📜 Example Input (JSON)
```json
{
  "mbti": "INTJ",
  "iq": 140,
  "eq": 120,
  "moral": "care"
}
```

### 🔍 Accepted Fields
| Field | Type     | Description                                                  |
|-------|----------|--------------------------------------------------------------|
| `mbti` | string   | 16-type Myers-Briggs personality code                      |
| `iq`   | integer  | Abstract intelligence score (e.g., Raven’s Matrices)        |
| `eq`   | integer  | Emotional intelligence quotient (e.g., MSCEIT)              |
| `moral`| string   | User’s dominant moral foundation (e.g., care, liberty, etc.)|

✅ Optional Schema: `/schemas/user_profile.schema.json`

---

## 🔼 OUTPUT STRUCTURE

**Function Endpoint:**  `generate_eden_payload(user_id, profile_dict, secret_key)`

### 📦 Returns a bundled payload as:
```json
{
  "avatar": {...},
  "token": "...",
  "tree_of_life": {...},
  "meritcoin": {...},
  "edenquest": {...},
  "dao": {...},
  "world_tree": {...}
}
```

### 📂 Output Components & Schemas

#### 1. 🎭 `avatar` → `/schemas/avatar.schema.json`
- MBTI type
- EdenQuest archetype (Builder, Guardian, Healer, Strategist)
- Elemental affinity (Air, Earth, Fire, Water)
- Aura and glyph data

#### 2. 🔐 `token`
- Encrypted identity string from Secure Enclave (placeholder in simulation)

#### 3. 🌿 `tree_of_life` → `/schemas/tree_of_life.schema.json`
- Trait values (0–100 scale)
- Holistic health index

#### 4. 🪙 `meritcoin` → `/schemas/xp_meritcoin.schema.json`
- Current XP level
- XP earned and next-level threshold
- Lock status (true/false)

#### 5. 🧠 `edenquest` → `/schemas/edenquest.schema.json`
- AI-assigned symbolic quest
- Includes title, theme, metaphor, growth target

#### 6. 🗳️ `dao` → `/schemas/dao.schema.json`
- Last proposal metadata
- Vote tally and outcome status

#### 7. 🌐 `world_tree` → `/schemas/world_tree.schema.json`
- Global Eden health index
- DAO user count
- Symbolic world system state

---

## 🧭 INTERFACE DESIGN NOTES
- Each output can be rendered independently or displayed as part of a full dashboard
- Visual feedback loops can represent real-time symbolic shifts (e.g., tree growth, aura flicker)
- Zero-Knowledge Token integration will allow XP and world state verification without exposing raw user data
