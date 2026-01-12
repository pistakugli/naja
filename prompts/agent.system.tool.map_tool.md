### map_tool:
Display locations on a map with markers.

#### Arguments:
 *  "markers" (array) : Array of marker objects with latitude, longitude, title
 *  "title" (Optional, string) : Map title

#### Usage examples:
\`\`\`json
{
    "thoughts": ["Showing restaurant locations"],
    "tool_name": "map_tool",
    "tool_args": {
        "title": "Nearby Restaurants",
        "markers": [
            {"latitude": "40.7128", "longitude": "-74.0060", "title": "Restaurant A"},
            {"latitude": "40.7580", "longitude": "-73.9855", "title": "Restaurant B"}
        ]
    }
}
\`\`\`
