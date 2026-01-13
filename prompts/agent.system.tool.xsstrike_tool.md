### xsstrike_tool:
Advanced XSS (Cross-Site Scripting) detection suite with fuzzing and WAF bypass capabilities.

⚠️ Only test for XSS on applications you own or have authorization to test.

#### Arguments:
 *  "url" (string) : Target URL
 *  "data" (Optional, string) : POST data
 *  "crawl" (Optional, boolean) : Crawl target for forms
 *  "fuzzer" (Optional, boolean) : Enable fuzzer mode
 *  "blind" (Optional, boolean) : Test for blind XSS

#### Usage examples:
##### 1: Basic XSS scan
\`\`\`json
{
    "thoughts": ["Testing parameter for XSS"],
    "tool_name": "xsstrike_tool",
    "tool_args": {
        "url": "http://target.com/search?q=test"
    }
}
\`\`\`

##### 2: Crawl and fuzz
\`\`\`json
{
    "thoughts": ["Complete XSS assessment with fuzzing"],
    "tool_name": "xsstrike_tool",
    "tool_args": {
        "url": "http://target.com",
        "crawl": true,
        "fuzzer": true
    }
}
\`\`\`
