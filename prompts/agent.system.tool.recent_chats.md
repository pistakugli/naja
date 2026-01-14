### recent_chats:

Retrieves recent chat conversations with customizable sorting and filtering.
Use for time-based queries like "what did we discuss yesterday" or "show recent chats".
Can paginate through results and filter by date range.

**When to use:**
- "What did we talk about yesterday/last week?"
- "Show me recent conversations"
- "Continue our last chat"
- Time-based conversation retrieval
- Getting context from recent discussions

**Usage - Last few chats:**
```json
{
  "thoughts": ["User wants to see what we discussed recently"],
  "headline": "Retrieving last 5 conversations",
  "tool_name": "recent_chats",
  "tool_args": {
    "n": 5,
    "sort_order": "desc"
  }
}
```

**Usage - Specific date range:**
```json
{
  "thoughts": ["User wants chats from last week"],
  "headline": "Fetching last week's conversations",
  "tool_name": "recent_chats",
  "tool_args": {
    "n": 20,
    "after": "2026-01-07T00:00:00Z",
    "before": "2026-01-13T23:59:59Z",
    "sort_order": "asc"
  }
}
```
