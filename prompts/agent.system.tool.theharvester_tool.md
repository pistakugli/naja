### theharvester_tool:
OSINT tool for gathering emails, subdomains, hosts, employee names, and more from public sources.

⚠️ Only gather information for authorized reconnaissance. Respect privacy laws.

#### Arguments:
 *  "domain" (string) : Target domain
 *  "sources" (string) : Data sources: "all", "google", "bing", "linkedin", "twitter", "shodan", "certspotter"
 *  "limit" (Optional, integer) : Limit results per source (default: 500)
 *  "dns" (Optional, boolean) : Perform DNS lookups

#### Usage examples:
##### 1: Basic email harvesting
\`\`\`json
{
    "thoughts": ["Gathering public emails for target domain"],
    "tool_name": "theharvester_tool",
    "tool_args": {
        "domain": "target.com",
        "sources": "google,bing,linkedin"
    }
}
\`\`\`

##### 2: Subdomain enumeration
\`\`\`json
{
    "thoughts": ["Finding subdomains from multiple sources"],
    "tool_name": "theharvester_tool",
    "tool_args": {
        "domain": "target.com",
        "sources": "all",
        "dns": true
    }
}
\`\`\`
