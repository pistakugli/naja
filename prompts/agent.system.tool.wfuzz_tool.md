### wfuzz_tool:
Advanced web application fuzzer. Test for security vulnerabilities by fuzzing parameters, headers, and POST data.

⚠️ Only fuzz applications you own or have authorization to test.

#### Arguments:
 *  "url" (string) : Target URL with FUZZ keyword(s)
 *  "wordlist" (string) : Path to wordlist
 *  "method" (Optional, string) : HTTP method (GET, POST, PUT, DELETE)
 *  "data" (Optional, string) : POST data with FUZZ keyword
 *  "headers" (Optional, string) : Custom headers
 *  "hide_code" (Optional, string) : Hide responses with specific status codes

#### Usage examples:
##### 1: Directory fuzzing
\`\`\`json
{
    "thoughts": ["Fuzzing for hidden paths"],
    "tool_name": "wfuzz_tool",
    "tool_args": {
        "url": "http://target.com/FUZZ",
        "wordlist": "/usr/share/wfuzz/wordlist/general/common.txt",
        "hide_code": "404"
    }
}
\`\`\`

##### 2: POST parameter fuzzing
\`\`\`json
{
    "thoughts": ["Testing POST parameters for SQL injection"],
    "tool_name": "wfuzz_tool",
    "tool_args": {
        "url": "http://target.com/login",
        "wordlist": "/usr/share/seclists/Fuzzing/SQLi/Generic-SQLi.txt",
        "method": "POST",
        "data": "username=admin&password=FUZZ"
    }
}
\`\`\`
