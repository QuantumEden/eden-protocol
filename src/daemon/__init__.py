"""
Daemon Package – Eden Protocol

Provides import path harmonization and daemon-level symbolic patching utilities.
"""

from .path_harmoniz import install_path_harmoniz

# Automatically install Harmoniz when this package is loaded
install_path_harmoniz()
