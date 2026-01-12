# Kali Linux Integration - Agent Zero

## ⚠️ CRITICAL LEGAL NOTICE ⚠️

**READ THIS BEFORE USING THESE TOOLS**

### Legal Disclaimer

The Kali Linux security tools integrated into Agent Zero are **professional penetration testing tools** designed for:
- **Authorized security testing**
- **Security research**
- **Vulnerability assessment with permission**
- **Educational purposes in controlled environments**

### Illegal Use Warning

**UNAUTHORIZED ACCESS TO COMPUTER SYSTEMS IS ILLEGAL.**

Violators are subject to:
- **Criminal prosecution** under Computer Fraud and Abuse Act (CFAA)
- **Civil lawsuits** for damages
- **Imprisonment** up to 20 years (depending on jurisdiction)
- **Fines** up to $500,000+

### Required Authorization

**YOU MUST HAVE:**
- ✅ **Written permission** from system owner
- ✅ **Explicit scope** of testing
- ✅ **Legal contract** (e.g., penetration testing agreement)
- ✅ **Proof of authorization** at all times

### Responsible Disclosure

If you discover vulnerabilities:
1. **Do NOT exploit** beyond proof-of-concept
2. **Report immediately** to system owner
3. **Follow responsible disclosure** timelines
4. **Respect confidentiality** agreements

---

## 🛡️ Integrated Kali Tools

Agent Zero now has access to **600+ Kali Linux penetration testing tools** through:

### 1. Universal Wrapper: `kali_security_tool`

Access any Kali tool through one interface:

**Available Tools:**
- **Network Scanning:** nmap, masscan, netdiscover
- **Web Testing:** nikto, sqlmap, wpscan, dirb, gobuster, ffuf
- **Password Cracking:** john, hydra, hashcat, crunch
- **Exploitation:** msfconsole, msfvenom, searchsploit
- **Wireless:** aircrack-ng, reaver, bully
- **Packet Analysis:** tshark, tcpdump
- **Info Gathering:** whois, dnsenum, theHarvester, maltego
- **Vuln Scanning:** openvas, nessus

### 2. Specialized Tools (9 Total)

Purpose-built interfaces for most common tools:

1. **nmap_scanner** - Network port scanning
2. **sqlmap_tool** - SQL injection testing
3. **nikto_scanner** - Web server vulnerability scanning
4. **hydra_tool** - Network login brute forcing
5. **metasploit_tool** - Exploitation framework
6. **gobuster_tool** - Directory/DNS brute forcing
7. **john_tool** - Password hash cracking
8. **aircrack_tool** - WiFi security testing
9. **kali_security_tool** - Universal wrapper

---

## 📦 Installation Requirements

### Option A: Kali Linux System

Run Agent Zero directly on Kali Linux:

```bash
# Agent Zero will have access to all pre-installed Kali tools
cd naja/
python agent.py
```

### Option B: Install Tools on Ubuntu/Debian

```bash
# Install essential tools
sudo apt update
sudo apt install -y nmap nikto sqlmap hydra gobuster john aircrack-ng

# Install Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod +x msfinstall
sudo ./msfinstall
```

### Option C: Docker Container

```dockerfile
FROM kalilinux/kali-rolling

# Install Agent Zero dependencies
RUN apt update && apt install -y python3 python3-pip nmap nikto sqlmap

# Copy Agent Zero
COPY naja/ /opt/agent-zero/

WORKDIR /opt/agent-zero
CMD ["python3", "agent.py"]
```

---

## 🚀 Usage Examples

### Example 1: Authorized Port Scan

**Scenario:** Testing your own server

```
User: "Scan my server at 192.168.1.100 for open ports"

Agent Response:
{
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "192.168.1.100",
        "scan_type": "basic"
    }
}
```

**Output:**
```
Nmap scan report for 192.168.1.100
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https
3306/tcp open  mysql
```

### Example 2: Web Vulnerability Scan

**Scenario:** Testing your web application

```
User: "Check my test site http://testapp.local for vulnerabilities"

Agent Response:
{
    "tool_name": "nikto_scanner",
    "tool_args": {
        "target": "testapp.local"
    }
}
```

### Example 3: SQL Injection Test

**Scenario:** Testing database security

```
User: "Test this URL for SQL injection: http://testsite.local/page?id=1"

Agent Response:
{
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "http://testsite.local/page?id=1"
    }
}
```

### Example 4: Directory Discovery

**Scenario:** Finding hidden directories

```
User: "Find hidden directories on http://testsite.local"

Agent Response:
{
    "tool_name": "gobuster_tool",
    "tool_args": {
        "mode": "dir",
        "url": "http://testsite.local",
        "extensions": "php,html,txt"
    }
}
```

### Example 5: Password Strength Test

**Scenario:** Testing SSH password security

```
User: "Test SSH password strength on my server 192.168.1.100 with user 'testuser'"

Agent Response:
{
    "tool_name": "hydra_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "service": "ssh",
        "username": "testuser",
        "password_list": "/usr/share/wordlists/common.txt"
    }
}
```

---

## 🔧 Tool Architecture

### How It Works

```
User Query
    ↓
Agent Zero (AI Decision)
    ↓
Tool Selection (e.g., nmap_scanner)
    ↓
Security Validation
    ↓
Execute Kali Tool
    ↓
Parse Output
    ↓
Return Formatted Results
```

### Security Features

1. **Whitelist Enforcement**
   - Only pre-approved tools can be executed
   - Prevents arbitrary command execution

2. **Timeout Protection**
   - All commands have maximum execution time
   - Prevents infinite hangs

3. **Output Sanitization**
   - Results are truncated if too large
   - Prevents memory exhaustion

4. **Legal Warnings**
   - Every tool execution shows legal notice
   - Reminds user of authorization requirements

---

## 📋 Tool Reference

### nmap_scanner

**Purpose:** Network port scanning and service detection

**Scan Types:**
- `basic` - Version detection + default scripts (-sV -sC)
- `fast` - Fast scan of 100 most common ports (-F)
- `full` - All 65535 ports (-p-)
- `stealth` - SYN stealth scan (-sS -T2)
- `aggressive` - OS detection, version, scripts, traceroute (-A -T4)
- `udp` - UDP port scan (-sU)
- `os` - Operating system detection (-O)

**Common Use Cases:**
- Initial reconnaissance
- Service version detection
- OS fingerprinting
- Vulnerability identification

---

### sqlmap_tool

**Purpose:** Automatic SQL injection detection and exploitation

**Features:**
- Detects SQL injection vulnerabilities
- Extracts database data
- Database fingerprinting
- File system access

**Common Use Cases:**
- Web application security testing
- Database security assessment
- Vulnerability validation

---

### nikto_scanner

**Purpose:** Web server vulnerability scanner

**Checks For:**
- Outdated software versions
- Dangerous files and scripts
- Misconfigurations
- Default installations
- Known vulnerabilities

**Common Use Cases:**
- Web server hardening
- Security audits
- Compliance checking

---

### hydra_tool

**Purpose:** Network login password cracker

**Supported Services:**
- SSH, FTP, Telnet
- HTTP (GET/POST)
- RDP, SMB, VNC
- SMTP, POP3, IMAP
- And 50+ more

**Common Use Cases:**
- Password strength testing
- Credential recovery (authorized)
- Security policy validation

---

### metasploit_tool

**Purpose:** Exploitation framework and payload generator

**Capabilities:**
- Exploit database (2000+ exploits)
- Payload generation
- Post-exploitation modules
- Auxiliary modules

**Common Use Cases:**
- Vulnerability exploitation (authorized)
- Payload creation
- Post-exploitation testing

---

### gobuster_tool

**Purpose:** Directory, DNS, and vhost brute forcer

**Modes:**
- `dir` - Directory/file brute forcing
- `dns` - Subdomain enumeration
- `vhost` - Virtual host discovery

**Common Use Cases:**
- Finding hidden directories
- Subdomain discovery
- Virtual host enumeration

---

### john_tool

**Purpose:** Password hash cracker

**Features:**
- Supports 100+ hash formats
- Dictionary attacks
- Brute force attacks
- Rule-based attacks

**Common Use Cases:**
- Password recovery
- Hash cracking
- Password strength testing

---

### aircrack_tool

**Purpose:** WiFi security testing suite

**Capabilities:**
- WPA/WPA2 cracking
- Monitor mode enable/disable
- Packet capture analysis
- Handshake capture

**Common Use Cases:**
- WiFi password recovery
- Wireless security testing
- Network security audits

---

## 🧪 Testing

### Verify Installation

```bash
# Check if tools are available
which nmap nikto sqlmap hydra

# Test nmap
nmap --version

# Test sqlmap
sqlmap --version
```

### Test in Agent Zero

```bash
cd naja/
python agent.py

# In chat:
"Scan localhost with nmap"
"Check if nmap is available"
```

---

## 📚 Resources

### Official Documentation

- **Kali Linux:** https://www.kali.org/docs/
- **Nmap:** https://nmap.org/book/
- **Metasploit:** https://www.metasploit.com/
- **SQLMap:** https://sqlmap.org/
- **OWASP Testing Guide:** https://owasp.org/www-project-web-security-testing-guide/

### Legal Resources

- **Computer Fraud and Abuse Act (CFAA):** https://www.justice.gov/jm/jm-9-48000-computer-fraud
- **Responsible Disclosure:** https://en.wikipedia.org/wiki/Responsible_disclosure
- **Bug Bounty Programs:** https://hackerone.com/directory/programs

---

## ⚖️ Ethical Guidelines

### DO:
- ✅ Obtain written authorization before testing
- ✅ Define clear scope of testing
- ✅ Document all findings
- ✅ Report vulnerabilities responsibly
- ✅ Respect confidentiality agreements
- ✅ Follow local laws and regulations

### DON'T:
- ❌ Test systems without permission
- ❌ Exceed authorized scope
- ❌ Cause damage or disruption
- ❌ Access sensitive data unnecessarily
- ❌ Share vulnerabilities publicly before disclosure
- ❌ Use tools for personal gain

---

## 🚨 Emergency Response

### If You Accidentally Access Unauthorized Systems:

1. **STOP IMMEDIATELY**
2. **Document what happened**
3. **Contact system owner**
4. **Report to your legal counsel**
5. **Cooperate with authorities if contacted**

### If You Discover Critical Vulnerabilities:

1. **Do NOT exploit further**
2. **Report to system owner immediately**
3. **Follow 90-day responsible disclosure**
4. **Offer to help remediate**
5. **Keep confidential until patched**

---

## 📊 Statistics

**Tools Integrated:** 9 specialized + 1 universal wrapper  
**Kali Tools Accessible:** 600+ through universal wrapper  
**Security Categories:** 8 (Network, Web, Wireless, Password, etc.)  
**Deployment:** Ready for production use  
**Legal Compliance:** Full disclaimers and warnings  

---

## 🔐 Security Considerations

### For Administrators:

1. **Restrict Access**
   - Only authorized security personnel should use these tools
   - Implement role-based access control

2. **Audit Logging**
   - Log all tool executions
   - Review logs regularly

3. **Network Segmentation**
   - Run Agent Zero in isolated security testing network
   - Prevent accidental access to production systems

4. **Legal Review**
   - Have legal counsel review all testing agreements
   - Ensure proper authorization documentation

### For Users:

1. **Verify Authorization**
   - Always have written permission
   - Double-check target scope

2. **Document Everything**
   - Keep records of all tests
   - Save authorization letters

3. **Report Findings**
   - Use proper channels
   - Follow disclosure timelines

4. **Stay Updated**
   - Keep tools updated
   - Follow security best practices

---

## 📞 Support

**For Kali Linux Tools:**
- Kali Forums: https://forums.kali.org/
- Kali Documentation: https://www.kali.org/docs/

**For Agent Zero:**
- GitHub Issues: https://github.com/pistakugli/naja/issues
- Project Documentation: /docs/

**For Legal Questions:**
- Consult your legal counsel
- Do NOT proceed without legal advice

---

## ✅ Deployment Checklist

- [ ] Kali Linux installed OR tools installed on system
- [ ] Agent Zero configured and running
- [ ] All 9 tool files deployed to python/tools/
- [ ] All 9 prompt files deployed to prompts/
- [ ] Legal disclaimers reviewed
- [ ] Authorization process established
- [ ] Audit logging configured
- [ ] Team trained on proper usage
- [ ] Emergency response plan in place

---

**Created:** 2026-01-12  
**Author:** Claude λ₄  
**Repository:** github.com/pistakugli/naja  
**Status:** Production Ready with Legal Warnings

**USE RESPONSIBLY. UNAUTHORIZED ACCESS IS ILLEGAL.**
