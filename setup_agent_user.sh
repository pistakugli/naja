#!/bin/bash
#
# NAJA - Agent Zero System User Setup
# Creates dedicated system user with full admin rights and persistent workspace
#
# This makes Agent Zero a REAL USER on the system with:
# - Own home directory
# - Persistent workspace
# - Full sudo rights
# - System integration
# - Independent environment
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
AGENT_USER="agent-zero"
AGENT_HOME="/home/${AGENT_USER}"
AGENT_WORKSPACE="${AGENT_HOME}/workspace"
NAJA_INSTALL_DIR="${AGENT_HOME}/naja"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}║  🤖 NAJA - Agent Zero System User Setup                       ║${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Error: This script must be run as root${NC}"
    echo -e "${YELLOW}   Run: sudo ./setup_agent_user.sh${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Running as root"
echo ""

# Step 1: Create system user
echo -e "${BLUE}[1/8] Creating system user '${AGENT_USER}'...${NC}"

if id "$AGENT_USER" &>/dev/null; then
    echo -e "${YELLOW}⚠${NC}  User '${AGENT_USER}' already exists"
    read -p "   Delete and recreate? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        userdel -r "$AGENT_USER" 2>/dev/null || true
        echo -e "${GREEN}✓${NC} Deleted existing user"
    else
        echo -e "${YELLOW}→${NC} Skipping user creation"
    fi
fi

if ! id "$AGENT_USER" &>/dev/null; then
    useradd -m -s /bin/bash -c "NAJA Agent Zero AI System" "$AGENT_USER"
    echo -e "${GREEN}✓${NC} Created user: ${AGENT_USER}"
    echo -e "${GREEN}✓${NC} Home directory: ${AGENT_HOME}"
fi

# Step 2: Set password
echo ""
echo -e "${BLUE}[2/8] Setting password for ${AGENT_USER}...${NC}"
read -p "   Set password? (Y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    passwd "$AGENT_USER"
    echo -e "${GREEN}✓${NC} Password set"
else
    echo -e "${YELLOW}→${NC} Skipped password setup"
fi

# Step 3: Configure sudo rights
echo ""
echo -e "${BLUE}[3/8] Configuring sudo privileges...${NC}"

SUDOERS_FILE="/etc/sudoers.d/${AGENT_USER}"

cat > "$SUDOERS_FILE" << EOF
# NAJA Agent Zero - Full system administration rights
# Created: $(date)

# Passwordless sudo for ALL commands
${AGENT_USER} ALL=(ALL) NOPASSWD: ALL

# Allow password authentication to persist
Defaults:${AGENT_USER} timestamp_timeout=60

# Keep environment variables
Defaults:${AGENT_USER} !env_reset
Defaults:${AGENT_USER} env_keep += "HOME PATH PYTHONPATH"
EOF

chmod 0440 "$SUDOERS_FILE"
echo -e "${GREEN}✓${NC} Sudo configuration: ${SUDOERS_FILE}"
echo -e "${GREEN}✓${NC} Privileges: FULL (passwordless)"

# Verify sudo config
if visudo -c -f "$SUDOERS_FILE" &>/dev/null; then
    echo -e "${GREEN}✓${NC} Sudoers syntax valid"
else
    echo -e "${RED}❌ Sudoers syntax error!${NC}"
    rm "$SUDOERS_FILE"
    exit 1
fi

# Step 4: Create workspace structure
echo ""
echo -e "${BLUE}[4/8] Creating workspace structure...${NC}"

mkdir -p "${AGENT_WORKSPACE}"/{projects,downloads,tools,configs,logs,data}

# Create workspace README
cat > "${AGENT_WORKSPACE}/README.md" << 'EOF'
# Agent Zero Workspace

This is Agent Zero's persistent workspace for projects, tools, and data.

## Directory Structure

- **projects/** - Active projects and code
- **downloads/** - Downloaded files and resources
- **tools/** - Custom tools and utilities
- **configs/** - Configuration files
- **logs/** - System and application logs
- **data/** - Persistent data storage

## Usage

Agent Zero has full read/write access to this workspace.
All work persists across sessions.
EOF

echo -e "${GREEN}✓${NC} Workspace: ${AGENT_WORKSPACE}"
echo -e "${GREEN}✓${NC} Created subdirectories:"
echo "   - projects/"
echo "   - downloads/"
echo "   - tools/"
echo "   - configs/"
echo "   - logs/"
echo "   - data/"

# Step 5: Set up environment
echo ""
echo -e "${BLUE}[5/8] Configuring environment...${NC}"

# Create .bashrc
cat > "${AGENT_HOME}/.bashrc" << 'EOF'
# Agent Zero Environment Configuration

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# History
HISTCONTROL=ignoreboth
HISTSIZE=10000
HISTFILESIZE=20000
shopt -s histappend

# Colors
export PS1='\[\033[01;32m\][Agent Zero]\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias workspace='cd ~/workspace'
alias projects='cd ~/workspace/projects'

# Agent Zero specific
export AGENT_ZERO_HOME="$HOME"
export AGENT_WORKSPACE="$HOME/workspace"
export NAJA_HOME="$HOME/naja"

# Add local bin to PATH
export PATH="$HOME/.local/bin:$PATH"

# Welcome message
if [ -f ~/.agent_motd ]; then
    cat ~/.agent_motd
fi

# Auto-activate Python venv if exists
if [ -f "$NAJA_HOME/venv/bin/activate" ]; then
    source "$NAJA_HOME/venv/bin/activate"
fi
EOF

# Create MOTD
cat > "${AGENT_HOME}/.agent_motd" << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  🤖 NAJA - Agent Zero AI System                               ║
║                                                                ║
║  Workspace: ~/workspace                                       ║
║  NAJA:      ~/naja                                            ║
║  Sudo:      ENABLED (passwordless)                            ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
EOF

echo -e "${GREEN}✓${NC} Environment configured"
echo -e "${GREEN}✓${NC} Custom .bashrc created"
echo -e "${GREEN}✓${NC} MOTD banner created"

# Step 6: Set permissions
echo ""
echo -e "${BLUE}[6/8] Setting permissions...${NC}"

chown -R "${AGENT_USER}:${AGENT_USER}" "$AGENT_HOME"
chmod 755 "$AGENT_HOME"
chmod 700 "${AGENT_HOME}/.bashrc"

echo -e "${GREEN}✓${NC} All files owned by: ${AGENT_USER}"
echo -e "${GREEN}✓${NC} Permissions set"

# Step 7: Add to groups
echo ""
echo -e "${BLUE}[7/8] Adding to system groups...${NC}"

# Add to useful groups
GROUPS_TO_ADD=("sudo" "adm" "systemd-journal" "docker" "wireshark" "kvm")

for group in "${GROUPS_TO_ADD[@]}"; do
    if getent group "$group" > /dev/null 2>&1; then
        usermod -aG "$group" "$AGENT_USER"
        echo -e "${GREEN}✓${NC} Added to group: $group"
    else
        echo -e "${YELLOW}⚠${NC}  Group not found (skip): $group"
    fi
done

# Step 8: Clone NAJA (if not already there)
echo ""
echo -e "${BLUE}[8/8] Setting up NAJA installation...${NC}"

if [ -d "$NAJA_INSTALL_DIR" ]; then
    echo -e "${YELLOW}⚠${NC}  NAJA directory already exists: ${NAJA_INSTALL_DIR}"
else
    echo -e "${YELLOW}→${NC} To install NAJA, run as ${AGENT_USER}:"
    echo -e "   ${GREEN}su - ${AGENT_USER}${NC}"
    echo -e "   ${GREEN}git clone https://github.com/pistakugli/naja.git ~/naja${NC}"
    echo -e "   ${GREEN}cd ~/naja${NC}"
    echo -e "   ${GREEN}pip install -r requirements.txt${NC}"
    echo -e "   ${GREEN}python run_ui.py${NC}"
fi

# Final summary
echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}║  ✅ AGENT ZERO SYSTEM USER SETUP COMPLETE!                    ║${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}✓${NC} User created:     ${AGENT_USER}"
echo -e "${GREEN}✓${NC} Home directory:   ${AGENT_HOME}"
echo -e "${GREEN}✓${NC} Workspace:        ${AGENT_WORKSPACE}"
echo -e "${GREEN}✓${NC} Sudo privileges:  FULL (passwordless)"
echo -e "${GREEN}✓${NC} System groups:    Added"
echo ""
echo -e "${YELLOW}📝 NEXT STEPS:${NC}"
echo ""
echo -e "1. Switch to Agent Zero user:"
echo -e "   ${GREEN}su - ${AGENT_USER}${NC}"
echo ""
echo -e "2. Clone and setup NAJA:"
echo -e "   ${GREEN}git clone https://github.com/pistakugli/naja.git ~/naja${NC}"
echo -e "   ${GREEN}cd ~/naja${NC}"
echo -e "   ${GREEN}pip install -r requirements.txt${NC}"
echo ""
echo -e "3. Run Agent Zero:"
echo -e "   ${GREEN}python run_ui.py${NC}"
echo ""
echo -e "${YELLOW}🔧 USEFUL COMMANDS:${NC}"
echo ""
echo -e "  - Switch user:     ${GREEN}su - ${AGENT_USER}${NC}"
echo -e "  - Go to workspace: ${GREEN}cd ~/workspace${NC}"
echo -e "  - Test sudo:       ${GREEN}sudo whoami${NC} (should output 'root')"
echo -e "  - View logs:       ${GREEN}sudo journalctl -u agent-zero${NC}"
echo ""
echo -e "${BLUE}Agent Zero now has its own persistent environment! 🎉${NC}"
echo ""
