#!/bin/bash

# NAJA Skills Installer
# Installs Claude AI Skills system for Agent Zero

set -e

SKILLS_DIR="skills"
ARCHIVE_URL="https://github.com/pistakugli/naja/releases/download/v1.0-skills/naja-skills.tar.gz"

echo "═══════════════════════════════════════════════════════════"
echo "  NAJA - Claude AI Skills Installer"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Check if skills already installed
if [ -d "$SKILLS_DIR/public" ] && [ -d "$SKILLS_DIR/examples" ]; then
    echo "✅ Skills are already installed!"
    echo ""
    echo "Installed skills:"
    echo "  Public: $(ls -1 $SKILLS_DIR/public | grep -v '.skill' | wc -l) skills"
    echo "  Examples: $(ls -1 $SKILLS_DIR/examples | grep -v '.skill' | wc -l) skills"
    echo ""
    echo "To reinstall, run: rm -rf $SKILLS_DIR && ./install_skills.sh"
    exit 0
fi

echo "📦 Installing Claude AI Skills..."
echo ""

# Create skills directory
mkdir -p "$SKILLS_DIR"

# Check if archive exists locally
if [ -f "naja-skills.tar.gz" ]; then
    echo "✅ Found local skills archive"
    ARCHIVE="naja-skills.tar.gz"
elif [ -f "../naja-skills.tar.gz" ]; then
    echo "✅ Found skills archive in parent directory"
    ARCHIVE="../naja-skills.tar.gz"
else
    echo "📥 Downloading skills from GitHub..."
    
    # Try to download from GitHub release
    if command -v wget &> /dev/null; then
        wget -q --show-progress "$ARCHIVE_URL" -O naja-skills.tar.gz
        ARCHIVE="naja-skills.tar.gz"
    elif command -v curl &> /dev/null; then
        curl -L "$ARCHIVE_URL" -o naja-skills.tar.gz
        ARCHIVE="naja-skills.tar.gz"
    else
        echo "❌ Error: wget or curl required to download skills"
        echo ""
        echo "Manual installation:"
        echo "1. Download: $ARCHIVE_URL"
        echo "2. Extract: tar -xzf naja-skills.tar.gz"
        exit 1
    fi
fi

# Extract archive
echo ""
echo "📦 Extracting skills..."
tar -xzf "$ARCHIVE" -C .

echo ""
echo "✅ Skills installed successfully!"
echo ""

# Show installed skills
echo "Installed skills:"
echo ""
echo "PUBLIC SKILLS (6):"
ls -1 "$SKILLS_DIR/public" | grep -v ".skill" | sed 's/^/  • /'

echo ""
echo "EXAMPLE SKILLS (10):"
ls -1 "$SKILLS_DIR/examples" | grep -v ".skill" | sed 's/^/  • /'

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  Installation Complete!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "📚 Documentation: skills/README.md"
echo "🚀 Start NAJA: python run_ui.py"
echo ""
echo "Agent Zero will now have access to 16 expert skills for:"
echo "  • Document creation (Word, PowerPoint, Excel, PDF)"
echo "  • Web UI design"
echo "  • Visual artwork"
echo "  • Specialized workflows"
echo ""
