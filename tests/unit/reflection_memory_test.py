# tests/unit/reflection_memory_test.py

"""
Reflection Memory Test – Daemon Symbolic Memory Logging

Validates symbolic memory log integrity and structure when storing sandbox results.
"""

import json
import os
import uuid
from pathlib import Path
from src.ai.diagnostic.reflection_memory import store_sandbox_result, MEMORY_FILE

def test_store_sandbox_result_creates_file_and_logs_data():
    # Setup
    if MEMORY_FILE.exists():
        os.remove(MEMORY_FILE)

    fake_result = {
        "synchronicity_id": str(uuid.uuid4()),
        "symbolic_plan": "print('test')",
        "context": "test_suite",
        "user_id": "test_user",
        "timestamp": "2025-05-27T00:00:00Z",
        "success": True,
        "message": "Executed in test.",
        "symbol": "ritual_bridge"
    }

    # Execute
    store_sandbox_result(fake_result)

    # Validate
    assert MEMORY_FILE.exists(), "Memory file was not created."

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)

    assert isinstance(memory, list), "Memory file does not contain a list."
    assert len(memory) > 0, "Memory list is empty."
    assert memory[-1]["symbol"] == "ritual_bridge", "Symbol mismatch in memory entry."
    assert memory[-1]["user_id"] == "test_user", "User ID not stored correctly."

    print("✅ Reflection memory test passed.")
