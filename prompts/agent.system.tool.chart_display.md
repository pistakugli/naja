### chart_display:

Creates inline charts and graphs from data. Essential for health queries, time-series data, trends, comparisons, and dashboards.
Supports line charts, bar charts, and scatter plots.
Can display multiple data series with custom colors and formatting.

**IMPORTANT:** Always use this tool for health/fitness data with multiple points. Don't just list numbers - visualize them!

**When to use:**
- ANY health query with time-series data (steps, weight, sleep, etc.)
- Comparing multiple metrics
- Showing trends over time
- Displaying dashboards or summaries
- Skip only for simple single-number answers like "steps today"

**Usage - Line chart:**
```json
{
  "thoughts": ["User wants to see their step count over the last week"],
  "headline": "Displaying step count chart",
  "tool_name": "chart_display",
  "tool_args": {
    "title": "Daily Steps - Last 7 Days",
    "style": "line",
    "series": [{
      "name": "Steps",
      "values": ["8234", "10567", "9823", "7654", "11234", "9876", "10123"]
    }],
    "x_axis": {
      "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    },
    "y_axis": {
      "title": "Steps"
    }
  }
}
```

**Usage - Multiple series:**
```json
{
  "thoughts": ["Comparing weight and body fat percentage over time"],
  "headline": "Body composition trends",
  "tool_name": "chart_display",
  "tool_args": {
    "title": "Body Composition - January",
    "style": "line",
    "series": [
      {
        "name": "Weight (kg)",
        "values": ["75.2", "74.8", "74.5", "74.3"],
        "color": "#3498db"
      },
      {
        "name": "Body Fat %",
        "values": ["18.5", "18.2", "17.9", "17.8"],
        "color": "#e74c3c"
      }
    ],
    "x_axis": {
      "data": ["Week 1", "Week 2", "Week 3", "Week 4"]
    }
  }
}
```
