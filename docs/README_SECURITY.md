# 🔐 Eden Protocol – Security & Deployment Policy

> Last updated: 2025-05-26 UTC  
> Author: Eden Systems Governance Unit

---

## 🛡️ Overview

The Eden Protocol integrates symbolic therapy, DAO voting, and AI-powered growth into a unified system. Security policies must safeguard sensitive identity signals, behavioral data, and encrypted DAO activity — without compromising symbolic flexibility or user sovereignty.

---

## 🔐 Environment Key Strategy

All API and system-level keys must be stored in a hidden `.env` file (or secure vault).

### Example Structure:
```env
PYTHONPATH=src
HUME_API_KEY=...
ELEVENLABS_API_KEY=...
OPENAI_API_KEY=...
PINECONE_API_KEY=...
```

### Enforcement:

- ✅ `.env` is excluded via `.gitignore`
- ✅ Never commit real keys to version control
- ✅ Use `.env.example` with placeholder values for onboarding

---

## 🧠 AI Access Security

Eidolon connects to OpenAI, ElevenLabs, WhisperX, and Hume APIs.

### Key Policies:

- Rotate API keys quarterly or upon contributor departure
- Never allow public-facing frontend access to backend keys
- Limit concurrency rate in development environments

---

## 🕵️‍♂️ User Identity & Soulform Anonymity

User payloads and soulform records are **pseudo-anonymous**.

### Protections:

- DAO proposals are soulbound (non-transferable)
- Only hashed zkXP logs are stored long-term
- Journals are stored in offline append-only mode
- Session caches and semantic memory never leave server
- Opt-in flags control world visibility of reflections or rituals

---

## 🔁 zkXP & DAO Integrity Layer

All XP gains, quests, transformations, and reflections are hashed into a zkXP commit structure.

### Integrity Rules:

- Duplicate XP commits auto-flagged
- All proposals require zkXP linkage to be eligible
- Tribunal votes are stored in tamper-evident logs
- Vote tampering triggers a full DAO snapshot recall

---

## 🧬 Dev Security Practice

- All contributors must pass symbolic onboarding
- All test simulations are run offline or with mock data
- DAO updates and ritual logic require >66% symbolic approval

---

## ⚠️ Incident Response

Any system irregularity, DAO proposal corruption, or unauthorized key event should be logged under `/logs/security/`.

> “In Eden, growth is sacred — but protection is sacred too.”

