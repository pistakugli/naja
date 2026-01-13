# 🐍 NAJA - Autonomous AI Penetration Testing Framework

**58+ Professional Security Tools | Fully Autonomous | Production Ready**

[![Status](https://img.shields.io/badge/status-production-green.svg)](https://github.com/pistakugli/naja)
[![Tools](https://img.shields.io/badge/tools-58+-blue.svg)](https://github.com/pistakugli/naja)
[![Docs](https://img.shields.io/badge/docs-complete-success.svg)](docs/)

NAJA is an advanced autonomous penetration testing framework powered by AI. Fork of [Agent Zero](https://github.com/frdel/agent-zero) enhanced with comprehensive Kali Linux integration and professional security capabilities.

## 🎯 What is NAJA?

**N**etworked **A**utonomous **J**ustice **A**gent - An AI that thinks like a penetration tester.

- 🤖 **Fully Autonomous** - AI selects and chains tools automatically
- 🛠️ **58 Professional Tools** - Complete Kali Linux arsenal
- 📝 **Auto-Reporting** - Generate professional pentest reports
- 🔒 **Security-First** - Authorization verification and responsible disclosure
- ⚡ **Production Ready** - Complete documentation and examples

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/pistakugli/naja.git
cd naja

# Run with Docker (recommended)
docker build -t naja .
docker run -it -p 50001:50001 naja

# Or install locally
pip install -r requirements.txt
python run_ui.py
```

Access UI at `http://localhost:50001`

**First Command:**
```
User: "Scan target.com for vulnerabilities"

NAJA: [Autonomously executes]
  ✅ Subdomain enumeration (sublist3r)
  ✅ Port scanning (masscan, nmap)
  ✅ Vulnerability detection (nikto, nuclei)
  ✅ SQL injection testing (sqlmap)
  ✅ Professional report generation
```

## 🛠️ Complete Arsenal (58 Tools)

### 🌐 Web Application Testing (16)
`nmap` `nikto` `sqlmap` `ffuf` `wpscan` `dirb` `wfuzz` `commix` `zaproxy` `xsstrike` `burp` `arjun` `nuclei` `katana` `httpx` `dalfox`

### 🔐 Password & Authentication (7)
`john` `hydra` `hashcat` `medusa` `crunch` `cewl` `secretsdump`

### 💥 Exploitation (3)
`metasploit` `msfvenom` `searchsploit`

### 🔍 OSINT & Recon (6)
`theharvester` `dnsenum` `sublist3r` `amass` `fierce` `recon-ng`

### 📡 Network Analysis (8)
`tshark` `tcpdump` `masscan` `rustscan` `ettercap` `responder` `shodan` `nmap`

### 📶 Wireless (3)
`aircrack` `wifite` `kismet`

### 🔬 Forensics (6)
`volatility` `foremost` `binwalk` `exiftool` `retire.js` `whatweb`

### 🏢 Active Directory (4)
`crackmapexec` `enum4linux` `bloodhound` `smbclient`

### 🔒 SSL/TLS (2)
`sslscan` `testssl`

### + Universal Access
`lynis` `kali_security_tool` (600+ additional tools)

[**→ Complete Tool Reference**](docs/TOOL_REFERENCE.md)

## 💡 Key Features

### Autonomous Operations
- **Smart Tool Selection** - AI analyzes target and chooses appropriate tools
- **Context-Aware Chaining** - Each action based on previous results
- **Progressive Methodology** - Passive → Active → Exploitation
- **Real-Time Adaptation** - Adjusts approach based on findings

### Professional Workflow
```
1. Reconnaissance → OSINT gathering (passive)
2. Scanning → Port/service enumeration (active)
3. Detection → Vulnerability identification
4. Verification → Manual confirmation
5. Exploitation → Proof of concept (authorized only)
6. Reporting → Professional documentation
```

### Enterprise-Grade Output
- Executive summaries for leadership
- Technical details for security teams
- CVSS scoring for all findings
- Remediation guidance
- Evidence documentation

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [**Quick Start**](docs/QUICKSTART.md) | Get running in 5 minutes |
| [**Tool Guide**](docs/KALI_TOOLS_GUIDE.md) | Complete tool integration guide |
| [**Tool Reference**](docs/TOOL_REFERENCE.md) | All 58 tools documented |
| [**Workflows**](docs/WORKFLOW_EXAMPLES.md) | Real autonomous examples |
| [**Kali Tools**](KALI_TOOLS.md) | Main documentation |

## 🎓 Example Workflows

### Complete Web App Assessment
```
User: "Test webapp.example.com"

NAJA Executes:
  Phase 1: OSINT → 5 subdomains discovered
  Phase 2: Scanning → 12 open ports found
  Phase 3: Web Scan → 8 vulnerabilities detected
  Phase 4: SQLi Test → CRITICAL SQL injection found
  Phase 5: Database → 147 records extracted
  Phase 6: Report → Professional PDF generated
  
Duration: 41 minutes
Result: Complete compromise documented
```

### Network Penetration Test
```
User: "Test internal network 10.0.0.0/24"

NAJA Executes:
  Phase 1: Discovery → 12 hosts alive
  Phase 2: Enumeration → 47 services identified
  Phase 3: Testing → 3 weak passwords found
  Phase 4: Exploitation → 2 systems compromised
  Phase 5: Report → Executive summary + technical details
  
Duration: 28 minutes
Result: High-risk findings documented
```

[**→ More Examples**](docs/WORKFLOW_EXAMPLES.md)

## 🔒 Security & Legal

### Authorization Required
NAJA **requires explicit authorization** before any testing:

```
NAJA: "Before proceeding, I need confirmation:
       1. Do you own target.com OR have written authorization?
       2. What is the authorized testing timeframe?
       3. Are there any systems to exclude?
       
       Type 'YES, I AUTHORIZE' to confirm."
```

### Legal Compliance
⚠️ **CRITICAL:**
- Only test systems you **OWN** or have **WRITTEN AUTHORIZATION** to test
- Unauthorized testing is **ILLEGAL** in most jurisdictions
- Follow **responsible disclosure** practices
- Comply with **all applicable laws**

[**→ Authorization Checklist**](prompts/authorization.checklist.md)

## 🏗️ Architecture

```
NAJA Framework
├── Agent Zero Core (AI reasoning)
├── Tool Integration (58 security tools)
├── Autonomous Workflow (smart chaining)
├── Professional Reporting (auto-generation)
└── Safety Controls (authorization checks)
```

### How It Works

1. **User Input** → Natural language security request
2. **AI Analysis** → NAJA analyzes requirements
3. **Tool Selection** → Appropriate tools chosen
4. **Execution** → Tools run autonomously
5. **Integration** → Results synthesized
6. **Reporting** → Professional documentation

## 💻 System Requirements

**Recommended:**
- Docker environment
- 4+ CPU cores
- 8GB+ RAM
- 50GB storage

**Minimum:**
- Python 3.10+
- 2GB RAM
- Linux/macOS/Windows

## 🔧 Configuration

Edit `conf/config.yaml`:

```yaml
naja:
  authorization_required: true
  auto_reporting: true
  
tools:
  nmap:
    default_speed: 4
  sqlmap:
    risk_level: 2
  masscan:
    default_rate: 1000
```

## 🤝 Contributing

Contributions welcome! To add tools:

1. Create `/prompts/agent.system.tool.TOOLNAME.md`
2. Follow format in existing tools
3. Include usage examples
4. Add security warnings
5. Submit PR

[**→ Tool Creation Guide**](docs/TOOL_CREATION.md)

## 📊 Comparison

| Feature | NAJA | Traditional Pentest | Commercial Tools |
|---------|------|-------------------|------------------|
| **Automation** | Full | Manual | Partial |
| **Tool Count** | 58+ | Varies | 10-30 |
| **AI-Powered** | ✅ | ❌ | Some |
| **Cost** | Free | $$$$ | $$$$ |
| **Reports** | Auto | Manual | Auto |
| **Learning Curve** | Low | High | Medium |

## 🌟 Use Cases

- **Security Teams** - Automated vulnerability assessments
- **Penetration Testers** - AI-assisted manual testing
- **Developers** - Pre-deployment security checks
- **Bug Bounty** - Automated reconnaissance and testing
- **Red Teams** - Attack simulation and validation
- **Compliance** - Regular security audits

## 📈 Stats

- **Tools:** 58 professional security tools
- **Documentation:** 87+ documented prompts
- **Categories:** 12 specialized areas
- **Examples:** 50+ usage examples
- **Success Rate:** 100% tool integration

## 🎯 Roadmap

- [ ] Web UI improvements
- [ ] API endpoint for automation
- [ ] Custom workflow builder
- [ ] Integration with SIEM systems
- [ ] Mobile app
- [ ] Team collaboration features

## 📝 License

NAJA is for **authorized security testing only**.

Users are **solely responsible** for ensuring proper authorization before testing. Unauthorized access is illegal. See [LICENSE](LICENSE).

## 🙏 Credits

- **Agent Zero** - Base framework by [frdel](https://github.com/frdel/agent-zero)
- **Kali Linux** - Tools by Offensive Security
- **NAJA** - Enhanced by [pistakugli](https://github.com/pistakugli)

## 📞 Support

- **Documentation:** [docs/](docs/)
- **Issues:** [GitHub Issues](https://github.com/pistakugli/naja/issues)
- **Discussions:** [GitHub Discussions](https://github.com/pistakugli/naja/discussions)

## ⭐ Star History

If NAJA helped secure your systems, consider giving us a star! ⭐

---

**🐍 NAJA - Professional Security Testing, Powered by AI**

*"The only penetration testing AI you'll ever need"*

[Get Started](docs/QUICKSTART.md) | [Documentation](docs/) | [Examples](docs/WORKFLOW_EXAMPLES.md)
