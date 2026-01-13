### testssl_tool:
Comprehensive TLS/SSL testing. Check for vulnerabilities, cipher strength, and protocol support.

#### Arguments:
 *  "target" (string) : Target host:port
 *  "protocols" (Optional, boolean) : Test SSL/TLS protocols
 *  "ciphers" (Optional, boolean) : Test cipher suites
 *  "vulnerabilities" (Optional, boolean) : Test for known vulnerabilities (Heartbleed, POODLE, etc.)

#### Usage examples:
##### 1: Full TLS assessment
\`\`\`json
{
    "thoughts": ["Complete TLS security assessment"],
    "tool_name": "testssl_tool",
    "tool_args": {
        "target": "target.com:443",
        "protocols": true,
        "ciphers": true,
        "vulnerabilities": true
    }
}
\`\`\`

##### 2: Vulnerability scan only
\`\`\`json
{
    "thoughts": ["Testing for SSL/TLS vulnerabilities"],
    "tool_name": "testssl_tool",
    "tool_args": {
        "target": "target.com:443",
        "vulnerabilities": true
    }
}
\`\`\`
