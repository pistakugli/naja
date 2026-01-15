#!/bin/bash
# NAJA - Install Claude Skills

echo "📥 Downloading Claude Skills..."
wget -O /tmp/claude_skills.tar.gz https://github.com/pistakugli/naja/releases/download/v1.1-claude-skills/claude_skills.tar.gz

echo "📦 Extracting..."
tar -xzf /tmp/claude_skills.tar.gz

echo "✅ Claude Skills installed!"
echo "   Location: claude_skills/"
echo "   Skills: 16"
