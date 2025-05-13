# 🧩 Eden Protocol – Interface Contract

This document defines the data input and output structure between the Eden Protocol backend and all user-facing interfaces (mobile, desktop, web, XR/VR clients, and DAO platforms).

---

## 🔽 INPUT STRUCTURE

All inputs are passed to the `generate_eden_payload()` function via the `user_profile` dictionary.

### 📜 Example Input (JSON)

```json
{
  "mbti": "INTJ",
  "iq": 140,
  "eq": 120,
  "moral": "care",
  "sacred_path": "Hermeticism",
  "group_opt_in": true,
  "disclosure": {
    "diagnosis": ["PTSD"],
    "trauma_tags": ["combat", "insomnia"],
    "service_connected": true
  }
}
```

### ✅ Accepted Fields

- `mbti` (string): Myers-Briggs type (e.g. `"INTJ"`)
- `iq` (integer): Intelligence score
- `eq` (integer): Emotional intelligence score
- `moral` (string): Dominant moral alignment (e.g. `"care"`, `"justice"`, `"loyalty"`)
- `sacred_path` (string): Spiritual or philosophical archetype
- `group_opt_in` (boolean): Whether the user joins a symbolic guild or operates solo
- `disclosure` (object): Voluntary trauma and diagnostic information

#### 🔐 Disclosure Subfields

- `diagnosis` (string[]): List of medical or psychological diagnoses
- `trauma_tags` (string[]): Keywords describing trauma (e.g. `"combat"`, `"loss"`)
- `service_connected` (boolean): Whether trauma is tied to military or public service

---

## 📤 OUTPUT STRUCTURE

The output is a payload object used to generate EdenQuest environments and symbolic state updates.

### 📜 Example Output (JSON)

```json
{
  "archetype": "Strategist",
  "conviction_glyph": "☯",
  "tree_traits": {
    "discipline": 88,
    "resilience": 91,
    "mindfulness": 72,
    "expression": 67,
    "physical_care": 60,
    "emotional_regulation": 75
  },
  "xp_awarded": 100,
  "quest_unlocked": true,
  "disclosure_adjustment": {
    "resilience": 12,
    "emotional_regulation": 9
  }
}
```

### ✅ Output Field Descriptions

- `archetype` (string): Assigned symbolic class based on MBTI
- `conviction_glyph` (string): Unicode glyph representing moral alignment
- `tree_traits` (object): Map of internal growth attributes (0–100 scale)
- `xp_awarded` (integer): Experience points granted after sync
- `quest_unlocked` (boolean): Indicates if a quest was generated
- `disclosure_adjustment` (object): Healing boost applied due to honesty

---

## 🧠 Interpretation

Eden Protocol interfaces (apps, VR clients, web dashboards) should render the output visually using:

- Tree growth animations based on `tree_traits`
- Symbolic auras or glyphs via `conviction_glyph`
- Quests or feedback loops initiated via `quest_unlocked`
- XP visualizations using `xp_awarded`

Interfaces must **never expose disclosure content** to other users or store it externally without explicit consent. Trait bonuses from `disclosure_adjustment` are symbolic reinforcements, not diagnostics.

This contract is versioned alongside the schema and is updated only after full system integration tests.
