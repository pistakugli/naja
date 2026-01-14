### conversation_search:

Searches past conversations and chat history by keywords.

**WORKFLOW:**
```json
{
  "thoughts": ["Searching memory for previous discussions about topic"],
  "tool_name": "memory_load",
  "tool_args": {
    "query": "search keywords here"
  }
}
```

**WHEN TO USE:**
- "What did we discuss about X?"
- "Find previous conversation"
- Retrieving past context

**HOW IT WORKS:**
Uses Agent Zero's built-in memory_load tool with search query.
Searches through conversation history and saved memories.

**EXAMPLE:**
User: "What did we discuss about SQL injection?"
```json
{
  "thoughts": ["Searching memory for SQL injection discussions"],
  "tool_name": "memory_load",
  "tool_args": {
    "query": "SQL injection"
  }
}
```

This uses existing memory_load tool.
