### sqlmap_tool:
Automatic SQL injection detection and exploitation tool. For authorized web application testing.

⚠️ Only test applications you own or have written authorization to test.

#### Arguments:
 *  "url" (string) : Target URL to test
 *  "data" (Optional, string) : POST data
 *  "technique" (Optional, string) : SQL injection technique (B=Boolean, E=Error, U=Union, S=Stacked, T=Time)

#### Usage examples:
##### 1: Test GET parameter
\`\`\`json
{
    "thoughts": ["Testing authorized site for SQL injection"],
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "http://testsite.local/page.php?id=1"
    }
}
\`\`\`

##### 2: Test POST request
\`\`\`json
{
    "thoughts": ["Testing login form for SQL injection"],
    "tool_name": "sqlmap_tool",
    "tool_args": {
        "url": "http://testsite.local/login.php",
        "data": "username=admin&password=pass"
    }
}
\`\`\`
