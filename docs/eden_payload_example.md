# 📦 Eden Payload Example

> This document showcases a fully formed output from the Eden Protocol backend using `generate_eden_payload()`. It includes all relevant symbolic systems from Phase XII: avatar, aura, sacred path, quest logic, DAO integration, and group state.

---

## 🔽 Input Profile
```json
{
  "mbti": "INFJ",
  "iq": 135,
  "eq": 122,
  "moral": "care",
  "sacred_path": "Zen Buddhism",
  "group_opt_in": true
}
```

---

## 🔼 Output Payload
```json
{
  "avatar": {
    "mbti": "INFJ",
    "archetype": "Healer",
    "element": "Water",
    "aura_color": "#6DDCCF",
    "glyph": "🜄",
    "sacred_path": "Zen Buddhism"
  },
  "token": "1a2b3c...zk_signature_hash...",
  "tree_of_life": {
    "discipline": 55,
    "resilience": 62,
    "mindfulness": 80,
    "expression": 74,
    "physical_care": 60,
    "emotional_regulation": 83,
    "health_index": 69
  },
  "meritcoin": {
    "level": 3,
    "xp": 275,
    "xp_threshold": 400,
    "locked": false
  },
  "edenquest": {
    "title": "Return to the Silent Garden",
    "theme": "Stillness before action",
    "metaphor": "Emptying the cup to find clarity",
    "growth_target": "Mindfulness"
  },
  "dao": {
    "last_proposal": "Ritual Access Classifications v2",
    "vote_weight": 2,
    "status": "eligible"
  },
  "world_tree": {
    "eden_health": 0.782,
    "active_dao_users": 431,
    "symbolic_state": "Blossoming"
  },
  "group_state": {
    "status": "linked",
    "synergy_score": 0.88,
    "ritual_instance": "echo_cathedral_072"
  }
}
```

---

## 🧬 Notes

- `avatar.glyph` and `aura_color` are symbolic and sacred-path adjusted.
- `tree_of_life.health_index` reflects a composite of 6 trait branches.
- `edenquest` is AI-generated, symbolic, and therapeutically aligned.
- `group_state` only appears if `group_opt_in` was set to true.
- `token` is a ZK placeholder representing secure enclave identity.

---

> Every payload is a mirror. It is not proof of perfection — it is proof of intention.
