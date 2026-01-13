### tshark_tool:
Terminal-based Wireshark. Capture and analyze network packets from command line.

⚠️ Only capture traffic on networks you own or have authorization to monitor.

#### Arguments:
 *  "interface" (Optional, string) : Network interface (e.g., "eth0", "wlan0")
 *  "filter" (Optional, string) : Capture filter (BPF syntax)
 *  "count" (Optional, integer) : Number of packets to capture
 *  "output_file" (Optional, string) : Save capture to file (.pcap)
 *  "display_filter" (Optional, string) : Display filter for analysis

#### Usage examples:
##### 1: Capture HTTP traffic
\`\`\`json
{
    "thoughts": ["Capturing HTTP packets for analysis"],
    "tool_name": "tshark_tool",
    "tool_args": {
        "interface": "eth0",
        "filter": "tcp port 80",
        "count": 100
    }
}
\`\`\`

##### 2: Analyze existing pcap file
\`\`\`json
{
    "thoughts": ["Analyzing captured traffic"],
    "tool_name": "tshark_tool",
    "tool_args": {
        "input_file": "/tmp/capture.pcap",
        "display_filter": "http.request"
    }
}
\`\`\`
