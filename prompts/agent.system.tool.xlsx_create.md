### xlsx_create:

Creates Excel spreadsheets (.xlsx) with formulas, formatting, and analysis.

**⚠️ CRITICAL WORKFLOW:**

**STEP 1: Read Skill**
```json
{
  "thoughts": ["Reading xlsx skill for spreadsheet best practices and formulas"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/public/xlsx/SKILL.md | head -200"
  }
}
```

**STEP 2: Create Spreadsheet**
```json
{
  "thoughts": ["Creating Excel spreadsheet with formulas and professional formatting"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from openpyxl import Workbook\nfrom openpyxl.styles import Font, PatternFill, Alignment\n\n# Create workbook\nwb = Workbook()\nws = wb.active\nws.title = 'Data'\n\n# Headers with formatting\nheaders = ['Item', 'Quantity', 'Price', 'Total']\nfor col, header in enumerate(headers, start=1):\n    cell = ws.cell(row=1, column=col)\n    cell.value = header\n    cell.font = Font(bold=True)\n    cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')\n\n# Data with formulas\nws['A2'] = 'Item 1'\nws['B2'] = 10\nws['C2'] = 5.99\nws['D2'] = '=B2*C2'  # Formula\n\n# Save\nwb.save('/root/spreadsheet.xlsx')\nprint('✅ Spreadsheet created: /root/spreadsheet.xlsx')"
  }
}
```

**WHEN TO USE:**
- "Create spreadsheet/Excel file"
- Data analysis, financial models, tracking sheets
- Any tabular data with calculations

**KEY CAPABILITIES:**
- Formulas (SUM, AVERAGE, IF, VLOOKUP, etc.)
- Cell formatting (fonts, colors, borders)
- Conditional formatting
- Charts and graphs
- Multiple sheets
- Data validation

**COMMON FORMULAS:**
- `=SUM(A1:A10)` - Sum range
- `=AVERAGE(B2:B20)` - Average
- `=IF(C2>100, "High", "Low")` - Conditional
- `=VLOOKUP(D2, A:B, 2, FALSE)` - Lookup

**FILE LOCATION:**
Always save to: `/root/filename.xlsx`

**EXAMPLE - Vulnerability Tracker:**
1. Read skill for formula and formatting techniques
2. Create sheets:
   - Headers: Vulnerability, Severity, Status, Date Found
   - Conditional formatting for severity (Red=Critical, Yellow=Medium, Green=Low)
   - Summary sheet with COUNT formulas
   - Charts showing vulnerability distribution

**LIBRARIES:**
- `openpyxl` for .xlsx files
- `pandas` for data manipulation (optional)

This uses code_execution_tool with Python runtime.
