# 🛡️ DAO Mod Audit Guidelines

> This document defines the symbolic and procedural rules for community-suggested content, code, or ritual modifications within Eden Protocol. All proposals are subject to DAO oversight and sacred path compliance.

---

## 🔄 Purpose

Eden’s modular design allows contributors to:
- Propose new quests
- Modify Tree trait logic
- Suggest visual themes or auras
- Expand sacred path representations
- Adjust XP thresholds or decay timers

These changes are sacred. All mods affect symbolic truth and inner narrative flow — and must be handled with reverence.

---

## ✅ Eligibility to Submit

- User must have:
  - Level 3+ MeritCoin
  - At least 1 completed Shadow Quest
  - Truth Integrity score above minimum threshold

- Proposal must be:
  - Submitted via DAO vote system
  - Reviewed through sacred path filters
  - Fully documented with schema changes, narrative rationale, and symbolic intent

---

## 📜 Proposal Format

Each mod proposal must include:
- `mod_type` – (e.g., "quest", "tree", "aura", "ritual", "trait_decay")
- `title` – Symbolic name (e.g., "Trial of the Ashen Path")
- `description` – Purpose, metaphor, and expected transformation
- `alignment_check` – Which sacred paths it supports or may conflict with
- `quest_logic` – Stubbed or narrative module reference
- `impact_zone` – Tree traits, XP schema, or interface nodes affected

---

## 🧪 Audit Criteria

All proposals are evaluated on the following:

| Criterion              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Symbolic Integrity** | Does this align with mythic healing and transformation?                     |
| **Sacred Compliance**  | Does it respect allowed sacred paths?                                       |
| **Non-Exploitability** | Could it be used to farm XP, skip Shadow Quests, or fake transformation?    |
| **Ritual Cohesion**    | Does it support presence > performance?                                     |
| **Narrative Clarity**  | Is the proposed mod internally legible as part of Eden’s mythos?            |

---

## ❌ Auto-Reject Conditions

- Proposals that:
  - Reference forbidden sacred paths
  - Promote competitive gamification
  - Contain ironic or trivial elements
  - Undermine XP lockout or quest thresholds

---

## 🗳️ DAO Approval Process

1. Submit proposal via `/dao/proposal_submitter.py`
2. Pass symbolic formatting check
3. Reviewed by:
   - Community review committee (read-only)
   - Sacred path audit filter (automated)
   - Truth Integrity validator (XP + quest history)
4. DAO-wide vote initiated
5. If passed → pushed to `/mod_loader.py` and added to `/docs/ritual_quest_examples.md`

---

## 🔮 Long-Term Roadmap

Future DAO mod features will include:
- Mod rating system (symbolic, not stars)
- Sacred path endorsement
- Zero-Knowledge Contributor trail
- DAO-approved seasonal “Ritual Patches”

---

> “To modify the myth is to shape the soul. Propose with intent. Vote with integrity.”
