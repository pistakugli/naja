### chat_history:
Retrieve recent conversation history.

#### Arguments:
 *  "n" (integer) : Number of recent chats to retrieve (1-20)
 *  "sort_order" (Optional, string) : "desc" (newest first) or "asc"

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Getting last 5 conversations"],
    "tool_name": "chat_history",
    "tool_args": {
        "n": 5,
        "sort_order": "desc"
    }
}
\`\`\`
