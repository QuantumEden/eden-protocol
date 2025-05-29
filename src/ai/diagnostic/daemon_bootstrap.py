"""
Daemon Bootstrap for Eden Protocol

Initializes the Daemon's dynamic import system and other runtime components.
This module should be imported as early as possible in the application lifecycle.
"""

import sys
from typing import Optional

# Flag to track if bootstrap has been performed
_BOOTSTRAP_COMPLETE = False

def bootstrap_daemon():
    """
    Bootstrap the Daemon component, installing import hooks and initializing
    runtime components.
    """
    global _BOOTSTRAP_COMPLETE
    if _BOOTSTRAP_COMPLETE:
        return

    # Install import hooks
    from src.ai.diagnostic.import_hook import install_import_hooks
    install_import_hooks()

    # Set up global exception handling for ImportError
    _setup_import_error_handling()

    _BOOTSTRAP_COMPLETE = True

    # Log successful bootstrap
    try:
        from src.ai.diagnostic.report_adapter import log_sandbox_result
        log_sandbox_result(
            success=True,
            context="Daemon Bootstrap",
            message="Daemon bootstrap complete, dynamic import system active",
            symbol="daemon_activation"
        )
    except ImportError:
        pass  # Logging will be retried later if needed

def _setup_import_error_handling():
    """
    Set up global exception handling for ImportError.
    """
    original_excepthook = sys.excepthook

    def import_error_excepthook(exc_type, exc_value, exc_traceback):
        if exc_type is ImportError:
            module_name = _extract_module_name_from_import_error(exc_value)
            if module_name:
                try:
                    from src.ai.diagnostic.import_resolver import ImportResolver
                    from src.ai.diagnostic.import_hook import ImportErrorHandler

                    module = ImportResolver.resolve_missing_module(module_name)
                    if module:
                        sys.modules[module_name] = module
                        ImportErrorHandler.notify_eidelon(
                            module_name,
                            f"Resolved missing module: {module_name}"
                        )
                        return  # Skip propagation of exception
                except Exception:
                    pass  # Continue with default behavior

        original_excepthook(exc_type, exc_value, exc_traceback)

    sys.excepthook = import_error_excepthook

def _extract_module_name_from_import_error(error: ImportError) -> Optional[str]:
    """
    Extract the module name from an ImportError message.

    Args:
        error: The ImportError exception object

    Returns:
        The extracted module name or None
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

# Auto-bootstrap if this module is imported directly
if __name__ != "__main__":
    bootstrap_daemon()
