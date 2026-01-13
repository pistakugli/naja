### wpscan_tool:
WordPress security scanner. Enumerate plugins, themes, users, and vulnerabilities in WordPress sites.

⚠️ Only scan WordPress sites you own or have written authorization to test.

#### Arguments:
 *  "url" (string) : Target WordPress URL
 *  "enumerate" (Optional, string) : What to enumerate: "p" (plugins), "t" (themes), "u" (users), "vp" (vulnerable plugins), "ap" (all plugins)
 *  "api_token" (Optional, string) : WPVulnDB API token for vulnerability data
 *  "detection_mode" (Optional, string) : Detection mode: "mixed", "passive", "aggressive"

#### Usage examples:
##### 1: Basic WordPress scan
\`\`\`json
{
    "thoughts": ["Scanning authorized WordPress site"],
    "tool_name": "wpscan_tool",
    "tool_args": {
        "url": "https://target-wordpress.com",
        "enumerate": "vp,u"
    }
}
\`\`\`

##### 2: Aggressive scan with all enumeration
\`\`\`json
{
    "thoughts": ["Full WordPress security audit"],
    "tool_name": "wpscan_tool",
    "tool_args": {
        "url": "https://target.com",
        "enumerate": "ap,at,u",
        "detection_mode": "aggressive"
    }
}
\`\`\`
