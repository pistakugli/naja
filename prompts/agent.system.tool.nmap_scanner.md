### nmap_scanner:
Network port scanner using nmap. Discover open ports, services, and OS information.

⚠️ Only scan networks/systems you own or have written authorization to test.

#### Arguments:
 *  "target" (string) : Target IP address or hostname
 *  "scan_type" (Optional, string) : Scan profile: "basic", "fast", "full", "stealth", "aggressive", "udp", "os"
 *  "ports" (Optional, string) : Specific ports to scan (e.g., "80,443" or "1-1000")

#### Usage examples:
##### 1: Basic scan
\`\`\`json
{
    "thoughts": ["Scanning authorized target for open ports"],
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "192.168.1.100",
        "scan_type": "basic"
    }
}
\`\`\`

##### 2: Aggressive scan with OS detection
\`\`\`json
{
    "thoughts": ["Need detailed info about target system"],
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "example.com",
        "scan_type": "aggressive"
    }
}
\`\`\`

##### 3: Specific ports
\`\`\`json
{
    "thoughts": ["Check if web ports are open"],
    "tool_name": "nmap_scanner",
    "tool_args": {
        "target": "10.0.0.1",
        "scan_type": "basic",
        "ports": "80,443,8080,8443"
    }
}
\`\`\`
