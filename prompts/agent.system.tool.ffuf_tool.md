### ffuf_tool:
Fast web fuzzer for discovering hidden files, directories, and parameters. Ultra-fast alternative to dirb/gobuster.

⚠️ Only use for AUTHORIZED security testing. Unauthorized testing is ILLEGAL.

#### Arguments:
 *  "url" (string) : Target URL with FUZZ keyword placeholder
 *  "wordlist" (string) : Path to wordlist file
 *  "method" (Optional, string) : HTTP method (GET, POST, PUT, DELETE)
 *  "extensions" (Optional, string) : File extensions to append (e.g., "php,html,txt")
 *  "filter_status" (Optional, string) : Filter responses by status code
 *  "match_status" (Optional, string) : Match only specific status codes
 *  "threads" (Optional, integer) : Number of threads (default: 40)

#### Usage examples:
##### 1: Directory discovery
\`\`\`json
{
    "thoughts": ["Scanning authorized target for hidden directories"],
    "tool_name": "ffuf_tool",
    "tool_args": {
        "url": "http://target.com/FUZZ",
        "wordlist": "/usr/share/wordlists/dirb/common.txt",
        "match_status": "200,301,302,403"
    }
}
\`\`\`

##### 2: File discovery with extensions
\`\`\`json
{
    "thoughts": ["Finding config files on target"],
    "tool_name": "ffuf_tool",
    "tool_args": {
        "url": "http://target.com/FUZZ",
        "wordlist": "/usr/share/wordlists/dirb/common.txt",
        "extensions": "php,txt,conf,bak",
        "filter_status": "404"
    }
}
\`\`\`

##### 3: Parameter fuzzing
\`\`\`json
{
    "thoughts": ["Testing for GET parameters"],
    "tool_name": "ffuf_tool",
    "tool_args": {
        "url": "http://target.com/page.php?FUZZ=test",
        "wordlist": "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt",
        "match_status": "200"
    }
}
\`\`\`
