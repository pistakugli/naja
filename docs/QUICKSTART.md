# NAJA Quick Start Guide

Get up and running with NAJA penetration testing in 5 minutes.

## Installation

### Prerequisites
- Docker (recommended) OR
- Python 3.10+
- Kali Linux tools (if not using Docker)

### Option 1: Docker (Recommended)
```bash
git clone https://github.com/pistakugli/naja.git
cd naja
docker build -t naja .
docker run -it naja
```

### Option 2: Manual Setup
```bash
git clone https://github.com/pistakugli/naja.git
cd naja
pip install -r requirements.txt
python initialize.py
python run_ui.py
```

## Your First Scan

### 1. Simple Port Scan
```
User: "Scan 192.168.1.1 for open ports"

NAJA will:
- Use nmap_scanner
- Detect open ports
- Identify services
- Present results
```

### 2. Web Vulnerability Scan
```
User: "Scan http://testsite.local for vulnerabilities"

NAJA will:
- Use nikto_scanner for web vulns
- Check for SQL injection with sqlmap
- Test for common vulnerabilities
- Generate report
```

### 3. Complete Network Assessment
```
User: "Perform full security assessment of 192.168.1.0/24"

NAJA will:
1. Port scan with nmap
2. Service enumeration
3. Vulnerability detection
4. Exploitation (if authorized)
5. Comprehensive report
```

## Understanding Tool Selection

NAJA automatically selects appropriate tools:

| Task | Tools Used |
|------|------------|
| Port scanning | nmap, masscan, rustscan |
| Web testing | nikto, sqlmap, ffuf, dirb |
| Password testing | john, hydra, hashcat |
| WiFi testing | aircrack, wifite |
| OSINT | theHarvester, amass, sublist3r |

## Configuration

### Set API Keys (if needed)
```bash
# Edit .env file
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

### Adjust Tool Settings
Edit `conf/config.yaml`:
```yaml
tools:
  nmap:
    default_speed: 4  # 0-5
    max_hosts: 256
  
  sqlmap:
    default_level: 2
    default_risk: 2
```

## Safety & Authorization

⚠️ **BEFORE ANY TESTING:**

1. Get written authorization
2. Define scope clearly
3. Set time windows
4. Establish communication
5. Plan for incidents

### Example Authorization Check
```
User: "I need to test mycompany.com"

NAJA: "Do you have written authorization to test mycompany.com? 
       Please confirm:
       - You own the domain OR
       - You have written permission from the owner"

User: "Yes, I am the owner and CTO"

NAJA: "Confirmed. Starting authorized security assessment..."
```

## Example Workflows

### Web Application Test
```
1. "Find subdomains for target.com"
2. "Scan all discovered subdomains"
3. "Test web application at app.target.com"
4. "Generate penetration test report"
```

### Network Audit
```
1. "Scan internal network 10.0.0.0/24"
2. "Identify critical services"
3. "Test for weak passwords"
4. "Document security findings"
```

### WiFi Security
```
1. "Scan for wireless networks"
2. "Test WPA password strength on MyNetwork"
3. "Generate WiFi security report"
```

## Getting Help

### Within NAJA
```
"What tools can you use?"
"How do I scan for SQL injection?"
"Show me example of port scanning"
```

### Documentation
- [Full Documentation](docs/)
- [Kali Tools Guide](docs/KALI_TOOLS_GUIDE.md)
- [Tool Reference](docs/TOOL_REFERENCE.md)

### Community
- GitHub Issues: https://github.com/pistakugli/naja/issues
- Discussions: https://github.com/pistakugli/naja/discussions

## Next Steps

1. ✅ Read [Kali Tools Guide](KALI_TOOLS_GUIDE.md)
2. ✅ Review [Security Best Practices](SECURITY.md)
3. ✅ Try example workflows
4. ✅ Customize for your needs

## License

NAJA is for authorized security testing only. See [LICENSE](../LICENSE) for details.
