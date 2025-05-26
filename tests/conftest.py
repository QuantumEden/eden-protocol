# tests/conftest.py
# Global pytest config – ensures import paths and environment config

import sys
import os
from dotenv import load_dotenv

def pytest_configure(config):
    """
    Hook into pytest initialization to patch sys.path
    for test imports across the Eden Protocol repository
    and load environment variables for API key validation.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Add each key folder explicitly
    src_path = os.path.join(base_dir, 'src')
    infra_path = os.path.join(base_dir, 'infra')
    sim_path = os.path.join(base_dir, 'sim')

    for path in [src_path, infra_path, sim_path]:
        if path not in sys.path:
            sys.path.insert(0, path)

    # Load environment variables from .env (use fallback if not present)
    env_path = os.path.join(base_dir, ".env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path, override=True)
