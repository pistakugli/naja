### pdf_create:

Creates PDF documents from scratch or fills in PDF forms.
Can extract text from PDFs, merge/split documents, add annotations.
Use for final documents, forms, or read-only content.

**When to use:**
- "Create a PDF"
- Fill in a PDF form
- Extract text from a PDF
- Merge multiple PDFs
- User needs a final, non-editable document

**Important:**
- Read /mnt/skills/public/pdf/SKILL.md for complete capabilities
- Use for FINAL documents (use docx for editing)
- Can fill in interactive PDF forms
- Extract text and tables from existing PDFs

**Capabilities:**
- Create PDFs from content
- Fill in PDF forms
- Extract text and tables
- Merge/split PDFs
- Add annotations and comments
- Password protection
- Compress PDFs

**Usage - Create PDF:**
```json
{
  "thoughts": ["User wants a final PDF report"],
  "headline": "Creating PDF report",
  "tool_name": "pdf_create",
  "tool_args": {
    "filename": "security_report.pdf",
    "content": {
      "title": "Security Assessment Report",
      "sections": [...]
    },
    "options": {
      "page_size": "A4",
      "margin": "1in"
    }
  }
}
```

**Usage - Fill PDF form:**
```json
{
  "thoughts": ["User needs to fill in a tax form"],
  "headline": "Filling PDF form fields",
  "tool_name": "pdf_create",
  "tool_args": {
    "input_pdf": "/path/to/form.pdf",
    "output_pdf": "filled_form.pdf",
    "form_data": {
      "name": "John Doe",
      "ssn": "XXX-XX-XXXX",
      "income": "75000"
    }
  }
}
```
