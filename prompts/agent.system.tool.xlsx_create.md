### xlsx_create:

Creates and edits Microsoft Excel (.xlsx) spreadsheets with formulas, formatting, and data analysis.
Supports complex formulas, pivot tables, charts, conditional formatting.
Can create financial models, data analysis, tracking sheets.

**When to use:**
- "Create a spreadsheet"
- User needs calculations or data analysis
- Budget tracking, financial modeling
- Data organization with formulas
- Any tabular data that needs Excel features

**Important:**
- Read /mnt/skills/public/xlsx/SKILL.md BEFORE creating spreadsheets
- Use formulas for calculations (SUM, AVERAGE, IF, VLOOKUP, etc.)
- Apply appropriate formatting (currency, dates, percentages)
- Can read existing Excel files and modify them

**Capabilities:**
- Formulas and functions (300+ Excel functions)
- Multiple sheets/tabs
- Charts and graphs
- Conditional formatting
- Data validation
- Pivot tables
- Named ranges
- Cell styling and formatting

**Usage:**
```json
{
  "thoughts": ["User needs a budget tracker with automatic calculations"],
  "headline": "Creating budget spreadsheet with formulas",
  "tool_name": "xlsx_create",
  "tool_args": {
    "filename": "monthly_budget.xlsx",
    "sheets": [
      {
        "name": "January",
        "data": [
          ["Category", "Budgeted", "Actual", "Difference"],
          ["Housing", "=1500", "=1450", "=B2-C2"],
          ["Food", "=500", "=485", "=B3-C3"]
        ],
        "formatting": {
          "B:C": {"number_format": "$#,##0.00"},
          "A1:D1": {"bold": true, "bg_color": "#4472C4"}
        }
      }
    ]
  }
}
```
