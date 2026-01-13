### zaproxy_tool:
OWASP ZAP (Zed Attack Proxy) - Automated web application security scanner and proxy.

⚠️ Only scan web applications you own or have written permission to test.

#### Arguments:
 *  "url" (string) : Target URL
 *  "scan_type" (Optional, string) : "spider" (crawl site), "active" (active scan), "passive" (passive scan), "full" (spider + active)
 *  "ajax_spider" (Optional, boolean) : Use AJAX spider for JavaScript-heavy apps
 *  "report_format" (Optional, string) : Output format: "html", "xml", "json", "md"

#### Usage examples:
##### 1: Quick spider scan
\`\`\`json
{
    "thoughts": ["Crawling target to discover pages"],
    "tool_name": "zaproxy_tool",
    "tool_args": {
        "url": "http://target.com",
        "scan_type": "spider"
    }
}
\`\`\`

##### 2: Full security scan
\`\`\`json
{
    "thoughts": ["Complete security assessment of authorized target"],
    "tool_name": "zaproxy_tool",
    "tool_args": {
        "url": "http://target.com",
        "scan_type": "full",
        "ajax_spider": true,
        "report_format": "html"
    }
}
\`\`\`
