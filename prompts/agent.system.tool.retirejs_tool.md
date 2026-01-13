### retirejs_tool:
JavaScript library vulnerability scanner. Detect outdated and vulnerable JS libraries.

⚠️ Only scan web applications you own or have authorization to test.

#### Arguments:
 *  "url" (Optional, string) : Target URL to scan
 *  "path" (Optional, string) : Local path to scan
 *  "output" (Optional, string) : Output format: "json", "jsonsimple", "cyclonedx"

#### Usage examples:
##### 1: Scan website
\`\`\`json
{
    "thoughts": ["Detecting vulnerable JavaScript libraries"],
    "tool_name": "retirejs_tool",
    "tool_args": {
        "url": "https://target.com"
    }
}
\`\`\`

##### 2: Scan local files
\`\`\`json
{
    "thoughts": ["Checking local JS files for vulnerabilities"],
    "tool_name": "retirejs_tool",
    "tool_args": {
        "path": "/var/www/html",
        "output": "json"
    }
}
\`\`\`
