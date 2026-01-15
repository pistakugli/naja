#!/bin/bash
echo "🚀 Setting up NAJA environment..."
export PATH="/mnt/user-data/naja:$PATH"
export PYTHONPATH="/mnt/user-data/python-packages:$PYTHONPATH"
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
echo "✅ Environment ready!"
echo "Run: naja-all to see available commands"
