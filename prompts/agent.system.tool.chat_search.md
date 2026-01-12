### chat_search:
Search through past conversation history by keywords.

#### Arguments:
 *  "query" (string) : Search keywords
 *  "max_results" (Optional, integer) : Maximum results (1-20)

#### Usage examples:
\`\`\`json
{
    "thoughts": ["User mentioned AI models before, searching history"],
    "tool_name": "chat_search",
    "tool_args": {
        "query": "AI models machine learning",
        "max_results": 5
    }
}
\`\`\`
