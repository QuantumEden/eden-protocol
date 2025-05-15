# 🌐 EdenQuest Web Interface – React.js / Next.js

> This folder defines the structure for the web-based Eden dashboard. It focuses on DAO participation, XP tracking, avatar identity review, and global system visualization via the World Tree.

---

## 🧱 Core Modules

### 🗳️ DAO Proposal Panel
- List of recent symbolic proposals
- Truth-weighted vote system
- Voter glyph + merit score preview
- “Soulbound Proposal” submission form

### 🌍 World Tree Dashboard
- Global user metrics (aggregate Tree health)
- Visual health branches (per trait across users)
- Heatmap of recent growth, decay, quests completed
- Pulse animation for system resonance
- 🔁 **Soulform Sync Pulse** — reflects active global transformations

### 🪙 XP & MeritCoin Explorer
- User XP chart + level history
- XP lockout log
- Disclosure token history (symbolic, non-identifying)
- MeritCoin soulbound index
- Soulform-based XP multiplier audit (if applicable)

### 🧬 Avatar Viewer + Audit Trail
- Avatar history (sacred path, glyph, archetype)
- Quest completion logs
- Symbolic Tree state over time
- 🌬️ **Soulform Visual Log**:
  - transformation names, timestamps, elemental affinities

---

## ⚙️ Component Structure

/ui/react_web_portal/
├── components/
│   ├── DAOVotePanel.tsx
│   ├── XPChart.tsx
│   ├── WorldTreeMap.tsx
│   ├── AvatarAudit.tsx
│   ├── DisclosureLog.tsx
├── pages/
│   ├── index.tsx
│   ├── dao.tsx
│   ├── avatar.tsx
│   ├── worldtree.tsx
├── utils/
│   └── sessionParser.ts
└── App.tsx

---

## 🔐 Data Sources

Pulls from:

- `/schemas/eden_payload.schema.json`
- `/schemas/app_session.schema.json`
- `soulform_visuals` object from `/infra/token_router_stub.py`
- DAO commit logs + XP commit chain (optional stubs)

---

## 🛡️ UX Design Philosophy

- DAO votes are solemn — not competitive
- World Tree should feel mythic, not gamified
- All logs must be symbolic — no raw data exposure
- Soulform presence must feel like a global ripple, not a badge
- Navigation flow: *XP → Avatar → DAO → World Tree*

---

## 🔮 Future Capabilities

- Public DAO proposal explorer  
- Guest user simulation mode  
- Modular merit-based mod submission (admin-only)  
- Live XP resonance graph from new user commits  
- Soulform constellation overlays on World Tree  

---

> The web dashboard is Eden’s temple of memory.  
> It records who we’ve become — and who we are becoming together.
