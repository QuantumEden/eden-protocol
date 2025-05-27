# examples/symbolic_error_test.py

"""
Symbolic Error Test – Jungian Synchronicity Trigger

Triggers various exception types to test Daemon’s symbolic classification system,
sandbox memory recording, and Jung-oriented reflection logging.
"""

from src.ai.diagnostic.sandbox_executor import try_symbolic_execution

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
        print(f"🔍 Running Test: {test['label']}")
        result = try_symbolic_execution(test["code"], context=test["label"])
        print("🧠 Result:", result)
        print("—" * 60)
