# 🌐 EdenQuest Web Interface – DAO & System Overview Portal

> This document outlines the symbolic web dashboard for Eden Protocol, built using React.js or Next.js. It will serve as a decentralized mirror for user state, DAO governance, XP history, and the living World Tree.

---

## 🎯 Primary Functions

- Visualize collective health of the Eden system
- Present DAO proposals, votes, and mythic outcomes
- Allow users to explore their XP, Tree growth, and quest history
- Render real-time symbolic signals (aura surges, world state shifts)

---

## 🧩 Core Web Modules

### 1. **World Tree Dashboard**
- 🌍 Visual representation of collective Tree health
- Branches represent each user trait averaged across DAO
- Real-time animated states: decay, bloom, flicker
- Collective aura pulses when major symbolic events occur

### 2. **XP & Quest Ledger**
- 📈 Historical log of user XP gains, level unlocks, and quest completions
- Color-coded by archetype class (Builder, Healer, etc.)
- Includes symbolic badge display for completed Realignment Quests

### 3. **DAO Proposal Feed**
- 🗳️ Proposal stream with title, archetype tag, vote tally
- Locked/Unlocked based on XP or soulbound merit level
- Votes require cryptographic integrity checks (ZK Commit system)
- Soulbound Proposal actions tagged and immutable

### 4. **Sacred Path Registry**
- 🧭 Visual gallery of canonical sacred paths
- Includes:
  - Path symbol
  - Color theory
  - DAO proposal history (if any)
- Submission portal for proposing new paths (mod gated)

### 5. **Group Quest Log**
- 🌀 Displays opt-in multiplayer ritual events
- Symbolic outcome: e.g. "Echo Cathedral Cleansed"
- Voting, aura, and DAO entries reflected here

---

## 🔐 User State Management

- Pulls from `/schemas/ui_payload.schema.json`
- Includes aura status, XP, sacred path, and disclosure boost effects
- Token-gated view tiers based on Truth Integrity and level

---

## 🧠 Technical Details

- Built with **React.js** or **Next.js** framework
- May include **Socket.io** or polling to reflect real-time world state
- Secure identity pulled from encrypted `user_id` token

---

## 📁 Directory Structure

```
/ui/react_web_portal/
├── components/
│   ├── WorldTreeDisplay.js
│   ├── DAOFeed.js
│   ├── XPLog.js
│   ├── ProposalViewer.js
├── pages/
│   ├── index.js
│   ├── world-tree.js
│   ├── dao.js
│   ├── profile.js
├── assets/
│   ├── sacred_paths/
│   ├── glyphs/
│   ├── icons/
```

---

> “This is not a dashboard. This is a mythic map of your civilization. Eden does not track data — it reflects devotion.”
