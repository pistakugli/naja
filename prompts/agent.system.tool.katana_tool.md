### katana_tool:
Next-generation web crawler. Fast, customizable web crawling and spidering.

#### Arguments:
 *  "url" (string) : Target URL
 *  "depth" (Optional, integer) : Crawl depth (default: 2)
 *  "js_crawl" (Optional, boolean) : Enable JavaScript parsing
 *  "output" (Optional, string) : Output file for discovered URLs

#### Usage examples:
##### 1: Basic crawl
\`\`\`json
{
    "thoughts": ["Crawling target application"],
    "tool_name": "katana_tool",
    "tool_args": {
        "url": "https://target.com",
        "depth": 3
    }
}
\`\`\`

##### 2: JavaScript-heavy app
\`\`\`json
{
    "thoughts": ["Crawling SPA with JavaScript parsing"],
    "tool_name": "katana_tool",
    "tool_args": {
        "url": "https://app.target.com",
        "js_crawl": true,
        "depth": 5,
        "output": "/tmp/crawled_urls.txt"
    }
}
\`\`\`
