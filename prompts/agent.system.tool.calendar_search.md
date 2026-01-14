### calendar_search:

Searches user's calendar events within a time range. Use to check schedule, find meetings, or see what's planned.
Can filter by calendar, date range, and event type.
Returns event details including title, time, location, attendees.

**When to use:**
- "What's on my calendar today/this week?"
- "Do I have any meetings tomorrow?"
- "Show me my schedule"
- "When is my next appointment?"

**Usage:**
```json
{
  "thoughts": ["User wants to see their schedule for today"],
  "headline": "Checking calendar for today's events",
  "tool_name": "calendar_search",
  "tool_args": {
    "start_time": "2026-01-14T00:00:00Z",
    "end_time": "2026-01-14T23:59:59Z",
    "limit": 50
  }
}
```

```json
{
  "thoughts": ["User wants to check if they're free tomorrow afternoon"],
  "headline": "Searching calendar for tomorrow afternoon",
  "tool_name": "calendar_search",
  "tool_args": {
    "start_time": "2026-01-15T12:00:00Z",
    "end_time": "2026-01-15T18:00:00Z"
  }
}
```
