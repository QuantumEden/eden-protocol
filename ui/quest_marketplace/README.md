# Quest Marketplace – Eden Protocol UI Guide

This folder defines the design, rules, and structure of Eden’s symbolic quest activation interface.

The “Marketplace” is a metaphor.  
It is not commercial. It is sacred.

---

## Purpose

The Quest Marketplace allows users to:

- Unlock **Soulform Trials** (Phoenix, Dragon, Wyrm, etc.)
- Accept **Mythic Dungeons** tied to Tree imbalance
- Trigger **Community Rituals** proposed by the DAO
- Replay completed Hero or Shadow arcs for XP restoration

---

## Interface Design

### Core Screens

- **Trial Unlock Panel**
  - Requires level + trait balance + MeritCoin
  - One-time entry per form
  - Visual preview, aura animation, and elemental theme

- **Shadow Dungeon List**
  - Appears only if Tree decay or quest failures detected
  - High-stakes reflection quests
  - Entry locks other UI functions until resolved

- **DAO Ritual Gallery**
  - Top-rated symbolic quests by trusted users
  - “Soulbound Proposal” status badge
  - Verified via vote or curator key

---

## User Flow

1. Open Quest Marketplace
2. See what’s available based on Tree + XP
3. Select a ritual trial
4. Complete voice-prompted quest or dungeon
5. Earn symbolic token, XP, or transformation trigger

---

## Rules

- No quests may be purchased
- No shortcut via grind or fiat
- All trials must pass avatar, soulform, or DAO gate
- Each soulform has a unique dungeon only visible to eligible users

---

## Voice Integration

- Each quest is narrated by a trio:
  - Mentor (guidance)
  - Echo (resistance)
  - Inner Voice (reflection)

- Voice roles rotate per quest type

---

## UX Mandates

- Do not list “rewards” in numeric terms
- Visuals must remain mythic, dark, sacred
- Touch input must mimic ritual gestures (swipe, long press)

---

## Developer Notes

- Marketplace is bound to `generate_eden_payload()` + XP ledger
- Soulform dungeons require `soulform_id` and `level >= 7`
- DAO rituals require proposal hash and vote verification

---

> The Quest Marketplace is not a feature.
> It is a gate.
> Enter only when the system calls your name.
