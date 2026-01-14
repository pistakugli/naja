# 🐍 NAJA - AI Penetration Testing with Kali Linux

**Agent Zero + 58 Kali Linux Tools | Autonomous Security Testing**

[![Agent Zero](https://img.shields.io/badge/based%20on-Agent%20Zero-blue.svg)](https://github.com/frdel/agent-zero)
[![Kali Tools](https://img.shields.io/badge/kali%20tools-58-red.svg)](docs/TOOL_REFERENCE.md)
[![Status](https://img.shields.io/badge/status-active-green.svg)](https://github.com/pistakugli/naja)
[![Fixed](https://img.shields.io/badge/Agent%20Zero%20%23803-fixed-brightgreen.svg)](https://github.com/agent0ai/agent-zero/issues/803)

NAJA je [Agent Zero](https://github.com/frdel/agent-zero) fork sa integriranim Kali Linux penetration testing alatima. Agent Zero pruža AI reasoning framework, a ja sam dodao 58 profesionalnih security tools.

## 🎯 Šta je NAJA?

**NAJA = Agent Zero Framework + Kali Linux Integration**

- 🤖 **Agent Zero Core** - AI reasoning, tool calling, autonomous execution
- 🛠️ **58 Kali Tools** - Professional penetration testing arsenal  
- 📝 **Auto Reporting** - Generate professional security reports
- 🔒 **Authorization Checks** - Built-in legal compliance

## 🆕 Latest Updates (2026-01-14)

**✅ Fixed Agent Zero Issue #803**
- Resolved `AttributeError: '_auth_server_provider'` bug
- Updated for fastmcp 2.3.4 compatibility
- Added missing `openai` dependency

**✅ RFC Configuration Added**
- Remote Function Call support for development instances
- Secure communication between production/development
- See [RFC_SETUP.md](RFC_SETUP.md) for details

## 📦 Šta je uključeno?

### Agent Zero Framework (Original)
- AI reasoning engine
- Tool calling system
- Autonomous execution
- 28 built-in tools (memory, web, code execution, etc.)
- Multi-agent collaboration

### Moje Kali Linux Integration (Dodato)
**58 penetration testing tools u 12 kategorija:**

```
🌐 Web Testing (16):      nmap, nikto, sqlmap, ffuf, wpscan, dirb, wfuzz,
                          commix, zaproxy, xsstrike, burp, arjun, nuclei,
                          katana, httpx, dalfox

🔐 Password (7):          john, hydra, hashcat, medusa, crunch, cewl,
                          secretsdump

💥 Exploitation (3):      metasploit, msfvenom, searchsploit

🔍 OSINT (6):             theharvester, dnsenum, sublist3r, amass, fierce,
                          recon-ng

📡 Network (8):           tshark, tcpdump, masscan, rustscan, ettercap,
                          responder, shodan, nmap

📶 Wireless (3):          aircrack, wifite, kismet

🔬 Forensics (6):         volatility, foremost, binwalk, exiftool, retire.js,
                          whatweb

🏢 Active Directory (4):  crackmapexec, enum4linux, bloodhound, smbclient

🔒 SSL/TLS (2):           sslscan, testssl

🎭 Social Eng (1):        setoolkit

📁 Fuzzing (1):           gobuster

🔧 Auditing (2):          lynis, kali_security_tool (wrapper za 600+ tools)
```

**[→ Svi tools detaljno](docs/TOOL_REFERENCE.md)**

## 🚀 Quick Start

### Standard Setup

```bash
# Clone repo
git clone https://github.com/pistakugli/naja.git
cd naja

# Setup environment
cp .env.example .env
# Edit .env and add your API keys

# Install dependencies
pip install -r requirements.txt

# Install Claude AI Skills (16 expert workflow systems)
./install_skills.sh

# Run
python run_ui.py
```

Otvori browser: `http://localhost:50001`

**Note:** Skills provide expert-level guidance for document creation, web design, and specialized workflows. See `skills/README.md` for details.

### Docker Setup

```bash
# Docker (recommended)
docker build -t naja .
docker run -it -p 50001:50001 naja
```

### Development Instance (RFC)

**For advanced debugging with separate development environment:**

```bash
# See detailed RFC setup guide
cat RFC_SETUP.md

# Quick setup:
# 1. Set RFC_PASSWORD in .env
# 2. Run development instance (Docker or local)
# 3. Configure in settings
```

**[→ Complete RFC Guide](RFC_SETUP.md)**

## ⚙️ Configuration

### Required (.env file)
```bash
ANTHROPIC_API_KEY=your-key-here
DEFAULT_MODEL=anthropic/claude-sonnet-4-20250514
```

### Optional (RFC for development)
```bash
RFC_PASSWORD=your-secure-password
```

See [.env.example](.env.example) for complete configuration.

## 💬 Primer korišćenja

**Agent Zero tools (original):**
```
User: "Search web for latest python tutorials"
NAJA: [Uses Agent Zero's web_search tool]
```

**Kali tools (dodato):**
```
User: "Scan target.com for SQL injection"
NAJA: [Uses sqlmap_tool from Kali integration]
  ✅ Authorization check
  ✅ Port scan (nmap)
  ✅ SQLi test (sqlmap)
  ✅ Report generation
```

**Kombinovano:**
```
User: "Research company.com and test their security"
NAJA: [Uses both Agent Zero & Kali tools]
  ✅ Web search for info (Agent Zero)
  ✅ OSINT gathering (Kali: theharvester, sublist3r)
  ✅ Port scanning (Kali: masscan, nmap)
  ✅ Vulnerability testing (Kali: nikto, nuclei)
  ✅ Professional report (Custom)
```

## 🏗️ Kako radi?

```
┌─────────────────────────────────────────────────┐
│          User Request                           │
└────────────────┬────────────────────────────────┘
                 │
         ┌───────▼──────────┐
         │   Agent Zero     │ ← AI reasoning
         │   AI Engine      │
         └───────┬──────────┘
                 │
         ┌───────▼──────────┐
         │  Tool Selection  │
         └───────┬──────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼────────┐        ┌──────▼─────────┐
│ Agent Zero │        │  Kali Linux    │
│   Tools    │        │     Tools      │
│  (28)      │        │     (58)       │
└───┬────────┘        └──────┬─────────┘
    │                        │
    └────────────┬───────────┘
                 │
         ┌───────▼──────────┐
         │    Execution     │
         └───────┬──────────┘
                 │
         ┌───────▼──────────┐
         │   Result to AI   │
         └───────┬──────────┘
                 │
         ┌───────▼──────────┐
         │  Response to     │
         │      User        │
         └──────────────────┘
```

## 📚 Dokumentacija

| Doc | Opis |
|-----|------|
| [Quick Start](docs/QUICKSTART.md) | Startuj za 5 min |
| [Tool Reference](docs/TOOL_REFERENCE.md) | Svi 58 Kali tools |
| [Workflows](docs/WORKFLOW_EXAMPLES.md) | Primeri autonomous testing |
| [Kali Guide](docs/KALI_TOOLS_GUIDE.md) | Detaljni integration guide |
| **[RFC Setup](RFC_SETUP.md)** | Development instance configuration |

## 🔒 Legal & Authorization

**⚠️ VAŽNO:**
- NAJA testira SAMO sisteme koje posedujete ili za koje imate PISANU AUTORIZACIJU
- Neautorizovano testiranje je ILEGALNO
- Built-in authorization check pre svakog testa
- Follow responsible disclosure

## 🎯 Use Cases

**Agent Zero capabilities (original):**
- General AI assistant
- Code generation & execution
- Web research & browsing
- Memory & knowledge management
- Multi-agent collaboration

**+ Kali Linux capabilities (dodato):**
- Web application penetration testing
- Network security assessment
- OSINT & reconnaissance
- Password auditing
- Active Directory testing
- Wireless security
- Digital forensics

## 🐛 Troubleshooting

### Common Issues

**AttributeError: '_auth_server_provider'**
- ✅ Fixed in latest version (commit 9c05182)
- Update: `git pull && pip install -r requirements.txt`

**ModuleNotFoundError: No module named 'openai'**
- ✅ Fixed in requirements.txt (commit c5c8b40)
- Install: `pip install -r requirements.txt`

**"No RFC password" warning**
- ℹ️ Optional feature for development instances
- See [RFC_SETUP.md](RFC_SETUP.md) or ignore if not needed

## 🤝 Contributing

Dodavanje novih Kali tools:

1. Kreiraj `/prompts/agent.system.tool.TOOLNAME.md`
2. Prati format postojećih tools
3. Dodaj usage examples
4. Include security warnings
5. Submit PR

## 📊 Stats

```
Agent Zero Framework:  20 tools (original)
Kali Integration:      58 tools (security testing)
Claude AI Tools:       12 tools (documents, design, viz)
Total Tools:           90 tools

Claude AI Skills:      16 expert workflow systems
- Public Skills:       6 (docx, pptx, xlsx, pdf, web, product)
- Example Skills:      10 (art, design, workflows)

Documentation:         90+ prompt files + 16 skill guides
Status:                Active development
Fixes:                 Agent Zero #803 resolved
```

## 🙏 Credits

- **[Agent Zero](https://github.com/frdel/agent-zero)** - Base AI framework by [frdel](https://github.com/frdel)
- **Kali Linux** - Security tools by Offensive Security
- **NAJA** - Kali integration by [pistakugli](https://github.com/pistakugli)

## ⚖️ License

- **Agent Zero**: MIT License (original framework)
- **NAJA additions**: Authorized security testing only
- **Kali Tools**: Respective tool licenses

**See [LICENSE](LICENSE) for details**

---

**🐍 NAJA = Agent Zero + Kali Linux**

*AI Reasoning Framework meets Professional Security Tools*

[Get Started](docs/QUICKSTART.md) | [Documentation](docs/) | [Tool Reference](docs/TOOL_REFERENCE.md) | [RFC Setup](RFC_SETUP.md)
