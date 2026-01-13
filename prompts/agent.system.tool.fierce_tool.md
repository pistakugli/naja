### fierce_tool:
DNS reconnaissance tool. Locate non-contiguous IP space and hostnames.

#### Arguments:
 *  "domain" (string) : Target domain
 *  "dnsserver" (Optional, string) : DNS server to use
 *  "threads" (Optional, integer) : Number of threads
 *  "subdomains" (Optional, string) : Subdomain wordlist file

#### Usage examples:
##### 1: Basic DNS recon
\`\`\`json
{
    "thoughts": ["Scanning DNS for target domain"],
    "tool_name": "fierce_tool",
    "tool_args": {
        "domain": "target.com"
    }
}
\`\`\`

##### 2: Custom DNS server and wordlist
\`\`\`json
{
    "thoughts": ["Using custom resolver for DNS enum"],
    "tool_name": "fierce_tool",
    "tool_args": {
        "domain": "target.com",
        "dnsserver": "8.8.8.8",
        "subdomains": "/usr/share/fierce/hosts.txt"
    }
}
\`\`\`
