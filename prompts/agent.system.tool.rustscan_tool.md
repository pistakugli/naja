### rustscan_tool:
Modern ultra-fast port scanner written in Rust. Faster than nmap with automatic nmap integration.

⚠️ Only scan targets you own or have authorization to test.

#### Arguments:
 *  "targets" (string) : Target IP addresses
 *  "ports" (Optional, string) : Port range (e.g., "1-1000", "80,443")
 *  "ulimit" (Optional, integer) : Ulimit for faster scanning (default: 5000)
 *  "batch_size" (Optional, integer) : Batch size for port scanning
 *  "nmap" (Optional, boolean) : Run nmap on discovered ports

#### Usage examples:
##### 1: Ultra-fast port discovery
\`\`\`json
{
    "thoughts": ["Lightning-fast port scan"],
    "tool_name": "rustscan_tool",
    "tool_args": {
        "targets": "192.168.1.100",
        "ulimit": 5000
    }
}
\`\`\`

##### 2: Scan with nmap integration
\`\`\`json
{
    "thoughts": ["Fast discovery then detailed nmap scan"],
    "tool_name": "rustscan_tool",
    "tool_args": {
        "targets": "10.0.0.50",
        "ports": "1-10000",
        "nmap": true
    }
}
\`\`\`
