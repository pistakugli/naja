# 🐍 NAJA - Kali Linux Integration

**40+ Professional Penetration Testing Tools** integrated into Agent Zero framework.

## 🎯 What is NAJA?

NAJA is an autonomous AI penetration testing framework - a fork of Agent Zero enhanced with comprehensive Kali Linux toolkit integration.

**Key Features:**
- 🤖 **Autonomous Pentesting** - AI selects and chains tools automatically
- 🛠️ **40+ Kali Tools** - Professional security toolkit
- 📝 **Full Documentation** - Every tool documented with examples
- 🔒 **Security First** - Legal warnings and authorization checks
- 📊 **Auto Reporting** - Generate professional pentest reports

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/pistakugli/naja.git
cd naja

# Run with Docker (recommended)
docker build -t naja .
docker run -it naja

# Or install locally
pip install -r requirements.txt
python run_ui.py
```

**First Command:**
```
User: "Scan target.com for vulnerabilities"

NAJA automatically:
1. Uses nmap for port scanning
2. Runs nikto for web vulnerabilities
3. Tests for SQL injection
4. Generates comprehensive report
```

## 📚 Documentation

- **[Quick Start Guide](docs/QUICKSTART.md)** - Get running in 5 minutes
- **[Kali Tools Guide](docs/KALI_TOOLS_GUIDE.md)** - Complete tool documentation
- **[Tool Reference](docs/TOOL_REFERENCE.md)** - All 40 tools listed

## 🛠️ Available Tools

### 🌐 Web Application Testing (9 tools)
- `nmap_scanner` - Port scanning & service detection
- `nikto_scanner` - Web vulnerability scanner
- `sqlmap_tool` - SQL injection testing
- `ffuf_tool` - Fast web fuzzer
- `wpscan_tool` - WordPress security scanner
- `dirb_tool`, `wfuzz_tool`, `commix_tool`, `zaproxy_tool`, `xsstrike_tool`

### 🔐 Password & Brute Force (6 tools)
- `john_tool` - Password hash cracker
- `hydra_tool` - Network service brute forcer
- `hashcat_tool` - GPU-accelerated cracking
- `medusa_tool`, `crunch_tool`, `cewl_tool`

### 💥 Exploitation (3 tools)
- `metasploit_tool` - Exploitation framework
- `msfvenom_tool` - Payload generator
- `searchsploit_tool` - Exploit database

### 🔍 OSINT & Recon (6 tools)
- `theharvester_tool` - Email/subdomain OSINT
- `amass_tool` - Attack surface mapping
- `sublist3r_tool`, `dnsenum_tool`, `fierce_tool`, `reconng_tool`

### 📡 Network Analysis (7 tools)
- `masscan_tool` - Ultra-fast port scanner
- `rustscan_tool` - Modern fast scanner
- `tshark_tool` - Packet analysis
- `tcpdump_tool`, `ettercap_tool`, `responder_tool`

### 📶 Wireless (3 tools)
- `aircrack_tool` - WiFi security testing
- `wifite_tool` - Automated WiFi auditing
- `kismet_tool` - Wireless detector

### 🔬 Forensics (3 tools)
- `volatility_tool` - Memory forensics
- `binwalk_tool` - Firmware analysis
- `foremost_tool` - File carving

### 🎭 Social Engineering (1 tool)
- `setoolkit_tool` - Social Engineering Toolkit

### 🔧 Universal Access
- `kali_security_tool` - Wrapper for 600+ additional Kali tools

**Total: 40 specialized tools + universal wrapper**

## 💻 Usage Examples

### Example 1: Web Application Assessment
```
User: "Perform security assessment of app.target.com"

NAJA will:
1. Scan for open ports (nmap)
2. Identify web server (nmap -sV)
3. Check for vulnerabilities (nikto)
4. Test for SQL injection (sqlmap)
5. Fuzz for hidden files (ffuf)
6. Generate detailed report
```

### Example 2: Network Penetration Test
```
User: "Test security of internal network 10.0.0.0/24"

NAJA will:
1. Fast port discovery (masscan)
2. Detailed service enumeration (nmap)
3. Search for exploits (searchsploit)
4. Test weak passwords (hydra)
5. Document all findings
```

### Example 3: OSINT Gathering
```
User: "Gather intelligence on company.com"

NAJA will:
1. Find subdomains (amass, sublist3r)
2. Collect emails (theHarvester)
3. Enumerate DNS (dnsenum)
4. Map attack surface
5. Generate intelligence report
```

## 🔒 Security & Legal

⚠️ **IMPORTANT:**
- Only test systems you OWN or have WRITTEN authorization to test
- Unauthorized penetration testing is ILLEGAL
- Follow responsible disclosure practices
- Comply with all applicable laws

## 📖 How It Works

NAJA uses **prompt engineering** to teach Agent Zero how to use each tool:

1. **Tool Prompts** - Each tool has a detailed prompt in `/prompts/`
2. **AI Selection** - Agent Zero reads prompts and selects appropriate tools
3. **Automatic Chaining** - Tools are chained together for complex tasks
4. **Smart Parameters** - AI determines optimal tool parameters
5. **Result Integration** - All results synthesized into reports

### Example Tool Prompt Format:
```markdown
### tool_name:
Description and use cases

⚠️ Security warnings

#### Arguments:
 *  "arg1" (type) : Description
 *  "arg2" (Optional, type) : Description

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Why I'm using this tool"],
    "tool_name": "tool_name",
    "tool_args": {"arg1": "value"}
}
\`\`\`
```

## 🏗️ Architecture

```
NAJA
├── Agent Zero Core (AI framework)
├── Kali Tools Integration (40+ tools)
├── Tool Prompts (detailed documentation)
├── Autonomous Selection (AI chooses tools)
└── Report Generation (professional output)
```

## 🔧 Configuration

Edit `conf/config.yaml`:
```yaml
tools:
  nmap:
    default_speed: 4
  sqlmap:
    default_level: 2
    default_risk: 2
```

## 🤝 Contributing

Contributions welcome! To add a tool:

1. Create `/prompts/agent.system.tool.TOOLNAME.md`
2. Follow existing format
3. Include usage examples
4. Add security warnings
5. Submit PR

## 📝 License

NAJA is for **authorized security testing only**. See [LICENSE](LICENSE).

## 🌟 Credits

- **Agent Zero** - Base framework by [frdel](https://github.com/frdel/agent-zero)
- **NAJA** - Kali integration by [pistakugli](https://github.com/pistakugli)
- **Kali Linux** - Tools by Offensive Security

## 📞 Support

- **Documentation:** [docs/](docs/)
- **Issues:** [GitHub Issues](https://github.com/pistakugli/naja/issues)
- **Discussions:** [GitHub Discussions](https://github.com/pistakugli/naja/discussions)

## 🎓 Learn More

- [Kali Linux Documentation](https://www.kali.org/docs/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Penetration Testing Execution Standard](http://www.pentest-standard.org/)

---

**⚡ NAJA - Autonomous AI Penetration Testing Framework**

*Professional security testing, powered by AI* 🐍
