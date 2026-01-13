### kismet_tool:
Wireless network detector, sniffer, and IDS. Supports WiFi, Bluetooth, SDR, and more.

⚠️ Only monitor wireless networks you own or have authorization to monitor.

#### Arguments:
 *  "interface" (string) : Network interface
 *  "capture" (Optional, boolean) : Enable packet capture
 *  "output_prefix" (Optional, string) : Output file prefix
 *  "channel_hop" (Optional, boolean) : Enable channel hopping

#### Usage examples:
##### 1: Basic wireless detection
\`\`\`json
{
    "thoughts": ["Detecting wireless networks in area"],
    "tool_name": "kismet_tool",
    "tool_args": {
        "interface": "wlan0",
        "channel_hop": true
    }
}
\`\`\`

##### 2: Full capture with logging
\`\`\`json
{
    "thoughts": ["Complete wireless monitoring"],
    "tool_name": "kismet_tool",
    "tool_args": {
        "interface": "wlan0",
        "capture": true,
        "output_prefix": "/tmp/kismet_capture"
    }
}
\`\`\`
