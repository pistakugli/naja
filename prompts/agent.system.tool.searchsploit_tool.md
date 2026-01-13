### searchsploit_tool:
Exploit database search tool. Search for exploits by software, version, CVE, or keyword.

#### Arguments:
 *  "search_term" (string) : Search query (software name, version, CVE number)
 *  "exact" (Optional, boolean) : Exact title match
 *  "www" (Optional, boolean) : Show exploit-db.com URLs
 *  "json" (Optional, boolean) : Output in JSON format

#### Usage examples:
##### 1: Search for WordPress exploits
\`\`\`json
{
    "thoughts": ["Finding WordPress vulnerabilities"],
    "tool_name": "searchsploit_tool",
    "tool_args": {
        "search_term": "WordPress 5.8"
    }
}
\`\`\`

##### 2: Search by CVE
\`\`\`json
{
    "thoughts": ["Looking up specific CVE exploit"],
    "tool_name": "searchsploit_tool",
    "tool_args": {
        "search_term": "CVE-2021-44228",
        "www": true
    }
}
\`\`\`
