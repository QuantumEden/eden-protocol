# tests/integration/daemon_patch_simulation_test.py

"""
Integration Test – Daemon Symbolic Patch Execution

Simulates a symbolic repair plan using the daemon's sandbox executor
and verifies successful execution and logging as a synchronicity.
"""

from src.ai.diagnostic.daemon import attempt_runtime_patch
from src.ai.diagnostic.reflection_memory import MEMORY_FILE
import json
import os

def test_symbolic_patch_execution():
    symbolic_plan = """
global TEST_SYMBOL
TEST_SYMBOL = 'alive'
"""
    context = "integration_test"

    result = attempt_runtime_patch(symbolic_plan, context)

    assert result["success"] is True
    assert result["symbol"] == "ritual_bridge"
    assert "TEST_SYMBOL" in globals()
    assert globals()["TEST_SYMBOL"] == "alive"

    # Check memory file was updated
    assert MEMORY_FILE.exists()

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
        found = any(entry.get("symbol") == "ritual_bridge" and entry.get("context") == context for entry in memory)
        assert found
