#!/bin/bash
# Eden Protocol Development Environment Setup

# Install required dependencies
pip install jsonschema

# Set up PYTHONPATH in .env file
echo "PYTHONPATH=$(pwd)" > .env

# Create helper alias for running simulations with correct PYTHONPATH
echo "alias run_sim=\"python3 run_simulation.py\"" >> .env

echo "Setup complete! To activate the environment, run:"
echo "source .env"
