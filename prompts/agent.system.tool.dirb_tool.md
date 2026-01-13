### dirb_tool:
Web content scanner. Brute force directories and files on web servers using wordlist-based attack.

⚠️ Only scan web servers you own or have explicit permission to test.

#### Arguments:
 *  "url" (string) : Target URL
 *  "wordlist" (Optional, string) : Path to wordlist (default: /usr/share/dirb/wordlists/common.txt)
 *  "extensions" (Optional, string) : File extensions to search (e.g., ".php,.html,.txt")
 *  "save_output" (Optional, string) : Save results to file

#### Usage examples:
##### 1: Basic directory scan
\`\`\`json
{
    "thoughts": ["Finding hidden directories on authorized target"],
    "tool_name": "dirb_tool",
    "tool_args": {
        "url": "http://target.com"
    }
}
\`\`\`

##### 2: Scan with custom wordlist and extensions
\`\`\`json
{
    "thoughts": ["Looking for config files"],
    "tool_name": "dirb_tool",
    "tool_args": {
        "url": "http://target.com",
        "wordlist": "/usr/share/wordlists/dirb/big.txt",
        "extensions": ".conf,.bak,.old"
    }
}
\`\`\`
