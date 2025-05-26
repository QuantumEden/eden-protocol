# tests/conftest.py
# Global pytest configuration – ensures import paths and environment setup

import sys
import os
from dotenv import load_dotenv

def pytest_configure(config):
    """
    Hook into pytest initialization to:
    - Patch sys.path to support imports across Eden Protocol repo
    - Load .env file to enable secure API key validation
    """

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Add project root and subfolders to sys.path
    paths_to_patch = [
        base_dir,
        os.path.join(base_dir, 'src'),
        os.path.join(base_dir, 'infra'),
        os.path.join(base_dir, 'sim'),
        os.path.join(base_dir, 'tests')  # for test-to-test imports
    ]

    for path in paths_to_patch:
        if path not in sys.path:
            sys.path.insert(0, path)

    # Load .env for API keys and configuration
    env_path = os.path.join(base_dir, ".env")
    fallback_env = os.path.join(base_dir, ".env.example")

    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path, override=True)
    elif os.path.exists(fallback_env):
        load_dotenv(dotenv_path=fallback_env, override=True)
