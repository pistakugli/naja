### recent_chats:

Retrieves recent conversation history.

**WORKFLOW:**
```json
{
  "thoughts": ["Loading recent chat history"],
  "tool_name": "chat_history",
  "tool_args": {}
}
```

**WHEN TO USE:**
- "What did we talk about recently?"
- "Show recent conversations"
- Context from previous chats

**HOW IT WORKS:**
Uses Agent Zero's built-in chat_history tool.
Returns recent messages from current conversation.

**EXAMPLE:**
User: "What were we discussing before?"
```json
{
  "thoughts": ["Retrieving recent conversation context"],
  "tool_name": "chat_history",
  "tool_args": {}
}
```

This uses existing chat_history tool.
