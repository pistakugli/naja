### docx_create:

Creates and edits Microsoft Word (.docx) documents with professional formatting.
Supports tracked changes, comments, styles, tables, images, headers/footers.
Can create reports, proposals, letters, resumes, or any professional document.

**When to use:**
- "Create a Word document/report/proposal"
- "Write a professional letter"
- "Generate a resume"
- User needs a document for sharing/printing
- Any substantial written content that should be in .docx format

**Important:** 
- Use docx for PROFESSIONAL documents (reports, proposals, business docs)
- Use markdown for casual content or code documentation
- Always create the actual file, don't just show content

**Capabilities:**
- Professional formatting (headers, fonts, styles)
- Tables and lists
- Track changes and comments
- Images and diagrams
- Headers/footers with page numbers
- Multiple sections with different formatting

**Usage:**
```json
{
  "thoughts": ["User wants a professional project proposal document"],
  "headline": "Creating project proposal in Word format",
  "tool_name": "docx_create",
  "tool_args": {
    "filename": "project_proposal.docx",
    "content": {
      "title": "AI Implementation Proposal",
      "sections": [
        {"heading": "Executive Summary", "text": "..."},
        {"heading": "Technical Approach", "text": "..."},
        {"heading": "Timeline", "text": "..."}
      ],
      "formatting": {
        "style": "professional",
        "include_toc": true,
        "header": "Confidential",
        "footer": "Page {PAGE}"
      }
    }
  }
}
```

**Best practices:**
- Read /mnt/skills/public/docx/SKILL.md for complete capabilities
- Create file in /home/claude first for processing
- Move final version to /mnt/user-data/outputs for sharing
- Use proper headings and styles
- Include tables for structured data
