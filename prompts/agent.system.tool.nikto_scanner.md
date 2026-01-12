### nikto_scanner:
Web server vulnerability scanner. Checks for outdated software, dangerous files, misconfigurations.

⚠️ Only scan web servers you own or have authorization to test.

#### Arguments:
 *  "target" (string) : Target hostname or IP
 *  "port" (Optional, string) : Port number (default: 80)
 *  "ssl" (Optional, boolean) : Use HTTPS (default: false)

#### Usage examples:
##### 1: Basic HTTP scan
\`\`\`json
{
    "thoughts": ["Scanning authorized web server for vulnerabilities"],
    "tool_name": "nikto_scanner",
    "tool_args": {
        "target": "example.com"
    }
}
\`\`\`

##### 2: HTTPS scan
\`\`\`json
{
    "thoughts": ["Scanning HTTPS site on custom port"],
    "tool_name": "nikto_scanner",
    "tool_args": {
        "target": "secure.example.com",
        "port": "8443",
        "ssl": true
    }
}
\`\`\`
