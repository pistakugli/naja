### sslscan_tool:
SSL/TLS configuration analyzer. Test cipher suites, protocols, and certificate validity.

#### Arguments:
 *  "target" (string) : Target host:port
 *  "show_certificate" (Optional, boolean) : Display certificate details
 *  "check_ciphers" (Optional, boolean) : Test supported ciphers

#### Usage examples:
##### 1: Basic SSL scan
\`\`\`json
{
    "thoughts": ["Checking SSL/TLS configuration"],
    "tool_name": "sslscan_tool",
    "tool_args": {
        "target": "target.com:443"
    }
}
\`\`\`

##### 2: Detailed certificate check
\`\`\`json
{
    "thoughts": ["Analyzing certificate and ciphers"],
    "tool_name": "sslscan_tool",
    "tool_args": {
        "target": "target.com:443",
        "show_certificate": true,
        "check_ciphers": true
    }
}
\`\`\`
