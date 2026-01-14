### calendar_event_create:

Creates calendar events and reminders (output as .ics file).

**WORKFLOW:**
```json
{
  "thoughts": ["Creating calendar event for meeting"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from icalendar import Calendar, Event\nfrom datetime import datetime\n\ncal = Calendar()\nevent = Event()\nevent.add('summary', 'Meeting Title')\nevent.add('dtstart', datetime(2026, 1, 15, 14, 0, 0))\nevent.add('dtend', datetime(2026, 1, 15, 15, 0, 0))\nevent.add('description', 'Meeting description')\ncal.add_component(event)\n\nwith open('/root/event.ics', 'wb') as f:\n    f.write(cal.to_ical())\nprint('✅ Event created: /root/event.ics')"
  }
}
```

**WHEN TO USE:**
- "Schedule meeting/event"
- "Create calendar reminder"
- Event creation requests

**LIBRARY:**
- `icalendar` for .ics file creation

This uses code_execution_tool with Python runtime.
