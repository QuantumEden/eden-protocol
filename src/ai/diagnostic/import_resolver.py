"""
Import Resolver for Eden Protocol

Provides utilities for resolving imports dynamically and creating proxy modules
when needed. Works with the import_hook system to provide runtime import healing.
"""
import sys
import inspect
from types import ModuleType
from typing import Dict, List, Optional, Any, Callable
from pathlib import Path

from src.ai.diagnostic.import_hook import create_proxy_module, RESOLVED_MODULES

class ImportResolver:
    """
    Resolves imports dynamically by creating proxy modules or finding alternative paths.
    """
    @staticmethod
    def resolve_missing_module(name: str) -> Optional[ModuleType]:
        """
        Attempt to resolve a missing module by various strategies.

        Args:
            name: The full name of the module to resolve

        Returns:
            A module object if resolution was successful, None otherwise
        """
        if name in RESOLVED_MODULES:
            return RESOLVED_MODULES[name]

        similar_module = ImportResolver._find_similar_module(name)
        if similar_module:
            return similar_module

        return ImportResolver._create_empty_proxy(name)

    @staticmethod
    def _find_similar_module(name: str) -> Optional[ModuleType]:
        """
        Find a module with a similar name that might be a suitable substitute.

        Args:
            name: Name of the missing module

        Returns:
            A proxy module mimicking a similar module, or None if not found
        """
        parts = name.split('.')

        if len(parts) > 1:
            parent_name = '.'.join(parts[:-1])
            try:
                parent = __import__(parent_name, fromlist=['__name__'])
                return create_proxy_module(name, {'__parent__': parent_name})
            except ImportError:
                pass

        final_part = parts[-1]
        for module_name in list(sys.modules.keys()):
            if module_name.endswith('.' + final_part):
                return create_proxy_module(name, {'__similar__': module_name})

        return None

    @staticmethod
    def _create_empty_proxy(name: str) -> ModuleType:
        """
        Create an empty proxy module as a last resort.

        Args:
            name: Name of the proxy module

        Returns:
            A minimal placeholder module
        """
        return create_proxy_module(name, {
            '__proxy__': True,
            '__doc__': f"Proxy module for {name} created by Eden Protocol Daemon"
        })

    @staticmethod
    def inject_function(module_name: str, function_name: str, implementation: Callable) -> bool:
        """
        Inject a function into a module, creating the module if it doesn't exist.

        Args:
            module_name: The name of the module to inject into
            function_name: The name of the function to inject
            implementation: The function implementation

        Returns:
            True if injection was successful, False otherwise
        """
        try:
            if module_name in sys.modules:
                module = sys.modules[module_name]
            elif module_name in RESOLVED_MODULES:
                module = RESOLVED_MODULES[module_name]
            else:
                module = create_proxy_module(module_name)

            setattr(module, function_name, implementation)
            RESOLVED_MODULES[module_name] = module

            if module_name not in sys.modules:
                sys.modules[module_name] = module

            return True
        except Exception:
            return False
