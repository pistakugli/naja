### calendar_event_create:

Creates calendar events directly in user's calendar app. Use for scheduling meetings, appointments, reminders, or any time-based activities.
Can create single events or recurring events (daily, weekly, monthly, yearly).
Supports event details: title, description, location, attendees, reminders.
Always check current time first using user_time tool to understand relative dates.

**When to use:**
- User says "schedule", "add to calendar", "book time", "remind me"
- Creating meetings or appointments
- Setting up recurring events
- Scheduling deliverables or deadlines

**Usage - Simple event:**
```json
{
  "thoughts": ["User wants to schedule a meeting tomorrow at 2 PM"],
  "headline": "Creating calendar event for team meeting",
  "tool_name": "calendar_event_create",
  "tool_args": {
    "new_events": [{
      "title": "Team Meeting",
      "start_time": "2026-01-15T14:00:00Z",
      "end_time": "2026-01-15T15:00:00Z",
      "event_description": "Weekly team sync",
      "location": "Conference Room A"
    }]
  }
}
```

**Usage - Recurring event with reminders:**
```json
{
  "thoughts": ["User wants weekly standup every Monday"],
  "headline": "Creating recurring weekly standup",
  "tool_name": "calendar_event_create",
  "tool_args": {
    "new_events": [{
      "title": "Weekly Standup",
      "start_time": "2026-01-20T09:00:00Z",
      "end_time": "2026-01-20T09:30:00Z",
      "recurrence": {
        "frequency": "weekly",
        "days_of_week": ["MO"],
        "human_readable_frequency": "Every Monday",
        "rrule": "FREQ=WEEKLY;BYDAY=MO"
      },
      "nudges": [{
        "method": "notification",
        "minutes_before": 15
      }]
    }]
  }
}
```
