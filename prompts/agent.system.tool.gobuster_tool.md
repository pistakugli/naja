### gobuster_tool:
Fast directory, DNS, and vhost brute forcer. For authorized web application testing.

⚠️ Only use on web applications you own or have authorization to test.

#### Arguments:
 *  "mode" (string) : Mode: "dir" (directories), "dns" (subdomains), "vhost" (virtual hosts)
 *  "url" (string) : Target URL or domain
 *  "wordlist" (Optional, string) : Wordlist path (default: /usr/share/wordlists/dirb/common.txt)
 *  "extensions" (Optional, string) : File extensions for dir mode (e.g., "php,html,txt")

#### Usage examples:
##### 1: Directory brute force
\`\`\`json
{
    "thoughts": ["Finding hidden directories on authorized site"],
    "tool_name": "gobuster_tool",
    "tool_args": {
        "mode": "dir",
        "url": "http://testsite.local",
        "extensions": "php,html,txt"
    }
}
\`\`\`

##### 2: Subdomain enumeration
\`\`\`json
{
    "thoughts": ["Discovering subdomains"],
    "tool_name": "gobuster_tool",
    "tool_args": {
        "mode": "dns",
        "url": "example.com",
        "wordlist": "/usr/share/wordlists/subdomains.txt"
    }
}
\`\`\`
