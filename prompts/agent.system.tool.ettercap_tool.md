### ettercap_tool:
Comprehensive suite for man-in-the-middle attacks. Sniff live connections, filter content, and more.

⚠️ CRITICAL: Only use on networks you own. MITM attacks are illegal without authorization.

#### Arguments:
 *  "interface" (string) : Network interface
 *  "target1" (Optional, string) : First target IP
 *  "target2" (Optional, string) : Second target IP (usually gateway)
 *  "mitm" (Optional, string) : MITM method: "arp", "icmp", "dhcp"
 *  "filter" (Optional, string) : Content filter file

#### Usage examples:
##### 1: ARP poisoning MITM
\`\`\`json
{
    "thoughts": ["Authorized MITM test on lab network"],
    "tool_name": "ettercap_tool",
    "tool_args": {
        "interface": "eth0",
        "target1": "192.168.1.100",
        "target2": "192.168.1.1",
        "mitm": "arp"
    }
}
\`\`\`

##### 2: Passive sniffing
\`\`\`json
{
    "thoughts": ["Monitoring network traffic passively"],
    "tool_name": "ettercap_tool",
    "tool_args": {
        "interface": "eth0",
        "mode": "passive"
    }
}
\`\`\`
