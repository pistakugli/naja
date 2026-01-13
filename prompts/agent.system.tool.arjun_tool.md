### arjun_tool:
HTTP parameter discovery suite. Find hidden GET/POST parameters.

⚠️ Only test applications you own or have authorization to test.

#### Arguments:
 *  "url" (string) : Target URL
 *  "method" (Optional, string) : HTTP method: "GET", "POST", "JSON"
 *  "wordlist" (Optional, string) : Custom parameter wordlist
 *  "threads" (Optional, integer) : Number of threads (default: 5)

#### Usage examples:
##### 1: GET parameter discovery
\`\`\`json
{
    "thoughts": ["Finding hidden GET parameters"],
    "tool_name": "arjun_tool",
    "tool_args": {
        "url": "https://target.com/api/user",
        "method": "GET"
    }
}
\`\`\`

##### 2: POST parameter discovery
\`\`\`json
{
    "thoughts": ["Discovering POST parameters"],
    "tool_name": "arjun_tool",
    "tool_args": {
        "url": "https://target.com/login",
        "method": "POST",
        "threads": 10
    }
}
\`\`\`
