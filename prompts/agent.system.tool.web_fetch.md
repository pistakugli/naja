### web_fetch:
Fetch complete content from a web page URL. Simpler and faster than browser_agent for basic content extraction.

!!! Use this for quick page content retrieval
!!! For JavaScript-heavy sites, use browser_agent instead

#### Arguments:
 *  "url" (string) : The full URL to fetch (must start with http:// or https://)
 *  "extract_text" (Optional, boolean) : Extract clean text from HTML (default: true)
 *  "max_length" (Optional, integer) : Maximum content length in characters (default: 50000)

#### Usage examples:
##### 1: Fetch article content
\`\`\`json
{
    "thoughts": ["User wants content from this article", "I'll fetch and extract clean text"],
    "tool_name": "web_fetch",
    "tool_args": {
        "url": "https://example.com/article",
        "extract_text": true
    }
}
\`\`\`

##### 2: Fetch raw HTML
\`\`\`json
{
    "thoughts": ["Need to analyze the HTML structure"],
    "tool_name": "web_fetch",
    "tool_args": {
        "url": "https://example.com",
        "extract_text": false
    }
}
\`\`\`
