"""
Symbolic Interpreter – Jungian Classification Engine

Maps runtime exceptions and anomalies to symbolic archetypes
for synchronicity interpretation by the Daemon and the Jung AI.
"""

from typing import Optional

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
        try:
            from src.ai.diagnostic.daemon import resolve_import
            module_name = _extract_module_name_from_import_error(e)
            if module_name and resolve_import(module_name):
                return "daemon_import_resolution"
        except Exception:
            pass
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

def _extract_module_name_from_import_error(error: ImportError) -> Optional[str]:
    """
    Extracts the module name from an ImportError message, if possible.

    Args:
        error: The ImportError exception

    Returns:
        The name of the module that failed to import
    """
    msg = str(error)

    if "No module named" in msg:
        parts = msg.split("'")
        if len(parts) >= 2:
            return parts[1]
    elif "cannot import name" in msg and "from" in msg:
        parts = msg.split("'")
        if len(parts) >= 4:
            return parts[3]

    return None
