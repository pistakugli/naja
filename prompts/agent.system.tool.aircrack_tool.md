### aircrack_tool:
WiFi security testing tool. For authorized wireless network security assessment.

⚠️ Only test wireless networks you own or have explicit authorization to test.

#### Arguments:
 *  "action" (string) : Action: "crack" (crack WPA), "monitor" (enable monitor mode), "stop_monitor"
 *  "capture_file" (Optional, string) : Packet capture file for cracking
 *  "bssid" (Optional, string) : Target access point BSSID
 *  "wordlist" (Optional, string) : Wordlist for WPA cracking
 *  "interface" (Optional, string) : Wireless interface (default: wlan0)

#### Usage examples:
##### 1: Crack WPA key
\`\`\`json
{
    "thoughts": ["Cracking WPA key from captured handshake"],
    "tool_name": "aircrack_tool",
    "tool_args": {
        "action": "crack",
        "capture_file": "/tmp/capture.cap",
        "bssid": "AA:BB:CC:DD:EE:FF",
        "wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
\`\`\`

##### 2: Enable monitor mode
\`\`\`json
{
    "thoughts": ["Putting WiFi adapter in monitor mode"],
    "tool_name": "aircrack_tool",
    "tool_args": {
        "action": "monitor",
        "interface": "wlan0"
    }
}
\`\`\`
