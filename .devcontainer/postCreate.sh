#!/usr/bin/env bash
set -euxo pipefail

# Upgrade pip + core packaging tools
python -m pip install --upgrade pip setuptools wheel

# Install requirements if file exists
if [[ -f ./.devcontainer/requirements.txt ]]; then
  pip install -r ./.devcontainer/requirements.txt
fi

# Ensure Jupyter kernel is registered
python -m ipykernel install --user --name "python-base" --display-name "Python (base)"
