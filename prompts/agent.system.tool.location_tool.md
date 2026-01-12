### location_tool:
Get user's current geographic location.

#### Arguments:
 *  "accuracy" (Optional, string) : "precise" or "approximate"

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Need user location for weather"],
    "tool_name": "location_tool",
    "tool_args": {
        "accuracy": "approximate"
    }
}
\`\`\`
