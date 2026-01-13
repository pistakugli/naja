### commix_tool:
Automatic command injection and exploitation tool. Test web applications for OS command injection vulnerabilities.

⚠️ CRITICAL: Only test applications you own. Command injection can cause serious damage.

#### Arguments:
 *  "url" (string) : Target URL
 *  "data" (Optional, string) : POST data
 *  "cookie" (Optional, string) : Session cookie
 *  "level" (Optional, integer) : Test level (1-3, default: 1)
 *  "technique" (Optional, string) : Injection technique: "classic", "eval-based", "time-based", "file-based"

#### Usage examples:
##### 1: Test GET parameter
\`\`\`json
{
    "thoughts": ["Testing for command injection in parameter"],
    "tool_name": "commix_tool",
    "tool_args": {
        "url": "http://target.com/page.php?cmd=ping",
        "level": 1
    }
}
\`\`\`

##### 2: Test POST data
\`\`\`json
{
    "thoughts": ["Testing POST form for OS command injection"],
    "tool_name": "commix_tool",
    "tool_args": {
        "url": "http://target.com/submit",
        "data": "input=test",
        "technique": "time-based"
    }
}
\`\`\`
