### httpx_tool:
Fast HTTP toolkit. Probe for live hosts, technologies, status codes, and more.

#### Arguments:
 *  "target" (string) : Target URL, domain, or file with targets
 *  "tech_detect" (Optional, boolean) : Detect web technologies
 *  "status_code" (Optional, boolean) : Show status codes
 *  "title" (Optional, boolean) : Extract page titles
 *  "threads" (Optional, integer) : Number of threads (default: 50)

#### Usage examples:
##### 1: Probe live hosts
\`\`\`json
{
    "thoughts": ["Checking which hosts are alive"],
    "tool_name": "httpx_tool",
    "tool_args": {
        "target": "/tmp/subdomains.txt",
        "status_code": true,
        "title": true
    }
}
\`\`\`

##### 2: Technology detection
\`\`\`json
{
    "thoughts": ["Identifying web technologies"],
    "tool_name": "httpx_tool",
    "tool_args": {
        "target": "target.com",
        "tech_detect": true
    }
}
\`\`\`
