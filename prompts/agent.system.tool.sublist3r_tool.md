### sublist3r_tool:
Fast subdomain enumeration using OSINT. Searches multiple sources including Google, Yahoo, Bing, Baidu, and more.

#### Arguments:
 *  "domain" (string) : Target domain
 *  "bruteforce" (Optional, boolean) : Enable brute force enumeration
 *  "threads" (Optional, integer) : Number of threads
 *  "ports" (Optional, string) : Scan subdomains for specific ports

#### Usage examples:
##### 1: Basic subdomain enumeration
\`\`\`json
{
    "thoughts": ["Finding subdomains for target"],
    "tool_name": "sublist3r_tool",
    "tool_args": {
        "domain": "target.com"
    }
}
\`\`\`

##### 2: With port scanning
\`\`\`json
{
    "thoughts": ["Finding subdomains and checking for web servers"],
    "tool_name": "sublist3r_tool",
    "tool_args": {
        "domain": "target.com",
        "ports": "80,443,8080,8443"
    }
}
\`\`\`
