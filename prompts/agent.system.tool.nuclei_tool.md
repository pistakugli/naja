### nuclei_tool:
Fast vulnerability scanner based on templates. Scan for thousands of known vulnerabilities.

⚠️ Only scan targets you own or have authorization to test.

#### Arguments:
 *  "target" (string) : Target URL or file with URLs
 *  "templates" (Optional, string) : Template tags (e.g., "cve", "sqli", "xss", "exposure")
 *  "severity" (Optional, string) : Severity filter: "critical", "high", "medium", "low"
 *  "output" (Optional, string) : Output file path

#### Usage examples:
##### 1: Scan with all templates
\`\`\`json
{
    "thoughts": ["Comprehensive vulnerability scan"],
    "tool_name": "nuclei_tool",
    "tool_args": {
        "target": "https://target.com"
    }
}
\`\`\`

##### 2: CVE scan only
\`\`\`json
{
    "thoughts": ["Scanning for known CVEs"],
    "tool_name": "nuclei_tool",
    "tool_args": {
        "target": "https://target.com",
        "templates": "cve",
        "severity": "critical,high"
    }
}
\`\`\`

##### 3: Exposure detection
\`\`\`json
{
    "thoughts": ["Looking for exposed sensitive files"],
    "tool_name": "nuclei_tool",
    "tool_args": {
        "target": "https://target.com",
        "templates": "exposure,misconfigurations"
    }
}
\`\`\`
