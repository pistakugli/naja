### conversation_search:

Searches through past conversations with the user to find relevant context and information.
Use when user references past discussions or when historical context would improve the response.
Claude's memories update periodically, so recent conversations may not yet be reflected.

**When to use:**
- User says "as we discussed", "you mentioned before", "what did we talk about"
- User asks about past conversations or topics
- References to "our conversation about X"
- Questions about what Claude remembers
- User assumes shared knowledge without context

**Usage:**
```json
{
  "thoughts": ["User is asking about a topic we discussed before"],
  "headline": "Searching past conversations about Python debugging",
  "tool_name": "conversation_search",
  "tool_args": {
    "query": "Python debugging breakpoints",
    "max_results": 5
  }
}
```

```json
{
  "thoughts": ["User wants to know what we discussed about their project"],
  "headline": "Finding previous project discussions",
  "tool_name": "conversation_search",
  "tool_args": {
    "query": "machine learning project dataset",
    "max_results": 10
  }
}
```
