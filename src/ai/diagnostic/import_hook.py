"""
Import Hook System for Eden Protocol

Provides dynamic import resolution capabilities to the Daemon component,
allowing it to intercept and resolve import errors at runtime without
modifying source files.
"""
import sys
import importlib.abc
import importlib.util
import importlib.machinery
from types import ModuleType
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path

# Cache for resolved modules to avoid repeated lookups
RESOLVED_MODULES: Dict[str, ModuleType] = {}
# Cache for module search paths
MODULE_PATHS: Dict[str, str] = {}
# Flag to prevent recursive import attempts
IMPORT_IN_PROGRESS: List[str] = []

class EdenImportFinder(importlib.abc.MetaPathFinder):
    """
    Custom import finder that attempts to locate modules that would otherwise fail to import.
    """
    @staticmethod
    def find_spec(fullname: str, path: Optional[List[str]] = None, target: Optional[ModuleType] = None):
        # Skip if we're already trying to import this module (prevent recursion)
        if fullname in IMPORT_IN_PROGRESS:
            return None

        # Skip if module is already successfully imported or in standard library
        if fullname in sys.modules or not "." in fullname:
            return None

        # Skip third-party packages
        if not fullname.startswith(('src.', 'api.', 'infra.', 'sim.')):
            return None

        try:
            IMPORT_IN_PROGRESS.append(fullname)

            # Check if we've already resolved this module
            if fullname in RESOLVED_MODULES:
                module = RESOLVED_MODULES[fullname]
                return importlib.machinery.ModuleSpec(fullname, EdenImportLoader(fullname, module))

            # Try to find the module in alternative locations
            module_path = EdenModuleMapper.find_module_path(fullname)
            if module_path:
                spec = importlib.util.spec_from_file_location(fullname, module_path)
                if spec:
                    return spec

            return None
        finally:
            if fullname in IMPORT_IN_PROGRESS:
                IMPORT_IN_PROGRESS.remove(fullname)

class EdenImportLoader(importlib.abc.Loader):
    """
    Custom loader that loads modules from alternative locations or creates proxy modules.
    """
    def __init__(self, fullname: str, module: Optional[ModuleType] = None):
        self.fullname = fullname
        self.module = module

    def create_module(self, spec):
        if self.module:
            return self.module
        return None  # Use default module creation

    def exec_module(self, module):
        if self.module:
            return  # Using cached module

        RESOLVED_MODULES[self.fullname] = module
        ImportErrorHandler.log_resolution(self.fullname, module.__file__ if hasattr(module, '__file__') else "memory")

class EdenModuleMapper:
    """
    Maps module names to file paths, searching alternative locations when standard imports fail.
    """
    @staticmethod
    def find_module_path(fullname: str) -> Optional[str]:
        if fullname in MODULE_PATHS:
            return MODULE_PATHS[fullname]

        parts = fullname.split('.')
        potential_paths = []

        # src/module/submodule.py
        potential_paths.append('/'.join(parts) + '.py')
        # src/module/submodule/__init__.py
        potential_paths.append('/'.join(parts) + '/__init__.py')

        if len(parts) >= 3:
            alt_path = f"src/{parts[-1]}.py"
            potential_paths.append(alt_path)
            alt_init_path = f"src/{parts[-1]}/__init__.py"
            potential_paths.append(alt_init_path)

            if len(parts) >= 4:
                alt_path2 = f"src/{parts[-2]}/{parts[-1]}.py"
                potential_paths.append(alt_path2)
                alt_init_path2 = f"src/{parts[-2]}/{parts[-1]}/__init__.py"
                potential_paths.append(alt_init_path2)

        root_dir = Path(__file__).parent.parent.parent.parent
        for path in potential_paths:
            full_path = root_dir / path
            if full_path.exists():
                MODULE_PATHS[fullname] = str(full_path)
                return str(full_path)

        return None

class ImportErrorHandler:
    """
    Handles import errors by coordinating with Jung/Eidelon for user feedback.
    """
    @staticmethod
    def log_resolution(module_name: str, file_path: str):
        try:
            from src.ai.diagnostic.report_adapter import log_sandbox_result
            log_sandbox_result(
                success=True,
                context="Import Resolution",
                message=f"Dynamically resolved import for {module_name} from {file_path}",
                symbol="daemon_import_resolution"
            )
        except Exception:
            pass

    @staticmethod
    def notify_eidelon(module_name: str, error_msg: str):
        try:
            from src.ai.council.jungian import jungian_reflection
            insight = jungian_reflection(
                user_id="system",
                message=f"Import error occurred: {error_msg}",
                context=f"Module {module_name} could not be imported"
            )
            from src.ai.diagnostic.report_adapter import log_sandbox_result
            log_sandbox_result(
                success=False,
                context="Import Resolution",
                message=insight,
                symbol="jung_import_insight"
            )
            return insight
        except Exception as e:
            print(f"Failed to notify Eidelon about import error: {e}")
            return None

def install_import_hooks():
    for finder in sys.meta_path:
        if isinstance(finder, EdenImportFinder):
            return
    sys.meta_path.insert(0, EdenImportFinder())

def create_proxy_module(name: str, attributes: Dict[str, Any] = None) -> ModuleType:
    module = ModuleType(name)
    if attributes:
        for key, value in attributes.items():
            setattr(module, key, value)
    RESOLVED_MODULES[name] = module
    return module
