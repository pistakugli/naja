#!/bin/bash
# Auto-restore NAJA + Agent Zero na svakom startu

echo "🔄 AUTO-RESTORING NAJA + AGENT ZERO..."

# Copy sve u /usr/local/bin
cp /mnt/user-data/naja/naja* /usr/local/bin/ 2>/dev/null
cp /mnt/user-data/naja/agent-zero* /usr/local/bin/ 2>/dev/null

# Set permissions
chmod +x /usr/local/bin/naja* 2>/dev/null
chmod +x /usr/local/bin/agent-zero* 2>/dev/null

# Setup symlink za Python
mkdir -p /opt/naja
ln -sf /mnt/user-data/python-packages /opt/naja/python-packages 2>/dev/null

# Environment
export PATH="/usr/local/bin:$PATH"
export PYTHONPATH="/opt/naja/python-packages:$PYTHONPATH"
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"

echo "✅ Restored!"
echo "📦 Available tools:"
ls -1 /usr/local/bin/naja* /usr/local/bin/agent-zero* 2>/dev/null | wc -l
