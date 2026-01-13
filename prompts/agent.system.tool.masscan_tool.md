### masscan_tool:
Ultra-fast port scanner. Scan entire Internet in minutes. Much faster than nmap for large networks.

⚠️ CRITICAL: Only scan networks you own. Unauthorized scanning can cause legal issues.

#### Arguments:
 *  "targets" (string) : Target IP/CIDR (e.g., "192.168.1.0/24", "10.0.0.1-255")
 *  "ports" (string) : Ports to scan (e.g., "80,443", "1-1000", "U:53,161")
 *  "rate" (Optional, integer) : Packets per second (default: 100)
 *  "banners" (Optional, boolean) : Grab service banners
 *  "exclude" (Optional, string) : Exclude IPs from scan

#### Usage examples:
##### 1: Fast port scan
\`\`\`json
{
    "thoughts": ["Rapid port discovery on authorized network"],
    "tool_name": "masscan_tool",
    "tool_args": {
        "targets": "192.168.1.0/24",
        "ports": "80,443,8080,8443",
        "rate": 1000
    }
}
\`\`\`

##### 2: Full TCP scan with banners
\`\`\`json
{
    "thoughts": ["Complete port scan with service detection"],
    "tool_name": "masscan_tool",
    "tool_args": {
        "targets": "10.0.0.0/24",
        "ports": "1-65535",
        "rate": 10000,
        "banners": true
    }
}
\`\`\`
