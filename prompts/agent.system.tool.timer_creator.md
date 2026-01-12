### timer_creator:
Create countdown timers for specified duration.

#### Arguments:
 *  "duration_seconds" (integer) : Timer duration in seconds
 *  "message" (string) : Timer label

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Setting 5 minute timer"],
    "tool_name": "timer_creator",
    "tool_args": {
        "duration_seconds": 300,
        "message": "Check oven"
    }
}
\`\`\`
