# src/ai/diagnostic/symbolic_interpreter.py

"""
Symbolic Interpreter – Jungian Classification Engine

Maps runtime exceptions and anomalies to symbolic archetypes
for synchronicity interpretation by the Daemon and the Jung AI.
"""

def classify_exception(e: Exception) -> str:
    """
    Converts an exception into a symbolic archetype.
    This symbolic label is used in Daemon memory and overlays.

    Args:
        e (Exception): The exception to classify

    Returns:
        str: Symbolic classification string
    """
    error_str = str(e).lower()

    if isinstance(e, ImportError):
        return "path_dissonance"
    elif isinstance(e, KeyError):
        return "lost_map_piece"
    elif isinstance(e, ValueError):
        return "mirror_reflection"
    elif isinstance(e, AttributeError):
        return "shadow_aspect"
    elif isinstance(e, TypeError):
        return "inversion_conflict"
    elif isinstance(e, TimeoutError):
        return "ritual_disruption"
    elif "none" in error_str or "null" in error_str:
        return "void_intrusion"
    elif "circular" in error_str or "recursion" in error_str:
        return "ouroboros_loop"
    else:
        return "undefined_synchronicity"
