### event_manager:
Manage calendar events - create, update, or delete events.

#### Arguments:
 *  "action" (string) : Action to perform - "create", "update", or "delete"
 *  "title" (string) : Event title
 *  "start_time" (string) : Start time in ISO format
 *  "end_time" (Optional, string) : End time
 *  "description" (Optional, string) : Event description
 *  "location" (Optional, string) : Event location

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Creating calendar event"],
    "tool_name": "event_manager",
    "tool_args": {
        "action": "create",
        "title": "Team Meeting",
        "start_time": "2026-01-15T14:00:00",
        "end_time": "2026-01-15T15:00:00",
        "location": "Conference Room A"
    }
}
\`\`\`
