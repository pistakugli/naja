# Kali Linux Security Tools - Installation Guide

NAJA provides two installation options for Kali Linux security tools:

## 📦 Two Installers Available

### 1. **install_kali_tools.sh** - Essential Tools (RECOMMENDED)
- **Tools:** 100+ most popular security tools
- **Time:** 10-20 minutes
- **Disk:** ~1 GB
- **Best for:** Quick setup, production use, most common scenarios

### 2. **install_kali_tools_FULL.sh** - Complete Suite
- **Tools:** 600+ ALL Kali security tools
- **Time:** 30-60 minutes
- **Disk:** ~2-3 GB
- **Best for:** Comprehensive setup, research, full coverage

---

## 🚀 Quick Start

### Essential Installation (Recommended)
```bash
sudo chmod +x install_kali_tools.sh
sudo ./install_kali_tools.sh
```

### Full Installation
```bash
sudo chmod +x install_kali_tools_FULL.sh
sudo ./install_kali_tools_FULL.sh
```

---

## 📊 What's Included

### Essential Tools (100+)

**Network Scanning:**
- nmap, masscan, netdiscover, hping3, unicornscan, zmap

**Web Testing:**
- nikto, sqlmap, wpscan, dirb, gobuster, ffuf, wfuzz

**Password Cracking:**
- john, hashcat, hydra, medusa, ncrack, crunch

**Exploitation:**
- metasploit-framework, beef-xss, searchsploit

**Wireless:**
- aircrack-ng, reaver, bully, wifite

**Packet Analysis:**
- wireshark, tshark, tcpdump, ettercap

**Forensics:**
- volatility, binwalk, foremost, autopsy

### Full Tools (600+)

Everything from Essential PLUS:

**Advanced Tools:**
- All GUI security tools
- Rare vulnerability scanners
- Specialized forensics tools
- Hardware hacking tools
- Advanced exploitation frameworks
- Complete reverse engineering suite
- All OSINT tools
- Social engineering frameworks

---

## 🎯 Which One Should You Choose?

### Choose **Essential** if:
- ✅ You want quick setup
- ✅ You cover 95% of security testing scenarios
- ✅ You want terminal-friendly tools
- ✅ You're on limited disk space
- ✅ You're deploying to production

### Choose **Full** if:
- ✅ You want EVERYTHING
- ✅ You do comprehensive security research
- ✅ You need rare/specialized tools
- ✅ You want GUI tools included
- ✅ You have 3GB disk space available

---

## 🔧 Auto-Install Feature

**Both installers are complemented by auto-install!**

Agent Zero can automatically install ANY missing tool on-demand:

```python
# Agent Zero detects tool is missing
# Automatically runs: sudo apt-get install <tool>
# Installs and executes seamlessly
```

**This means:**
- Essential installer + auto-install = Full coverage!
- Install only what you need, when you need it
- Best of both worlds

---

## ✅ Verification

After installation, verify your tools:

**Essential:**
```bash
verify-kali-tools
```

**Full:**
```bash
verify-kali-tools-full
```

---

## 📝 Platform Support

### Kali Linux
- Most tools pre-installed
- Installers add missing tools
- Full compatibility

### Ubuntu / Debian
- Installers work perfectly
- Most tools available in repos
- Some Kali-specific tools may not be available

### Other Linux
- Partial compatibility
- Tools available in repos will install
- Manual installation may be needed for some

---

## 🔐 Security Warning

**These are PENETRATION TESTING tools!**

⚠️ **Only use on systems you own or have explicit permission to test**

❌ Unauthorized use is ILLEGAL
❌ Testing on others' systems = CRIME
✅ Use for authorized security testing only
✅ Perfect for lab environments

---

## 🛠 Integration with Agent Zero

Once installed, all tools are accessible to Agent Zero:

```python
# Network scanning
tool: "kali_security"
args: {"tool": "nmap", "args": ["-sS", "target.com"]}

# Web testing
tool: "kali_security"
args: {"tool": "nikto", "args": ["-h", "target.com"]}

# Password cracking
tool: "kali_security"
args: {"tool": "john", "args": ["hashes.txt"]}

# ANY tool from Essential or Full installation!
```

---

## 📚 Tool Categories

Both installers organize tools by category:

1. **Information Gathering** - OSINT, enumeration, reconnaissance
2. **Vulnerability Analysis** - Scanners, analyzers
3. **Web Applications** - Web testing, SQL injection, XSS
4. **Database Assessment** - DB security testing
5. **Password Attacks** - Cracking, brute force
6. **Wireless Attacks** - WiFi hacking
7. **Exploitation** - Frameworks, exploits
8. **Sniffing & Spoofing** - Network analysis
9. **Post Exploitation** - Privilege escalation
10. **Forensics** - Analysis, recovery
11. **Reverse Engineering** - Disassembly, debugging
12. **Stress Testing** - DoS, load testing
13. **Hardware Hacking** - Physical security
14. **Social Engineering** - Phishing, SET
15. **Reporting** - Documentation tools
16. **Network Tools** - Tunneling, proxying
17. **OSINT** - Intelligence gathering
18. **Additional** - Utilities, languages

---

## 💡 Tips

**Update tool databases:**
```bash
# Update Metasploit
msfupdate

# Update Exploit Database
searchsploit -u

# Update system
sudo apt-get update && sudo apt-get upgrade
```

**Save disk space:**
- Use Essential installer
- Enable auto-install for rare tools
- Clean up: `sudo apt-get autoremove`

**Speed up installation:**
- Use fast internet connection
- Run during off-peak hours
- Consider local package mirror

---

## 📖 More Information

**GitHub:** https://github.com/pistakugli/naja

**Documentation:**
- Agent Zero integration guide
- Tool usage examples
- Security best practices

**Support:**
- Report issues on GitHub
- Check documentation
- Review tool-specific help: `<tool> --help`

---

## 🎉 Ready to Go!

After installation:
1. Verify tools are installed
2. Test a few commands
3. Start using Agent Zero with full Kali arsenal!

**Happy (ethical) hacking! 🔐**
