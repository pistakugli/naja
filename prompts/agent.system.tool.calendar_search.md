### calendar_search:

Searches and retrieves calendar events (from .ics files).

**WORKFLOW:**
```json
{
  "thoughts": ["Searching for calendar events"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from icalendar import Calendar\nfrom datetime import datetime\n\n# Read calendar file\nwith open('calendar.ics', 'rb') as f:\n    cal = Calendar.from_ical(f.read())\n\n# Search events\nfor component in cal.walk():\n    if component.name == 'VEVENT':\n        print(f\"Event: {component.get('summary')}\")\n        print(f\"Date: {component.get('dtstart').dt}\")"
  }
}
```

**WHEN TO USE:**
- "What's on my calendar?"
- "Find events"
- Calendar queries

This uses code_execution_tool with Python runtime.
