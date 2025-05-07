# Simulation Module (`/sim`)

This directory contains simulation and testing scripts used to validate and prototype core systems within the Eden Protocol infrastructure.

These files are not intended for production deployment but serve as:
- Behavioral verification tools
- Development staging utilities
- Logic testing harnesses
- Proof-of-concept scaffolding

---

## Contents

| File | Description |
|------|-------------|
| `avatar_identity_engine_simulation.py` | Runs multiple psychometric profiles through the Avatar Identity Engine to test symbolic accuracy |

---

## Usage

All simulation scripts assume that core logic modules (like `identity_engine.py`) exist within `/src/` and follow the Eden Protocol architecture.

To run a simulation:
```bash
python sim/avatar_identity_engine_simulation.py
```

---

> "What we simulate, we prototype. What we prototype, we manifest."
