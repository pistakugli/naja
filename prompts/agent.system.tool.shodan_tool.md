### shodan_tool:
Shodan search engine for Internet-connected devices. Discover exposed services and vulnerabilities.

⚠️ Requires Shodan API key. Only scan infrastructure you own or have authorization to investigate.

#### Arguments:
 *  "query" (string) : Shodan search query
 *  "facets" (Optional, string) : Facets to get summary stats (e.g., "country,port")
 *  "count" (Optional, boolean) : Just return count, not results

#### Usage examples:
##### 1: Search for organization
\`\`\`json
{
    "thoughts": ["Finding exposed services for authorized organization"],
    "tool_name": "shodan_tool",
    "tool_args": {
        "query": "org:\"Acme Corp\""
    }
}
\`\`\`

##### 2: Find vulnerable services
\`\`\`json
{
    "thoughts": ["Searching for vulnerable versions"],
    "tool_name": "shodan_tool",
    "tool_args": {
        "query": "apache 2.4.49",
        "facets": "country,port"
    }
}
\`\`\`

##### 3: Count results
\`\`\`json
{
    "thoughts": ["Checking exposure count"],
    "tool_name": "shodan_tool",
    "tool_args": {
        "query": "net:203.0.113.0/24",
        "count": true
    }
}
\`\`\`
