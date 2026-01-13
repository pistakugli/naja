### burp_suite_tool:
Industry-standard web application security testing. Automated scanning, crawling, and vulnerability detection.

⚠️ Only test web applications you own or have written authorization to test.

#### Arguments:
 *  "target" (string) : Target URL
 *  "scan_type" (string) : "crawl_and_audit", "crawl_only", "audit_only"
 *  "config_file" (Optional, string) : Path to Burp configuration file
 *  "report_file" (Optional, string) : Path to output report

#### Usage examples:
##### 1: Full automated scan
\`\`\`json
{
    "thoughts": ["Running comprehensive Burp Suite scan"],
    "tool_name": "burp_suite_tool",
    "tool_args": {
        "target": "https://app.target.com",
        "scan_type": "crawl_and_audit",
        "report_file": "/tmp/burp_report.html"
    }
}
\`\`\`

##### 2: Crawl only
\`\`\`json
{
    "thoughts": ["Mapping application structure"],
    "tool_name": "burp_suite_tool",
    "tool_args": {
        "target": "https://app.target.com",
        "scan_type": "crawl_only"
    }
}
\`\`\`
