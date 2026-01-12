### alarm_creator:
Create alarms for specific times (daily recurring or one-time).

#### Arguments:
 *  "hour" (integer) : Hour in 24-hour format (0-23)
 *  "minute" (integer) : Minute (0-59)
 *  "message" (string) : Alarm label/message
 *  "days" (Optional, array) : Days to repeat (1=Sunday, 7=Saturday)

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Setting morning alarm"],
    "tool_name": "alarm_creator",
    "tool_args": {
        "hour": 7,
        "minute": 30,
        "message": "Wake up",
        "days": [2, 3, 4, 5, 6]
    }
}
\`\`\`
