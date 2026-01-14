### pdf_create:

Creates PDF documents from content or fills PDF forms.

**⚠️ CRITICAL WORKFLOW:**

**STEP 1: Read Skill**
```json
{
  "thoughts": ["Reading pdf skill for creation and form-filling techniques"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/public/pdf/SKILL.md | head -200"
  }
}
```

**STEP 2A: Create PDF from Content**
```json
{
  "thoughts": ["Creating PDF document with professional formatting"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from reportlab.lib.pagesizes import letter\nfrom reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table\nfrom reportlab.lib.styles import getSampleStyleSheet\nfrom reportlab.lib.units import inch\n\n# Create PDF\ndoc = SimpleDocTemplate('/root/output.pdf', pagesize=letter)\nstory = []\nstyles = getSampleStyleSheet()\n\n# Title\ntitle = Paragraph('Document Title', styles['Title'])\nstory.append(title)\nstory.append(Spacer(1, 0.2*inch))\n\n# Content\ncontent = Paragraph('Content goes here...', styles['Normal'])\nstory.append(content)\n\n# Build\ndoc.build(story)\nprint('✅ PDF created: /root/output.pdf')"
  }
}
```

**STEP 2B: Fill PDF Form**
```json
{
  "thoughts": ["Filling PDF form fields with provided data"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from fillpdf import fillpdfs\n\n# Fill form\ndata = {\n    'field_name_1': 'value1',\n    'field_name_2': 'value2'\n}\n\nfillpdfs.write_fillable_pdf('input_form.pdf', '/root/filled_form.pdf', data)\nprint('✅ PDF form filled: /root/filled_form.pdf')"
  }
}
```

**WHEN TO USE:**
- "Create PDF", "fill out form"
- Final documents, form completion
- Converting content to PDF format

**KEY CAPABILITIES:**
- Create PDFs from scratch
- Fill interactive PDF forms
- Extract text/tables from PDFs
- Merge/split PDFs
- Add watermarks

**FILE LOCATION:**
Always save to: `/root/filename.pdf`

**LIBRARIES:**
- `reportlab` for PDF creation
- `PyPDF2` for manipulation
- `fillpdf` for form filling

This uses code_execution_tool with Python runtime.
