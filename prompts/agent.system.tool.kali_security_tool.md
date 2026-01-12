### kali_security_tool:
Universal wrapper for Kali Linux security tools. Enables access to 600+ penetration testing tools.

⚠️ **CRITICAL**: Only use for AUTHORIZED security testing with explicit permission.
Unauthorized access is ILLEGAL. User assumes all legal responsibility.

!!! This tool provides access to professional penetration testing tools
!!! Requires Kali Linux environment or installed tools
!!! Always obtain written authorization before testing

#### Arguments:
 *  "tool" (string) : Tool name from whitelist (nmap, nikto, sqlmap, hydra, etc.)
 *  "args" (array or string) : Tool-specific arguments
 *  "target" (Optional, string) : Target IP/hostname
 *  "timeout" (Optional, integer) : Execution timeout in seconds (default: 300)

#### Available Tools:
**Network Scanning**: nmap, masscan, netdiscover
**Web Testing**: nikto, sqlmap, wpscan, dirb, gobuster, ffuf
**Password Cracking**: john, hydra, hashcat, crunch
**Exploitation**: msfconsole, msfvenom, searchsploit
**Wireless**: aircrack-ng, reaver, bully
**Packet Analysis**: tshark, tcpdump
**Info Gathering**: whois, dnsenum, theHarvester
**Vuln Scanning**: openvas, nessus

#### Usage examples:
##### 1: Port scan with nmap
\`\`\`json
{
    "thoughts": ["User authorized to scan their own server", "Using nmap for port discovery"],
    "tool_name": "kali_security_tool",
    "tool_args": {
        "tool": "nmap",
        "target": "192.168.1.100",
        "args": ["-sV", "-sC"]
    }
}
\`\`\`

##### 2: Web vulnerability scan
\`\`\`json
{
    "thoughts": ["Authorized web app testing", "Using nikto for vulnerability detection"],
    "tool_name": "kali_security_tool",
    "tool_args": {
        "tool": "nikto",
        "target": "http://testsite.local",
        "args": ["-h", "testsite.local"]
    }
}
\`\`\`

##### 3: SQL injection test
\`\`\`json
{
    "thoughts": ["Testing authorized target for SQL injection"],
    "tool_name": "kali_security_tool",
    "tool_args": {
        "tool": "sqlmap",
        "args": ["-u", "http://target.com/page?id=1", "--batch"]
    }
}
\`\`\`

##### 4: Directory brute force
\`\`\`json
{
    "thoughts": ["Finding hidden directories on authorized target"],
    "tool_name": "kali_security_tool",
    "tool_args": {
        "tool": "gobuster",
        "args": ["dir", "-u", "http://target.com", "-w", "/usr/share/wordlists/dirb/common.txt"]
    }
}
\`\`\`
