### memory_edit:

Saves or updates information in long-term memory.

**WORKFLOW:**
```json
{
  "thoughts": ["Saving important information to memory"],
  "tool_name": "memory_save",
  "tool_args": {
    "title": "Brief title for this memory",
    "content": "Detailed information to remember"
  }
}
```

**WHEN TO USE:**
- User asks to remember something
- Important info worth saving
- Context for future conversations

**HOW IT WORKS:**
Uses Agent Zero's built-in memory_save tool.
Stores information in long-term memory database.
Can be retrieved later with conversation_search.

**EXAMPLE:**
User: "Remember that I work at Anthropic as a security researcher"
```json
{
  "thoughts": ["Saving user's work information to memory"],
  "tool_name": "memory_save",
  "tool_args": {
    "title": "User work information",
    "content": "User works at Anthropic as a security researcher"
  }
}
```

This uses existing memory_save tool.
