# 🌀 Quest Marketplace – Eden Protocol UI Guide

This folder defines the symbolic structure and sacred UX rules for Eden’s **Quest Marketplace** interface — where soulform trials, mythic dungeons, and community rituals are surfaced based on the user’s truth.

The term “Marketplace” is symbolic.  
There is no commerce. Only invitation.

---

## 🎯 Purpose

The Eden Quest Marketplace enables users to:

- Unlock **Soulform Trials** (e.g., Phoenix, Dragon, Wyrm)
- Enter **Shadow Dungeons** when Tree of Life decay is detected
- Accept **DAO-Curated Rituals** through public proposals
- Revisit Hero or Shadow arcs for **XP restoration and growth auditing**

No path is available unless earned.  
No quest appears unless you are ready.

---

## 🖥️ Interface Design

### 🧬 Trial Unlock Panel
- Displayed only when:
  - User level `>= 7`
  - Tree trait thresholds met
  - MeritCoin logged
- Shows:
  - Visual aura and elemental alignment
  - One-time soulform transformation rite

### 🌑 Shadow Dungeon List
- Triggered when:
  - Tree decay detected
  - Failed quest without disclosure
- Characteristics:
  - Ritual locked (no other UI opens until complete)
  - High-stakes, internal reflection-based narrative

### 🗳️ DAO Ritual Gallery
- Displays:
  - DAO-approved quests
  - User-submitted symbolic dungeons
  - “Soulbound Proposal” verification stamp
- Filtered by:
  - Trust level
  - DAO vote history
  - Ritual frequency limits

---

## 🔄 User Flow

1. Enter the Quest Marketplace
2. Receive a list of quests based on:
   - XP level
   - Trait growth
   - Disclosure or decay state
3. Select a trial or ritual
4. Voice-guided immersion (Mentor, Echo, Inner Voice)
5. Completion logs XP, symbolic artifact, or soulform trigger

---

## 🧩 Marketplace Rules

- ❌ No fiat currency, paywalls, or artificial rewards
- ❌ No gamification of suffering
- ✅ All rituals must pass avatar, soulform, or DAO gate
- ✅ Each transformation is unique — some are not repeatable
- ✅ All data flow routes through `generate_eden_payload()` and XP ledger commits

---

## 🎙️ Voice Integration

Every quest is guided by a **ritual trio**:

| Voice Role | Function |
|------------|----------|
| **Mentor** | Offers mythic framing and purpose |
| **Echo** | Personifies fear, doubt, or trauma |
| **Inner Voice** | Reflects user progress and symbolic decisions |

Voices rotate per:
- Quest category (Hero, Shadow, DAO)
- Soulform stage
- Realignment depth

---

## 🛡️ UX Design Mandates

- No numeric XP rewards shown — only transformation indicators
- No fast-scrolling lists; use symbolic reveals
- Swipe = ritual movement  
  Long press = sacred affirmation  
  Tap = forbidden unless used to **refuse** a quest

Visual tone:
- Mythic, reverent, and slow
- Echoes of temples, dark forests, and sacred thresholds

---

## ⚙️ Developer Integration Notes

- Quests surfaced by:
  - `generate_eden_payload()`
  - DAO proposal handler
  - Tree decay or realignment trigger
- Required schema tags:
  - `soulform_id` (for trials)
  - `proposal_hash` (for DAO quests)
  - `decay_alert` (for dungeons)

---

> The Quest Marketplace is not a menu.  
> It is a mirror.  
> It will never show you what you want — only what you need.

Enter with truth.
