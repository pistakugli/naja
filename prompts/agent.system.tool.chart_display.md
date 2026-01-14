### chart_display:

Creates inline charts and graphs for data visualization.

**WORKFLOW:**

**Create Chart with matplotlib/plotly:**
```json
{
  "thoughts": ["Creating chart to visualize data trends"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "import matplotlib.pyplot as plt\n\n# Data\nx = [1, 2, 3, 4, 5]\ny = [10, 25, 20, 30, 45]\n\n# Create chart\nplt.figure(figsize=(10, 6))\nplt.plot(x, y, marker='o')\nplt.title('Data Trend')\nplt.xlabel('Time')\nplt.ylabel('Value')\nplt.grid(True)\n\n# Save\nplt.savefig('/root/chart.png')\nprint('✅ Chart created: /root/chart.png')"
  }
}
```

**WHEN TO USE:**
- "Show me a chart/graph"
- Data visualization requests
- Trend analysis
- Comparing metrics

**CHART TYPES:**
- Line charts (trends over time)
- Bar charts (comparisons)
- Pie charts (proportions)
- Scatter plots (correlations)
- Heatmaps (2D data)

**LIBRARIES:**
- `matplotlib` for static charts
- `plotly` for interactive charts
- `seaborn` for statistical visualizations

**FILE LOCATION:**
Save to: `/root/chart.png`

**EXAMPLE - Security Scan Results:**
```python
import matplotlib.pyplot as plt

severities = ['Critical', 'High', 'Medium', 'Low']
counts = [5, 12, 28, 41]

plt.bar(severities, counts, color=['red', 'orange', 'yellow', 'green'])
plt.title('Vulnerability Distribution')
plt.savefig('/root/vuln_chart.png')
```

This uses code_execution_tool with Python runtime.
