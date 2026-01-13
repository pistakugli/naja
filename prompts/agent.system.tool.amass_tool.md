### amass_tool:
OWASP Amass - Advanced network mapping and attack surface discovery tool.

#### Arguments:
 *  "domain" (string) : Target domain
 *  "mode" (string) : "intel" (intelligence gathering), "enum" (enumeration), "viz" (visualization)
 *  "passive" (Optional, boolean) : Passive reconnaissance only
 *  "brute" (Optional, boolean) : Enable brute forcing
 *  "output" (Optional, string) : Output file

#### Usage examples:
##### 1: Passive enumeration
\`\`\`json
{
    "thoughts": ["Passive subdomain discovery"],
    "tool_name": "amass_tool",
    "tool_args": {
        "domain": "target.com",
        "mode": "enum",
        "passive": true
    }
}
\`\`\`

##### 2: Active enumeration with brute force
\`\`\`json
{
    "thoughts": ["Complete attack surface mapping"],
    "tool_name": "amass_tool",
    "tool_args": {
        "domain": "target.com",
        "mode": "enum",
        "brute": true,
        "output": "/tmp/amass_results.txt"
    }
}
\`\`\`
