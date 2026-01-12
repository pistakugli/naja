### user_time:
Get current time and date information in specified timezone. Essential for scheduling and temporal reasoning.

!!! Always use this before creating events or alarms
!!! Provides ISO format timestamps for consistency

#### Arguments:
 *  "timezone" (Optional, string) : Timezone name (default: "UTC"). Examples: "America/New_York", "Europe/London", "Asia/Tokyo"

#### Usage examples:
##### 1: Get current time
\`\`\`json
{
    "thoughts": ["Need to know current time for scheduling"],
    "tool_name": "user_time",
    "tool_args": {
        "timezone": "UTC"
    }
}
\`\`\`

##### 2: Get time in specific timezone
\`\`\`json
{
    "thoughts": ["User is in New York, need local time"],
    "tool_name": "user_time",
    "tool_args": {
        "timezone": "America/New_York"
    }
}
\`\`\`
