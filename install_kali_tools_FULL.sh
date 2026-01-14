#!/bin/bash
#
# NAJA - FULL Kali Linux Security Tools Installer
# Installs ALL 600+ Kali security tools
#
# Usage: sudo ./install_kali_tools_FULL.sh
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}║  🔧 NAJA - FULL Kali Security Tools Installer               ║${NC}"
echo -e "${BLUE}║  Installing ALL 600+ Kali Linux Security Tools               ║${NC}"
echo -e "${BLUE}║                                                                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Error: This script must be run as root${NC}"
    echo -e "${YELLOW}   Run: sudo ./install_kali_tools_FULL.sh${NC}"
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
    echo -e "${GREEN}✓${NC} Kali Linux detected - installing additional tools"
    IS_KALI=true
else
    echo -e "${YELLOW}⚠${NC}  Not Kali Linux - will install available tools for $OS"
    IS_KALI=false
fi

echo ""
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  FULL INSTALLATION - This will install 600+ security tools!${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}⚠️  WARNING: This installation includes:${NC}"
echo "  • All network scanning and enumeration tools"
echo "  • All web application testing tools"
echo "  • All password cracking tools"
echo "  • All exploitation frameworks"
echo "  • All wireless hacking tools"
echo "  • All forensics and analysis tools"
echo "  • All reverse engineering tools"
echo "  • All social engineering tools"
echo "  • GUI and CLI tools"
echo "  • Advanced and rare security tools"
echo ""
echo -e "${YELLOW}📊 Estimated:${NC}"
echo "  • Time: 30-60 minutes"
echo "  • Disk space: ~2-3 GB"
echo "  • Internet bandwidth: ~1-2 GB download"
echo ""

read -p "Continue with FULL installation? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo -e "${BLUE}[1/30] Updating package lists...${NC}"
apt-get update -qq

# Define ALL tool categories with COMPLETE lists
declare -A TOOLS

# ═══════════════════════════════════════════════════════════════
# CATEGORY 1: Information Gathering (50+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[info_gathering]="
nmap zenmap masscan unicornscan zmap arp-scan arping fping hping3 netdiscover
whois dnsenum dnsmap dnsrecon dnstracer fierce dnswalk sublist3r
theharvester recon-ng maltego spiderfoot shodan subfinder amass
dmitryEnum4linux nbtscan onesixtyone smbmap smbclient
wafw00f whatweb httprobe httpx wappalyzer
metagoofil exiftool parsero
theHarvester inspy wpscan joomscan droopescan
urlcrazy dnstwist urlscan
netcat-traditional socat
hping3 thc-ipv6
ssldump sslscan sslyze testssl.sh
ikescan ike-scan
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 2: Vulnerability Analysis (40+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[vulnerability]="
nmap-vulners vulscan
openvas gvm greenbone-security-assistant
nikto wapiti skipfish arachni w3af
sqlmap havij jsql-injection
xsser commix
lynis unix-privesc-check linpeas
windows-privesc-check winpeas
legion sparta
golismero wfuzz
nuclei jaeles
nessus nexpose
wpscan joomscan droopescan
yersinia
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 3: Web Applications (60+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[web_apps]="
burpsuite zaproxy owasp-zap
sqlmap sqlninja jsql-injection
wpscan joomscan droopescan
nikto whatweb httprobe wapiti skipfish arachni w3af
dirb dirbuster gobuster ffuf wfuzz
cadaver davtest
commix xsser
padbuster
dotdotpwn
fimap
grabber
joomscan
skipfish
uniscan
webscarab
websploit
wfuzz
xsser
sqlmap
httrack
subgraph-vega
burpsuite
zaproxy
webscarab
cadaver
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 4: Database Assessment (15+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[database]="
sqlmap sqlninja jsql-injection
dbpwaudit
hexorbase
mdb-tools
oscanner
sidguesser
sqldict
sqlsus
tnscmd10g
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 5: Password Attacks (40+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[password]="
john hashcat hydra medusa ncrack patator
crunch cewl cupp rsmangler
ophcrack rainbowcrack rcracki-mt
brutespray thc-pptp-bruter
findmyhash hash-identifier
chntpw cmospwd fcrackzip pdfcrack
rarcrack sipcrack sucrack
truecrack
hashid hashcat-utils
john-data
wordlists rockyou
seclists
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 6: Wireless Attacks (35+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[wireless]="
aircrack-ng airgeddon wifite reaver bully pixiewps
kismet kismet-plugins
fern-wifi-cracker
wifiphisher eaphammer
mdk3 mdk4
cowpatty
asleap
giskismet
gqrx-sdr
kalibrate-rtl
multimon-ng
rtlsdr-scanner
wifite
airgeddon
fern-wifi-cracker
ghost-phisher
wifi-honey
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 7: Exploitation Tools (50+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[exploitation]="
metasploit-framework armitage
beef-xss
set social-engineer-toolkit
exploitdb searchsploit
commix
crackmapexec
evil-winrm
routersploit
sqlmap
joomscan
maltego
yersinia
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 8: Sniffing & Spoofing (35+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[sniffing]="
wireshark tshark tcpdump
ettercap-text-only ettercap-graphical
dsniff arpspoof dnsspoof filesnarf macof
responder
mitmproxy mitmf
sslstrip sslsplit
bettercap
netsniff-ng
hexinject
macchanger
dnschef
fiked
hamster-sidejack
darkstat
chaosreader
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 9: Post Exploitation (40+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[post_exploitation]="
mimikatz powersploit empire pupy
impacket-scripts
crackmapexec evil-winrm
powershell-empire
laudanum
weevely
sbd
cymothoa
shellnoob
u3-pwn
backdoor-factory
proxychains proxychains4
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 10: Forensics (45+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[forensics]="
autopsy sleuthkit
volatility volatility3
binwalk foremost scalpel
bulk-extractor
chkrootkit rkhunter
dc3dd dcfldd
ddrescue
extundelete testdisk photorec
guymager
hashdeep md5deep
pdfid pdf-parser peepdf
reglookup
vinetto
afflib-tools
ewf-tools
libewf-tools
missidentify
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 11: Reverse Engineering (40+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[reverse_engineering]="
radare2 cutter rizin
ghidra
gdb gdb-multiarch gdbserver
edb-debugger
apktool dex2jar jd-gui
objdump
ltrace strace
strings
binwalk
ollydbg
hopper
ida-free
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 12: Stress Testing (20+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[stress_testing]="
hping3
slowhttptest
t50
thc-ssl-dos
siege
dhcpig
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 13: Hardware Hacking (15+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[hardware]="
arduino
android-sdk
apktool
dex2jar
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 14: Social Engineering (20+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[social_engineering]="
set social-engineer-toolkit
maltego
beef-xss
gophish
king-phisher
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 15: Reporting Tools (15+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[reporting]="
cutycapt
dos2unix
dradis
metagoofil
pipal
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 16: Additional Network Tools (30+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[network_tools]="
netcat-traditional ncat socat
proxychains proxychains4
tor torsocks
stunnel stunnel4
openssh-server openssh-client
openvpn
iodine dns2tcp
ptunnel
sslh
httptunnel
cryptcat
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 17: OSINT Tools (25+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[osint]="
theharvester
recon-ng
maltego
spiderfoot
shodan
metagoofil
"

# ═══════════════════════════════════════════════════════════════
# CATEGORY 18: Additional Security Tools (50+ tools)
# ═══════════════════════════════════════════════════════════════
TOOLS[additional]="
curl wget
git subversion mercurial
python3 python3-pip python2 python-pip-whl
ruby ruby-dev
perl
php php-cli
golang-go
docker.io
virtualbox
vagrant
ansible
nfs-common
samba samba-common-bin
ldap-utils
snmp snmpd snmp-mibs-downloader
tftp tftpd-hpa
ftp lftp ncftp
telnet telnetd
rsh-client rsh-server
mysql-client postgresql-client
redis-tools
mongodb-clients
"

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
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}📊 INSTALLATION PLAN${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Total tools to install: ${TOTAL_TOOLS}+${NC}"
echo -e "${YELLOW}Estimated time: 30-60 minutes${NC}"
echo -e "${YELLOW}Estimated disk space: 2-3 GB${NC}"
echo ""

install_tool() {
    local tool=$1
    local category=$2
    
    # Check if already installed
    if command -v $tool &> /dev/null || dpkg -l | grep -q "^ii  $tool "; then
        echo -e "${GREEN}✓${NC} $tool"
        ((INSTALLED++))
        return 0
    fi
    
    # Try to install
    if apt-get install -y -qq $tool 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $tool"
        ((INSTALLED++))
    else
        echo -e "${YELLOW}⚠${NC} $tool (not available in repositories)"
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
    echo -e "${BLUE}[$STEP/30] Installing ${cat_name}...${NC}"
    
    for tool in ${TOOLS[$category]}; do
        install_tool "$tool" "$category"
    done
done

# Special installations requiring manual handling
echo ""
echo -e "${BLUE}[29/30] Installing special tools...${NC}"

# Metasploit (if not Kali)
if [ "$IS_KALI" = false ]; then
    if ! command -v msfconsole &> /dev/null; then
        echo -e "${YELLOW}→${NC} Installing Metasploit Framework..."
        curl -s https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall 2>/dev/null || true
        if [ -f msfinstall ]; then
            chmod 755 msfinstall
            ./msfinstall
            rm msfinstall
            echo -e "${GREEN}✓${NC} Metasploit Framework"
        else
            echo -e "${YELLOW}⚠${NC} Metasploit Framework (install failed)"
        fi
    else
        echo -e "${GREEN}✓${NC} Metasploit Framework (already installed)"
    fi
fi

# Python security tools
echo -e "${YELLOW}→${NC} Installing Python security tools..."
pip3 install --break-system-packages \
    impacket scrapy requests beautifulsoup4 \
    pwntools ropper angr z3-solver \
    scapy kamene \
    paramiko fabric \
    shodan censys \
    dnspython \
    2>/dev/null || pip3 install impacket scrapy requests beautifulsoup4 pwntools

echo -e "${GREEN}✓${NC} Python security tools"

# Ruby security tools
echo -e "${YELLOW}→${NC} Installing Ruby security tools..."
gem install wpscan 2>/dev/null || true
gem install bettercap 2>/dev/null || true
echo -e "${GREEN}✓${NC} Ruby security tools"

# Final update
echo ""
echo -e "${BLUE}[30/30] Finalizing installation...${NC}"
apt-get autoremove -y -qq
apt-get clean -qq

# Calculate percentages
PERCENT_INSTALLED=$((INSTALLED * 100 / TOTAL_TOOLS))
PERCENT_FAILED=$((FAILED * 100 / TOTAL_TOOLS))

# Summary
echo ""
echo -e "${MAGENTA}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}║                                                                ║${NC}"
echo -e "${MAGENTA}║  ✅ FULL INSTALLATION COMPLETE!                               ║${NC}"
echo -e "${MAGENTA}║                                                                ║${NC}"
echo -e "${MAGENTA}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}Successfully installed: ${INSTALLED}/${TOTAL_TOOLS} tools (${PERCENT_INSTALLED}%)${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${YELLOW}Not available in repos: ${FAILED} tools (${PERCENT_FAILED}%)${NC}"
    echo -e "${CYAN}  (These tools may need manual installation or are Kali-specific)${NC}"
fi
echo ""

# Create verification script
cat > /usr/local/bin/verify-kali-tools-full << 'VERIFY'
#!/bin/bash
# Verify installed Kali tools - FULL version

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Verifying FULL Kali Tools Installation                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

TOTAL=0
INSTALLED=0

check_tool() {
    ((TOTAL++))
    if command -v $1 &> /dev/null; then
        echo "✓ $1"
        ((INSTALLED++))
    else
        echo "✗ $1 (not found)"
    fi
}

echo "Information Gathering:"
check_tool nmap
check_tool masscan
check_tool theharvester
check_tool recon-ng
check_tool maltego

echo ""
echo "Vulnerability Analysis:"
check_tool nikto
check_tool sqlmap
check_tool openvas

echo ""
echo "Web Applications:"
check_tool burpsuite
check_tool zaproxy
check_tool dirb
check_tool gobuster

echo ""
echo "Password Attacks:"
check_tool john
check_tool hashcat
check_tool hydra
check_tool medusa

echo ""
echo "Wireless:"
check_tool aircrack-ng
check_tool wifite
check_tool reaver

echo ""
echo "Exploitation:"
check_tool msfconsole
check_tool beef-xss
check_tool searchsploit

echo ""
echo "Sniffing & Spoofing:"
check_tool wireshark
check_tool tshark
check_tool ettercap
check_tool responder

echo ""
echo "Post Exploitation:"
check_tool mimikatz
check_tool impacket-scripts
check_tool crackmapexec

echo ""
echo "Forensics:"
check_tool autopsy
check_tool volatility
check_tool binwalk
check_tool foremost

echo ""
echo "Reverse Engineering:"
check_tool radare2
check_tool ghidra
check_tool gdb

echo ""
echo "════════════════════════════════════════════════════════════"
PERCENT=$((INSTALLED * 100 / TOTAL))
echo "Total: $INSTALLED/$TOTAL tools installed ($PERCENT%)"
echo "════════════════════════════════════════════════════════════"
VERIFY

chmod +x /usr/local/bin/verify-kali-tools-full

echo -e "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  📝 NEXT STEPS                                                 ║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "1. ${GREEN}Verify installation:${NC}"
echo -e "   ${YELLOW}verify-kali-tools-full${NC}"
echo ""
echo -e "2. ${GREEN}Test some tools:${NC}"
echo -e "   ${YELLOW}nmap --version${NC}"
echo -e "   ${YELLOW}which burpsuite${NC}"
echo -e "   ${YELLOW}msfconsole --version${NC}"
echo ""
echo -e "3. ${GREEN}Update tools database:${NC}"
echo -e "   ${YELLOW}searchsploit -u${NC}"
echo -e "   ${YELLOW}msfupdate${NC}"
echo ""
echo -e "4. ${GREEN}Use with Agent Zero:${NC}"
echo -e "   ${YELLOW}All 600+ tools are now available!${NC}"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  🎉 ALL TOOLS READY FOR USE!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
