# src/ai/diagnostic/reflection_memory.py

"""
Reflection Memory – Symbolic Memory Archive

Records symbolic runtime actions, synchronicities, and reflections
into persistent structured memory for future introspection.
"""

import json
import uuid
import datetime
from pathlib import Path
from typing import Dict

MEMORY_FILE = Path("memory/symbolic_reflections.json")

def store_sandbox_result(result: Dict):
    """
    Appends a symbolic execution record to long-term memory.

    Args:
        result (dict): Execution result and context
    """
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if MEMORY_FILE.exists():
        with MEMORY_FILE.open("r", encoding="utf-8") as f:
            memory = json.load(f)
    else:
        memory = []

    memory.append({
        "id": str(uuid.uuid4()),
        "type": "sandbox_execution",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        **result
    })

    with MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)
