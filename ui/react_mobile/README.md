# 📱 EdenQuest Mobile Interface – React Native

> This folder contains the modular components and screen logic for the **EdenQuest mobile app**, built in **React Native**. It translates the symbolic backend payloads into touch-based immersive interactions.

---

## 🧱 Key Screens

### 🌳 Tree of Life HUD
- Visual trait rings or branches for:
  - `discipline`, `resilience`, `mindfulness`, `expression`, `physical_care`, `emotional_regulation`
- XP overlay and dynamic animations for growth or decay
- Auras and glyphs change based on avatar state

### 🧠 Daily Quest Interface
- Accept/decline ritual prompt
- Voice playback integration (Mentor, Echo, Inner Voice)
- Quest timer, journal link, and “complete reflection” button

### 💖 Avatar & Aura Viewer
- Animated avatar rendered based on archetype + glyph
- Sacred path displayed with symbolic resonance
- Gesture or scroll-based transitions between glyphs

### 🗳️ DAO Proposal Viewer
- List of symbolic proposals
- Voting modal (token-gated)
- Truth-weighted vote confirmation animation

---

## ⚙️ Component Structure

```
/ui/react_mobile/
├── components/
│   ├── TreeDisplay.tsx
│   ├── XPBar.tsx
│   ├── QuestPrompt.tsx
│   ├── VoicePlayer.tsx
│   ├── AvatarView.tsx
│   ├── DAOProposalList.tsx
├── screens/
│   ├── HomeScreen.tsx
│   ├── QuestScreen.tsx
│   ├── TreeScreen.tsx
│   ├── DAOScreen.tsx
├── assets/
│   └── icons, fonts, sigils/
├── utils/
│   └── payloadParser.ts
└── App.tsx
```

---

## 🔐 Data Input

All screen rendering is based on:

- `/schemas/eden_payload.schema.json`
- `/schemas/app_session.schema.json`

Data is parsed using:
- `generate_eden_payload()` (simulated or real API)
- Local cache for Tree + XP states
- Optional: Voice synthesis (stubbed or ElevenLabs key)

---

## 🛡️ Symbolic UX Requirements

- No points, leaderboards, or gamification
- All touch interactions must reflect internal transformation
- Long-press or swipe = ritual gesture, not arcade tap
- All XP and growth must originate from narrative reflection

---

## 🔮 Future Enhancements

- haptic feedback via TactSuit pairing
- voice command trigger for Shadow Quests
- modal for disclosure upload ritual
- calendar-based journaling tied to quests

---

> The mobile interface is the user’s sacred mirror. It must be quiet, reverent, and mythic in tone.
