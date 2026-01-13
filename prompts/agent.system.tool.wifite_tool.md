### wifite_tool:
Automated wireless auditing tool. Attacks multiple WEP/WPA/WPS encrypted networks.

⚠️ CRITICAL: Only test wireless networks you own. Unauthorized access is illegal.

#### Arguments:
 *  "interface" (string) : Wireless interface in monitor mode
 *  "kill" (Optional, boolean) : Kill interfering processes
 *  "wpa" (Optional, boolean) : Only attack WPA networks
 *  "wep" (Optional, boolean) : Only attack WEP networks
 *  "wps" (Optional, boolean) : Only attack WPS networks
 *  "dict" (Optional, string) : Path to wordlist for WPA

#### Usage examples:
##### 1: Auto wireless audit
\`\`\`json
{
    "thoughts": ["Automated attack on authorized test network"],
    "tool_name": "wifite_tool",
    "tool_args": {
        "interface": "wlan0mon",
        "kill": true
    }
}
\`\`\`

##### 2: WPA only with wordlist
\`\`\`json
{
    "thoughts": ["Testing WPA security"],
    "tool_name": "wifite_tool",
    "tool_args": {
        "interface": "wlan0mon",
        "wpa": true,
        "dict": "/usr/share/wordlists/rockyou.txt"
    }
}
\`\`\`
