# tests/unit/symbolic_interpreter_test.py

"""
Unit Test – Symbolic Interpreter Classification

Verifies that the symbolic interpreter correctly maps exceptions
to symbolic archetypes for Jungian synchronicity tracking.
"""

from src.ai.diagnostic.symbolic_interpreter import classify_exception

def test_classify_import_error():
    e = ImportError("No module named 'missing'")
    assert classify_exception(e) == "path_dissonance"

def test_classify_key_error():
    e = KeyError("missing_key")
    assert classify_exception(e) == "lost_map_piece"

def test_classify_value_error():
    e = ValueError("bad value")
    assert classify_exception(e) == "mirror_reflection"

def test_classify_attribute_error():
    e = AttributeError("no such attribute")
    assert classify_exception(e) == "shadow_aspect"

def test_classify_type_error():
    e = TypeError("expected int, got str")
    assert classify_exception(e) == "inversion_conflict"

def test_classify_timeout_error():
    e = TimeoutError("operation timed out")
    assert classify_exception(e) == "ritual_disruption"

def test_classify_void_error():
    e = Exception("NoneType has no attribute")
    assert classify_exception(e) == "void_intrusion"

def test_classify_recursion_error():
    e = Exception("maximum recursion depth exceeded")
    assert classify_exception(e) == "ouroboros_loop"

def test_classify_unknown_error():
    e = Exception("unexpected behavior")
    assert classify_exception(e) == "undefined_synchronicity"
