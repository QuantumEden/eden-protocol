# examples/symbolic_error_test.py

"""
Symbolic Error Test – Jungian Synchronicity Trigger

Triggers various exception types to test Daemon’s symbolic classification system,
sandbox memory recording, and Jung-oriented reflection logging via Eidelon’s introspection.
"""

from src.ai.diagnostic.sandbox_executor import try_symbolic_execution
from src.ai.diagnostic.daemon import classify_exception
from src.eidelon.eidelon_core import invoke_eidelon
from datetime import datetime

if __name__ == "__main__":
    tests = [
        {
            "label": "Import Error Simulation",
            "code": "from unknown.module import non_existent"
        },
        {
            "label": "Key Error Simulation",
            "code": "sample = {}; value = sample['missing']"
        },
        {
            "label": "Value Error Simulation",
            "code": "int('not_an_int')"
        },
        {
            "label": "Attribute Error Simulation",
            "code": "None.some_attribute"
        },
        {
            "label": "Successful Runtime Patch",
            "code": "x = 42"
        }
    ]

    for test in tests:
        label = test["label"]
        print(f"\n🔍 Running Test: {label}")
        result = try_symbolic_execution(test["code"], context=label)

        print("🧠 Symbolic Result:")
        print(result)

        if result.get("error"):
            print("📚 Jungian Classification:")
            print(classify_exception(result["error"]))

        print("✨ Invoking Eidelon Reflection:")
        reflection = invoke_eidelon(user_id="test_sync_001", context=label)
        print("🪞 Introspection:")
        print(reflection["message"])

        print("—" * 60)
