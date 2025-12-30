# !/usr/bin/env bash
# Download and install the uv utility for dependency management
curl -LsSf https://astral.sh/uv/install.sh | sh

# Stop script on error
set -e

# Activate uv
source $HOME/.local/bin/env

# Install project dependencies using Makefile
make install
