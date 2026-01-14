#!/bin/bash
#
# NAJA - Kali Linux Security Tools Auto-Installer
# Automatically installs 100+ most popular Kali security tools
#
# Usage: sudo ./install_kali_tools.sh
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}║  🔧 NAJA - Kali Security Tools Auto-Installer                ║${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Error: This script must be run as root${NC}"
    echo -e "${YELLOW}   Run: sudo ./install_kali_tools.sh${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Running as root"
echo ""

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    VERSION=$VERSION_ID
else
    echo -e "${RED}❌ Cannot detect OS${NC}"
    exit 1
fi

echo -e "${BLUE}Detected OS:${NC} $OS $VERSION"
echo ""

# Check if Kali Linux
if [ "$OS" = "kali" ]; then
    echo -e "${GREEN}✓${NC} Kali Linux detected - most tools already installed"
    IS_KALI=true
else
    echo -e "${YELLOW}⚠${NC}  Not Kali Linux - will install available tools"
    IS_KALI=false
fi

echo ""
echo -e "${BLUE}This will install 100+ security tools including:${NC}"
echo "  • Network scanners (nmap, masscan, zmap)"
echo "  • Web scanners (nikto, sqlmap, wpscan)"
echo "  • Password crackers (john, hashcat, hydra)"
echo "  • Exploitation tools (metasploit)"
echo "  • Wireless tools (aircrack-ng)"
echo "  • Forensics tools (volatility, binwalk)"
echo "  • And many more..."
echo ""

read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo -e "${BLUE}[1/10] Updating package lists...${NC}"
apt-get update -qq

# Define tool categories
declare -A TOOLS

# Network Scanning
TOOLS[network]="nmap masscan netdiscover hping3 unicornscan zmap arp-scan arping fping"

# Web Application Testing
TOOLS[web]="nikto sqlmap wpscan dirb gobuster ffuf wfuzz whatweb httprobe dirsearch commix"

# Password Cracking
TOOLS[password]="john hashcat hydra medusa ncrack patator crunch cewl"

# Exploitation
TOOLS[exploit]="metasploit-framework exploitdb searchsploit beef-xss set"

# Wireless
TOOLS[wireless]="aircrack-ng reaver bully pixiewps kismet wifite"

# Packet Analysis
TOOLS[packet]="wireshark tshark tcpdump ettercap-text-only dsniff"

# Information Gathering
TOOLS[info]="whois dnsenum dnsrecon fierce theharvester recon-ng subfinder amass"

# Vulnerability Scanning  
TOOLS[vuln]="openvas lynis nikto wapiti skipfish"

# Forensics
TOOLS[forensics]="volatility-tools foremost binwalk autopsy sleuthkit scalpel exiftool"

# Network Tools
TOOLS[network_tools]="netcat-traditional socat proxychains4 stunnel4 sslscan sslyze testssl.sh"

# Sniffing & Spoofing
TOOLS[sniff]="responder macchanger"

# Post Exploitation
TOOLS[post]="impacket-scripts linpeas winpeas pspy"

# Reverse Engineering
TOOLS[reverse]="radare2 ghidra objdump gdb ltrace strace"

# Social Engineering
TOOLS[social]="gophish"

# Database
TOOLS[database]="sqlmap sqlninja"

# Misc
TOOLS[misc]="curl wget git python3-pip docker.io ncat proxychains tor"

# Installation counter
TOTAL_TOOLS=0
INSTALLED=0
FAILED=0
SKIPPED=0

# Count total tools
for category in "${!TOOLS[@]}"; do
    for tool in ${TOOLS[$category]}; do
        ((TOTAL_TOOLS++))
    done
done

echo ""
echo -e "${BLUE}[2/10] Installing tools...${NC}"
echo -e "${YELLOW}Total tools to install: ${TOTAL_TOOLS}${NC}"
echo ""

install_tool() {
    local tool=$1
    local category=$2
    
    # Check if already installed
    if command -v $tool &> /dev/null || dpkg -l | grep -q "^ii  $tool "; then
        echo -e "${GREEN}✓${NC} $tool (already installed)"
        ((INSTALLED++))
        return 0
    fi
    
    # Try to install
    if apt-get install -y -qq $tool 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $tool"
        ((INSTALLED++))
    else
        echo -e "${RED}✗${NC} $tool (not available)"
        ((FAILED++))
    fi
}

# Install by category
STEP=2
for category in "${!TOOLS[@]}"; do
    ((STEP++))
    
    # Capitalize category name
    cat_name=$(echo $category | sed 's/_/ /g' | sed 's/\b\(.\)/\u\1/g')
    
    echo ""
    echo -e "${BLUE}[$STEP/10] Installing ${cat_name} tools...${NC}"
    
    for tool in ${TOOLS[$category]}; do
        install_tool "$tool" "$category"
    done
done

# Special installations requiring manual handling
echo ""
echo -e "${BLUE}[9/10] Installing special tools...${NC}"

# Metasploit (if not Kali)
if [ "$IS_KALI" = false ]; then
    if ! command -v msfconsole &> /dev/null; then
        echo -e "${YELLOW}→${NC} Installing Metasploit Framework..."
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
        chmod 755 msfinstall
        ./msfinstall
        rm msfinstall
        echo -e "${GREEN}✓${NC} Metasploit Framework"
    else
        echo -e "${GREEN}✓${NC} Metasploit Framework (already installed)"
    fi
fi

# Python tools
echo -e "${YELLOW}→${NC} Installing Python security tools..."
pip3 install --break-system-packages impacket scrapy requests beautifulsoup4 sqlmap 2>/dev/null || pip3 install impacket scrapy requests beautifulsoup4 sqlmap
echo -e "${GREEN}✓${NC} Python security tools"

# Final update
echo ""
echo -e "${BLUE}[10/10] Finalizing installation...${NC}"
apt-get autoremove -y -qq
apt-get clean -qq

# Summary
echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}║  ✅ INSTALLATION COMPLETE!                                    ║${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}Successfully installed: ${INSTALLED}/${TOTAL_TOOLS} tools${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${YELLOW}Not available: ${FAILED} tools${NC}"
fi
echo ""

# Create verification script
cat > /usr/local/bin/verify-kali-tools << 'VERIFY'
#!/bin/bash
# Verify installed Kali tools

echo "Verifying Kali security tools installation..."
echo ""

check_tool() {
    if command -v $1 &> /dev/null; then
        echo "✓ $1"
    else
        echo "✗ $1 (not found)"
    fi
}

echo "Network Scanning:"
check_tool nmap
check_tool masscan
check_tool netdiscover

echo ""
echo "Web Testing:"
check_tool nikto
check_tool sqlmap
check_tool gobuster

echo ""
echo "Password Cracking:"
check_tool john
check_tool hashcat
check_tool hydra

echo ""
echo "Exploitation:"
check_tool msfconsole
check_tool searchsploit

echo ""
echo "Wireless:"
check_tool aircrack-ng

echo ""
echo "Packet Analysis:"
check_tool wireshark
check_tool tshark
check_tool ettercap

echo ""
echo "Forensics:"
check_tool volatility
check_tool binwalk
check_tool foremost
VERIFY

chmod +x /usr/local/bin/verify-kali-tools

echo -e "${YELLOW}📝 NEXT STEPS:${NC}"
echo ""
echo -e "1. Verify installation:"
echo -e "   ${GREEN}verify-kali-tools${NC}"
echo ""
echo -e "2. Test a tool:"
echo -e "   ${GREEN}nmap --version${NC}"
echo -e "   ${GREEN}which burpsuite${NC}"
echo ""
echo -e "3. Use with Agent Zero:"
echo -e "   ${GREEN}Agent Zero can now use all installed tools!${NC}"
echo ""
echo -e "${BLUE}All tools ready for use! 🎉${NC}"
echo ""
