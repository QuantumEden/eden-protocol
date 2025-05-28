# 🔐 Eden Protocol – Security & Deployment Policy

> Last updated: 2025-05-27 UTC  
> Author: Eden Systems Governance Unit

---

## 🛡️ Overview

The Eden Protocol integrates symbolic therapy, multi-agent AI orchestration (Eidelon), DAO governance, and blockchain-synchronized growth mechanics. Security protocols are engineered to protect sensitive identity metadata, soulform progression, and immutable XP commitments — all without compromising user sovereignty, symbolic evolution, or systemic introspection.

---

## 🔐 Environment Key Strategy

All operational API and AI keys are stored via a secure `.env` file structure.

### Example `.env` file:
```env
PYTHONPATH=src
HUME_API_KEY=...
ELEVENLABS_API_KEY=...
OPENAI_API_KEY=...
PINECONE_API_KEY=...
```

### Key Enforcement Policies:
- ✅ Never expose `.env` to version control – enforced via `.gitignore`
- ✅ Use `.env.example` with placeholder values for team onboarding
- ✅ Rotate keys every 90 days or immediately following contributor departure
- ✅ Validate keys through a CI/CD symbolic integrity check during deployment

---

## 🧠 AI Access & Role Security

Eidolon accesses OpenAI, ElevenLabs, Whisper, and Hume APIs. Each component is containerized within its symbolic role (e.g., Daemon, Jung, CBT).

### Protections:
- No frontend client has direct access to AI keys
- Concurrency throttled in dev/test environments
- Symbolic safeguards enforce ethical memory retention
- Emotion input never cached without Ritual Safeguard flag

---

## 🕵️‍♂️ User Identity & Soulform Anonymity

The system operates under **pseudo-anonymous identity constraints**. Soulform traits, journal data, and DAO votes are soulbound and non-transferable.

### Active Protections:
- Journals stored offline in append-only memory banks
- Semantic memory decays if opt-in flags are revoked
- zkXP logs are cryptographically committed using zero-knowledge proofs
- No full user payload ever leaves server or enters analytic pipelines

---

## 🔁 zkXP & DAO Integrity Layer

All quest completions, XP rewards, transformations, and proposal eligibility are bound to zkXP commitments and mirrored to a tamper-evident logbook.

### Enforcement Rules:
- Rituals must produce zkXP logs to gain progression credit
- All DAO proposals require zkXP authentication
- Suspicious vote behavior triggers an automatic Tribunal recall
- Duplicate or failed commits are sandboxed and flagged for symbolic review

---

## 🧬 Dev Security Practice

- Contributors undergo symbolic onboarding and audit review
- Simulations are executed with mocks unless in trusted enclave
- Ritual logic and DAO rules require >66% symbolic council approval before merge
- Daemon automatically logs anomalies under `/logs/security/` for flag review

---

## ⚠️ Incident Response & Symbolic Failures

All systemic disruptions, API failures, DAO anomalies, or suspicious ritual behavior should be recorded as **synchronicities** and symbolically triaged.

> “In Eden, growth is sacred — but protection is sacred too.”
