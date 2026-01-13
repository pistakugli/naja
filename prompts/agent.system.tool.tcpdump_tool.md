### tcpdump_tool:
Powerful packet capture and analysis tool. Dump network traffic for forensic analysis.

⚠️ Only capture traffic on authorized networks.

#### Arguments:
 *  "interface" (Optional, string) : Network interface
 *  "filter" (Optional, string) : Packet filter expression
 *  "count" (Optional, integer) : Number of packets to capture
 *  "output_file" (Optional, string) : Output pcap file
 *  "verbose" (Optional, boolean) : Verbose output

#### Usage examples:
##### 1: Capture DNS queries
\`\`\`json
{
    "thoughts": ["Monitoring DNS traffic"],
    "tool_name": "tcpdump_tool",
    "tool_args": {
        "interface": "eth0",
        "filter": "port 53",
        "output_file": "/tmp/dns.pcap"
    }
}
\`\`\`

##### 2: Capture specific host traffic
\`\`\`json
{
    "thoughts": ["Monitoring traffic to specific host"],
    "tool_name": "tcpdump_tool",
    "tool_args": {
        "filter": "host 192.168.1.100",
        "count": 1000,
        "verbose": true
    }
}
\`\`\`
