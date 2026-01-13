### whatweb_tool:
Web technology fingerprinting. Identify CMS, frameworks, servers, and technologies.

#### Arguments:
 *  "url" (string) : Target URL
 *  "aggression" (Optional, integer) : Aggression level (1-4, default: 1)
 *  "plugins" (Optional, string) : Specific plugins to use

#### Usage examples:
##### 1: Basic fingerprinting
\`\`\`json
{
    "thoughts": ["Identifying web technologies"],
    "tool_name": "whatweb_tool",
    "tool_args": {
        "url": "https://target.com"
    }
}
\`\`\`

##### 2: Aggressive scan
\`\`\`json
{
    "thoughts": ["Deep technology detection"],
    "tool_name": "whatweb_tool",
    "tool_args": {
        "url": "https://target.com",
        "aggression": 3
    }
}
\`\`\`
