### dalfox_tool:
Powerful XSS scanner and fuzzer. Parameter analysis and XSS detection.

⚠️ Only test for XSS on applications you own or have authorization to test.

#### Arguments:
 *  "url" (string) : Target URL
 *  "data" (Optional, string) : POST data
 *  "cookie" (Optional, string) : Cookie header
 *  "blind" (Optional, string) : Blind XSS callback URL

#### Usage examples:
##### 1: GET parameter XSS
\`\`\`json
{
    "thoughts": ["Testing for XSS in GET parameters"],
    "tool_name": "dalfox_tool",
    "tool_args": {
        "url": "https://target.com/search?q=test"
    }
}
\`\`\`

##### 2: POST XSS with authentication
\`\`\`json
{
    "thoughts": ["Testing authenticated endpoint for XSS"],
    "tool_name": "dalfox_tool",
    "tool_args": {
        "url": "https://target.com/comment",
        "data": "comment=test",
        "cookie": "session=abc123"
    }
}
\`\`\`

##### 3: Blind XSS
\`\`\`json
{
    "thoughts": ["Testing for blind XSS vulnerabilities"],
    "tool_name": "dalfox_tool",
    "tool_args": {
        "url": "https://target.com/feedback",
        "blind": "https://myserver.com/callback"
    }
}
\`\`\`
