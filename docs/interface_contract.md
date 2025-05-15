# Eden Protocol – Interface Contract

This document defines the data input and output structure between the Eden Protocol backend and all user-facing interfaces (mobile, desktop, web, XR/VR clients, and DAO platforms).

---

## Input Structure

All inputs are passed to the `generate_eden_payload()` function via the `user_profile` dictionary.

### Example Input (JSON)

```
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
  },
  "current_soulform": {
    "id": "phoenix",
    "name": "Ashborn Phoenix",
    "elemental_affinity": "Fire",
    "activated_at": "2025-05-14T17:00:00Z"
  }
}
```

### Accepted Fields

- `mbti` (string): Myers-Briggs type (e.g. "INTJ")
- `iq` (integer): Intelligence score
- `eq` (integer): Emotional intelligence score
- `moral` (string): Dominant moral alignment
- `sacred_path` (string): Spiritual or philosophical archetype
- `group_opt_in` (boolean): Symbolic group flag
- `disclosure` (object): Diagnostic and trauma metadata
- `current_soulform` (object, optional): Active transformation record

---

## Output Structure

The output is a payload used to generate EdenQuest environments and symbolic avatar updates.

### Example Output (JSON)

```
{
  "archetype": "Strategist",
  "conviction_glyph": "yin_yang",
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
  },
  "soulform_visuals": {
    "id": "phoenix",
    "name": "Ashborn Phoenix",
    "elemental_affinity": "Fire",
    "aura_effect": "Flare Pulse",
    "body_shader": "Iridescent Ash",
    "animation_override": "Ascend_SlowLoop"
  }
}
```

### Output Fields

- `archetype`: Avatar identity from MBTI
- `conviction_glyph`: Symbol of moral alignment
- `tree_traits`: Six-dimension behavioral health index (0–100 scale)
- `xp_awarded`: Experience granted on this sync
- `quest_unlocked`: Flag if a new EdenQuest was generated
- `disclosure_adjustment`: Trait modifiers granted from voluntary truth
- `soulform_visuals`: Cosmetic and symbolic rendering overlays for transformed state

---

## Interface Guidelines

UI clients (mobile, web, XR) must render:

- Tree visuals from `tree_traits`
- XP animations from `xp_awarded`
- Quests and timers if `quest_unlocked` is true
- Auras and conviction glyphs based on `conviction_glyph`
- Avatar overlays from `soulform_visuals` where present

Disclosure data must never be shared externally or stored in plain text. All trait boosts are symbolic, not diagnostic. This contract is versioned and updated only with schema lock + simulation validation.
