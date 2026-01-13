### dnsenum_tool:
DNS enumeration tool. Discover DNS records, subdomains, and network ranges.

#### Arguments:
 *  "domain" (string) : Target domain
 *  "enum" (Optional, boolean) : Enable DNSSEC enumeration
 *  "threads" (Optional, integer) : Number of threads for brute force
 *  "subfile" (Optional, string) : Subdomain wordlist file

#### Usage examples:
##### 1: Basic DNS enumeration
\`\`\`json
{
    "thoughts": ["Enumerating DNS records for target"],
    "tool_name": "dnsenum_tool",
    "tool_args": {
        "domain": "target.com"
    }
}
\`\`\`

##### 2: Subdomain brute force
\`\`\`json
{
    "thoughts": ["Brute forcing subdomains"],
    "tool_name": "dnsenum_tool",
    "tool_args": {
        "domain": "target.com",
        "subfile": "/usr/share/wordlists/dnsmap.txt",
        "threads": 10
    }
}
\`\`\`
