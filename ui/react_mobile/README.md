# 📱 EdenQuest Mobile UI – React Native Design Blueprint

> This document outlines the core mobile user interface logic and layout for EdenQuest. It serves as a guide for implementing the symbolic healing experience on mobile devices via React Native.

---

## 🎯 Primary Goals

- Render symbolic feedback in a trauma-safe, non-gamified interface
- Reflect avatar state, Tree of Life, XP level, and daily quests
- Provide access to DAO proposals (read-only or vote if eligible)
- Integrate voice-driven symbolic quest guidance (optional)

---

## 🧩 Core UI Components

### 1. **Tree of Life Screen**
- 🌳 Vertical tree diagram with animated branches
- Each branch represents a trait (Discipline, Expression, etc.)
- Branches animate or flicker based on health values (0–100)
- Tap to view symbolic breakdown and growth history

### 2. **Avatar & Aura Panel**
- 🧬 Displays archetype class, aura glyph, and sacred path
- Aura pulse reflects current alignment or shadow flicker
- Optional toggle for voice reflection ("Inner Voice" journal mode)

### 3. **XP Tracker**
- 🪙 XP meter shows progress toward next merit level
- Locked if user has triggered a symbolic violation
- XP earned shown in session summary

### 4. **Daily Quest Interface**
- 📜 Displays current EdenQuest assignment
- Shows:
  - Quest title
  - Theme (e.g. “Reclaiming Discipline”)
  - Metaphor (e.g. “Walk the Labyrinth”)
  - Completion ritual
- Mark as complete triggers soft voice narration or reflection

### 5. **DAO Feed (Optional)**
- 🗳️ Read-only DAO updates (proposals, votes, group ritual triggers)
- Unlocks voting if truth integrity or XP thresholds are met

---

## 🔐 Additional Features

- Biometric unlock for session resume (Face ID/Touch ID)
- Token-gated access to deeper quests based on Tree health
- Aura emergency override (for user-triggered cooldown/reset)

---

## 🧠 Technical Notes

- Built with **React Native** and optional **Expo** framework
- Uses payloads from `/schemas/ui_payload.schema.json`
- Can be simulated using mocked JSON until backend connection is live

---

## 📁 Directory Structure

```
/ui/react_mobile/
├── components/
│   ├── TreeVisualizer.js
│   ├── QuestPanel.js
│   ├── XPTracker.js
│   ├── AuraDisplay.js
├── screens/
│   ├── HomeScreen.js
│   ├── QuestScreen.js
│   ├── TreeScreen.js
│   ├── DAODashboard.js
├── assets/
│   ├── glyphs/
│   ├── auras/
│   ├── icons/
```

---

> “Your phone is not a window — it is a mirror. EdenQuest renders your soul in light and branch and breath.”
