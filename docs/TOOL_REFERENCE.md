# NAJA Tool Reference

Complete reference of all 40+ Kali Linux tools in NAJA.

## Quick Reference Table

| Tool | Category | Purpose | Complexity |
|------|----------|---------|------------|
| nmap_scanner | Network | Port scanning | ⭐⭐ |
| masscan_tool | Network | Fast port scan | ⭐⭐ |
| rustscan_tool | Network | Ultra-fast scan | ⭐ |
| nikto_scanner | Web | Vulnerability scan | ⭐⭐ |
| sqlmap_tool | Web | SQL injection | ⭐⭐⭐ |
| ffuf_tool | Web | Web fuzzing | ⭐⭐ |
| wpscan_tool | Web | WordPress scan | ⭐⭐ |
| dirb_tool | Web | Directory brute | ⭐ |
| wfuzz_tool | Web | Advanced fuzzing | ⭐⭐⭐ |
| commix_tool | Web | Command injection | ⭐⭐⭐ |
| zaproxy_tool | Web | OWASP ZAP | ⭐⭐⭐ |
| xsstrike_tool | Web | XSS detection | ⭐⭐ |
| john_tool | Password | Hash cracking | ⭐⭐ |
| hydra_tool | Password | Brute forcing | ⭐⭐ |
| hashcat_tool | Password | GPU cracking | ⭐⭐⭐ |
| medusa_tool | Password | Parallel brute | ⭐⭐ |
| crunch_tool | Password | Wordlist gen | ⭐ |
| cewl_tool | Password | Web wordlist | ⭐ |
| metasploit_tool | Exploit | Framework | ⭐⭐⭐⭐ |
| msfvenom_tool | Exploit | Payload gen | ⭐⭐⭐ |
| searchsploit_tool | Exploit | Exploit search | ⭐ |
| theharvester_tool | OSINT | Email/subdomain | ⭐⭐ |
| dnsenum_tool | OSINT | DNS enum | ⭐⭐ |
| sublist3r_tool | OSINT | Subdomain disc | ⭐ |
| amass_tool | OSINT | Attack surface | ⭐⭐⭐ |
| fierce_tool | OSINT | DNS recon | ⭐⭐ |
| reconng_tool | OSINT | Recon framework | ⭐⭐⭐ |
| tshark_tool | Network | Packet analysis | ⭐⭐⭐ |
| tcpdump_tool | Network | Packet capture | ⭐⭐ |
| ettercap_tool | Network | MITM | ⭐⭐⭐⭐ |
| responder_tool | Network | LLMNR poison | ⭐⭐⭐ |
| aircrack_tool | Wireless | WiFi cracking | ⭐⭐⭐ |
| wifite_tool | Wireless | Auto WiFi audit | ⭐⭐ |
| kismet_tool | Wireless | WiFi detector | ⭐⭐ |
| volatility_tool | Forensics | Memory analysis | ⭐⭐⭐⭐ |
| foremost_tool | Forensics | File carving | ⭐⭐ |
| binwalk_tool | Forensics | Firmware analysis | ⭐⭐⭐ |
| setoolkit_tool | Social Eng | SE toolkit | ⭐⭐⭐⭐ |
| gobuster_tool | Fuzzing | Dir/DNS fuzzing | ⭐⭐ |
| kali_security_tool | Universal | 600+ tools | ⭐⭐⭐ |

**Legend:** ⭐ Easy | ⭐⭐ Medium | ⭐⭐⭐ Advanced | ⭐⭐⭐⭐ Expert

## Tool Details

See individual tool documentation in `/prompts/agent.system.tool.*.md`

## Tool Selection Guide

### For Network Discovery
1. **Fast scan (< 5 min):** masscan, rustscan
2. **Detailed scan:** nmap with -sV -sC
3. **Packet analysis:** tshark, tcpdump

### For Web Testing
1. **Basic scan:** nikto
2. **Directory discovery:** ffuf, dirb, gobuster
3. **SQL injection:** sqlmap
4. **XSS:** xsstrike
5. **Full audit:** zaproxy

### For Password Attacks
1. **Online brute force:** hydra, medusa
2. **Offline cracking:** john, hashcat
3. **Wordlist creation:** crunch, cewl

### For OSINT
1. **Subdomains:** sublist3r, amass, fierce
2. **Emails:** theHarvester
3. **Complete recon:** reconng, amass

## Command Cheat Sheet

### Port Scanning
```bash
# Fast
masscan -p80,443 10.0.0.0/24 --rate 1000

# Detailed
nmap -sV -sC -p- target.com

# Ultra-fast
rustscan -a target.com
```

### Web Testing
```bash
# Directory fuzzing
ffuf -u http://target.com/FUZZ -w wordlist.txt

# SQL injection
sqlmap -u "http://target.com/page?id=1" --batch

# WordPress scan
wpscan --url https://wordpress.com --enumerate vp,u
```

### Password Cracking
```bash
# Hash cracking
john hashes.txt --wordlist=rockyou.txt

# SSH brute force
hydra -l admin -P passwords.txt ssh://target.com

# GPU cracking
hashcat -m 0 -a 0 hashes.txt rockyou.txt
```

## Performance Tips

### Speed Optimization
- Use masscan/rustscan for initial discovery
- Parallel tool execution when possible
- Adjust rate limits for network capacity

### Resource Management
- GPU tools (hashcat) need proper drivers
- Memory forensics (volatility) need sufficient RAM
- Some tools are CPU-intensive (john, hashcat)

## Troubleshooting

### Common Issues

**"Tool not found"**
```bash
apt update && apt install <toolname>
```

**"Permission denied"**
```bash
sudo <command>  # Or run NAJA as root
```

**"Network unreachable"**
- Check firewall
- Verify connectivity
- Check routing

## Updates

Tools are regularly updated. To check versions:
```bash
nmap --version
sqlmap --version
metasploit --version
```

For latest tools, see: https://github.com/pistakugli/naja
